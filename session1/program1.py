import getpass

passwordFile = open('password.txt')
secretPassword = passwordFile.read()
print("wesh c'est quoi le mot de passe?")
typedPassword = getpass.getpass()
if typedPassword == secretPassword:
    print('yeap')
elif typedPassword == '12345':
    print('frrRèrre fais un effort avec tes passwords')
else:
    print('nope')
