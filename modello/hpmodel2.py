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

def jumps(j,rngseed,par):
    #par[0] number of jumps
    #par[1] target poool size
    #par[2] max host length
    #par[3] max numb of effector per path at time0
    #par[4] max numb of target per effector gene
    #par[5] mu1
    #par[6] mu2
    #par[7] rates
    Hn={} #host dictionary
    rng.seed(rngseed)
    for jn in xrange(par[0]):
        l=rng.randint(1,par[2]) #length of host genome
        u=mda.newhost.NEWHOST(l,par[1])
        Hn[jn]=u
    r=0.0
    j=0
    while r<=.5:
        j++1
        pathogen_dic=mda.newhost.NEWPATHOGEN(par[1],par[3],par[4])#,itr)
        r=sum(mda.gpmap.g_p_mapa(Hn[0],pathogen_dic).values())/float(len(Hn[0]))
        #if j%1000==0:
        #    print '*'
    '''print r
    print Hn[0]
    printuseful(pathogen_dic,Hn[0])'''
    path_pop={}
    path_pop[0]=[0,[10]]
    path_r={}
    path_r[0]=r
    path_genomes={}
    path_genomes[0]=pathogen_dic
    for t in xrange(par[0]*par[8]):
        for el in path_pop:
            if path_pop[el][1][-1]>=0:
                print t,el
                path_pop[el][1].append(mda.population.N_calc(path_pop,path_r,el,path_pop[el][1][-1],par[9]))
    print >>open("plotthis","w"),path_pop[0][1]



def main():
    seeds=[]
    NUM_PROCESSES = 1
    SEED=987654321
    children = []
    ##########
    #Parameters
    DT=5000
    NJ=10 #number of jumps
    K=100 #target pool size
    LHmax=50 #max host genome length
    NEO=5 #max numer of effector per pathogen at time 0
    NTO=10 #max number of target for each effector gene
    MU1=1.0/3
    MU2=2.0/3
    m1=0.01 #mutation
    m2=0.01 #duplication
    m3=0.01 #deletion
    m4=0.01 #hgt
    NH=10**5
    PV=[NJ,K,LHmax,NEO,NTO,MU1,MU2,[m1,m2,m3,m4],DT,NH] #parameters values
    ##########
    for process in xrange(NUM_PROCESSES):
        pid = os.fork()
        seeds.append(SEED-process)
        if pid:
            children.append(pid)
        else:
            i=str(process)+".dat"
#            writefile(i,seeds[process])
            jumps(i,seeds[process],PV)
            os._exit(0)

    for i, child in enumerate(children):
        os.waitpid(child, 0)

if __name__ == "__main__":
    main()
