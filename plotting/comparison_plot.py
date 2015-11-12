#!usr/bin/python
#####################cell 1#########################
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import argparse
import os
plt.style.use('bmh')
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
########each directory has a different DT
parser.add_argument("p1",help="path to the right directory")
parser.add_argument("p2", help="path to the second directory")
parser.add_argument("p3", help="path to the third directory")
parser.add_argument("p4", help="path to the last directory")
parser.add_argument("p5",help="path to the directory no jumps")
#parser.add_argument("r", type=int, help="number of runs for directory")
###*parser.add_argument("j", type=int, help="number of jumps")###*
args=parser.parse_args() ###*
pth1=args.p1
pth2=args.p2
pth3=args.p3
pth4=args.p4
pthno=args.p5
#RUNS=args.r
main_path=[pth1,pth2,pth3,pth4]
print pth1,pth2,pth3,pth4,pthno
###*xi=range(1,(args.j+1))###*
##############files with data##########################
n1=pth1+"CDATAV.p"
n2=pth2+"CDATAV.p"
n3=pth3+"CDATAV.p"
n4=pth4+"CDATAV.p"
nno=pthno+"CDATAV.p"
print n1, n2, n3, n4#*,nno
f1=open(n1,"rb")
NOPE1=pickle.load(f1)
f1.close()
f2=open(n2,"rb")
NOPE2=pickle.load(f2)
f2.close()
f3=open(n3,"rb")
NOPE3=pickle.load(f3)
f3.close()
f4=open(n4,"rb")
NOPE4=pickle.load(f4)
f4.close()
fno=open(nno,"rb")
NOJU=pickle.load(fno)
fno.close()

#######plot same Qi different DT#################
#print NOPE1[0][1], 'tempo?'
#print NOPE1[0][2]

#Data=[t,LAV,NAV,STDN,STDL]
T1=NOPE1[0]
T2=NOPE2[0]
T3=NOPE3[0]
T4=NOPE4[0]
TNO=NOJU[0]

assert T1==T2==T4

pts1=NOPE1[1].keys()
pts2=NOPE2[1].keys()
pts3=NOPE3[1].keys()
pts4=NOPE4[1].keys()
ptsno=NOJU[1].keys()

assert pts1==pts2==pts3==pts4

d={}
d['DT5000']=["$\Delta T=5.0\\times 10^3$",NOPE1,T1]
d['DT10000']=["$\Delta T= 1.0\\times 10^4$",NOPE2,T2]
d['DT15000']=["$\Delta T= 1.5 \\times 10^4$",NOPE3,T3]
d['DT20000']=["$\Delta T= 2.0\\times 10^4$",NOPE4,T4]
####no need for this d['infinity']=["$\Delta T=\infty$",NOJU,TNO]

######################################################################################################
#plotting total length over time for same c and different DT (it miss the infinity and color map)
######################################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    axesa.plot(T1,NOPE1[1][x],'c-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T2,NOPE2[1][x],'m-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T3,NOPE3[1][x],'k-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T4,NOPE4[1][x],'g-',label="$\Delta T= 2.0\\times 10^4$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')'''

