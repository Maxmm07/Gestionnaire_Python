import tkinter as tk
import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "enregistrement_taches.json")

taches = []

# partie Lux
def sauvegarder_taches():
    with open(json_path, "w") as file:
        json.dump(taches, file)

try:
    with open(json_path, "r") as file:
        taches = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    pass

def ajouter_tache():
    nom = nom_entry.get()
    description = description_entry.get()
    date_echeance = date_echeance_entry.get()
    
    if nom and description: 
        tache_listbox.insert(tk.END, nom) 
        taches.append({"Nom": nom, "Description": description, "Échéance": date_echeance})
        description_entry.delete(0, tk.END)
        date_echeance_entry.delete(0, tk.END)
        sauvegarder_taches()

def marquer_comme_terminee():
    selected_index = tache_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tache_listbox.itemconfig(index, {'bg': 'light green'})
        taches[index]["Terminée"] = True
        sauvegarder_taches()

def supprimer_tache():
    selected_index = tache_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tache_listbox.delete(index)
        del taches[index]
        sauvegarder_taches()

def afficher_liste_taches():
    for tache in taches:
        print(f"Nom : {tache['Nom']}, Description : {tache['Description']}, Échéance : {tache['Échéance']}")

fenetre = tk.Tk()
fenetre.title("Gestionnaire de Tâches")

# entrées gestionnaire
nom_label = tk.Label(fenetre, text="Nom de la tâche:")
nom_label.pack()
nom_entry = tk.Entry(fenetre)
nom_entry.pack()

description_label = tk.Label(fenetre, text="Description de la tâche:")
description_label.pack()
description_entry = tk.Entry(fenetre)
description_entry.pack()

date_echeance_label = tk.Label(fenetre, text="Date d'échéance:")
date_echeance_label.pack()

date_echeance_entry = tk.Entry(fenetre)
date_echeance_entry.pack()

# partie boutons
ajouter_bouton = tk.Button(fenetre, text="Ajouter", command=ajouter_tache)
ajouter_bouton.pack()

tache_listbox = tk.Listbox(fenetre)
tache_listbox.pack()

supprimer_bouton = tk.Button(fenetre, text="Supprimer", command=supprimer_tache)
supprimer_bouton.pack()

marquer_bouton = tk.Button(fenetre, text="Terminée", command=marquer_comme_terminee)
marquer_bouton.pack()

afficher_bouton = tk.Button(fenetre, text="Afficher la liste des tâches", command=afficher_liste_taches)
afficher_bouton.pack()

fenetre.geometry("600x500")

fenetre.mainloop()