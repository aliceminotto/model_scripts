##########################################
def transform(nxtr,gen,rk,tepar,effpar, events_list):
    import math
    gi=nxtr[0]
    ri=nxtr[1]
    #events_list

    zn=gen[gi][0]
    gx={}

    if zn=='eff':
        if ri==0:
            ki=0
            for u in gen.keys():
              rn=[]
              for zk in gen[u]:
                rn.append(zk)
              gx[ki]=rn # [gen[u][0],gen[u][1]]
              ki+=1
            nu=[]
            nu.append('eff')
            l=math.floor((effpar[1]-effpar[0])*rk.uniform()+effpar[0])
            nu.append(l)
            nu.append(rk.uniform_pos())
            ng=len(gx.keys())
            gx[ng]=nu
            events_list.append(0)

        if ri==1:
            ki=0
            for u in gen.keys():
              if u != gi:
                rn=[]
                for zk in gen[u]:
                  rn.append(zk)
                gx[ki]=rn#[gen[u][0],gen[u][1]]
                ki+=1
            ng=len(gx.keys())
            l=gen[gi][1]+math.floor( (1-2.0*rk.uniform())*50 )
            if l<=math.floor(0.1*effpar[0]):
              if l>=0.0:
                gx[ng]=['te',l]
            else:
              coin=rk.uniform()
              if coin<0.5:
                ds=0.01+gen[gi][2]
                gx[ng]=[gen[gi][0],l,ds]
              else:
                ds=gen[gi][2]-0.01
                if ds<0.0:
                  ds=0.0
              gx[ng]=[gen[gi][0],l,ds]
              events_list.append(1)

        if ri==2:
            ki=0
            for u in gen.keys():
                rn=[]
                for zi in gen[u]:
                  rn.append(zi)
                gx[ki]=rn #[gen[u][0],gen[u][1]]
                ki+=1
            ng=len(gx.keys())
            gx[ng]=[gen[gi][0],gen[gi][1],gen[gi][2]]
            events_list.append(2)

        if ri==3:
            ki=0
            for i in gen.keys():
                if i != gi:
                    rn=[]
                    for zk in gen[i]:
                      rn.append(zk)
                    gx[ki]=rn #[gen[i][0],gen[i][1],gen[i][2]]
                if i == gi:
                    gx[ki]=['eff',gen[gi][1],0.0]
                ki+=1
            nu=[]
            nu.append('te')
            l=math.floor( (tepar[1]-tepar[0])*rk.uniform()+tepar[0] )
            nu.append(l)
            ng=len(gx.keys())
            gx[ng]=nu
            events_list.append(3)

        if ri==4:
          ki=0
          for i in gen.keys():
            if i!=gi:
                rn=[]
                for zk in gen[i]:
                  rn.append(zk)
                gx[ki]=rn
                ki+=1
                events_list.append(4)

    if zn=='te':
        if ri==0:
          ki=0
          for i in gen.keys():
            rn=[]
            for zk in gen[i]:
              rn.append(zk)

            gx[ki]=rn#[gen[i][0],gen[i][1]]
            ki+=1
          nu=[]
          nu.append('te')
          l=math.floor( (tepar[1]-tepar[0])*rk.uniform()+tepar[0] )
          nu.append(l)
          ng=len(gx.keys())
          gx[ng]=nu
          events_list.append(5)

        if ri==1:
          ki=0
          for u in gen.keys():
            rn=[]
            for zk in gen[u]:
              rn.append(zk)
            gx[ki]=rn #[gen[u][0],gen[u][1]]
            ki+=1
          ng=len(gx.keys())
          gx[ng]=[gen[gi][0],gen[gi][1]]
          events_list.append(6)

        if ri==2:
          ki=0
          for i in gen.keys():
            if i!=gi:
                gx[ki]=gen[i]
                ki+=1
          events_list.append(7)

    return gx
