#changing notebook file to have a single python script that can run on the cluster

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import argparse ###*
import os ###*
###*#%matplotlib inline
###*pwd
import pickle
###*import numpy as np
###*import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
###*change the path to go to the right directory
###*pth='/usr/users/TSL_20/minottoa/new/' ###*'../'
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
""")) ###*
parser.add_argument("p",help="path to the right directory") ###*
parser.add_argument("r", type=int, help="number of runs")###*
parser.add_argument("j", type=int, help="number of jumps")###*
args=parser.parse_args() ###*
pth=args.p ###*
xi=range(1,(args.j+1))###*
folder=''###*'minottoa/'#PAPER/'
subf=''###*'new/'#PLL2/'
#subf2='RUNSL2/'
runsx='RUN0/'
nx='n0/'
###*xi=range(1,21)
dbina=500
dbinb=50
#plt.style.use('fivethirtyeight')
plt.style.use('bmh')
###*print plt.style.available

###*xi=range(1,11)
###*print xi
ltj={}
nhj={}
xtj=[]
ytj=[]
ztj=[]
n=0
for j in xi:

    fin=pth+folder+subf+runsx+nx+'pts'+str(j)+'plotdata.p'
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
    axesa.plot(ltj[i][0],ltj[i][1],".-", markersize=2, linewidth=1.1)


markerline, stemlines, baseline=axesa.stem(xtj,ztj,linefmt='--', markerfmt='.', basefmt='',stemlineswidth=0.1)
#plt.setp(markerline, 'markerfacecolor', 'b')
#plt.setp(stemlines, 'linewidth', 1)

fig, axesb = plt.subplots(1,figsize=(10, 8))

for i in nhj.keys():
    axesb.plot(nhj[i][0],nhj[i][1],".-", markersize=2, linewidth=1.1)
    #axesb.axvline(nhj[i][0][0],0.0,nhj[i][1][0], color='k', linestyle='--')
#axesb.stem(xtj,ytj,linefmt='--', markerfmt='bo', basefmt='r-')

markerline, stemlines, baseline=axesb.stem(xtj,ytj,linefmt='--', markerfmt='.', basefmt='',stemlineswidth=0.1)

###*print xi
ltj={}
ltja={}
ltjb={}
nhj={}
nhja={}
nhjb={}
xtj=[]
ytj=[]
ztj=[]
n=0
for j in xi:

    fin=pth+folder+subf+runsx+nx+'pts'+str(j)+'plotdata.p'
    #print fin
    f=open(fin,"rb")
    A=pickle.load(f)
    ###*print A
    f.close()
    lj=A[1]
    lja=A[10]
    ljb=A[11]
    print len(lja), len(ljb)
    nj=A[2]
    nja=A[3]
    njb=A[4]
    tj=[]
    #tnj=[]
    for i in range(len(nj)):
        tj.append(i+n*len(nj))

    xtj.append(n*len(nj))
    ytj.append(nj[0])
    ztj.append(lj[0])
    n+=1
    ltj[j]=[tj,lj]
    ltja[j]=[tj,lja]
    ltjb[j]=[tj,ljb]
    nhj[j]=[tj,nj]
    nhja[j]=[tj,nja]
    nhjb[j]=[tj,njb]
    #raw_input()
fig, axesa = plt.subplots(1,figsize=(10, 10))

xtjl=[xtj[1]+i for i in xtj]

###
##fig.suptitle('RXLR effectors length distribution P. Infestans', fontsize=40)
axesa.set_ylabel("$Length$ $(bp)$", fontsize=40)
axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesa.xaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))
###
ms=0.1
kn=0

for i in ltj.keys():
    if kn==0:
        axesa.plot(ltj[i][0],ltj[i][1],marker=".",color='black',alpha=0.85,markersize=0.1,label="total length")
        axesa.plot(ltja[i][0],ltja[i][1],marker=".",color='red',alpha=0.85,markersize=0.1,label="Eff length")
        axesa.plot(ltjb[i][0],ltjb[i][1],marker=".",color='blue',alpha=0.85,markersize=0.1,label="T.E. lenght")
        kn=1
    else:
        axesa.plot(ltj[i][0],ltj[i][1],marker=".",color='black',alpha=0.85,markersize=0.1)
        axesa.plot(ltja[i][0],ltja[i][1],marker=".",color='red',alpha=0.85,markersize=0.1)
        axesa.plot(ltjb[i][0],ltjb[i][1],marker=".",color='blue',alpha=0.85,markersize=0.1)

markerline, stemlines, baseline=axesa.stem(xtj,ztj,linefmt='--.',markerfmt='.',basefmt='',stemlineswidth=0.1)
plt.setp(baseline, 'color','b', 'linewidth', 0)
axesa.legend(loc='best', fancybox=True, framealpha=0.5)
#axesa.stem(xtjl,ltja,linefmt='--', markerfmt='bo', basefmt='r-')
#axesa.stem(xtjl,ltjb,linefmt='--', markerfmt='o', basefmt='r-')

####################################################################################
####################################################################################
####################################################################################
###*uncommented stuff to save pic
fout=folder+subf###*+subf2
namepth=pth+fout+"typrunlength"#.svg" ###*add pth
print namepth

fig.patch.set_alpha(0.5)
#fig.savefig(namepth+'.eps',format='eps' ,dpi=1200, bbox_inches='tight')
###*comment line below because of runtimeerror arise (it should be saving the same image in different format, shouldn't it?)
fig.savefig(namepth+'.png',format='png' ,dpi=1200, bbox_inches='tight')
###*commented below cause jpg is not supported?????
###*fig.savefig(namepth+'.jpg',formar='jpg' ,dpi=1200, bbox_inches='tight')



####################################################################################
####################################################################################
####################################################################################
fig, axesb = plt.subplots(1,figsize=(10, 10))

axesb.set_ylabel("$Number$ $of$ $units$", fontsize=40)
axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))
###
ms=1
kn=0

for i in nhj.keys():

    if kn==0:
        axesb.plot(nhj[i][0],nhj[i][1],marker='.',color='black',alpha=0.85,markersize=1.0,label="total number")
        axesb.plot(nhj[i][0],nhja[i][1],marker='.',color='red',alpha=0.85,markersize=1.0,label="Eff number")
        axesb.plot(nhj[i][0],nhjb[i][1],marker='.',color='blue',alpha=0.85,markersize=1.0,label="T.E. number")
        kn=1

    else:
        axesb.plot(nhj[i][0],nhj[i][1],marker='.', color='black',alpha=0.85,markersize=1.0)
        axesb.plot(nhj[i][0],nhja[i][1],marker='.',color='red',alpha=0.85,markersize=1.0)
        axesb.plot(nhj[i][0],nhjb[i][1],marker='.',color='blue',alpha=0.85,markersize=1.0)



markerlinex, stemlinesx, baselinex=axesb.stem(xtj,ytj,linefmt='--.',markerfmt='.',basefmt='')
plt.setp(baselinex, 'color','b', 'linewidth', 0)
axesb.legend(loc='best', fancybox=True, framealpha=0.5)
###################################################################
###################################################################
###*uncomment lines to make image be saved
#fout=folder+subf+subf2
namepth=pth+fout+"typrunnumbers"#.svg" ###*add pth
print namepth
#fig.set_size_inches(13.5,10.5)
fig.patch.set_alpha(0.5)
#fig.savefig(namepth,dpi=100, bbox_inches='tight')

#fig.savefig(namepth+'.eps',format='eps',dpi=1200, bbox_inches='tight')
fig.savefig(namepth+'.png',format='png' ,dpi=1200, bbox_inches='tight')
#fig.savefig(namepth+'.svg',format='svg', dpi=200, bbox_inches='tight')
###*commented below cause jpg is not supported
###*fig.savefig(namepth+'.jpg',format='jpg',dpi=1200, bbox_inches='tight')

fig, axesb = plt.subplots(1,figsize=(10, 10))
axesb.set_ylabel("$Number$ $of$ $TE's$", fontsize=40)
axesb.set_xlabel("$Number$ $of$ $EG's$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))
###

##########################################
for i in nhj.keys():

    axesb.plot(nhjb[i][1],nhja[i][1],".",markersize=1.0)


from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
axins = zoomed_inset_axes(axesb, 3.0, loc=4)

for i in nhj.keys():

    axins.plot(nhjb[i][1],nhja[i][1],"o",markersize=4.0)

x1, x2, y1, y2 = 350, 470, 900, 1100 #specify the limits
axins.set_xlim(x1, x2) # apply the x-limits
axins.set_ylim(y1, y2) # apply the y-limits
plt.yticks(visible=False)
plt.xticks(visible=False)
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
mark_inset(axesb, axins, loc1=1, loc2=2, fc="none", ec="0.0")

##############################################
#ax_inset=fig.add_axes([0.35,0.17,0.65,0.5])
#ax_inset.xaxis.set_tick_params(labelsize=11)
#ax_inset.yaxis.set_tick_params(labelsize=11)

#for i in nhj.keys():
#    ax_inset.plot(nhjb[i][1],nhja[i][1],"o",markersize=4.0)
#ax_inset.set_ylim(900,1100)
#ax_inset.set_xlim(350,480)

######################################

    #axesb.axvline(nhj[i][0][0],0.0,nhj[i][1][0], color='k', linestyle='--')
#axesb.stem(xtj,ytj,linefmt='--', markerfmt='bo', basefmt='r-')
###############################################################
###############################################################
###############################################################
###*uncomment lines to make images be saved
fout=folder+subf###*+subf2
namepth=pth+fout+"randomwalk"#.eps"###*add pth
##print namepth
#fig.set_size_inches(13.5,10.5)
fig.patch.set_alpha(0.5)
#fig.savefig(namepth+'.eps', dpi=1200, bbox_inches='tight')
fig.savefig(namepth+'.png', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.svgz', dpi=600, bbox_inches='tight')
###*commented below cau8se jpg is not supported
###*fig.savefig(namepth+'.jpg', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.pdf', dpi=1200, bbox_inches='tight')

plt.gcf().canvas.get_supported_filetypes()

nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/'] #Parameters C ###*uncommented this line
###*nX=['n0/']
rnX=[]
import numpy as np
for mu in range(args.r): ###*(50): ###*changed the number of runs
    ###*if mu!=18 and mu!=49: ###*add line to avoid exctiontions
    if all(os.listdir(pth+'RUN'+str(mu)+'/'+x)==[] for x in nX): ###*
        pass ###*
    else: ###*
        rnX.append('RUN'+str(mu)+'/')                          #RUNS R0,R1,...,
###*xi=range(1,11)   ###*in theory we don't have any jumps here is ti fine if i leave it as it is?                                           #jumps
#############################################################
n=0
M=0
t=[]

NAV={}
NAVa={}
NAVb={}

LAV={}
LAVa={}
LAVb={}




STDN={}
STDNa={}
STDNb={}

STDL={}
LSTDa={}
LSTDb={}

for pc in nX: #n0, n1, etc
    AVN={}
    AVNa={}
    AVNb={}

    AVL={}
    AVLa={}
    AVLb={}

    for rj in rnX: #R0, R1, R2, ...
        #n=0
        L=[]
        N=[]
        Na=[]
        Nb=[]
        La=[]
        Lb=[]

        for ji in xi: #j1, j2, j2,j3

            fin=pth+folder+subf+ rj + pc +'pts'+str(ji)+'plotdata.p'
            #print fin
            f=open(fin,"rb")
            A=pickle.load(f)
            f.close()
            lz=A[1]
            nz=A[2]
            nza=A[3]
            nzb=A[4]

            lza=A[10]
            lzb=A[11]

            for k in lz:
                if M==0:
                    t.append(n)
                    n+=1.0
                L.append(k)
            for k in nz:
                N.append(k)
            for k in nza:
                Na.append(k)
            for k in nzb:
                Nb.append(k)
            for k in lza:
                La.append(k)
            for k in lzb:
                Lb.append(k)


        M=1
        AVN[rj]=N
        AVNa[rj]=Na
        AVNb[rj]=Nb
        AVL[rj]=L
        AVLa[rj]=La
        AVLb[rj]=Lb

    avl=[]
    stdl=[]
    avn=[]
    stdn=[]

    avna=[]
    stdna=[]
    avnb=[]
    stdnb=[]

    avla=[]
    stdnla=[]
    avlb=[]
    stdnlb=[]

    print(AVN.keys())

    rj=0
    for tr in t:
        avx=[]
        avx2=[]
        avxa=[]
        avxb=[]
        avx2a=[]
        avx2b=[]

        for mu in AVN.keys():
            avx.append(AVN[mu][rj])
            avxa.append(AVNa[mu][rj])
            avxb.append(AVNb[mu][rj])
            avx2.append(AVL[mu][rj])
            avx2a.append(AVLa[mu][rj])
            avx2b.append(AVLb[mu][rj])

        avl.append(np.mean(avx2))
        stdl.append(np.std(avx2))

        avn.append(np.mean(avx))
        stdn.append(np.std(avx))

        avna.append(np.mean(avxa))
        stdna.append(np.std(avxa))

        avnb.append(np.mean(avxb))
        stdnb.append(np.std(avxb))


        avla.append(np.mean(avx2a))
        stdnla.append(np.std(avx2a))

        avlb.append(np.mean(avx2b))
        stdnlb.append(np.std(avx2b))

        rj+=1
    NAV[pc]=avn
    NAVa[pc]=avna
    NAVb[pc]=avnb
    LAV[pc]=avl
    LAVa[pc]=avla
    LAVb[pc]=avlb

    STDN[pc]=stdn
    STDL[pc]=stdl
    STDNa[pc]=stdna
    STDNb[pc]=stdnb
    LSTDa[pc]=stdnla
    LSTDb[pc]=stdnlb


print len(t)
            #raw_input()

#############################################################

fig1, axesa = plt.subplots(1,figsize=(10, 8))
axesa.set_ylabel("$< Lengths >_{Ens}$", fontsize=40)
axesa.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesa.xaxis.set_tick_params(labelsize=20)
axesa.xaxis.set_major_formatter(mtick.FormatStrFormatter('%2.e'))
axesa.yaxis.set_tick_params(labelsize=20)
axesa.yaxis.set_major_formatter(mtick.FormatStrFormatter('%2.e'))

fig2, axesb = plt.subplots(1,figsize=(10, 10))
axesb.set_ylabel("$<Number$ $of$ $units>_{Ens}$", fontsize=40)
axesb.set_xlabel("$Time$ $(Evolutionary$ $events)$",fontsize=40)
axesb.xaxis.set_tick_params(labelsize=20)
axesb.xaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))
axesb.yaxis.set_tick_params(labelsize=20)
axesb.yaxis.set_major_formatter(mtick.FormatStrFormatter('%1.e'))

ltn=0

for ck in NAV.keys():


    ytjb=[]
    ytjba=[]
    ytjbb=[]
    ytja=[]
    for i in xtj:
        ytjb.append(NAV[ck][i])
        ytjba.append(NAV[ck][i])
        ytjbb.append(NAV[ck][i])
        ytja.append(LAV[ck][i])

    if ltn==0:
        axesb.plot(t,NAV[ck],color="black",label="Average Num of Units")
        #ltn=1
    else:
        axesb.plot(t,NAV[ck],color="black")


    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in NAV[ck]:
        yrrminus.append(sj-STDN[ck][l])
        yrrplus.append(sj+STDN[ck][l])
        l+=1

    axesb.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesb.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    if ltn==0:
        axesb.plot(t,NAVa[ck],color="red",label="Average Num of E. Units")
        #ltn=1
    else:
        axesb.plot(t,NAVa[ck],color="red")

    #axesb.plot(t,NAVa[ck])
    yrrminusa=[]
    yrrplusa=[]
    l=0
    for sj in NAVa[ck]:
        yrrminusa.append(sj-STDNa[ck][l])
        yrrplusa.append(sj+STDNa[ck][l])
        l+=1

    axesb.fill_between(t, yrrminusa, yrrplusa,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesb.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    if ltn==0:
        axesb.plot(t,NAVb[ck],color="blue",label="Average Num of TE's")
        #ltn=1
    else:
        axesb.plot(t,NAVb[ck],color="blue")

    #axesb.plot(t,NAVb[ck])
    yrrminusb=[]
    yrrplusb=[]
    l=0
    for sj in NAVb[ck]:
        yrrminusb.append(sj-STDNb[ck][l])
        yrrplusb.append(sj+STDNb[ck][l])
        l+=1

    axesb.fill_between(t, yrrminusb, yrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    axesb.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')


    ###########################

    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in LAV[ck]:

        yrrminus.append(sj-STDL[ck][l])
        yrrplus.append(sj+STDL[ck][l])
        l+=1
    axesa.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    if ltn==0:
        axesa.plot(t,LAV[ck],color="black",label="Average Length")
        #ltn=1
    else:
        axesa.plot(t,LAV[ck],color="black")

    #axesa.plot(t,LAV[ck])

    #axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')
    #axesa.fill_between(t, yrrminusb, yrrplusb,
    #alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')


    if ltn==0:
        axesa.plot(t,LAVa[ck],color="red",label="Average EGs Length")
        #ltn=1
    else:
        axesa.plot(t,LAVa[ck],color="red")

    #axesa.plot(t,LAVa[ck])

    lyrrminusa=[]
    lyrrplusa=[]
    l=0
    for sj in LAVa[ck]:
        lyrrminusa.append(sj-LSTDa[ck][l])
        lyrrplusa.append(sj+LSTDa[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusa, lyrrplusa, alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')


    if ltn==0:
        axesa.plot(t,LAVb[ck],color="blue",label="Average TEs Length")
        ltn=1
    else:
        axesa.plot(t,LAVb[ck],color="blue")


    #axesa.plot(t,LAVb[ck])
    lyrrminusb=[]
    lyrrplusb=[]
    l=0
    for sj in LAVb[ck]:
        lyrrminusb.append(sj-LSTDb[ck][l])
        lyrrplusb.append(sj+LSTDb[ck][l])
        l+=1


    axesa.fill_between(t, lyrrminusb, lyrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')

###############################################################
axesb.legend(loc='best', fancybox=True, framealpha=0.5)
fout=pth+folder+subf#+subf2
namepth=fout+"averagesl"#.eps"
##print namepth
##fig.set_size_inches(13.5,10.5)
fig1.patch.set_alpha(0.5)
#fig1.savefig(namepth+'.eps', dpi=1200, bbox_inches='tight')
fig1.savefig(namepth+'.png', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.svgz', dpi=600, bbox_inches='tight')
###*commented below cause jpg is not supported
###*fig1.savefig(namepth+'.jpg', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.pdf', dpi=1200, bbox_inches='tight')


##############################################################
axesa.legend(loc='best', fancybox=True, framealpha=0.5)

namepth=fout+"averagesn"#.eps"
##print namepth
##fig.set_size_inches(13.5,10.5)
fig2.patch.set_alpha(0.5)
#fig2.savefig(namepth+'.eps', dpi=1200, bbox_inches='tight')
fig2.savefig(namepth+'.png', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.svgz', dpi=600, bbox_inches='tight')
###*commented below cause jpg is not supported
###*fig2.savefig(namepth+'.jpg', dpi=1200, bbox_inches='tight')
##fig.savefig(namepth+'.pdf', dpi=1200, bbox_inches='tight')

for ck in LAV.keys():

    fig, axesa = plt.subplots(1,figsize=(10, 8))
    axesa.plot(t,LAV[ck])
    axesa.stem(xtj,ytja,linefmt='--', markerfmt='bo', basefmt='r-')
    #########################
    yrrminus=[]
    yrrplus=[]
    l=0
    for sj in LAV[ck]:

        yrrminus.append(sj-STDL[ck][l])
        yrrplus.append(sj+STDL[ck][l])
        l+=1
    axesa.fill_between(t, yrrminus, yrrplus,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')



    axesa.plot(t,LAVa[ck])

    lyrrminusa=[]
    lyrrplusa=[]
    l=0
    for sj in LAVa[ck]:
        lyrrminusa.append(sj-LSTDa[ck][l])
        lyrrplusa.append(sj+LSTDa[ck][l])
        l+=1

    axesa.fill_between(t, lyrrminusa, lyrrplusa, alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    #axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

    axesa.plot(t,LAVb[ck])
    lyrrminusb=[]
    lyrrplusb=[]
    l=0
    for sj in LAVb[ck]:
        lyrrminusb.append(sj-LSTDb[ck][l])
        lyrrplusb.append(sj+LSTDb[ck][l])
        l+=1


    axesa.fill_between(t, lyrrminusb, lyrrplusb,
    alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')
    axesa.stem(xtj,ytjb,linefmt='--', markerfmt='bo', basefmt='r-')

print nX #pars
print rnX #runs
print xi #jumps
print LAV.keys()
print folder, subf,# subf2

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
            file= pth+folder+subf+rn+prt+'pts'+str(jp)+'plotdata.p'
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

#changed saving order to avoid memoryerror stop the program if it raised at CDATAV dumping
par=[args.p,args.r,args.j] ###*added
name2=pth+"CDATAV_par.p" ###*added
pickle.dump(par,open(name2,"wb"), protocol=2) ###*

Data=[t,LAV,NAV,STDN,STDL]
name=pth+"CDATAVcomp.p" ###*as above
pickle.dump(Data,open(name,"wb"))
Data=[t,LAV,NAV,STDN,STDL,NAVa,NAVb,STDNa,STDNb,LAVa,LAVb,LSTDa,LSTDb]
name=pth+"CDATAV.p" ###*changed to have only one code in the main dir (added pth+)
pickle.dump(Data,open(name,"wb"),protocol=2)
