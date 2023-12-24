def goal():
        n=1
        a=3000
        a1=1.005*a
        a_n=a1
        
        while(a_n<20000):
                a_n=1.005*(a+a_n)
                n+=1
                
        return  n

a=goal()
print(a)
