import sys
sys.stdin=open("input.txt","r")
def solution(new_id):
    answer = ''
    new_id1=''
    for id in new_id: #소문자
        if 'A'<=id<='Z':
            id=chr(ord(id)-(ord('A')-ord('a')))
        new_id1+=id
    # print(new_id1)
    new_id2=''
    for id in new_id1: #가능문자
        if not ('a'<=id<='z' or '0'<=id<='9' or id=='-' or id=='_' or id=='.'): continue
        new_id2+=id
    # print(new_id2)
    new_id3=''
    for id in new_id2: #연속 . 지우기
        if len(new_id3)==0:
            new_id3+=id
        else:
            if new_id3[-1]=='.' and id=='.': continue
            new_id3+=id
    # print(new_id3)
    if len(new_id3)>0 and new_id3[0]=='.': new_id3=new_id3[1:]
    if len(new_id3)>0 and new_id3[-1]=='.': new_id3=new_id3[:-1]
    if len(new_id3)==0:
        new_id3+='a'
    if len(new_id3)>=16:
        new_id3=new_id3[:15]
        if new_id3[-1] == '.': new_id3 = new_id3[:-1]
    elif len(new_id3)<=2:
        new_id3+=new_id3[-1]*(3-len(new_id3))
    answer=new_id3
    return answer
for _ in range(5):
    print(solution(input()))