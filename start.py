from main import *


print("1. Register new site")
print("2. Find existing site")
q = int(input(""))


if q == 1:
    q1 = input("Site: ")
    q3 = input("Username: ")
    code, key = encrypt_function()
    sendDB(code, q1, key, q3)
else:
    q1 = input("site: ")
    code, key, name = findDB(q1)
    print("Username: " + name)
    if key != 0:
        decrypt_function(code, key)
    else:
        print(code)


# fails = 0
# successes = 0
# while True:
#     for x in range(3):
#         code, key, secret= encrypt_function()
#         # print(key)
#         ensecret = decrypt_function(code, key)
#         if secret != ensecret:
#             fails = fails+1
#             print("This failed: " + secret)
#         else:
#             successes += 1
#             if successes % 10000 == 0:
#                 print(f'Number of successes: {successes}, number of failures: {fails}')


