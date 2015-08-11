'''
Created on Aug 10, 2015

@author: ngo

'''
from math import pi, sin, cos
X=50
Y=40
K=5
R=287
CP=1005
M=1
N=50
PN=[150, 400, 650, 900, 1000]
P0=1000
det=1200
dex=100000
F=14.584*(10**(-5))
NO_OF_DECIMAL=3
t=[18, 8, -41, -87, -233]
Goc=[pi/12, pi/3, 2*pi/3, 8*pi/9, 35*pi/36]
Gio=[5, 10.8, 18, 20.2, 19.1]
Zcao=[110, 980, 4940, 7880, 14000]
M1= M/(4*det)
dataPath="C:\Users\ngo\Desktop\temp"

Ut=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Ut1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Ut2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

Vt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Vt1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Vt2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

TEt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
TEt1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
TEt2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

Qt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Qt1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Qt2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

PHI=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Wt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

PS= [[0 for j in range(Y)]for i in range(X)]
PSt1= [[0 for j in range(Y)]for i in range(X)]
PSt2= [[0 for j in range(Y)]for i in range(X)]
Ws= [[0 for j in range(Y)]for i in range(X)]

def init(self):
    print("Khoi tao so lieu")
    for k in range(K):
        sgoc=sin(Goc[k])        
        cgoc=cos(Goc[k])
        Tt=273+t[k]
        if k==(K-1): Ptb=25
        else: Ptb=(PN[k]+PN[k+1])/2
        for i in range(X):
            for j in range(Y):
                Ut[k][i][j]=Gio[k]*cgoc
                Vt[k][i][j]= Gio[k]*sgoc
                TEt[k][i][j]= (Tt*((1000/Ptb)**0.286))
                Qt[k][i][j]=0
                PHI[k][i][j]=Zcao[k]
                Wt[k][i][j]=0
                Ut1[k][i][j]=Ut[k][i][j]
                Vt1[k][i][j]=Vt[k][i][j]
                TEt1[k][i][j]=TEt[k][i][j]
                Qt1[k][i][j]=Qt[k][i][j]
    for i in range(X):
        for j in range(Y):
            PS[i][j]=P0
            Ws[i][j]=0;
            PSt1[i][j]=PS[i][j]
    print("Khoi tao thanh cong")
if __name__ == '__main__':
    pass