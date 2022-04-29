T = input()

a = []
for i in range(int(T)):
    a.append(input())
    
    

def control(string):
    c = ""
    d = ""
    for i in range(len(string)):
        if i %2 == 0:
            c = c+string[i]
        else:
            d = d+string[i]
    print(c,d)        
        
for i in a:
    control(i)
