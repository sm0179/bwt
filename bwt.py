import os
from collections import OrderedDict
from operator import itemgetter
os.chdir("/Users/sm0179/Documents/bwt")
f=open("seq.in","r")
lines=f.readlines()
s=lines[0].strip()+'$'
p=lines[1].strip()

def suffixarray(s):
    suff=list()
    for i in range(len(s)):
        suff.append((i,s[i:]))
    suff_arr=sorted(suff,key=itemgetter(1))
    return list(map(lambda x: x[0], suff_arr))
    
def bwt(s):
    bw=list()
    for i in suffixarray(s):
        if i==0: bw.append("$")
        else: bw.append(s[i-1])
    return ''.join(bw)

sa=suffixarray(s)
bw=bwt(s)
print(bw)

def rankbwt(bw):
    rank=list()
    totals={}
    for c in bw:
        if c not in totals:
            totals[c]=1
            rank.append(0)
        else:
            rank.append(totals[c])
            totals[c]+=1
    return totals, rank


def firstcol(tots):
    first={}
    i=0
    for c in sorted(tots):
        first[c]=i
        i+=tots[c]
    return first

totals, rank=rankbwt(bw)
first=firstcol(totals)
print(first)

def bsearch(bw,p):
    l=first[p[-1]]
    r=l+totals[p[-1]]
    i=len(p)-2
    while i>=0 and l<r:
        if bw[l:r].find(p[i])!=-1:
            l_last=l+bw[l:r].find(p[i])
        else:
            return 0
        if bw[l:r].rfind(p[i])!=-1:
            r_last=l+bw[l:r].rfind(p[i])
        l=first[p[i]]+rank[l_last]
        r=first[p[i]]+rank[r_last]+1
        print(l,r)
        i=i-1
    return r-l, sa[l:r]

print(bsearch(bw,p))
            
           

