!#usr/bin/python
#######cell 2##############
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import argparse
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
parser.add_argument("p",help="path to the right directory") ###*
#parser.add_argument("r", type=int, help="number of runs")###*
#parser.add_argument("j", type=int, help="number of jumps")###*
args=parser.parse_args() ###*
pth=args.p ###*
pth='../'
folder=''#PAPER/'
subf=''#PLL2/'
subf2=''#RUNS/'
runsx='RUN8/'
nx='n0/'
xi=range(1,(args.j+1))###*xi=range(1,11)
dbina=500
dbinb=50
plt.style.use('bmh')
print plt.style.available

########cell 3##################
###*xi=range(1,11)
ltj={}
nhj={}
xtj=[]
ytj=[]
ztj=[]
n=0
for j in xi:

    fin=pth+folder+subf+subf2+runsx+nx+'pts'+str(j)+'plotdata.p'
    #print fin
    f=open(fin,"rb")
    A=pickle.load(f)
    f.close()
    lj=A[1]
    nj=A[2]
    tj=[]
    #tnj=[]
    for i in range(len(nj)):
        tj.append(i+n*len(nj))

    xtj.append(n*len(nj))
    ytj.append(nj[0])
    ztj.append(lj[0])
    n+=1
    ltj[j]=[tj,lj]
    nhj[j]=[tj,nj]

    #raw_input()
fig, axesa = plt.subplots(1,figsize=(10, 8))

for i in ltj.keys():
     axesa.plot(ltj[i][0],ltj[i][1],"-")
axesa.stem(xtj,ztj,linefmt='--', markerfmt=' ', basefmt=' ')


fig, axesb = plt.subplots(1,figsize=(10, 8))

for i in nhj.keys():
    axesb.plot(nhj[i][0],nhj[i][1],"-")
    #axesb.axvline(nhj[i][0][0],0.0,nhj[i][1][0], color='k', linestyle='--')
axesb.stem(xtj,ytj,linefmt='--', markerfmt=' ', basefmt=' ')

#############cell 4##################
xtj

#############cell 5################
nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/']
fig, axesa = plt.subplots(1,figsize=(10, 8))
fig, axesb = plt.subplots(1,figsize=(10, 8))

color=iter(cm.rainbow(np.linspace(0,1,len(nX))))
u=0
#nx='n1/'
for kj in nX:
    ltj={}
    nhj={}
    xtj=[]
    ytj=[]
    ztj=[]
    n=0
    for j in xi:

        fin=pth+folder+subf+subf2+runsx+kj+'pts'+str(j)+'plotdata.p'
        #print fin
        f=open(fin,"rb")
        A=pickle.load(f)
        f.close()
        lj=A[1]
        nj=A[2]
        tj=[]
        #tnj=[]
        for i in range(len(nj)):
            tj.append(i+n*len(nj))

        xtj.append(n*len(nj))
        ytj.append(nj[0])
        ztj.append(lj[0])
        n+=1
        ltj[j]=[tj,lj]
        nhj[j]=[tj,nj]

    #raw_input()
    #fig, axesa = plt.subplots(1,figsize=(10, 8))
    c=next(color)
    for i in ltj.keys():
         axesa.plot(ltj[i][0],ltj[i][1],c=c)
    if kj=='n0/':
        axesa.stem(xtj,ztj,linefmt='--', markerfmt='bo', basefmt='r-')
        axesb.stem(xtj,ytj,linefmt='--', markerfmt='bo', basefmt='r-')


    #fig, axesb = plt.subplots(1,figsize=(10, 8))

    for i in nhj.keys():
        axesb.plot(nhj[i][0],nhj[i][1],c=c)
        #axesb.axvline(nhj[i][0][0],0.0,nhj[i][1][0], color='k', linestyle='--')
    #axesb.stem(xtj,ytj,linefmt='--', markerfmt='bo', basefmt='r-')

#############cell 6###############
    #nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/'] #Parameters C
rnX=[]
for mu in range (19):
    rnX.append('RUN'+str(mu)+'/')                          #RUNS R0,R1,...,
###*xi=range(1,11) #jumps
print rnX
#raw_input()
#############################################################
n=0
M=0
t=[]

NAV={}
LAV={}
STDN={}
STDL={}

for pc in nX: #n0, n1, etc
    AVN={}
    AVL={}
    for rj in rnX: #R0, R1, R2, ...
        #n=0
        L=[]
        N=[]

        for ji in xi: #j1, j2, j2,j3

            fin=pth+folder+subf+subf2+ rj + pc +'pts'+str(ji)+'plotdata.p'
            #print fin
            f=open(fin,"rb")
            A=pickle.load(f)
            #print fin, len(A)
            f.close()
            lz=A[1]
            nz=A[2]
            for k in lz:
                if M==0:
                    t.append(n)
                    n+=1.0
                L.append(k)
            for k in nz:
                N.append(k)
        M=1
        AVN[rj]=N
        AVL[rj]=L

    avl=[]
    stdl=[]
    avn=[]
    stdn=[]
    print(AVN.keys())

    rj=0
    for tr in t:
        avx=[]
        avx2=[]
        for mu in AVN.keys():
            avx.append(AVN[mu][rj])
            avx2.append(AVL[mu][rj])
        avl.append(np.mean(avx2))
        stdl.append(np.std(avx2))

        avn.append(np.mean(avx))
        stdn.append(np.std(avx))
        rj+=1
    NAV[pc]=avn
    LAV[pc]=avl
    STDN[pc]=stdn
    STDL[pc]=stdl

