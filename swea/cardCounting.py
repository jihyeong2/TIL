import sys
sys.stdin=open("input.txt","r")
def isPossible(cards,card_dic,card_set):
    for i in range(0,len(cards),3):
        card=cards[i:i+3]
        if card in card_set: return False
        card_set.add(card)
        card_dic[card[0]]-=1
    return True
T=int(input())
for tc in range(1,T+1):
    cards,card_dic,card_set=input(),{'S':13,'D':13,'H':13,'C':13},set()
    result=''
    if not isPossible(cards,card_dic,card_set):
        result+='ERROR'
    else:
        for val in card_dic.values():
            result+=str(val)+' '
    print('#{} {}'.format(tc,result))