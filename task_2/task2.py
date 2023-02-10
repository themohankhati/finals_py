print(" Park Run Timer\n ~~~~~~~~~~~~~~~~\n")
print("Let's go!")
runners_number,runners_time,fastest_t,slowest_t=0,0,0,0
fastest_t=float('inf') #inf represent to the infinity

while True:
    try:
        inn=input(" >")
        #splitting into runners number and time in secs
        a,b=inn.split('::')
        b=int(b)
        #total numbers and time
        runners_number+=1
        runners_time+=b
        
        #calculating avg time 
        avg_t=runners_time/runners_number
        avg_t_in_min=avg_t//60
        avg_t_in_sec=avg_t%60
        
        #fastest and slowest time
        if b<fastest_t:
            fastest_t=b
            fastest_runner=a
        if b>slowest_t:
            slowest_t=b
        
        #converting secs into minutes and secs
        fastest_t_in_min=fastest_t//60
        fastest_t_in_sec=fastest_t%60
        slowest_t_in_min=slowest_t//60
        slowest_t_in_sec=slowest_t%60
    
    except ValueError:
        #if user type END then it will print runners num,avg time, fastest time slowest time and fastest runner. 
        if inn=="END": 
            print("Total runners:",runners_number)
            #displaying avg time 
            if avg_t_in_min==1 and avg_t_in_sec!=1:
                 print("Average time:",avg_t_in_min,"minute"",",avg_t_in_sec,"seconds")
            if avg_t_in_min!=1 and avg_t_in_sec==1:
                 print("Average time:",avg_t_in_min,"minutes"",",avg_t_in_sec,"second")
            if avg_t_in_min==1 and avg_t_in_sec==1:
                 print("Average time:",avg_t_in_min,"minute"",",avg_t_in_sec,"second")
            if avg_t_in_min!=1 and avg_t_in_sec!=1:
                 print("Average time:",avg_t_in_min,"minutes"",",avg_t_in_sec,"seconds")
           
           #displaying fastest time
            if fastest_t_in_min==1 and fastest_t_in_sec!=1:
                print("Fastest time:",fastest_t_in_min,"minute"",",fastest_t_in_sec,"seconds")
            if fastest_t_in_min!=1 and fastest_t_in_sec==1:
                 print("Fastest time:",fastest_t_in_min,"minutes"",",fastest_t_in_sec,"second")
            if fastest_t_in_min==1 and fastest_t_in_sec==1:
                print("Fastest time:",fastest_t_in_min,"minute"",",fastest_t_in_sec,"second")
            if fastest_t_in_min!=1 and fastest_t_in_sec!=1:
                print("Fastest time:",fastest_t_in_min,"minutes"",",fastest_t_in_sec,"seconds")
            
            #displaying slowest time
            if slowest_t_in_min==1 and slowest_t_in_sec!=1:
                print("Slowest time:",slowest_t_in_min,"minute"",",slowest_t_in_sec,"seconds")
            if slowest_t_in_min!=1 and slowest_t_in_sec==1:
                 print("Slowest time:",slowest_t_in_min,"minutes"",",slowest_t_in_sec,"second")
            if slowest_t_in_min==1 and slowest_t_in_sec==1:
                 print("Slowest time:",slowest_t_in_min,"minute"",",slowest_t_in_sec,"second")
            if slowest_t_in_min!=1 and slowest_t_in_sec!=1:
                 print("Slowest time:",slowest_t_in_min,"minutes"",",slowest_t_in_sec,"seconds")
            print("Best Time Here:","Runner","#",fastest_runner)
            break
        else:
            print("Error in data stream. Ignorning. Carry on.") 