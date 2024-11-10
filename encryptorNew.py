import string

abc = string.ascii_letters + ' ' + string.digits + string.punctuation

goodInput = False
abcSet = set(abc)
key = input("Enter Key: ")
keyIndex = []
encrypted = []
decrypted = []
newIndex = 0
for k in key:
    keyIndex.append(abc.index(k))

chooseUse = int(input('Enter 1 for encryption or 2 for  decryption: '))
if chooseUse == 1:
    while not goodInput:
        message = input('Enter your message with ASCII characters not including tab, linefeed, return, formfeed, and vertical tab: ')
        if set(message) <= abcSet:
            goodInput = True
    for i in range(len(message)):
        keyNumIndex = keyIndex[i % len(keyIndex)]
        newIndex = (abc.index(message[i]) + keyNumIndex) % len(abc)
        encrypted.append(abc[newIndex % len(abc)])
    print(''.join(encrypted))
    input('press Enter to close')
elif chooseUse == 2:
    while not goodInput:
        encryptedM = input('Enter your encrypted string with ASCII characters not including tab, linefeed, return, formfeed, and vertical tab: ')
        if set(encryptedM) <= abcSet:
            goodInput = True   
    for i in range(len(encryptedM)):
        keyNumIndex = keyIndex[i % len(keyIndex)]
        newIndex = (abc.index(encryptedM[i]) - keyNumIndex) % len(abc)
        decrypted.append(abc[newIndex % len(abc)])
    print(''.join(decrypted))
    input('press Enter to close')
else:
    input('you have entered a wrong input, relaunch the program and try again')