print len(t)
            #raw_input()

#############################################################
##############cell 7######################
for ck in NAV.keys():
    fig, axesa = plt.subplots(1,figsize=(10, 8))
    fig, axesb = plt.subplots(1,figsize=(10, 8))

    ytjb=[]
    ytja=[]
    for i in xtj:
        ytjb.append(NAV[ck][i])
        ytja.append(LAV[ck][i])

    axesb.plot(t,NAV[ck])

    yerrminus=[]
    yerrplus=[]
    l=0
    for sj in NAV[ck]:
        yerrminus.append(sj-STDN[ck][l])
        yerrplus.append(sj+STDN[ck][l])
        l+=1

    axesb.fill_between(t, yerrminus, yerrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    axesb.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    yerrminusb=[]
    yerrplusb=[]
    l=0
    for sj in LAV[ck]:
        yerrminusb.append(sj-STDL[ck][l])
        yerrplusb.append(sj+STDL[ck][l])
        l+=1


    axesa.plot(t,LAV[ck])
    axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')

    axesa.fill_between(t, yerrminusb, yerrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

  #################cell 8####################
print nX #pars
print rnX #runs
print xi #jumps
print LAV.keys()
print folder, subf, subf2

##############cell 9#####################
#raw_input()

#for rn in rnX:
ALLSERIES={}
kt=0
n=0
#clr=iter(cm.rainbow(np.linspace(0,1,len(xi))))
tj=[]
for prt in nX:
    fig, axesa = plt.subplots(1,figsize=(10, 8))
    fig, axesb = plt.subplots(1,figsize=(10, 8))
    #####################


    #ytjb=[]
    #ytja=[]
    #for i in xtj:
    #    ytjb.append(NAV[ck][i])
    #    ytja.append(LAV[ck][i])

    axesb.plot(t,NAV[prt],'black')

    yerrminus=[]
    yerrplus=[]
    l=0
    for sj in NAV[prt]:
        yerrminus.append(sj-STDN[prt][l])
        yerrplus.append(sj+STDN[prt][l])
        l+=1

    axesb.fill_between(t, yerrminus, yerrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesb.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    yerrminusb=[]
    yerrplusb=[]
    l=0
    for sj in LAV[prt]:
        yerrminusb.append(sj-STDL[prt][l])
        yerrplusb.append(sj+STDL[prt][l])
        l+=1


    axesa.plot(t,LAV[ck],'black')
    #axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')

    axesa.fill_between(t, yerrminusb, yerrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')
##################


    for rn in rnX:
        nz=[]
        lz=[]
        #tj=[]
        for jp in xi:
            file= pth+folder+subf+subf2+rn+prt+'pts'+str(jp)+'plotdata.p'
            #print file
            f=open(file,"rb")
            A=pickle.load(f)
            f.close()
            lz.extend(A[1])
            nz.extend(A[2])
            if kt==0:
                for i in range(len(A[1])):
                    tj.append(i+n*len(A[1]))
                n+=1
            #raw_input()
        kt=1
        print len(tj), len(lz), len(nz)

        #c=next(clr)
        #fig, axesa = plt.subplots(1,figsize=(10, 8))
        axesa.plot(tj,lz)#,c=c)
        axesb.plot(tj,nz)#,c=c)

#################cell 10#######################
Data=[t,LAV,NAV,STDN,STDL]
name="CDATAI.p"
pickle.dump(Data,open(name,"wb"))
###############cell 11#######################
'''print nX #pars
print rnX #runs
print xi #jumps
print LAV.keys()
print folder, subf, subf2
runsx='RUN0/'
print runsx

##################cell 12####################
###*xi=range(1,11)
ltj={}
nhj={}
xtj=[]
ytj=[]
ztj=[]
tnets=[]
tneffs=[]

n=0
for j in xi:

    fin=folder+subf+subf2+runsx+nx+'pts'+str(j)+'plotdata.p'
    #print fin
    f=open(fin,"rb")
    A=pickle.load(f)
    print len(A)
    f.close()
    lj=A[1]
    nj=A[2]
    ntes=A[8]
    neffs=A[9]
    tj=[]
    #tnj=[]
    for i in range(len(nj)):
        tj.append(i+n*len(nj))

    xtj.append(n*len(nj))
    ytj.append(nj[0])
    ztj.append(lj[0])
    n+=1
    ltj[j]=[tj,lj]
    nhj[j]=[tj,nj]
    #tnets[j]=[tj,ntes]
    #tneffs[j]=[tj,neffs]
    #raw_input()
fig, axesa = plt.subplots(1,figsize=(10, 8))

for i in ltj.keys():
     axesa.plot(ltj[i][0],ltj[i][1],"r--o")
axesa.stem(xtj,ztj,linefmt='--', markerfmt='bo', basefmt='r-')


fig, axesb = plt.subplots(1,figsize=(10, 8))

for i in nhj.keys():
    axesb.plot(nhj[i][0],nhj[i][1],"r--o")

#for i in tnets.keys():
#    axesb.plot(tnets[i][0],tnets[i][1],"b")

    #axesb.axvline(nhj[i][0][0],0.0,nhj[i][1][0], color='k', linestyle='--')
axesb.stem(xtj,ytj,linefmt='--', markerfmt='bo', basefmt='r-')'''
