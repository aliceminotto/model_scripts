#!usr/bin/python
import matplotlib.pyplot as plot
import pickle
import numpy as np
import matplotlib.ticker as mtick

NJMP=20
process=10
pth="../../../../results_second_model/DT20000_10_1/"
pna='jump'
pnb='testpops.p'

ranges=[1,2,5,20]

for nproc in xrange(process):

    #define figure to use here
    fig = plot.figure(figsize=(20, 8))
    fig.suptitle('$\Delta T=2.0\\times 10^4$', fontsize=18)
    ax1=plot.subplot(2,2,1)
    ax2=plot.subplot(2,2,2)#, sharey=ax1)
    ax3=plot.subplot(2,2,3)
    ax4=plot.subplot(2,2,4)#, sharey=ax3)
    minip={ax1:ranges[0],ax2:ranges[1],ax3:ranges[2],ax4:ranges[3]}

    for subp in sorted(minip):

        Rs=[]
        ts=[]
        print '*******************************************'
        print subp

        for nj in xrange(minip[subp]):

            print 'jumps: ',minip[subp]
            print 'opening ', str(nproc)+pna+str(nj)+pnb
            fin=str(nproc)+pna+str(nj)+pnb
            f=open(pth+fin,"rb")
            A=pickle.load(f)
            f.close()

            #subp.set_ylabel("$N_j(t)$",fontsize=30)
            #axes.set_xlabel("Time t (Generations)",fontsize=30)

            tij=[]
            for i in A.keys():
                ti=(range(A[i][0],A[i][0]+len(A[i][1])))
                subp.plot(ti,A[i][1],'-',linewidth=1.5,label=str(i))
                tij.append(A[i][0])
            Rs.append(110000)
            print 'will add stem at ', min(tij)
            ts.append(min(tij))

        markerline, stemlines, baseline=subp.stem(ts,Rs,linefmt='--', markerfmt='.', basefmt='',stemlineswidth=0.1)
        plot.setp(stemlines, 'linewidth', 1, 'color', 'k')

        print "axis formatter for subplot ", subp
        subp.xaxis.set_tick_params(labelsize=10)
        subp.yaxis.set_tick_params(labelsize=10)
        if subp!=ax2 or subp!=ax4:
            subp.yaxis.set_major_formatter(mtick.ScalarFormatter(useMathText=True))
            subp.ticklabel_format(style='sci', scilimits=(0,0))

        subp.set_ylim(0.0, 110000)
        if subp==ax2 or subp==ax4:
            plot.setp(subp.get_yticklabels(), visible=False)
            subp.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.0f'))

            #plot.xlim(min(tij),min(tij)+DT)
        subp.tick_params(labelsize=16)
    plot.tight_layout()
    fig.patch.set_alpha(0.5)
    namefig='popdyn_'+'.png'

    fig.savefig(pth+str(nproc)+namefig,dpi=100, bbox_inches='tight')
    plot.savefig(pth+str(nproc)+'popdyn_'+'.svg', bbox_inches='tight')
    plot.close(fig)

'''fig, axes = plot.subplots(1, 1, figsize=(20, 8))

        axes.set_ylabel("$N_j(t)$",fontsize=30)
        axes.set_xlabel("Time t (Generations)",fontsize=30)

        ts=[]
        Rs=[]

        #####################################################
        for nj in xrange(NJMP):
            fin=str(nproc)+pna+str(nj)+pnb
            print fin

            f=open(pth+fin,"rb")
            A=pickle.load(f)
            f.close()

            tij=[]
            for i in A.keys():
                ti=range(A[i][0],A[i][0]+len(A[i][1]))
                axes.plot(ti,A[i][1],'-',label=str(i))
                tij.append(A[i][0])
            Rs.append(150000)
            ts.append(min(tij))

            plot.ylim(0.0, 150000)

        markerline, stemlines, baseline=axes.stem(ts,Rs,linefmt='--', markerfmt='.', basefmt='',stemlineswidth=0.1)
        plot.setp(stemlines, 'linewidth', 1)
        axes.tick_params(labelsize=30)

        fig.patch.set_alpha(0.5)
        namefig='popdyn.png'

        plot.savefig(pth+str(nproc)+namefig, dpi=100, bbox_inches='tight')
        plot.savefig(pth+str(nproc)+'popdyn.svg', bbox_inches='tight')
        plot.close(fig)'''
