def solution(play_time, adv_time, logs):
    startLogsSec=[]
    endLogsSec=[]
    for time in logs:
        start=time[0:time.find('-')]
        end=time[time.find('-')+1:]
        start=start.split(':')
        end=end.split(':')
        startSec,endSec=0,0
        for i in range(3):
            startSec+=int(start[i])*(60**(2-i))
            endSec+=int(end[i])*(60**(2-i))
        startLogsSec.append(startSec)
        endLogsSec.append(endSec)
    play_time=play_time.split(':')
    playTimeSec=0
    for i in range(3):
        playTimeSec += int(play_time[i]) * (60 ** (2 - i))

    adv_time=adv_time.split(':')
    advTimeSec=0
    for i in range(3):
        advTimeSec += int(adv_time[i]) * (60 ** (2 - i))


    playTimeArr=[0]*(playTimeSec+1)
    for i in range(len(logs)):
        playTimeArr[startLogsSec[i]]+=1
        playTimeArr[endLogsSec[i]]-=1

    for _ in range(2):
        for i in range(1,playTimeSec):
            playTimeArr[i]=playTimeArr[i]+playTimeArr[i-1]

    resTime,resMax=0,playTimeArr[advTimeSec-1],
    for i in range(advTimeSec,playTimeSec):
        if resMax<playTimeArr[i]-playTimeArr[i-advTimeSec]:
            resMax=playTimeArr[i]-playTimeArr[i-advTimeSec]
            resTime=i-advTimeSec+1

    hh=resTime//3600
    hh='0'+str(hh) if hh<10 else str(hh)
    mm=(resTime%3600)//60
    mm='0'+str(mm) if mm<10 else str(mm)
    ss=(resTime%3600)%60
    ss='0'+str(ss) if ss<10 else str(ss)
    answer=hh+':'+mm+':'+ss
    return answer

solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])