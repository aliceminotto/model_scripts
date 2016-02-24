#!usr/bin/python

import matplotlib.pyplot as plot
import pickle
import numpy as np
import matplotlib.ticker as mtick
pna='jump'
pnb='testpops.p'

NJMP=20
DT=1000
process=10
pth="../../../../results_second_model/prova/DT1000_10_05/"

nproc=5
fig, axes = plot.subplots(1, 1, figsize=(20, 8))
titstr='Typical evolutionary trajectory of the number of EGs\n'
print titstr
#raw_input()
axes.set_title(titstr, fontsize=35)
axes.set_ylabel("$n_{e,j}(t)$",fontsize=39)
axes.set_xlabel("Strain label",fontsize=30)
#axesb.set_xlim([0, 15])
axes.xaxis.set_tick_params(labelsize=30)
axes.yaxis.set_tick_params(labelsize=30)
###
tsmin=[]
tsmax=[]
Rs=[]
for nj in xrange(NJMP):
    fin=str(nproc)+pna+str(nj)+"genomes.p"
    print fin

    f=open(pth+fin,"rb")
    gr=pickle.load(f)
    f.close()

    x=[]
    y=[]
    for k in gr.keys():
        x.append(k)
    x.sort()
    for k in x:
        y.append(len(gr[k]))


    #fig, axes = plot.subplots(1, 1, figsize=(20, 8))
    plot.xlim([230,250])
    axes.plot(x,y,"-o")

fig.patch.set_alpha(0.5)
namefig='typngenevol.png'

plot.savefig(pth+"check_"+str(nproc)+namefig, dpi=100, bbox_inches='tight')
plot.close(fig)
