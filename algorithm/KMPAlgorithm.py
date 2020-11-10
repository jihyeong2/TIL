def KMP_Preprocess(p,next):
    M=len(p)
    i,j=0,-1
    while i<M:
        next[i]=j
        while j>=0 and p[i]!=p[j]:
            j=next[j]
        i+=1
        j+=1
def KMP_Search(t,p,next):
    N,M=len(t),len(p)
    i,j=0,0
    while i<N:
        while i>=0 and t[i]!=p[i]:
            j=next[j]
        i+=1
        j+=1
        if j==M:
            return i-j
    return -1