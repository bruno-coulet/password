import hashlib, json, os
registre=[]

def motDePasse():                       # Pour demander le mot de passe
    global password
    password=input("Choisissez un mot de passe : ")

def valid_motDePasse():                 # Pour valider (ou pas) le mot de passe
    specialCarac =['$','!', '@', '#', '%','^', '&', '*']
    if len(password)<8:
        print("Votre mot de passe doit contenir au moins 8 caractères !")
        motDePasse()
    if not any(char.isupper() for char in password):
        print("Votre mot de passe doit contenir au moins une lettre majuscule !")
        motDePasse()
    if not any(char.islower() for char in password):
        print("Votre mot de passe doit contenir au moins une lettre minuscule !")
        motDePasse()
    if not any(chr.isdigit() for chr in password):
        print("Votre mot de passe doit contenir au moins un chiffre !")
        motDePasse()
    if not any(char in specialCarac for char in password):
        print("Votre mot de passe doit contenir au moins un caractère spéciale : !, @, #, $, %, ^, &, *")
        motDePasse()
    else:
        print("\nMot de passe validé\n")

def crypt_256(password):                # Pour crypter le mot de passe
    m = hashlib.sha256()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

motDePasse()
valid_motDePasse()

hashed = crypt_256(password)             # enregistre le mot de passe crypté dans "hashed"
print("Le mot de passe a été crypté\n")

def passwordAcount():                   # Pour relier le mot de passe à un compte et l'enregistrer dans la bibliothèque registre
    global acount
    global registre
    acount=input("A quel compte ce mot de passe est-il relié : ")
    registre.append({acount: hashed})       # Use a dictionary instead of a set, and append new entries to the existing registre

passwordAcount()

print("\nRegistre des mots de passe :", registre,"\n")


# if not os.path.exists('save.json'):
#     with open('registre.json', 'a') as json_file:  # a donne toutes les permissions
#         json.dump(registre, json_file, indent=4)
#         json_file.write('\n')               # Add a newline to separate entries if needed

if os.path.exists('registre.json'):
    with open('registre.json', 'r') as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

# Append the new entry to the existing data
existing_data.extend(registre)

# Write the updated data back to the file
with open('registre.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)
    json_file.write('\n')