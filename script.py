# This python code written by 
# Vasudev Jaiswal

import pcrypt
import getpass


#get password from user input in hidden mode using getpass module
pass_word = getpass.getpass("Enter your password: ")

# #encrypt password and store it in variable

encrypted_password = pcrypt.crypt(pass_word, pcrypt.METHOD_SHA256, rounds=50000)

print("**************************** your password is encrypted  *********************************")
print("\n")
print(encrypted_password)

#***********************************************************************************
print("\n")
print("********************************** pcrypt ***************************************")

print("\n")

print("pcrypt methods are : {0}".format(pcrypt.methods))

print("\n")
print("default round is : {0}".format(pcrypt._ROUNDS_DEFAULT))

print("\n")
# I create my own salt using mksalt function

# mysalt = pcrypt.mksalt(pcrypt.METHOD_SHA512, rounds=45000)

# # using this salt
# print(pcrypt.crypt("123456", salt=mysalt))
