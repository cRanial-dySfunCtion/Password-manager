import main


print("1. Register new site")
print("2. Find existing site")
q = int(input(""))


if q == 1:
    q1 = input("Site: ")
    q3 = input("Username: ")
    code, key = main.encrypt()
    main.sendDB(code, q1, key, q3)
else:
    q1 = input("site: ")
    code, key, name = main.findDB(q1)
    print("Username: " + name)
    main.decrypt(code, key)


# fails = 0
# yay = 0
# while True:
#     for x in range(3):
#         code, key, secret= main.encrypt()
#         print(key)
#         ensecret = main.decrypt(code, key)
#         if secret != ensecret:
#             fails = fails+1
#             print("THis failed: " + secret)
#         else:
#             yay = yay +1
#             if yay % 10000 == 0:
#                 print(f'Number of successes: {yay}, number of failures: {fails}')
