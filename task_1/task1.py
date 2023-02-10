birds=["eagle","duck","swans", "sparrow", "crow", "parrot", "pigeons", "owl"]
animals=["zebra", "giraffe","camel", "hippo", "pig", "buffalo", "cow","dog"]
mountains=["sagarmatha", "k2", "kanchanjanga", "machhapuchhure", "dhaulagiri", "annapurna","makalu","manaslu"]
import random
count=1
ans=[]

print("Password Generator\n------------------\n------------------")
while True:
    try:
        num=input("How many passwords are needed?:")
        str=num
        num=int(num)

    except ValueError:
        #if Str is entered
        if str.isdigit()==False:
            print("Please enter the number.")
            continue   
    
    #if the num is betn 1 and 24 inclusive 
    if num>=1 and num<=24:
        combine=[(i+j+k) for i in birds for j in animals for k in mountains]
        # print(len(combine))
        # st=print(len(set(combine)))
        ans+=(random.choices(combine, k=num))
        for l in ans:
            print(count,"-->",l)
            count+=1
        break   #this'll end the loop
    
    #if the num<=0 and num>24
    else:
        print("Please enter the number between 1 and 24.")
        continue
            
    
        