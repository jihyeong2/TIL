'''
1.입력받은 중위표기식에서 토큰을 읽는다.
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어있는 연산자보다 우선순위가
높으면 스택에 push하고 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다
작을때까지 스택에서 pop한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없으면 push한다.
4. 토큰이 오른쪽 괄호(')')이면 스택 top에 왼쪽 괄호('(')가 나올때 까지 스텍에 pop연산을 수행하고
pop한 연산자를 출력한다. 왼쪽 괄호를 만나면 pop만하고 출력하지는 않는다.
5. 중위 표기식에 더 읽을 것이 없다면 중지하고, 더 읽을 것이 있다면 1부터 다시 반복한다.
6. 스택에 남아 있는 연산자를 모두 pop하여 출력한다.
- 스택 밖의 왼쪽괄호는 우선순위가 가장 높으며, 스택안의 왼쪽 괄호는 우선순위가 가장 낮다.
'''
import sys
sys.stdin=open("input.txt","r")
def icp(x):
    if x=='(': return 3
    elif x=='*': return 2
    elif x=='+': return 1
    else : return -1
def isp(x):
    if x=='(': return 0
    elif x=='+': return 1
    elif x=='*': return 2
    else: return -1
for tc in range(1,11):
    leng=int(input())
    expr=input()
    op,s1,s2=[],[],[]
    for x in expr:
        if '1'<=x<='9': s1.append(x)
        elif x=='+' or x=='*':
                while len(op)!=0 and isp(op[-1])>=icp(x):
                    if isp(op[-1]) >= icp(x):
                        s1.append(op.pop(-1))
                op.append(x)
        elif x=='(': op.append(x)
        else:
            while (op[-1]!='('):
                s1.append(op.pop(-1))
            op.pop(-1)
    if len(op)!=0:
        s1.append(op.pop(-1))
    for x in s1:
        if '1'<=x<='9': s2.append(int(x))
        elif x=='*':
            b,a=s2.pop(-1),s2.pop(-1)
            s2.append(a*b)
        else:
            b,a=s2.pop(-1),s2.pop(-1)
            s2.append(a+b)
    print('#{} {}'.format(tc,s2.pop(-1)))