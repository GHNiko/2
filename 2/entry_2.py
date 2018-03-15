yourWord = input("Enter any expression here: ").lower()
firstLetter = yourWord[0]
ount = yourWord.count(firstLetter)
def encrypt(yourWord,ount):
    result = ""
    for i in range(len(yourWord)):
        char = yourWord[i]

        if not (char.isalpha()):
            result += char
         
        elif (char.isupper()):
            result += chr((ord(char) + ount-65) % 26 + 65)

        else:
            result += chr((ord(char) + ount - 97) % 26 + 97) 
        
    return result
 

print (yourWord)
print (str(ount))
print (encrypt(yourWord,ount))
