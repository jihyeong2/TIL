function solution(bridge_length, weight, truck_weights) {
  let q=[];
  let t=0,idx=0,num=truck_weights.length,sum=0;
  while(num){
      t++;
      const len=q.length;
      for(let i=0; i<len; i++){
          let [w,d]=q.shift();
          // console.log(w,d);
          if(d+1>bridge_length){
              sum-=w;
              num--;
              continue;
          }
          q.push([w,d+1]);
          console.log(t,q);
      }
      if (idx<truck_weights.length && sum+truck_weights[idx]<=weight){
           q.push([truck_weights[idx],1]);
          sum+=truck_weights[idx];
          idx++;
      }
      // console.log(`시간: ${t} 남은 트럭 : ${num}, 트럭인덱스 : ${idx}, ${q} ${q.length}`);
  }
  return t;
}
console.log(solution(2,10,[7,4,5,6]));