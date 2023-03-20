#use of break and continue

#break
for i in range(1,101):
    if(i==50):
        break
    print(i,end=' ')
#continue    
for i in range(1,101):
    if(i==50):
        continue
    print(i,end=' ')
print()    

for i in range(1,101):
    if(i==50):
        pass
    print(i,end=' ')
