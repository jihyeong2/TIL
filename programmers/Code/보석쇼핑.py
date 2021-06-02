def solution(gems):
    gems_dict=dict()
    active_gems=list(set(gems))
    length=len(active_gems)
    for gem in active_gems:
        gems_dict[gem]=0
    gems_cnt=0
    s,minS,minE=0,0,len(gems)-1
    for i in range(len(gems)):
        if gems_dict[gems[i]]>=1:
            gems_dict[gems[i]]+=1
        else:
            gems_cnt+=1
            gems_dict[gems[i]]+=1
        while gems_dict[gems[s]]>1:
            gems_dict[gems[s]]-=1
            s+=1
        if gems_cnt>=length:
            if i-s<minE-minS:
                minE,minS=i,s

    return [minS+1,minE+1]

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])