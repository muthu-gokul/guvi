x,y=map(int,input().split())
z=list(map(int,input().split()))
s=0
for i in range(y):
    s+=z[i]
print(s)
