"""Exact independent checks for cyclic-difference image sizes."""
from math import comb
import argparse
import json

def valuation(x, p, cap):
    if not x:
        return cap
    v = 0
    while v < cap and x % p == 0:
        x //= p
        v += 1
    return v

def image_log(matrix, p, b):
    """Smith elimination over Z/(p**b); only invert units."""
    mod = p**b
    a = [[x % mod for x in row] for row in matrix]
    m, n = len(a), len(a[0]) if a else 0
    answer = 0
    for k in range(min(m,n)):
        pivot = None
        best = b
        for i in range(k,m):
            for j in range(k,n):
                v = valuation(a[i][j],p,b)
                if v < best:
                    best, pivot = v, (i,j)
                    if not best:
                        break
            if not best:
                break
        if pivot is None:
            break
        i,j = pivot
        a[k],a[i] = a[i],a[k]
        for row in a:
            row[k],row[j] = row[j],row[k]
        pv = p**best
        inv = pow(a[k][k]//pv,-1,mod)
        a[k] = [(x*inv)%mod for x in a[k]]
        for i in range(k+1,m):
            factor = a[i][k]//pv
            if factor:
                a[i] = [(x-factor*y)%mod for x,y in zip(a[i],a[k])]
        answer += b-best
    return answer

def thresholds(p,a,b):
    return [(b-j)*(p-1)*p**(a-j-1)+p**(a-j-1) if a>j else 1 for j in range(b)]

def check(p,a,b,all_times=True):
    n,mod = p**a,p**b
    ls = thresholds(p,a,b)
    T = max(ls)
    ts = range(T+2) if all_times else sorted({0,1,T,T+1,*[max(0,l+d) for l in ls for d in (-2,-1,0,1,2)]})
    failures=[]
    actual=[]
    for t in ts:
        cs=[0]*n
        for j in range(t+1):
            cs[j%n]=(cs[j%n]+(-1)**(t-j)*comb(t,j))%mod
        matrix=[[cs[(i-j)%n] for j in range(n)] for i in range(n)]
        r=image_log(matrix,p,b)
        predicted=sum(max(l-t,0) for l in ls)
        actual.append((t,r))
        if r!=predicted:
            failures.append((t,r,predicted))
    return dict(p=p,a=a,b=b,n=n,thresholds=ls,checks=len(actual),failures=failures,actual=actual)

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--p',type=int,default=2)
    ap.add_argument('--a',type=int,default=3)
    ap.add_argument('--b',type=int,default=4)
    ap.add_argument('--boundary-only',action='store_true')
    args=ap.parse_args()
    print(json.dumps(check(args.p,args.a,args.b,not args.boundary_only)))

