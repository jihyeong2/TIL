function solution(n) {
  let sum=n*(n+1)/2;
  let answer = new Array(sum).fill(0);
  let visit= new Array(sum).fill(0);
  let dirs=[0,1,0];
  let dir=0, num=1, idx=0;
  for(let i=0; i<sum;){
      idx+=dirs[dir];
      if(visit[idx] || idx>=sum){
          idx-=dirs[dir];
          if(dir==0) dirs[2]=-dirs[0];
          else if(dir==2) dirs[0]=-dirs[2];
          dir = dir+1<3 ? dir+1 : 0;
      }
      else{
          visit[idx]=1;
          answer[idx]=num++;
          if(dir!==1) dirs[dir]++;
          i++;
      }
  }
  return answer;
}