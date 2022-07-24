l,c,_=0,0,input()
for n in list(map(int,input().split())):
    c,l=c+len(list(filter(lambda x:x=='1',bin(n)[2:]))),max(l,len(bin(n)[2:]))
print(c+l-1)