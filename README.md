# Gestionnaire_Python
TP Python - 25/10/2023 - Gestionnaire de tâches. VAMBRE Maxime.

1] Importation de modules

```python 
import tkinter as tk
import os
import json
```

importation des modules nécessaires : tkinter pour l'interface utilisateur, os pour gérer les fichiers et répertoires, et json pour enregistrer les tâches depuis un fichier JSON.

2] Enregistrement des tâches

```python
script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, "enregistrement_taches.json")

taches = []

def sauvegarder_taches():
    with open(json_path, "w") as file:
        json.dump(taches, file)

try:
    with open(json_path, "r") as file:
        taches = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    pass
```

Détermine le chemin du fichier JSON ("enregistrement_taches.json") en fonction de l'emplacement du script.

3] Ajout d'une tâche

La fonction 'ajouter_tache()' est appelée lorsque l'utilisateur utilise le bouton "Ajouter", celle-ci récupère les valeurs des champs de texte pour le nom, la description et la date d'échéance, la tâche est ajoutée à la liste affichée à l'écran si les champs ne sont pas vides. Les tâches sont enregistrées dans le fichier JSON en appelant 'sauvegarder_taches()'.

4] Marquer une Tâche comme Terminée

La fonction 'marquer_comme_terminee()' est appelée lorsque l'utilisateur utilise le bouton "Terminer", si une tâche est definie comme terminée la couleur d'arrière-plan de cette tâche en vert et fait une maj de la liste des tâches enregistrées dans le fichier JSON.

5] Supprimer une Tâche

La fonction 'supprimer_tache()' est appelée lorsque l'utilisateur utilise le bouton "Supprimer", supprime la tâche de la liste et de la liste des tâches enregistrées dans le fichier JSON.

6] Afficher la Liste des Tâches

La fonction 'afficher_liste_taches()' est appelée lorsque l'utilisateur utilise le bouton "Afficher la liste des tâches", elle parcourt la liste des tâches enregistrées et affiche les détails de chaque tâche dans le terminal vscode.

7] Entrées 

```python
nom_label = tk.Label(fenetre, text="Nom de la tâche:")
nom_entry = tk.Entry(fenetre)

description_label = tk.Label(fenetre, text="Description de la tâche:")
description_entry = tk.Entry(fenetre)

date_echeance_label = tk.Label(fenetre, text="Date d'échéance:")
date_echeance_entry = tk.Entry(fenetre)
```

Permet de creer des étiquettes 'Labels' et des champs de texte pour entrer le nom, la description et la date d'échéance .

8] Boutons


```python
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
```

Boutons qui permettent à l'utilisateur d'interagir avec le gestionnaire de tâches, les fonctions 'command' sont associées à des actions comme l'ajout, la suppression, la marquage comme terminée et l'affichage des tâches.
