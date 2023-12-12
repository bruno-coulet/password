import hashlib, json, os, random, string

#-------------------    VARIABLES   ---------------------------------------------------------------------------

specialCarac =['$','!', '@', '#', '%','^', '&', '*']
registre = []
valid = False
hashed =''
hashed_exists = False


#-------------------    FONCTIONS   ---------------------------------------------------------------------------

def motDePasse():                                       # demande un mot de passe en input ou généré automatiquement
    global password
    password = input("Choisissez un mot de passe (ou appuyez sur Entrée pour générer un mot de passe aléatoire) : ")
    if not password:                                # si input vierge, appel la fonction generate_random_password
        password = generate_random_password()
        print(f"\nMot de passe aléatoire généré : {password}")
    validation()

def validation():                                       # valide le mot de passe -> valid = True
    global valid, hashed, hashed_exists, account_exists

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
    else:
        hashed = crypt_256(password)                        # enregistre le mot de passe crypté dans "hashed"
        
        for i in registre:
            for j in i:
                if hashed == j:
                    motDePasse()
        else:
            valid = True
            print("\nMot de passe validé")
            print("Le mot de passe a été crypté")



def generate_random_password(length=12):                # génère le mot de passe
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

def crypt_256(password):                                # Pour crypter le mot de passe
    m = hashlib.sha256()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

def passwordAccount_old():                                  # demande à quel compte relier le mot de passe
    global account
    global registre
    global hashed
    global valid
    global account_exists

    if valid == True:
        account = input("À quel compte ce mot de passe est-il relié : ")
     
        # vérifie si account existe dans registre
        account_exists = False
        for entry in registre:
            if account in entry:
                account_exists = True
                print(f"Le compte {account} existe déjà.")
                return
        # Sinon, ajoute account et hashed à registre    
        
        new_entry = {account: hashed}
        registre.append(new_entry)
        print(f"\nLe mot de passe pour le compte '{account}' a été ajouté à la liste registre.json\n")



#-------------------    SCRIPT  ---------------------------------------------------------------------------
#print ("valid =",valid)


if os.path.exists('registre.json'):
    with open('registre.json', 'r') as json_file:
        registre = json.load(json_file)
else:
    registre = []

print(f"\nAprès vérification :\nregistre = {registre}")

motDePasse()

registre.append(hashed)

if os.path.exists('registre.json'):                 # si registre.json existe
    with open('registre.json', 'r') as json_file:   # ouvre registre.json
        existing_data = json.load(json_file)        # charge son contenu dans existing_data
else:                                               # sinon
    existing_data = []                              # crée la liste existing_data

existing_data.extend(registre)                      # ajoute la liste registre à existing data

with open('registre.json', 'w') as json_file:       # ajoute existing_data à registre.json
    json.dump(existing_data, json_file, indent=4)
    json_file.write('\n')

print(f"\naprès la fonctions et le script :\nregistre = {registre}\n")





