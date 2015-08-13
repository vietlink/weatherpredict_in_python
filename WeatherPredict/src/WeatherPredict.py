'''
Created on Aug 10, 2015

@author: ngo


'''
from __future__ import division
from math import pi, sin, cos
import time
X=50
Y=40
K=5
R=287.0
CP=1005.0
M=1.0
N=8
PN=[1000.0, 900.0, 650.0, 300.0, 150.0]
P0=900.0
det=1200.0
det1= 2*det
dex=100000.0
F=14.584*(10**(-5))
NO_OF_DECIMAL=3
t=[18.0, 8.0, -41.0, -87.0, -233.0]
Goc=[pi/12, pi/3, 2*pi/3, 8*pi/9, 35*pi/36]
Gio=[5.0, 10.8, 18, 20.2, 19.1]
Zcao=[110.0, 980.0, 4940.0, 7880.0, 14000.0]
M1= M/(4*det)
RC=R/CP
#dataPath="C:\Users\ngo\Desktop\temp"

Ut=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Ut1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Ut2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

Vt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Vt1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Vt2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

TE_t=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
TE_t1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
TE_t2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

Q_t=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Q_t1=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Q_t2=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

PHI=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]
Wt=[[[0 for j in range(Y)]for i in range(X)]for k in range(K)]

PS= [[0 for j in range(Y)]for i in range(X)]
PS_t1= [[0 for j in range(Y)]for i in range(X)]
PS_t2= [[0 for j in range(Y)]for i in range(X)]
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
                Ut[k][i][j]=round(Gio[k]*cgoc, 3)
                Vt[k][i][j]= round(Gio[k]*sgoc, 3)
                TE_t[k][i][j]= round((Tt*((1000/Ptb)**0.286)), 3)
                Q_t[k][i][j]=0
                PHI[k][i][j]=Zcao[k]
                Wt[k][i][j]=0
                Ut1[k][i][j]=Ut[k][i][j]
                Vt1[k][i][j]=Vt[k][i][j]
                TE_t1[k][i][j]=TE_t[k][i][j]
                Q_t1[k][i][j]=Q_t[k][i][j]
        # time.sleep(2)
    for i in range(X):
        for j in range(Y):
            PS[i][j]=P0
            Ws[i][j]=0
            PS_t1[i][j]=PS[i][j]
    print("Khoi tao thanh cong")

