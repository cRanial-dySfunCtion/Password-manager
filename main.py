import random
import sqlite3
import math
import datetime
conn = sqlite3.connect('database.db')
c = conn.cursor()

def newpassword():
    secret = ""
    doublesecret = ""

    num = random.randint(100, 125)

    secret = secret + chr(num)
    doublesecret += str(num)

    for i in range(4):

        num = random.randint(33, 125)

        secret = secret + chr(num)
        doublesecret += f'{num:03}'

    return int(doublesecret), secret

def encryption(code, method):
    if method == 1:
        return encrypt1(code)
    elif method == 2:
        return encrypt2(code)
    elif method == 3:
        return encrypt3(code)

def encrypt1(code):
    encode = (code  * 5)
    return encode

def decrypt1(encode):
    codetwo = (encode // 5)
    return codetwo

def encrypt2(code):
    encode = (pow(code,2)+5)
    return encode

def decrypt2(encode):
    codetwo = int(math.sqrt(encode-5))
    return codetwo

def encrypt3(code):
    encode = (((((((code+5)*2)-10)*2)+15)-9)*2)
    return encode

def decrypt3(encode):
    codetwo = int(((((((encode/2)+9)-15)/2)+10)/2)-5)
    return codetwo

def decryption(code, method):
    if method == 1:
        return decrypt1(code)
    elif method == 2:
        return decrypt2(code)
    elif method == 3:
        return decrypt3(code)

def encrypt():
    key = random.randint(1, 3)
    secretbefore = ''
    ahhh = ''
    wyr = ''
    for x in range(3):
        test, secretnonbi = newpassword()
        secretbefore = secretbefore + secretnonbi
        if len(ahhh) > 0:
            ahhh += '.'
        ahhh = str(ahhh) + str(encryption(test, key))

        wyr = wyr + str(test)
    print(secretbefore)
    return ahhh, key # to db

def decrypt(code, key):
    place = 0
    split_list = code.split('.')
    dio = ''
    for x in range(3):
        ree = decryption(int(split_list[place]), key)
        dio = dio + str(ree)
        place = place + 1


    temp = dio
    decrypted_password = ''
    while len(temp) > 0:
        i = temp[:3]
        decrypted_password += chr(int(i))
        temp = temp[3:]

    print(decrypted_password)



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



