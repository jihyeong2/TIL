class Node():
    def __init__(self,depth):
        self.depth=depth
        self.child={}
        self.score=[]
class Trie():
    def __init__(self):
        self.head=Node(0)
    def trieInit(self,init_info):
        node=self.head
        for language in init_info[0]:
            node.child[language]=Node(1)
            node1=node.child[language]
            # print(init_info[0],node.child)
            for job in init_info[1]:
                node1.child[job]=Node(2)
                node2=node1.child[job]
                # print(init_info[1], node1.child)
                for years in init_info[2]:
                    node2.child[years]=Node(3)
                    node3=node2.child[years]
                    # print(init_info[2], node2.child)
                    for food in init_info[3]:
                        node3.child[food]=Node(4)
                        # print(init_info[3], node3.child)
    def insert(self, info):
        node=self.head
        for i in range(len(info)-1):
            node=node.child[info[i]]
        node.score.append(int(info[-1]))
    def scoreSort(self):
        node=self.head
        # print(node.child)
        for language in node.child.values():
            # print(language)
            node1=language
            # print(node1.child)
            for job in node1.child.values():
                node2=job
                # print(node2.child)
                for years in node2.child.values():
                    node3=years
                    # print(node3.child)
                    for food in node3.child.values():
                        node4=food
                        node4.score.sort()
def recursion_find(z,node,q):
    res=0
    if z==4:
        print(node.score,q[z])
        if q[z]=='-':
            res+=len(node.score)
        else:
            idx=-1
            for i in range(len(node.score)):
                if node.score[i]>=int(q[z]):
                    idx=i
                    break
            if idx!=-1:
                res+=len(node.score)-idx
    else:
        if q[z]=='-':
            for x in node.child.values():
                res+=recursion_find(z+1,x,q)
        else:
            res+=recursion_find(z+1,node.child[q[z]],q)
    return res
def solution(info, query):
    init_info=[['cpp','java','python'],['backend','frontend'],['junior','senior'],['chicken','pizza']]
    answer = []
    trie=Trie()
    trie.trieInit(init_info)
    for x in info:
        info_list=list(x.split())
        trie.insert(info_list)
    trie.scoreSort()
    for q in query:
        q=q.replace('and',' ',3)
        q_list=q.split()
        answer.append(recursion_find(0,trie.head,q_list))
    return answer
info=["java backend junior pizza 150","python frontend senior chicken 150","python frontend senior chicken 210","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150","- and - and - and - -"]
print(solution(info,query))