#!usr/bin/python

import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

def plotdictder(AVdict,DT,fname):

    dAVdict={}
    tnax={}
    fig, axesa= plt.subplots(1,figsize=(10, 8))
    fig, axesb= plt.subplots(1,figsize=(10, 8))
    for j in AVdict.keys():
        print j
    #dNavA[j]=np.diff(NAVa['n0/'])
    #dNavB[j]=np.diff(NAVb['n0/']
        tn=[]
        Da=[]
        to=0
        for mu in AVdict[j]:
            if to%DT==0:
                Da.append(mu)
                #Db.appedn()
                tn.append(to)
            to+=1

        dAVdict[j]=np.diff(Da)/DT
        tnax[j]=[k for k in tn]
        tnax[j].pop(-1)

        pickle.dump(dAVdict,open(fname ,"wb"), protocol=2) #optional

        axesa.plot(tnax[j],dAVdict[j],"o-", markersize=2, linewidth=1.1)
        axesb.plot(AVdict[j],"o-", markersize=2, linewidth=1.1)

    fig.patch.set_alpha(0.5)
    fig.savefig(fname+'.png',format='png' ,dpi=100, bbox_inches='tight')
    fig.savefig(fname+'.svg', bbox_inches='tight')

files=['/usr/users/TSL_20/minottoa/change_DT_Qi/DT5000/before_c_changes/CDATAV.p',
            '/usr/users/TSL_20/minottoa/change_DT_Qi/DT10000/bf_c/CDATAV.p', '/usr/users/TSL_20/minottoa/change_DT_Qi/DT15000/bf_c/CDATAV.p' ,
             '/usr/users/TSL_20/minottoa/change_DT_Qi/DT20000/bf_c/CDATAV.p' , '/usr/users/TSL_20/minottoa/new/bf_c/CDATAV.p']

for name in files:
    name=files[-2]
    with open(name, 'rb') as handle:
        DATA = pickle.load(handle)
        print len(DATA)

    t=DATA[0]
    NAVa=DATA[5]
    print type(NAVa)
    for x in range(10):
        for k in NAVa:
            print k, NAVa[k]
    NAVb=DATA[6]
    LAVa=DATA[9]
    LAVb=DATA[10]

    del DATA

    pickle.dump(NAVa,open(name[:-2]+"nava.p","wb"), protocol=2)
    pickle.dump(NAVb,open(name[:-2]+"navb.p","wb"),protocol=2)
    pickle.dump(LAVa,open(name[:-2]+"lava.p","wb"),protocol=2)
    pickle.dump(LAVb,open(name[:-2]+"lavb.p","wb"),protocol=2)

    del NAVa,NAVb,LAVa,LAVb

filesx=[name[:-2]+"nava.p",name[:-2]+"nava.p", name[:-2]+"nava.p", name[:-2]+"nava.p"]
DT=200

for data in filesx:
    with open(data, 'rb') as handle:
      avdict = pickle.load(handle)
    cn=0
    for j in avdict:
        dataname=data[:-2]+str(cn) #optional
        plotdictder(j,DT,dataname)
