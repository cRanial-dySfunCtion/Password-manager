import random
import sqlite3
import math
import datetime
conn = sqlite3.connect('database.db')
c = conn.cursor()

def newpassword():
    """make a new password that is 5 charactors long
    returns the number and charactor passwords
    the number gets stored in the database"""
    password_charactors = ""
    password_numbers = ""

    num = random.randint(100, 125) # get the ascii for the first charactor in the password  !!DO NOT TOUCH!!

    password_charactors += chr(num)
    password_numbers += str(num)

    for i in range(4):

        num = random.randint(33, 125) # get the ascii for the rest of the charactors  !!DO NOT TOUCH!!

        password_charactors += chr(num)
        password_numbers += f'{num:03}'

    return int(password_numbers), password_charactors


class encryptions():
    
    def method1(code):
        encode = (code * 5)
        return encode
    
    def method2(code):
        encode = (pow(code,2)+5)
        return encode
    
    def method3(code):
        encode = (((((((code+5)*2)-10)*2)+15)-9)*2)
        return encode


class decryptions():
    def method1(encode):
        codetwo = (encode // 5)
        return codetwo

    def method2(encode):
        codetwo = int(math.sqrt(encode-5))
        return codetwo

    def method3(encode):
        codetwo = int(((((((encode/2)+9)-15)/2)+10)/2)-5)
        return codetwo

def encrypt_function():
    key = random.randint(1, 3)
    encryption_methods = {1: encryptions.method1, 2: encryptions.method2, 3: encryptions.method3}
    full_charactor_password = ''
    full_number_password = ''

    for x in range(3):
        number_password_befor_encryption, charactor_password = newpassword()
        full_charactor_password += charactor_password
        if len(full_number_password) > 0:
            full_number_password += '.'
        full_number_password += str(encryption_methods[key](number_password_befor_encryption))

    print(full_charactor_password)

    return full_number_password, key # to db
    return full_number_password, key, full_charactor_password # for testing

def decrypt_function(code, key):
    decryption_methods = {1: decryptions.method1, 2: decryptions.method2, 3: decryptions.method3}
    split_list = code.split('.')
    decrypted_number_password = ''

    # decrypt the number password
    for place in range(3):
        decrypted_number_password += str(decryption_methods[key](int(split_list[place])))

    #convert back into charactors
    decrypted_password = ''
    while len(decrypted_number_password) > 0:
        number = decrypted_number_password[:3]
        decrypted_password += chr(int(number))
        decrypted_number_password = decrypted_number_password[3:]

    print(decrypted_password)
    return decrypted_password



def sendDB(code, site, key, name):
    date = datetime.date.today()
    c.execute("""insert into secrets (date, username, secret, site, key )
    values (?, ?, ?, ?, ?);
    """, (date, name, code, site, key))
    conn.commit()



def findDB(site):
    x = conn.execute("""SELECT secret, key, username FROM secrets WHERE site = (?);""", (site,))
    code, key, name = x.fetchone()
    return code, key, name





# c.execute("""CREATE TABLE secrets (
#             date text,
#             username text,
#             secret text,
#             site text,
#             key integer
#             )""")



