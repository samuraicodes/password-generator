# -*- coding: utf-8 -*-
import random



chars = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWEXYZ123456789.,-?¡¿"#$%&'
password = ''

amount_passwords = input('How many passwords do you need?')
amount_passwords = int(amount_passwords)

strongness = input('Password length?')
strongness = int(strongness)

for c in range(amount_passwords):
    for c in range(strongness):    
        password += random.choice(chars)
    print(password)
    password = ''
