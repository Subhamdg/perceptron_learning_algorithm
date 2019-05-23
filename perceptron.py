import numpy as nm

p=nm.array([
    [1,1,1,1],
    [-1,1,-1,1],
    [1,1,1,-1],
    [1,-1,-1,1]
    ])
t=nm.array([1,1,-1,-1])
rate=1
w=nm.array([0,0,0,0])
e_a=nm.array([])
while True:
    for i in range(0,4):
        n=nm.dot(w,(p[i].T))
        if(n<0):
            a=-1
        elif(n>=0):
            a=1
        e=t[i]-a
        nm.append(e_a,e)
        if(e<0):
            w=w-nm.dot(rate,p[i])
        elif(e>0):
            w=w+nm.dot(rate,p[i])
    sse=nm.dot(e,e.T)
    if(sse!=0):
        e_a=nm.array([])
    elif(sse==0):
        break
print(w)
