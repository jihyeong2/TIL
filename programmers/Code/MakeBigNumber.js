function solution(number, k) {
  let answer=[];
  number=number.split("");
  for(let i=0; i<number.length; i++){
      const num = number[i];
      while(k>0 && answer.length!==0 && answer[answer.length-1]<num){
          answer.pop();
          k--;
      }
      answer.push(num);
  }
  answer.splice(answer.length-k,k);
  return answer.join("");
}