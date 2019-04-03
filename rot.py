print("Enter text: ")
message = input()

for i in range(1, 26):
    translated = ""
    #iterate through message
    for symbol in message:
        #check to see if symbol is alphabetical
        if symbol.isalpha():
            num = ord(symbol)           #ord finds the decimal value of a character
            num += i                    #add i to the decimal value
            #testing to see if num is out of upper character set
            if symbol.isupper():
                #if it is, subtract 26 to wrap around
                if num > ord('Z'):
                    num -= 26
            #testing to see if num is out of lower character set
            elif symbol.islower():
                #if it is, subtract 26 to wrap around
                if num > ord('z'):
                    num -= 26
            #print the translated character
            translated += chr(num)
        #if symbol is not alphabetical, print symbol
        else:
            translated += symbol

    print('ROT',i,':',translated)