import hashlib, json, os, random, string, pprint

#-------------------    FONCTIONS   ---------------------------------------------------------------------------

def motDePasse():                                  # demande un mot de passe en input, sinon généré automatiquement -> validation()
    global password
    password = input("Choisissez un mot de passe (ou appuyez sur Entrée pour générer un mot de passe aléatoire) : ")
    if not password:                               # si input vierge, appel la fonction generate_random_password
        password = generate_random_password()
        print(f"\nMot de passe aléatoire généré : {password}")
    validation()

def validation():                                  # Si mdp ok-> crypt256() et valid = True. Sinon-> motDePasse()
    global valid, hashed#, hashed_exists, account_exists
    specialCarac =['$','!', '@', '#', '%','^', '&', '*']
    if len(password)<8:                                     # demande un autre mot de passe
        print("Votre mot de passe doit contenir au moins 8 caractères !")
        motDePasse()
    if not any(char.isupper() for char in password):        # demande un autre mot de passe
        print("Votre mot de passe doit contenir au moins une lettre majuscule !")
        motDePasse()
    if not any(char.islower() for char in password):        # demande un autre mot de passe
        print("Votre mot de passe doit contenir au moins une lettre minuscule !")
        motDePasse()
    if not any(chr.isdigit() for chr in password):          # demande un autre mot de passe
        print("Votre mot de passe doit contenir au moins un chiffre !")
        motDePasse()
    if not any(char in specialCarac for char in password):  # demande un autre mot de passe
        print("Votre mot de passe doit contenir au moins un caractère spéciale : !, @, #, $, %, ^, &, *")
        motDePasse()
    else:                                                   # appel crypt_256(), enregistre le mdp hashé dans "hashed"                            
        hashed = crypt_256(password)
        
def generate_random_password(length=12):           # génère le mot de passe, appelé dans motDePasse()
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

def crypt_256(password):                           # Pour crypter le mot de passe
    m = hashlib.sha256()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

#-------------------    SCRIPT  ---------------------------------------------------------------------------


if os.path.exists('registre.json'):                 # si registre.json existe
    with open('registre.json', 'r') as json_file:   # ouvre registre.json
        registre = json.load(json_file)             # charge son contenu dans registre
else:                                               # sinon
    registre = []                                   # crée la liste registre[]

print("\nAu début du script, registre.json contient :\n")
pprint.pprint(registre)
print('\n')

motDePasse()
if hashed not in registre:
    registre.append(hashed)
    print("\nMot de passe validé\n")
    print("Le mot de passe a été crypté et ajouté au registre")
else:
    print("\nCe mot de passe est déjà utilisé\nChoisissez un mot de passe différent !")

with open('registre.json', 'w') as json_file:       # ajoute existing_data à registre.json
    json.dump(registre, json_file, indent=4)
    json_file.write('\n')

print("\nA la fin du script, registre.json contient :\n")
pprint.pprint(registre)
print('\n')





