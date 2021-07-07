#!/usr/bin/python3

for i in range(1, 101):
    if (i % 3 == 0):
        if (i%5 == 0):
            print(i,"BEST")
        else:
            print(i,"GOOD")
    else:
        if (i%5 == 0):
            print(i,"BETTER")
        else:
            print(i) 
         
    
    
    


