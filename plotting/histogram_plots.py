#!usr/bin/python
import pickle
import matplotlib.pyplot as plt
import matplotlib.lines as lns
import matplotlib.ticker as mtick
from matplotlib.pyplot import cm
import numpy as np
import argparse
import os
plt.style.use('bmh')
parser=argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=("""
provide DT5000, 10000, 15000, 20000 and infinity in this order
"""))
parser.add_argument("p1",help="path to the right directory")
parser.add_argument("p2",help='path to 2nd directory')
parser.add_argument("p3",help='path to 3rd directory')
parser.add_argument("p4",help='path to 4th directory')
parser.add_argument("p5",help='path to 5th directory')
parser.add_argument("r", type=int, help="number of runs")
args=parser.parse_args()
pth1=args.p1
pth2=args.p2
pth3=args.p3
pth4=args.p4
pth5=args.p5
RUNS=args.r

nX=['n0/','n1/','n2/','n3/','n4/','n5/','n6/','n7/','n8/']
diz_pths={pth1:[nX],pth2:[nX],pth3:[nX],pth4:[nX],pth5:[['n0/']]}
diz_labels={pth1:"$\Delta T=5.0\\times 10^3$",pth2:"$\Delta T= 1.0\\times 10^4$",pth3:"$\Delta T= 1.5 \\times 10^4$",pth4:"$\Delta T= 2.0\\times 10^4$",pth5:"$\Delta T=\infty$"}
for key in diz_pths:
    rnX=[]
    for mu in range(RUNS): #not considering extinctions
        if all(os.listdir(key+'RUN'+str(mu)+'/'+x)==[] for x in diz_pths[key][0]):
            pass
        else:
            rnX.append('RUN'+str(mu)+'/')
    diz_pths[key].append(rnX)

#plotting distribution of len for each c value comparing different DTs
for c_value in nX:
    fig, axesa = plt.subplots(1,figsize=(16, 8),sharey=True)
    color=iter(cm.rainbow(np.linspace(0,1,5)))
    labels=[]
    line2d=[]

    for time_gap in [pth1,pth2,pth3,pth4,pth5]:
        efflen=[]
        telen=[]
        if time_gap!=pth5:
            for run in diz_pths[time_gap][1]:
                j=1
                #print type(time_gap)
                #print type(run)
                #print run
                #print type(c_value)
                fin=time_gap+run+c_value+'pts'+str(j)+'plotdata.p'
                while os.path.exists(fin):
                    f=open(fin,"rb")
                    A=pickle.load(f)
                    f.close()
                    efflen=efflen+A[5]
                    telen=telen+A[6]
                    j+=1
                    fin=time_gap+run+c_value+'pts'+str(j)+'plotdata.p'
        else:
            for run in diz_pths[time_gap][1]:
                j=1
                fin=time_gap+run+'n0/'+'pts'+str(j)+'plotdata.p'
                while os.path.exists(fin):
                    f=open(fin,"rb")
                    A=pickle.load(f)
                    f.close()
                    efflen=efflen+A[5]
                    telen=telen+A[6]
                    j+=1
                    fin=time_gap+run+'n0/'+'pts'+str(j)+'plotdata.p'
        col=next(color)
        plt.subplot(1,2,1)
        axesa.set_ylabel("$<Frequency>$", fontsize=40)
        axesa.set_xlabel("$Lengths$",fontsize=40)
        axesa.xaxis.set_tick_params(labelsize=20)
        axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
        axesa.yaxis.set_tick_params(labelsize=20)
        axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
        plt.ticklabel_format(style='sci', scilimits=(0,0))

        #hist1=plt.hist(efflen, range=(0,6000),bins=np.arange(0.0, 6000.0 + 100, 100.0)) #####
        #hist10=[x/float(RUNS*j) for x in hist1[0]] #####and below
        #plotthis=(hist10,hist1[1])
        plt.hist(efflen, histtype='step',ls='solid', color=col,label=diz_labels[time_gap],range=(0,6000), normed=1,bins=np.arange(0.0, 6000.0 + 100, 100.0),linewidth=1.0)

        line2d.append(lns.Line2D(range(len(efflen)),efflen,color=col,ls='solid'))
        labels.append(diz_labels[time_gap])

        plt.subplot(1,2,2)
        axesa.set_ylabel("$<Frequency>$", fontsize=40)
        axesa.set_xlabel("$Lengths$",fontsize=40)
        axesa.xaxis.set_tick_params(labelsize=20)
        axesa.xaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
        axesa.yaxis.set_tick_params(labelsize=20)
        axesa.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
        plt.ticklabel_format(style='sci', scilimits=(0,0))

        plt.hist(telen,histtype='step',ls='solid',color=col, normed=1,bins=np.arange(0.0, max(telen) + 100, 100.0),linewidth=1.0)
    titstr='$c='+str((int(c_value[-2])+1)/10.0)+'$'
    print titstr
    plt.subplot(1,2,1)
    plt.suptitle(titstr, fontsize=40)
    #plt.figlegend(loc='best', fancybox=True, framealpha=0.5)
    plt.figlegend(tuple(line2d),tuple(labels),loc='best')
    fig.savefig('/usr/users/TSL_20/minottoa/images/histograms/'+'lendistribution_plot'+str((int(c_value[-2])+1)/10.0)+'.png',format='png' ,dpi=1200, bbox_inches='tight')