def DuDoan():
    for k in range(K):
        for i in range (1, X-1):
            for j in range (1, Y-1):
                Ut2[k][i][j]=-M*(PHI[k][i+1][j]-PHI[k][i][j])/dex \
                        -M1*((Ut1[k][i][j]+Ut1[k][i+1][j])*(Ut1[k][i+1][j]-Ut1[k][i][j])+(Ut1[k][i][j]+Ut1[k][i-1][j])*(Ut1[k][i][j]-Ut1[k][i-1][j])) \
                        +F*(Vt1[k][i][j]+Vt1[k][i][j-1]+Vt1[k][i+1][j]+Vt1[k][i+1][j-1])/4 \
                        -M1*((Vt1[k][i][j]+Vt1[k][i+1][j])*(Ut1[k][i][j+1]-Ut1[k][i][j])+(Vt1[k][i][j-1]+Vt1[k][i+1][j-1])*(Ut1[k][i][j-1]-Ut1[k][i][j]))
                Ut2[k][i][j]=round(Ut2[k][i][j], 3)
                Vt2[k][i][j]= -M*(PHI[k][i][j+1]-PHI[k][i][j])/dex \
                        - M1*((Ut1[k][i][j]+Ut1[k][i][j+1])*(Vt1[k][i+1][j]-Vt1[k][i][j])+(Ut1[k][i-1][j]+Ut1[k][i-1][j+1])*(Vt1[k][i][j]-Vt1[k][i-1][j])) \
                        - M1*((Vt1[k][i][j]+Vt1[k][i][j+1])*(Vt1[k][i][j+1]-Vt1[k][i][j])+(Vt1[k][i][j]+Vt1[k][i][j-1])*(Vt1[k][i][j]-Vt1[k][i][j-1])) \
                        -F*(Ut1[k][i][j]+Ut1[k][i-1][j]+Ut1[k][i][j+1]+Vt1[k][i-1][j+1])/4
                Vt2[k][i][j]=round(Vt2[k][i][j], 3)
                if k==(K-1):
                    P1= (PN[k]+PN[k-1])/2
                    P2=25
                    P5=(PN[k]-P2)/(2*(P1-P2))
                    Ut2[k][i][j]= Ut2[k][i][j]-((Wt[k-1][i+1][j]+Wt[k-1][i][j])*P5*(Ut1[k][i][j]-Ut1[k-1][i][j]))/(PN[k]-PN[k-1])
                    Ut2[k][i][j]=round(Ut2[k][i][j], 3)
                    Vt2[k][i][j]= Vt2[k][i][j]-((Wt[k-1][i][j+1]+Wt[k-1][i][j])*P5*(Vt1[k][i][j]-Vt1[k-1][i][j]))/(PN[k]-PN[k-1])
                    Vt2[k][i][j]=round(Vt2[k][i][j], 3)
                    TE_t2[k][i][j]=0
                    Q_t2[k][i][j]=0
                else:
                    U1= (Ut1[k][i+1][j]+Ut1[k+1][i+1][j])/2
                    U2= (Ut1[k][i][j]+Ut1[k+1][i][j])/2
                    V1= (Vt1[k][i][j+1]+Vt1[k+1][i][j+1])/2
                    V2=(Vt1[k][i][j]+Vt1[k+1][i][j])/2
                    TE_t2[k][i][j]=-2*M1*(U1*(TE_t1[k][i+1][j]-TE_t1[k][i][j]) \
                                -U2*(TE_t1[k][i][j]-TE_t1[k][i-1][j]) \
                                +V1*(TE_t1[k][i][j+1]-TE_t1[k][i][j]) \
                                -V2*(TE_t1[k][i][j]-TE_t1[k][i][j-1]))
                    TE_t2[k][i][j]=round(TE_t2[k][i][j], 3)
                    Q_t2[k][i][j]=-2*M1*(U1*(Q_t1[k][i+1][j]-Q_t1[k][i][j]) \
                                -U2*(Q_t1[k][i][j]-Q_t1[k][i-1][j]) \
                                +V1*(Q_t1[k][i][j+1]-Q_t1[k][i][j]) \
                                -V2*(Q_t1[k][i][j]-Q_t1[k][i][j-1]))
                    Q_t2[k][i][j]=round(Q_t2[k][i][j], 3)
                    if k==0:
                        P1= (PN[k+1]+PN[k])/2
                        P2= (PN[k+2]+PN[k+1])/2
                        W9= (Wt[k+1][i][j]*P1+Wt[k][i][j]*P2)/(P1+P2)
                        W1= ((Wt[k][i+1][j]+Wt[k][i][j])+(Ws[i][j]+Ws[i+1][j]))/4
                        W2=((Wt[k][i][j+1]+Wt[k][i][j])+(Ws[i][j+1]+Ws[i][j]))/4
                        Ut2[k][i][j]=Ut2[k][i][j]-W1*(Ut1[k+1][i][j]-Ut1[k][i][j])/(PN[k+1]-PN[k])
                        Ut2[k][i][j]=round(Ut2[k][i][j], 3)
                        Vt2[k][i][j]=Vt2[k][i][j]-W2*(Vt1[k+1][i][j]-Vt1[k][i][j])/(PN[k+1]-PN[k])
                        Vt2[k][i][j]=round(Vt2[k][i][j], 3)
                        TE_t2[k][i][j]=TE_t2[k][i][j]-Wt[k][i][j]*(TE_t1[k+1][i][j]-TE_t1[k][i][j])/(PN[k+1]-PN[k])
                        TE_t2[k][i][j]=round(TE_t2[k][i][j], 3)
                        Q_t2[k][i][j]= Q_t2[k][i][j]-Wt[k][i][j]*(Q_t1[k+1][i][j]-Q_t1[k][i][j])/(PN[k+1]-PN[k])
                        Q_t2[k][i][j]=round(Q_t2[k][i][j], 3)
                        PS_t2[i][j]=-2*M1*(Ut1[k][i+1][j]*(PS_t1[i+1][j]-PS_t1[i][j])
                            -Ut1[k][i][j]*(PS_t1[i][j]-PS_t1[i-1][j])
                            +Vt1[k][i][j+1]*(PS_t1[i][j+1]-PS_t1[i][j])
                            -Vt1[k][i][j]*(PS_t1[i][j]-PS_t1[i][j-1]))
                        PS_t2[i][j]=round(PS_t2[i][j], 3)
                        PS_t2[i][j]=PS_t2[i][j]+W9-(((Ut1[k+1][i+1][j]-Ut1[k+1][i][j]) \
                            +(Vt1[k+1][i][j+1]-Vt1[k+1][i][j])+(Ut1[k][i+1][j]-Ut1[k][i][j]) \
                            +(Vt1[k][i][j+1]-Vt1[k][i][j]))*2*M1)*(PS_t1[i][j]-900)
                        PS_t2[i][j]=round(PS_t2[i][j], 3)
                    else:
                        P1= (PN[k-1]+PN[k])/2
                        P2= (PN[k]+PN[k+1])/2
                        Ut2[k][i][j]= Ut2[k][i][j]-(((Wt[k][i+1][j]+Wt[k][i][j])*(PN[k]-P2) \
                            +(Wt[k+1][i+1][j]+Wt[k+1][i][j])*(P1-PN[k]))/(2*(P1-P2)) \
                            *((Ut1[k-1][i][j]-Ut1[k][i][j])*(PN[k]-PN[k+1])/(PN[k-1]-PN[k])) \
                            +((Ut1[k][i][j]-Ut1[k+1][i][j])*(PN[k-1]-PN[k])/(PN[k]-PN[k+1])))/(PN[k-1]-PN[k+1])
                        Ut2[k][i][j]=round(Ut2[k][i][j], 3)
                        Vt2[k][i][j]= Vt2[k][i][j]-(((Wt[k][i][j+1]+Wt[k][i][j])*(PN[k]-P2) \
                            +(Wt[k+1][i][j+1]+Wt[k+1][i][j])*(P1-PN[k]))/(2*(P1-P2)) \
                            *((Vt1[k-1][i][j]-Vt1[k][i][j])*(PN[k]-PN[k+1])/(PN[k-1]-PN[k])) \
                            +((Vt1[k][i][j]-Vt1[k+1][i][j])*(PN[k-1]-PN[k])/(PN[k]-PN[k+1])))/(PN[k-1]-PN[k+1])
                        Vt2[k][i][j]=round(Vt2[k][i][j], 3)
                        TE_t2[k][i][j]=TE_t2[k][i][j]-Wt[k][i][j]*((TE_t1[k-1][i][j]-TE_t1[k][i][j]) \
                            *(PN[k]-PN[k+1])/(PN[k-1]-PN[k])+(TE_t1[k][i][j]-TE_t[k+1][i][j])*(PN[k+1]-PN[k])/(PN[k]-PN[k+1]))/(PN[k-1]-PN[k+1])
                        TE_t2[k][i][j]=round(TE_t2[k][i][j], 3)
                        Q_t2[k][i][j]= Q_t2[k][i][j]-Wt[k][i][j]*((Q_t1[k-1][i][j]-Q_t1[k][i][j])* \
                            (PN[k]-PN[k+1])/(PN[k-1]-PN[k])+(Q_t1[k][i][j]-Q_t1[k+1][i][j])* \
                            (PN[k-1]-PN[k])/(PN[k]-PN[k+1]))/(PN[k-1]-PN[k+1])
                        Q_t2[k][i][j]=round(Q_t2[k][i][j], 3)
    for k in range(K):
        for i in range(1,X-1):
            for j in range (1, Y-1):
                Ut2[k][i][j]= Ut[k][i][j]+det1*Ut2[k][i][j]
                Vt2[k][i][j]= Vt[k][i][j]+det1*Vt2[k][i][j]
                TE_t2[k][i][j]= TE_t[k][i][j]+det1*TE_t2[k][i][j]
                Q_t2[k][i][j]= Q_t[k][i][j]+det1*Q_t2[k][i][j]
                Ut[k][i][j]=Ut1[k][i][j]
                Ut1[k][i][j]=Ut2[k][i][j]
                Vt[k][i][j]=Vt1[k][i][j]
                Vt1[k][i][j]=Vt2[k][i][j]
                TE_t[k][i][j]=TE_t1[k][i][j]
                TE_t1[k][i][j]=TE_t2[k][i][j]
                Q_t[k][i][j]=Q_t1[k][i][j]
                Q_t1[k][i][j]=Q_t2[k][i][j]
    for i in range(1, X-1):
        for j in range (1, Y-1):
            PS_t2[i][j]= PS[i][j]+det1*PS_t2[i][j]
            PS[i][j]=PS_t1[i][j]
            PS_t1[i][j]=PS_t2[i][j]

