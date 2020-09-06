# def startSearch(words,length):
#     s,e=0,len(words)-1
#     if length<len(words[s]) or len(words[e])<length: return -1
#     if length==len(words[s]): return s
#     while s+1<e:
#         mid=(s+e)//2
#         if len(words[mid])<length: s=mid
#         else: e=mid
#     return e
# def endSearch(words,length):
#     s,e=0,len(words)-1
#     if length<len(words[s]) or len(words[e])<length: return -1
#     if length==len(words[e]): return e+1
#     while s+1<e:
#         mid=(s+e)//2
#         if len(words[mid])>length: e=mid
#         else: s=mid
#     return s+1
# def solution(words, queries):
#     answer = []
#     my_dict=dict()
#     words.sort(key=lambda x:len(x))
#     for query in queries:
#         cnt=my_dict.get(query, 0)
#         if cnt>0: answer.append(cnt)
#         else:
#             reverse_flag,length=0,len(query)
#             if query[0] == '?':
#                 query_reverse = query[::-1]
#                 q = query_reverse[:query_reverse.find('?')]
#                 idx=query_reverse.find('?')
#                 reverse_flag=1
#             else:
#                 q=query[:query.find('?')]
#                 idx=query.find('?')
#             start,end=startSearch(words,length),endSearch(words,length)
#             if start==-1 or end==-1 :
#                 answer.append(0)
#             else:
#                 for i in range(start,end):
#                     word=words[i]
#                     if reverse_flag:
#                         word=word[::-1]
#                         word=word[:idx]
#                     else:
#                         word=word[:idx]
#                     if q==word:
#                         cnt+=1
#                 answer.append(cnt)
#             my_dict[query]=cnt
#     return answer
class Node():
    def __init__(self,key):
        self.key=key
        self.length_remain = {}
        self.child={}
class trie():
    def __init__(self):
        self.head=Node(None)
    def insert(self,words):
        node=self.head
        l=len(words)
        node.length_remain[l]=node.length_remain.get(l,0)+1
        for word in words:
            if word not in node.child:
                node.child[word]=Node(word)
            node=node.child[word]
            l-=1
            node.length_remain[l] = node.length_remain.get(l, 0) + 1
    def search(self,words,leng):
        node=self.head
        if len(words)+leng not in node.length_remain:   return 0
        for word in words:
            if word not in node.child: return 0
            node=node.child[word]
        return node.length_remain.get(leng,0)
def solution(words,queries):
    t,t_rev=trie(),trie()
    answer=[]
    for word in words:
        t.insert(word)
        t_rev.insert(word[::-1])
    for query in queries:
        leng=len(query)
        if query[0]=='?':
            query=query[::-1]
            query=query[:query.find('?')]
            answer.append(t_rev.search(query,leng-len(query)))
        else:
            query = query[:query.find('?')]
            answer.append(t.search(query,leng-len(query)))
    return answer
words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))
