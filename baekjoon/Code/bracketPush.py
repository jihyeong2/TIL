import copy
def dfs(z,max_cnt,idx,bracket):
    if z==max_cnt:
        global result
        expr=copy.copy(expression)
        tmp_result=0
        for idx,i in enumerate(bracket):
            i-=(idx*2)
            if len(expr)==1:
                break
            tmp=0
            if expr[i+1] == '+':
                tmp=expr[i]+expr[i+2]
            elif expr[i+1] == '*':
                tmp=expr[i]*expr[i+2]
            else:
                tmp=expr[i]-expr[i+2]
            for j in range(3):
                expr.pop(i)
            expr.insert(i,tmp)
        while True:
            if len(expr)==1:
                tmp_result=expr[0]
                break
            tmp=0
            if expr[1] == '+':
                tmp=expr[0]+expr[2]
            elif expr[1] == '*':
                tmp=expr[0]*expr[2]
            else:
                tmp=expr[0]-expr[2]
            for j in range(3):
                expr.pop(0)
            expr.insert(0,tmp)
        result=max(result,tmp_result)
    else:
        if idx>=n-1: return
        for i in range(idx,n-1,2):
            bracket.append(i)
            dfs(z+1,max_cnt,i+4,bracket)
            bracket.pop(-1)
n=int(input())
expression=list(input())
result=float('-inf')
for i in range(0,n,2):
    expression[i]=int(expression[i])
for max_cnt in range(n//2+1):
    dfs(0,max_cnt,0,[])
print(result)