def ChuanDoan():
    for k in range(K):
        for i in range (1,X-1):
            for j in range (1,Y-1):
                R0= (TE_t1[k][i][j]*((PN[k]/P0)**RC))
                Ro= PN[k]/(R*R0)
                TV=(TE_t1[k][i][j]*(1+0.61*Q_t1[k][i][j]))
                if k==0:
                    P1=(PN[k]-PN[k+1])/2
                    P2=(PN[k+1]-PN[k+2])/2
                    P3=(PN[k+1]+PN[k+2])/2
                    V_TB=-M*(((Ut1[k][i+1][j]-Ut1[k][i][j]) \
                            +(Vt1[k][i][j+1]-Vt1[k][i][j]))*P2 \
                            +((Ut1[k+1][i+1][j]-Ut1[k+1][i][j]) \
                            +(Vt1[k+1][i][j+1]-Vt1[k+1][i][j]))*P1)/(dex*(P1+P2))
                    V_TB=round(V_TB,3)
                    PA3= PN[k+1]-P3
                    PA2= PN[k]-PN[k+1]
                    PA1=PN[k]-P3
                    Wt[k][i][j]=(-V_TB*PA1+(Ws[i][j]*PA3/PA2-Wt[k+1][i][j]*PA2/PA3))/(PA3/PA2-PA2/PA3)
                    Wt[k][i][j]=round(Wt[k][i][j], 3)
                    PHI[k][i][j]=(PHI[k+1][i][j]+R/Ro*TV*((PN[k]/P0)**RC)*(-PA2))
                    PHI[k][i][j]=round(PHI[k][i][j], 3)
                elif k==(K-1):
                    PA0= PN[k]-PN[k-1]
                    PHI[k][i][j]=(PHI[k-1][i][j]+R/Ro*TV*((PN[k]/P0)**RC)*PA0)
                    PHI[k][i][j]=round(PHI[k][i][j], 3)
                    Wt[k][i][j]=0
                else:
                    PP1= PN[k-1]-PN[k+1]
                    PP2= PN[k-1]-PN[k]
                    PP3= PN[k]-PN[k+1]
                    PHI[k][i][j]=(R/Ro*TV*((PN[k]/P0)**RC)*PP1+PHI[k-1][i][j]*PP3/PP2-PHI[k+1][i][j]*PP2/PP3)/(PP3/PP2-PP2/PP3)
                    PHI[k][i][j]=round(PHI[k][i][j], 3)
                    V_TB=-M*((Ut1[k][i+1][j]-Ut1[k][i][j])
                            +(Vt1[k][i][j+1]-Vt1[k][i][j])
                            +(Ut1[k+1][i+1][j]-Ut1[k+1][i][j])
                            +(Vt1[k+1][i][j+1]-Vt1[k+1][i][j]))/(2*dex)
                    V_TB=round(V_TB,3)
                    Wt[k][i][j]=(-V_TB*PP1+Wt[k-1][i][j]*PP3/PP2-Wt[k+1][i][j]*PP2/PP1)/(PP3/PP2- PP2/PP3)
                    Wt[k][i][j]=round(Wt[k][i][j], 3)
    P4=(PN[1]+PN[2])/2
    for i in range(1,X-1):
        for j in range(1,Y-1):
            VTS= M*((Ut1[1][i+1][j]-Ut1[1][i][j])+(Vt1[1][i][j+1]-Vt1[1][i][j]))/dex
            VTS=round(VTS,3)
            Ws[i][j]=Wt[1][i][j]+VTS*(P4- PN[1])
            Ws[i][j]=round( Ws[i][j],3)
