#sample message1
a = open("sample_message_1.txt", 'r') #reading the file.
messages = a.read() 
a.close() 

#sample message2
b=open("sample_message_2.txt",'r')
message=b.read()
b.close()

#sample message3
c=open("sample_message_3.txt",'r')
messag=c.read()
c.close()

#sample message4
d=open("sample_message_4.txt",'r')
messa=d.read()
d.close()
import string

alphabet = string.ascii_letters #alphabet in lowercase and uppercase

decrypted = ""

#taking input from the user.
key = int(input("Enter the key: "))

#if the key is entered 14
if key==14:
    for i in messages:
        if i in alphabet:  
            pos = alphabet.find(i)  
            new_pos = (pos - key) % 26  
            new_character = alphabet[new_pos]  
            decrypted += new_character
            # print(decrypted)  
        else:
            decrypted += i 
    for i in messa:
        if i in alphabet:  
            pos = alphabet.find(i)  
            new_pos = (pos - key) % 26  
            new_character = alphabet[new_pos]  
            decrypted += new_character
            # print(decrypted)  
        else:
            decrypted += i 
    print(decrypted)

#if the key is entered 11
if key==11:
    for i in message:
        if i in alphabet:  
            pos = alphabet.find(i)  
            new_pos = (pos - key) % 26  
            new_character = alphabet[new_pos]  
            decrypted += new_character
            # print(decrypted)  
        else:
            decrypted += i
    print(decrypted)

#if the key is entered 21
if key==21:
    for i in messag:
        if i in alphabet:  
            pos = alphabet.find(i)  
            new_pos = (pos - key) % 26  
            new_character = alphabet[new_pos]  
            decrypted += new_character
            # print(decrypted)  
        else:
            decrypted += i 
    print(decrypted)




