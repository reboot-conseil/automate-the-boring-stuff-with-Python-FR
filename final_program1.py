import getpass  

# lire dans un fichier le mot de passe et le charger en mémoire
passwordFile = open('password.txt')  
secretPassword = passwordFile.read()
# demander à l'utilisateur quel est le mot de passe
print("wesh c'est quoi le mot de passe?")
# récupérer le mot de passe saisi par l'utilisateur
typedPassword = getpass.getpass()
# comportement variable en fonction de ce qu'a entré l'utilisateur
if typedPassword == secretPassword:  
    print('yeap')  
elif typedPassword == '12345':  
    print('frrRèrre fais un effort avec tes passwords')  
else:  
    print('nope')
