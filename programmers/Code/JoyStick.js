function solution(name) {
  var answer = 0;
  let idx=0, cnt=0, dir=1;
  let visit = new Array(name.length).fill(0);
  for(let i=0; i<name.length; i++){
      if(name[i]==='A'){
          visit[i]=1;
          cnt++;
      }
  }
  while(true){
    const up = name[idx].charCodeAt(0)-'A'.charCodeAt(0);
    const down = 91-name[idx].charCodeAt(0);
    const goCnt = up>down ? down : up;
    answer+=goCnt;
    if(!visit[idx]) {
        cnt++;
        visit[idx]=1;
    }
    if(cnt>=name.length) break;
    let n_idx1,n_idx2;
    let cnt1=0,cnt2=0;
    for(let i=1; i<name.length; i++){
      cnt1++;
      n_idx1=(idx+i)%name.length;
      if(!visit[n_idx1]) break;
    }
    for(let i=1; i<name.length; i++){
      cnt2++;
      n_idx2=idx-i < 0 ? name.length+idx-i : idx-i;
      if(!visit[n_idx2]) break;
    }
    idx=cnt1>cnt2 ? n_idx2 : n_idx1;
    answer=cnt1>cnt2 ? answer+cnt2 : answer+cnt1;
}
return answer;
}
console.log(solution("JAN"));