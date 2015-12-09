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
    Hn={} #host dictionary
    rng.seed(rngseed)
    for jn in xrange(par[0]):
        l=rng.randint(1,par[2]) #length of host genome
        u=mda.newhost.NEWHOST(l,par[1])
        Hn[jn]=u
    pathogen_dic=mda.newhost.NEWPATHOGEN(par[1],par[3],par[4])#,itr)
    print pathogen_dic
    #writefile2(j,pathogen_dic)
    d_tar=mda.gpmap.g_p_mapa(Hn[0],pathogen_dic)
    d_eff=mda.gpmap.g_p_mapb(Hn[0],pathogen_dic)
    d_tar2=mda.gpmap.g_p_mapa2(Hn[0],pathogen_dic,.5)
    #print Hn[0]
    #printalltar(pathogen_dic)
    #print d_tar
    #print d_tar2
    print pathogen_dic
    pthnew=mda.transformations.mutation(pathogen_dic,0,par[1],par[5],par[6])
    print "mutation"
    print pthnew
    raw_input()
    pthnew=mda.transformations.deletion(pthnew,1)
    print "deletion"
    print pthnew
    raw_input()
    pthnew=mda.transformations.duplication(pthnew,2)
    print "duplication"
    print pthnew
    raw_input()
    pthnew=mda.transformations.hgt(pthnew,mda.newhost,par[4],par[1])
    print "hgt"
    print pthnew
    raw_input()
    pthnew=mda.transformations.tgain(pthnew,3,par[1])
    print "tgain"
    print pthnew
    raw_input()
    pthnew=mda.transformations.tremove(pthnew,4)
    print pthnew
    print "tloss"
    raw_input()
    print pathogen_dic


def main():
    seeds=[]
    NUM_PROCESSES = 1
    SEED=987654321
    children = []
    ##########
    #Parameters
    NJ=10 #number of jumps
    K=100 #target pool size
    LHmax=50 #max host genome length
    NEO=5 #max numer of effector per pathogen at time 0
    NTO=10 #max number of target for each effector gene
    MU1=1.0/3
    MU2=2.0/3
    PV=[NJ,K,LHmax,NEO,NTO,MU1,MU2] #parameters values
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
