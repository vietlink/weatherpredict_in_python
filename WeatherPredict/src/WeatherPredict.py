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

def init():
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

def DuDoan():
    for k in range(K):
        for i in range (1, X-1):
            for j in range (1, Y-1):
                Ut2[k][i][j]=-M*(PHI[k][i+1][j]-PHI[k][i][j])/dex \
                        -M1*((Ut1[k][i][j]+Ut1[k][i+1][j])*(Ut1[k][i+1][j]-Ut1[k][i][j])+(Ut1[k][i][j]+Ut1[k][i-1][j])*(Ut1[k][i][j]-Ut1[k][i-1][j])) \
                        +F*(Vt1[k][i][j]+Vt1[k][i][j-1]+Vt1[k][i+1][j]+Vt1[k][i+1][j-1])/4 \
                        -M1*((Vt1[k][i][j]+Vt1[k][i+1][j])*(Ut1[k][i][j+1]-Ut1[k][i][j])+(Vt1[k][i][j-1]+Vt1[k][i+1][j-1])*(Ut1[k][i][j-1]-Ut1[k][i][j]))
                Vt2[k][i][j]= -M*(PHI[k][i][j+1]-PHI[k][i][j])/dex \
                        - M1*((Ut1[k][i][j]+Ut1[k][i][j+1])*(Vt1[k][i+1][j]-Vt1[k][i][j])+(Ut1[k][i-1][j]+Ut1[k][i-1][j+1])*(Vt1[k][i][j]-Vt1[k][i-1][j])) \
                        - M1*((Vt1[k][i][j]+Vt1[k][i][j+1])*(Vt1[k][i][j+1]-Vt1[k][i][j])+(Vt1[k][i][j]+Vt1[k][i][j-1])*(Vt1[k][i][j]-Vt1[k][i][j-1])) \
                        -F*(Ut1[k][i][j]+Ut1[k][i-1][j]+Ut1[k][i][j+1]+Vt1[k][i-1][j+1])/4 \
                if k=(K-1):                
                    P1= (PN[k]+PN[k-1])/2
                    P2=25
                    P5=(PN[k]-P2)/(2*(P1-P2))
                    Ut2[k][i][j]= Ut2[k][i][j] \
                        -((Wt[k-1][i+1][j]+Wt[k-1][i][j])*P5*(Ut1[k][i][j]-Ut1[k-1][i][j]))/(PN[k]-PN[k-1])
                    Vt2[k][i][j]= Vt2[k][i][j] \
                                -((Wt[k-1][i][j+1]+Wt[k-1][i][j])*P5*(Vt1[k][i][j]-Vt1[k-1][i][j]))/(PN[k]-PN[k-1])
                    TE_t2[k][i][j]=0
                    Q_t2[k][i][j]=0
                else:
                    U1= (Ut1[k][i+1][j]+Ut1[k+1][i+1][j])/2
                    U2= (Ut1[k][i][j]+Ut1[k+1][i][j])/2
                    V1= (Vt1[k][i][j+1]+Vt1[k+1][i][j+1])/2
                    V2=(Vt1[k][i][j]+Vt1[k+1][i][j])/2
                    TEt2[k][i][j]=-2*M1*(U1*(TE_t1[k][i+1][j]-TE_t1[k][i][j]) \
                                -U2*(TE_t1[k][i][j]-TE_t1[k][i-1][j]) \
                                +V1*(TE_t1[k][i][j+1]-TE_t1[k][i][j]) \
                                -V2*(TE_t1[k][i][j]-TE_t1[k][i][j-1]))
                    Qt2[k][i][j]=-2*M1*(U1*(Q_t1[k][i+1][j]-Q_t1[k][i][j]) \
                                -U2*(Q_t1[k][i][j]-Q_t1[k][i-1][j]) \
                                +V1*(Q_t1[k][i][j+1]-Q_t1[k][i][j]) \
                                -V2*(Q_t1[k][i][j]-Q_t1[k][i][j-1]))
                        if k==0:
                            P1= (PN[k+1]+PN[k])/2
                            P2= (PN[k+2]+PN[k+1])/2
                            W9= (Wt[k+1][i][j]*P1+Wt[k][i][j]*P2)/(P1+P2)
                            W1= ((Wt[k][i+1][j]+Wt[k][i][j])+(Ws[i][j]+Ws[i+1][j]))/4
                            W2=((Wt[k][i][j+1]+Wt[k][i][j])+(Ws[i][j+1]+Ws[i][j]))/4
                            Ut2[k][i][j]=Ut2[k][i][j]-W1*(Ut1[k+1][i][j]-Ut1[k][i][j])/(PN[k+1]-PN[k])
                            Vt2[k][i][j]=Vt2[k][i][j]-W2*(Vt1[k+1][i][j]-Vt1[k][i][j])/(PN[k+1]-PN[k])
                            TEt2[k][i][j]=TE_t2[k][i][j]-Wt[k][i][j]*(TE_t1[k+1][i][j]-TE_t1[k][i][j])/(PN[k+1]-PN[k])
                            Qt2[k][i][j]= Q_t2[k][i][j]-Wt[k][i][j]*(Q_t1[k+1][i][j]-Q_t1[k][i][j])/(PN[k+1]-PN[k])
                            PSt2[i][j]=-2*M1*(Ut1[k][i+1][j]*(PSt1[i+1][j]-PSt1[i][j]) \
                                -Ut1[k][i][j]*(PS_t1[i][j]-PS_t1[i-1][j]) \
                                +Vt1[k][i][j+1]*(PS_t1[i][j+1]-PS_t1[i][j]) \
                                -Vt1[k][i][j]*(PS_t1[i][j]-PS_t1[i][j-1]))
                            PS_t2[i][j]=PS_t2[i][j]+W9-(((Ut1[k+1][i+1][j]-Ut1[k+1][i][j]) \
                                +(Vt1[k+1][i][j+1]-Vt1[k+1][i][j])+(Ut1[k][i+1][j]-Ut1[k][i][j]) \
                                +(Vt1[k][i][j+1]-Vt1[k][i][j]))*2*M1)*(PS_t1[i][j]-900)
                        else:
                            P1= (PN[k-1]+PN[k])/2
                            P2= (PN[k]+PN[k+1])/2
                            Ut2[k][i][j]= Ut2[k][i][j]-(((Wt[k][i+1][j]+Wt[k][i][j])*(PN[k]-P2) \
                                +(Wt[k+1][i+1][j]+Wt[k+1][i][j])*(P1-PN[k]))/(2*(P1-P2)) \
                                *((Ut1[k-1][i][j]-Ut1[k][i][j])*(PN[k]-PN[k+1])/(PN[k-1]-PN[k])) \
                                +((Ut1[k][i][j]-Ut1[k+1][i][j])*(PN[k-1]-PN[k])/(PN[k]-PN[k+1])))/(PN[k-1]-PN[k+1])
                                 
                            Vt2[k][i][j]= Vt2[k][i][j]-(((Wt[k][i][j+1]+Wt[k][i][j])*(PN[k]-P2) \
                                +(Wt[k+1][i][j+1]+Wt[k+1][i][j])*(P1-PN[k]))/(2*(P1-P2)) \
                                *((Vt1[k-1][i][j]-Vt1[k][i][j])*(PN[k]-PN[k+1])/(PN[k-1]-PN[k])) \
                                +((Vt1[k][i][j]-Vt1[k+1][i][j])*(PN[k-1]-PN[k])/(PN[k]-PN[k+1])))/(PN[k-1]-PN[k+1])
                            
                            TEt2[k][i][j]=TEt2[k][i][j]-Wt[k][i][j]*((TEt1[k-1][i][j]-TEt1[k][i][j]) \
                                *(PN[k]-PN[k+1])/(PN[k-1]-PN[k])+(TEt1[k][i][j]-TEt[k+1][i][j])*(PN[k+1]-PN[k])/(PN[k]-PN[k+1]))/(PN[k-1]-PN[k+1])
                            
                            Qt2[k][i][j]= Qt2[k][i][j]-Wt[k][i][j]*((Qt1[k-1][i][j]-Qt1[k][i][j])* \
                                (PN[k]-PN[k+1])/(PN[k-1]-PN[k])+(Qt1[k][i][j]-Qt1[k+1][i][j])* \
                                (PN[k-1]-PN[k])/(PN[k]-PN[k+1]))/(PN[k-1]-PN[k+1])
                            
                                
    print("Khoi tao thanh cong")
if __name__ == '__main__':
    pass