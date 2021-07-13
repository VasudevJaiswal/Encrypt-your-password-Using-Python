# Encrypt-your-password-Using-Python

Using this script, you can encrypt your password.

Steps involved
First install pcrypt module via command prompt or any terminal which you use by running the following command:
pip install pcrypt
Import pcrypt module to encrypt passwords.
Import getpass module to get password from user input in hidden mode.
NOTE:
The rounds=N option helps to improve key strengthening. The number of rounds has a larger impact on security than the selection of a hash function. For example, rounds=65536 means that an attacker has to compute 65536 hashes for each password he tests against the hash.