def printResult():
    print("U=")
    print3D(K,X,Y,Ut2)
    print("V=")
    print3D(K,X,Y,Vt2)
    print("TE=")
    print3D(K,X,Y,TE_t2)
    print("Q=")
    print3D(K,X,Y,Q_t2)
    print("Wt=")
    print3D(K,X,Y,Wt)
    print("PHI=")
    print3D(K,X,Y,PHI)
    print("PS=")
    print2D(X, Y, PS_t2)
def print3D(k, i, j, a=[[[]]]):
    for k in range(K):
        print("k=%d" %(k+1))
        print2D(i, j, a[k])

def print2D(i, j, a=[[]]):
    for i in range (X):
        for j in range (Y):
            # print (a[i][j])
            print(a[i][j], end=" ")
        print()
if __name__ == '__main__':
    print("CHUONG TRINH DU DOAN VA CHUAN DOAN THOI TIET")
    print("-------------------------------------------")
    init()
    print3D(K,X,Y,Ut1)
    for n in range(N):
        print(det1)
        det1=2*det
        if n==0: det1=det
        DuDoan()
        print("Ket thuc viec du bao")
        ChuanDoan()
        print("Ket thuc viec chuan doan")
        print("Ket thuc tinh toan cho buoc thoi gian %d" %(n+1))
    print("Ket thuc tinh toan")
    printResult()
