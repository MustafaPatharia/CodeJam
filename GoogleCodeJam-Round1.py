import random
t=int(input())
route=''
direction = ['S','E']
for j in range(t):
    
    n=int(input())
    p=input().upper()
    while p.count('E')!=p.count('S'):
        p=input().upper() 
    p=[i for i in p]

    while True:
        lydia=0
        mustafa=0
        route=''
        for k in p:
            pos=random.choice(direction)
        
            if k=='E':
                lydia+=1

                if pos=='E' and route.count('E')>(n-1):
                    mustafa+=1
    
                    if mustafa == lydia:
                        route+='S'
                        mustafa+=(n-1)                    

                    else:
                        route+='E'
                else:
                    route+='S'
                    mustafa+=n
                
            elif k=='S':
                lydia+=5

                if pos=='S' and route.count('S')>(n-1):
                    mustafa+=n
        
                    if mustafa==lydia:
                        route+='E'
                        mustafa-=(n-1)
    
                    else:
                        route+='S'
                else:
                    route+='E'
                    mustafa+=1
                        
        if(route.count('E')==route.count('S')):
            break

    print('Case #%d: '%(j+1)+route)

    
    

    
