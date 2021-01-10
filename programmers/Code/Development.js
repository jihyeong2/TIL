function solution(progresses, speeds) {
  var answer = [];
  let t=0;
  while(progresses.length>0){
    t++;
    for(let i=0; i<progresses.length; i++){
      progresses[i]=progresses[i]+speeds[i]<100 ? progresses[i]+speeds[i] : 100;
    }
    let cnt=0;
    while(progresses.length>0 && progresses[0]>=100){
      progresses.shift();
      speeds.shift();
      cnt++;
    }
    if(cnt!==0) answer.push(cnt);
  }
  return answer;
}
console.log(solution([93,30,55],[1,30,5]))