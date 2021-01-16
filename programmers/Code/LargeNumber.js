function solution(numbers) {
  const str = numbers.sort((a,b) => ((b+''+a)*1-(a+''+b)*1)).join('');
  return str[0] === '0' ? '0': str;
}
console.log(solution([6, 10, 2]))