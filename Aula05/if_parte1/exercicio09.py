n1 = int(input("Diga um numero: "))
n2 = int(input("diga outro numero: "))
n3 = int(input("diga um terceiro numero: "))
if (n1 >= n2): # n1>n2
    if(n2>=n3): print(str(n3)+" "+str(n2)+" "+ str(n1))# n1>n2>n3
    elif(n1>=n3): print(str(n2)+" "+str(n3)+" "+ str(n1))# n1>n3>n2
    else: print(str(n2)+" "+str(n1)+" "+ str(n3))# n3>n1>n2
else: # n2>n1
    if(n3>=n2): print(str(n1)+" "+str(n2)+" "+ str(n3))# n3>n2>n1
    elif(n3>=n1):print(str(n1)+" "+str(n3)+" "+ str(n2)) # n2>n3>n1 
    else: print(str(n3)+" "+str(n1)+" "+ str(n2)) # n2>n1>n3 

