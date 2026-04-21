#The user should input 8 digit password so if the password should contain characters number and symbol length must be between 8, 16, and above.

passwordlength = input('\nEnter password: ')

passwordlength = 16

if (passwordlength < 8):

    print('very weak')

if (passwordlength == 8):

    print('weak')

if (passwordlength > 8):

    print ('strong')

if (passwordlength > 16):

    print ('very atrong')
