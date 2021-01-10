// function solution(priorities, location) {
//   let cnt=0;
//   let curr_idx=0;
//   while(true){
//     let target = priorities.shift();
//     if(priorities.filter(num => num>target).length !== 0){
//       priorities.push(target);
//     }
//     else{
//       cnt++;
//       if(curr_idx===location) return cnt;
//     }
//     curr_idx = curr_idx>=priorities.length ? curr_idx=0 : curr_idx + 1;
//   }
// }
// console.log(solution([2, 1, 3, 2],2));
// console.log(solution([1,1,9,1,1,1],0));