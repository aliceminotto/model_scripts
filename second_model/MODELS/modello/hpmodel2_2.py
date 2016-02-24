#!usr/bin/python
import sys
sys.path.append('codes2/')
import itertools as itr
from itertools import product
import os,time
from multiprocessing import Process, Queue
import subprocess as sp
from math import floor
import math as mth
import pickle
import numpy as np
from numpy import random as rng
import modA as mda

def writefile(p1,p2):
    fin=open(p1,"w")
    print >>fin, p2
    fin.close()

def writefile2(p1,p2):
    fin=open(p1,"w")
    for k in p2.keys():
        print >>fin, str(k)+" "+str(p2[k])
    fin.close()

def printtarget(diz_p):
    for effector in diz_p:
        print effector,[x for x in diz_p[effector]]

def printuseful(diz_p,host):
    for effector in diz_p:
        print effector,[[x,diz_p[effector][x]] for x in diz_p[effector] if x in host]

def printalltar(diz_p):
    tar=set()
    for effector in diz_p:
        for target in diz_p[effector]:
            tar.add(target)
    print tar

def jumps(rngseed,par,proc):
    #par[0] number of jumps
    #par[1] target poool size K
    #par[2] max host length
    #par[3] max numb of effector per path at time0
    #par[4] max numb of target per effector gene
    #par[5] mu1
    #par[6] mu2
    #par[7] rates
    #par[8] DT
    #par[9] NH
    #par[10] pmin
    save_pth="../../../../results_second_model/prova/DT1000_10_05/"
    pmin=par[10]
    Hn={} #host dictionary
    rng.seed(rngseed)
    for jn in xrange(par[0]):
        l=rng.randint(1,par[2]) #length of host genome
        u=mda.newhost.NEWHOST(l,par[1])
        Hn[jn]=u
    pickle.dump(Hn,open(save_pth+str(proc)+"Hosts.p","wb"),protocol=2)
    #pickle.dump( path_r, open( str(proc)+"jump"+str(jn)+"r.p", "wb" ) )
    r=0.0
    j=0
    while r<=.1:
        j++1
        pathogen_dic=mda.newhost.NEWPATHOGEN(par[1],par[3],par[4])#,itr)
        r=sum(mda.gpmap.g_p_mapa(Hn[0],pathogen_dic).values())/float(len(Hn[0]))
	'''#print("looking for fit initial dude")
        if j%1000==0:
            print r, proc
	    print("still looking for fit initial dude")
	    raw_input()'''
    print r
    print Hn[0]
    printuseful(pathogen_dic,Hn[0])
    path_pop={}
    path_pop[0]=[0,[10]]
    path_r={}
    path_r[0]=r
    path_genomes={}
    path_probs={}
    events={}
    path_genomes[0]=pathogen_dic
    evitems = [0, 1, 2, 3]
    jn=0
    rnj=int(max(path_pop.keys()))+1
    for t in xrange(par[0]*par[8]):
        rmax=max(path_r.values())
        #rnj=int(max(path_pop.keys()))+1
        npflag=0
        npops=[]
        for el in path_pop:
            if path_pop[el][1][-1]>=0:
                path_probs[el]={}
                path_probs[el]=mda.transformations.probabilities(path_genomes[el],Hn[jn],par[7],path_pop[el][1][-1]) #pathogen,host,rates,pop
                events[el]={}
                events[el]=mda.transformations.events(path_probs[el]);
                if any(ev in events[el].values() for ev in evitems):
                    npthaux1={}
                    npthaux1=mda.transformations.transform(path_genomes[el],events[el],par[1],par[5],par[6],par[4])
                    raux=sum(mda.gpmap.g_p_mapa(Hn[jn],npthaux1).values())/float(len(Hn[jn]))
                    if raux>rmax:
                        path_r[rnj]=raux
                        path_genomes[rnj]=npthaux1
                        npops.append(rnj)
                        rnj+=1
                        npflag=1
        if npflag!=0:
            for jk in npops:
                path_pop[jk]=[t,[10]]

        assert path_pop.keys()==path_genomes.keys()
        flagest=0
        for el in path_pop:
            if path_pop[el][1][-1]>=0:
                #print t,el
                flagest=1
                path_pop[el][1].append(mda.population.N_calc(path_pop,path_r,el,path_pop[el][1][-1],par[9]))
        if flagest==0:
            print("ALL-DEATH")
            break

        if ((t%par[8])==(par[8]-1)):
            print "jump in progress"
            pickle.dump( path_pop, open(save_pth+str(proc)+"jump"+str(jn)+"testpops.p", "wb"),protocol=2)
            pickle.dump( path_genomes, open(save_pth+str(proc)+"jump"+str(jn)+"genomes.p", "wb"),protocol=2)
            pickle.dump( path_r, open(save_pth+str(proc)+"jump"+str(jn)+"r.p", "wb"),protocol=2)
            if jn<(par[0]-1):
                print "jump:",jn
                popx={}
                rux={}
                genomesx={}
                jn+=1
                for k in path_pop:
                    if (path_pop[k][1][-1]>10.0):
                        if (path_pop[k][1][-1]>par[10]):
                            popx[k]=[t,[pmin]]
                        else:
                            popx[k]=[t,[path_pop[k][1][-1]]]

                        genomesx[k]=mda.transformations.deepcopy(path_genomes[k])
                        rux[k]=sum(mda.gpmap.g_p_mapa(Hn[jn],genomesx[k]).values())/float(len(Hn[jn]))
                print popx
                #raw_input()
                path_pop={}
                path_genomes={}
                path_r={}
                print popx
                #raw_input()
                for k in popx.keys():
                    print popx[k]
                    #path_pop[k]=mda.transformations.deepcopy(popx[k])
                    path_pop[k]=popx[k]
                    #raw_input()
                    #path_genomes[k]=mda.transformations.deepcopy(genomesx[k])
                    #assert len(path_genomes[k])==len(genomesx[k])
                    path_genomes[k]=genomesx[k].copy()
                    #path_r[k]=mda.transformations.deepcopy(rux[k])
                    path_r[k]=rux[k]
                del popx
                del genomesx
                del rux
                print "jump completed"
                #raw_input()
            #jn+=1
            print jn

    print proc
    print("test completed")
    #print >>open("plotthis","w"),path_pop[0][1]



def main():
    seeds=[]
    NUM_PROCESSES=10
    SEED=594476731
    children=[]
    ##########
    #Parameters
    eta=0.5
    beta=1.5-eta
    DT=1000
    NJ=20 #number of jumps
    K=100 #target pool size
    LHmax=50 #max host genome length
    NEO=3 #max numer of effector per pathogen at time 0
    NTO=10 #max number of target for each effector gene
    MU1=eta*(1.0/3)
    MU2=beta*(2.0/3)
    m1=0.01 #mutation
    m2=0.01 #duplication
    m3=0.01 #deletion
    m4=0.01 #hgt
    NH=10**5
    pmin=NH/100.0
    PV=[NJ,K,LHmax,NEO,NTO,MU1,MU2,[m1,m2,m3,m4],DT,NH,pmin] #parameters values
    ##########
    for process in xrange(NUM_PROCESSES):
        pid = os.fork()
        seeds.append(SEED-(3+process))
        if pid:
            children.append(pid)
        else:
            #i=str(process)+".dat"
            #i=str(process)
#            writefile(i,seeds[process])
            jumps(seeds[process],PV,process)
            os._exit(0)

    for i, child in enumerate(children):
        os.waitpid(child, 0)

if __name__ == "__main__":
    main()
