#!usr/bin/python

import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

def plotdictder(AVdict,DT):

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

        axesa.plot(tnax[j],dAVdict[j],"o-", markersize=2, linewidth=1.1)

        axesb.plot(AVdict[j],"o-", markersize=2, linewidth=1.1)

        plt.show()

files=['/usr/users/TSL_20/minottoa/change_DT_Qi/DT5000/before_c_changes/CDATAV.p',
            '/usr/users/TSL_20/minottoa/change_DT_Qi/DT10000/bf_c/CDATAV.p', '/usr/users/TSL_20/minottoa/change_DT_Qi/DT15000/bf_c/CDATAV.p' ,
             '/usr/users/TSL_20/minottoa/change_DT_Qi/DT20000/bf_c/CDATAV.p' , '/usr/users/TSL_20/minottoa/new/bf_c/CDATAV.p']

for name in files:
    name=files[-2]
    with open(name, 'rb') as handle:
        DATA = pickle.load(handle)
        print len(DATA)

    #MINOTTO PERHAPS IT SHOULD BE EASIER TO SAVE THESE INDIVIDUALLY?
    #LIKE NAVa=DATA[5]
    #pickle.dump("NAVa",opeb('navadt=Whatehever','wb'))?

    t=DATA[0]
    NAVa=DATA[5]
    NAVb=DATA[6]
    LAVa=DATA[9]
    LAVb=DATA[10]

    del DATA

    pickle.dump(NAVa,open(name[:-2]+"nava.p","wb"), protocol=2)
    pickle.dump(NAVb,open(name[:-2]+"navb.p","wb"),protocol=2)
    pickle.dump(LAVa,open(name[:-2]+"lava.p","wb"),protocol=2)
    pickle.dump(LAVb,open(name[:-2]+"lavb.p","wb"),protocol=2)

    del NAVa,NAVb,LAVa,LAVb

    with open(name, 'rb') as handle:
      DATA = pickle.load(handle)
    print len(DATA)
    #raw_input()
    DT=50
    for j in DATA:
        plotdictder(j,DT)

    with open(name, 'rb') as handle:
      DATA = pickle.load(handle)
    print len(DATA)
    #raw_input()
    DT=500
    for j in DATA:
        plotdictder(j,DT)

    with open(name, 'rb') as handle:
      DATA = pickle.load(handle)
    print len(DATA)
    #raw_input()
    DT=1000
    for j in DATA:
        plotdictder(j,DT)
