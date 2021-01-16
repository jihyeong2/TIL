function solution(numbers) {
  let answer = 0;
  function comb(z,lim,ans,visit){
      let cnt=0;
      if(z==lim){
          const num = parseInt(ans,10);
          if(num==1) return 0;
          for(let i=2; i<num; i++){
              if(num%i==0) return 0;
          }
          return 1;
      }
      else{
          let check =new Array(10).fill(0);
          for(let i=0; i<numbers.length; i++){
              const num=parseInt(numbers[i],10);
              if(z==0 && num==0 || check[num] || visit[i]) continue;
              check[num]=1;
              visit[i]=1;
              cnt+=comb(z+1,lim,ans+numbers[i],visit);
              visit[i]=0;
          }
      }
      return cnt;
  }
  for(let i=1; i<=numbers.length; i++){
      let visit =new Array(10).fill(0);
      answer+=comb(0,i,'',visit);
  }
  return answer;
}