####################################################################################################
#plotting len of eff and tes over time for same c and different DT
####################################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))
    figb, axesb=plt.subplots(1,figsize=(10,8)) ###new

    axesa.set_ylabel("$< Lengths >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    axesb.set_ylabel("$< Lengths >_{Ens}$", fontsize=40) ###new
    axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40) ###new
    axesb.xaxis.set_tick_params(labelsize=20)###new
    axesb.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))###new
    axesb.yaxis.set_tick_params(labelsize=20) ###new
    axesb.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))###new
    plt.ticklabel_format(style='sci', scilimits=(0,0)) ###new

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    col=next(color)
    axesa.plot(T1,NOPE1[9][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[10][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T2,NOPE2[9][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[10][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T3,NOPE3[9][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[10][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T4,NOPE4[9][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[10][x],c=col,ls=':')
    col=next(color)
    axesa.plot(TNO,NOJU[9]['n0/'],c=col,ls='-', label="$\Delta T=\infty$")
    axesa.plot(TNO,NOJU[10]['n0/'],c=col,ls=':')

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    m1=np.ployfit(T1,NOPE1[9][x])
    m12=np.polyfit(T1,NOPE1[10][x])
    m2=np.polyfit(T2,NOPE2[9][x])
    m22=np.polyfit(T2,NOPE2[10][x])
    m3=np.polyfit(T3,NOPE3[9][x])
    m32=np.polyfit(T3,NOPE3[10][x])
    m4=np.polyfit(T4,NOPE4[9][x])
    m42=np.polyfit(T4,NOPE4[10][x])
    m5=np.polyfit(TNO,NOJU[9]['n0/'])
    m52=np.polyfit(TNO,NOJU[10]['n0/'])
    col=next(color)
    axesb.plot(m1,c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesb.plot(m12,c=col,ls=':')
    col=next(color)
    axesb.plot(m2,c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesb.plot(m22,c=col,ls=':')
    col=next(color)
    axesb.plot(m3,c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesb.plot(m32,c=col,ls=':')
    col=next(color)
    axesb.plot(m4,c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesb.plot(m42,c=col,ls=':')
    col=next(color)
    axesb.plot(m5,c=col,ls='-', label="$\Delta T=\infty$")
    axesb.plot(m52,c=col,ls=':')

    axesb.legend(loc='best', fancybox=True, framealpha=0.5)

    axesb.set_title(titstr, fontsize=40)

    axesb.set_xlim([0,80000])

    figb.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_te_derivate'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')

    c+=0.1

exit()
################################################################################################
#plotting total number of units over time for different c and same DT (it misses infinity and color map)
#################################################################################################
'''c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    axesa.plot(T1,NOPE1[2][x],'c-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T2,NOPE2[2][x],'m-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T3,NOPE3[2][x],'k-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T4,NOPE4[2][x],'g-',label="$\Delta T= 2.0\\times 10^4$")

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')'''

################################################################################################
#plotting number of tes and eff over time for same c and different DT
#############################################################################################
c=0.1
for x in pts1:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >_{Ens}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    color=iter(cm.rainbow(np.linspace(0,1,5))) ###change 4 when adding new

    col=next(color)
    axesa.plot(T1,NOPE1[5][x],c=col,ls='-',label="$\Delta T=5.0\\times 10^3$")
    axesa.plot(T1,NOPE1[6][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T2,NOPE2[5][x],c=col,ls='-',label="$\Delta T= 1.0\\times 10^4$")
    axesa.plot(T2,NOPE2[6][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T3,NOPE3[5][x],c=col,ls='-',label="$\Delta T= 1.5 \\times 10^4$")
    axesa.plot(T3,NOPE3[6][x],c=col,ls=':')
    col=next(color)
    axesa.plot(T4,NOPE4[5][x],c=col,ls='-',label="$\Delta T= 2.0\\times 10^4$")
    axesa.plot(T4,NOPE4[6][x],c=col,ls=':')
    col=next(color)
    axesa.plot(TNO,NOJU[5]['n0/'],c=col,ls='-',label="$\Delta T=\infty$")
    axesa.plot(TNO,NOJU[6]['n0/'],c=col,ls=':')

    axesa.legend(loc='best', fancybox=True, framealpha=0.5)

    val_c=c
    titstr='$c='+str(c)+'$'
    print titstr
    c+=0.1
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(c-0.1)+'.png',format='png' ,dpi=1200, bbox_inches='tight')

####################################################################################################################################
#same DT different c value
###################################################################################################################################

for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Number$ $of$ $units >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    for y in pts1:

        print x, y
        col=next(color)
        axesa.plot(d[x][2],d[x][1][5][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][6][y],c=col,ls=':')

        axesa.legend(loc='best', fancybox=True, framealpha=0.5)
        c+=0.1

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'unit_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=1200, bbox_inches='tight')

for x in d:
    fig, axesa = plt.subplots(1,figsize=(10, 8))

    axesa.set_ylabel("$< Lengths >$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
    plt.ticklabel_format(style='sci', scilimits=(0,0))

    c=0.1

    color=iter(cm.rainbow(np.linspace(0,1,len(pts1))))

    for y in pts1:

        col=next(color)
        axesa.plot(d[x][2],d[x][1][9][y],c=col,ls='-',label='$c='+str(c)+'$')
        axesa.plot(d[x][2],d[x][1][10][y],c=col,ls=':')

        axesa.legend(loc='best', fancybox=True, framealpha=0.5)
        c+=0.1

    titstr=d[x][0]
    print titstr
    axesa.set_title(titstr, fontsize=40)

    #axesa.set_xscale('log')
    axesa.set_xlim([0,80000])
    #axesa.set_xlim([0,80000])

    fig.savefig('/usr/users/TSL_20/minottoa/images/'+'len_plot_eff_Te'+str(x)+'.png',format='png' ,dpi=1200, bbox_inches='tight')

'''

##########################cell 18#############################
Rtlonga={}#
Rtlongb={}#

rtks=[]
for i in range(9):
    j='n'+str(i)+'/'
    rtks.append(j)
#print rtks

for jn in rtks:
    mua=[]
    mua=np.diff(LONG[1][jn])

    mub=[]
    mub=np.diff(LONG[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtlonga[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtlongb[jn]=avdfb

Rtshorta={}
Rtshortb={}

for jn in rtks:
    mua=[]
    mua=np.diff(SHORT[1][jn])

    mub=[]
    mub=np.diff(SHORT[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtshorta[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtshortb[jn]=avdfb

Rtmoda={}
Rtmodb={}

for jn in rtks:
    mua=[]
    mua=np.diff(MOD[1][jn])

    mub=[]
    mub=np.diff(MOD[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtmoda[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtmodb[jn]=avdfb

Rtmeda={}
Rtmedb={}
for jn in rtks:
    mua=[]
    mua=np.diff(MED[1][jn])

    mub=[]
    mub=np.diff(MED[2][jn])

    n=0
    avdfa=[]
    sn=0.0
    for j in mua:
        sn+=j
        n+=1
        avdfa.append(sn/n)
    Rtmeda[jn]=avdfa

    n=0
    avdfb=[]
    sn=0.0
    for j in mub:
        sn+=j
        n+=1
        avdfb.append(sn/n)

    Rtmedb[jn]=avdfb


Rtnopea={}
Rtnopeb={}

mua=[]
mua=np.diff(NOPE[1]['n0/'])

mub=[]
mub=np.diff(NOPE[2]['n0/'])

n=0
avdfa=[]
sn=0.0
for j in mua:
    sn+=j
    n+=1
    avdfa.append(sn/n)
Rtnopea['n0/']=avdfa

n=0
avdfb=[]
sn=0.0
for j in mub:
    sn+=j
    n+=1
    avdfb.append(sn/n)

Rtnopeb['n0/']=avdfb

##########################cell 19###############################
print Rtshorta.keys(), Rtshortb.keys(), Rtmoda.keys(), Rtmodb.keys(), Rtmeda.keys(), Rtmedb.keys(), Rtlonga.keys(), Rtlongb.keys()

########################cell 20#################################
fig, axesa = plt.subplots(1,figsize=(10, 8))
#fig, axesb = plt.subplots(1,figsize=(10, 8))

c=0.1
for i in rtks:

    fig, axesa = plt.subplots(1,figsize=(10, 8))
    fig, axesb = plt.subplots(1,figsize=(10, 8))
    titstr='C='+str(c)
    print titstr, i
    c+=0.1
#raw_input()

    axesa.set_title(titstr, fontsize=40)
    axesa.plot(Rtshorta[i],label="$\Delta T=5.0\\times10^3$")
    axesa.plot(Rtmeda[i],label="$\Delta T=1.0\\times10^4$")
    axesa.plot(Rtmoda[i],label="$\Delta T=1.5\\times10^4$")
    axesa.plot(Rtlonga[i],label="$\Delta T=2.0\\times10^4$")
    axesa.plot(Rtnopea['n0/'],label="$\Delta T=\infty$")
    axesa.set_xlim([0,20000])
    axesa.set_ylabel("$<\Delta L>_{t}$", fontsize=40)
    axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesa.xaxis.set_tick_params(labelsize=20)
    axesa.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesa.yaxis.set_tick_params(labelsize=20)
    axesa.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesa.legend(loc='best', fancybox=True, framealpha=0.5)




    axesb.set_title(titstr, fontsize=40)
    axesb.plot(Rtshortb[i],label="$\Delta T=5.0\\times10^3$")
    axesb.plot(Rtmedb[i],label="$\Delta T=1.0\\times10^4$")
    axesb.plot(Rtmodb[i],label="$\Delta T=1.5\\times10^4$")
    axesb.plot(Rtlongb[i],label="$\Delta T=2.0\\times10^4$")
    axesb.plot(Rtnopeb['n0/'],label="$\Delta T=\infty$")
    axesb.set_xlim([0,20000])
    axesb.set_ylabel("$<\Delta N_g>_{t}$", fontsize=40)
    axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
    axesb.xaxis.set_tick_params(labelsize=20)
    axesb.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesb.yaxis.set_tick_params(labelsize=20)
    axesb.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.1e'))
    axesb.legend(loc='best', fancybox=True, framealpha=0.5)'''
