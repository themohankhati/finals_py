import string
from random import choice
chars = string.digits
import re
email=''
a =open('student.txt','r')
x=[]
y=[]
z=[]

for i in a:
    b=i.split(", ")
    x.append(b)
    # print(x)

#appending first name into list  
for k in x:
    y.append(k[1].strip("\n"))
    # print(y)

    #last name spliting
    for l in y:
        d =l.split(',')
        # print(d)
    
        for j in d:
            e=j.split(' ')
            print(e)
    
    #appending first name and stu id into list
    z.append(k[0].strip("\n"))   
    #spliting id and first name
    for n in z:
        c=n.split(' ')
    
    if len(e)==3:
        email+=((c[0]+' '+e[0][0]+'.'+e[1][0]+'.'+e[2][0]+'.'+c[1]).lower()+''.join(choice(chars) for _ in range(4))+"@poppleton.ac.uk\n")
        email=re.sub("[-']","",email)
    if len(e)==2:
        email+=((c[0]+' '+e[0][0]+'.'+e[1][0]+'.'+c[1]).lower()+''.join(choice(chars) for _ in range(4))+"@poppleton.ac.uk\n")
        email=re.sub("[-']","",email)
    if len(e)==1:
        email+=((c[0]+' '+e[0][0]+'.'+c[1]).lower()+''.join(choice(chars) for _ in range(4))+"@poppleton.ac.uk\n")
        email=re.sub("[-']","",email)
print(str(email))

#writing email on another txt file
for m in email:
    b=open("email.txt","a+")
    b.write(m)
    b.close()



                
    
