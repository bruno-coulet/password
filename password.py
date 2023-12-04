import hashlib

# def tryAgain():          Apparement la variable validation ça ne sert à rien
#     global validation
#     validation = False
#     motDePasse()


# Demandez à l'utilisateur de choisir un mot de passe.
def motDePasse():
    global password
    password=input("Choisissez un mot de passe : ")

def valid_motDePasse():

    specialCarac =['$','!', '@', '#', '%','^', '&', '*']
    # validation = True

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

motDePasse()
valid_motDePasse()

print(f"Le mot de passe est : {password}\n")

def crypt_256(password):
    m = hashlib.sha256()
    m.update(password.encode('utf-8'))
    return m.hexdigest()

hashed_password = crypt_256(password)
print("Le mot de passe crypté est :", hashed_password)
