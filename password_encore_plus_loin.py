import hashlib, json, os, random, string
registre = []

def generate_random_password(length=12):
    specialCarac = ['$','!', '@', '#', '%','^', '&', '*']
    # 1 caractère aléatoire et obligatoire dans chaque catégories
    random_special = random.choice(specialCarac)
    random_digit = random.choice(string.digits)
    random_uppercase = random.choice(string.ascii_uppercase)
    random_lowercase = random.choice(string.ascii_lowercase)
    # mix les catégories dans 'characters'
    characters = string.ascii_letters + string.digits + ''.join(specialCarac)
    # 8 caractères restant à générer
    remaining_length = length - 4  
    remaining_characters = ''.join(random.choice(characters) for _ in range(remaining_length))
    # mélange les caractères obligatoire et restant dans'all_characters'
    all_characters = random_special + random_digit + random_uppercase + random_lowercase + remaining_characters
    password_list = list(all_characters)
    random.shuffle(password_list)
    return ''.join(password_list)

def motDePasse():
    global password
    password = input("Choisissez un mot de passe (ou appuyez sur Entrée pour générer un mot de passe aléatoire) : ")
    if not password:                    # si input vierge, appel la fonction generate_random_password
        password = generate_random_password()
        print(f"Mot de passe aléatoire généré : {password}")

def valid_motDePasse():
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

def passwordAcount():
    global acount
    global registre
    global hashed
    acount = input("À quel compte ce mot de passe est-il relié : ")
    # vérfie si acount existe dans registre
    if any(acount in entry for entry in registre):
        print(f"Le compte {acount} existe déjà.")
        return
    # Sinon, ajoute acount et hashed à registre    
    new_entry = {acount: hashed}
    registre.append(new_entry)
    print(f"Le mot de passe pour le compte '{acount}' a été ajouté au registre.")

passwordAcount()

if os.path.exists('registre.json'):                 # si registre.json existe
    with open('registre.json', 'r') as json_file:   # ouvre registre.json
        existing_data = json.load(json_file)        # charge son contenu dans existing_data
else:                                               # sinon
    existing_data = []                              # crée la liste existing_data

existing_data.extend(registre)                      # ajoute la liste registre à existing data

with open('registre.json', 'w') as json_file:       # ajoute existing_data à registre.json
    json.dump(existing_data, json_file, indent=4)
    json_file.write('\n')

