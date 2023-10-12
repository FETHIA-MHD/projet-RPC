import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("*********************************************************************************************************")
# Demander à l'utilisateur de choisir l'option
option = input(" 1: Créer fichier\n 2: Créer répertoire \n 3: Supprimer fichier \n 4: Supprimer répertoire\n 5: Modifier fichier\n 6: Liste des fichiers/répertoires \n 7: Ajouter des données à un fichier \n 8: Renommer un fichier/repertoire) \n \n Choisissez une option: ")

if option == "1":
    # Création d'un fichier
    file_path = input("\n Entrez le chemin du fichier à créer: ")

    response = server.manipulation('creation', file_path, 'file')
    if response['success']:
        print("\n * Création du fichier terminée *")
    else:
        print("\nÉchec de la création du fichier")

elif option == "2":
    # Création d'un répertoire
    directory_path = input("\nEntrez le chemin du répertoire à créer: ")
    response = server.manipulation('creation', directory_path, 'repertoire')
    if response['success']:
        print("\n * Création du répertoire terminée *")
    else:
        print("\nÉchec de la création du répertoire")

elif option == "3":
    # Suppression d'un fichier
    file_path = input("\nEntrez le chemin du fichier à supprimer: ")
    response = server.manipulation('suppression', file_path, 'file')
    if response['success']:
        print("\n * Suppression du fichier terminée * ")
    else:
        print("\nÉchec de la suppression du fichier")

elif option == "4":
    # Suppression d'un répertoire
    directory_path = input("\nEntrez le chemin du répertoire à supprimer: ")
    response = server.manipulation('suppression', directory_path, 'repertoire')
    if response['success']:
        print("\n * Suppression du répertoire terminée * ")
    else:
        print("\nÉchec de la suppression du répertoire")

elif option == "5":
    # Modification d'un fichier
    file_path = input("\nEntrez le chemin du fichier à modifier: ")
    new_content = input("\nEntrez le nouveau contenu du fichier: ")
    response = server.manipulation('modification', file_path, 'file', new_content)
    if response['success']:
        print("\n * Modification du fichier terminée *")
    else:
        print("\nÉchec de la modification du fichier")

elif option == "6":
    # Liste des fichiers/répertoires dans un chemin donné
    directory_path = input("\nEntrez le chemin du répertoire: ")
    files = server.list_files(directory_path)
    print("Fichiers/répertoires :", files)

elif option == "7":
    # Ajout de données à un fichier existant
    file_path = input("\nEntrez le chemin du fichier: ")
    data = input("\nEntrez les données à ajouter: ")
    response = server.add_data(file_path, data)
    if response['success']:
        print("\n * Données ajoutées au fichier *")
    else:
        print("\nÉchec de l'ajout de données au fichier")

elif option == "8":
    # Renommer un fichier ou un répertoire
    old_path = input("\nEntrez le chemin du fichier/répertoire à renommer: ")
    new_name = input("\nEntrez le nouveau nom: ")
    response = server.manipulation('rename', old_path, '', new_name)
    if response['success']:
        print("\n * Renommage du fichier/répertoire terminé * ")
    else:
        print("\nÉchec du renommage du fichier/répertoire")
else:
    print("Option invalide")