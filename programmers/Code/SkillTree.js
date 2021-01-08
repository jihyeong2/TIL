function solution(skill, skill_trees) {
  function isCorrect(tree){
    let arr_skill = skill.split('');
    for(let i=0; i<tree.length; i++){
      if(!skill.includes(tree[i])) continue;
      if(tree[i] === arr_skill.shift()) continue;
      return false;
    }
    return true;
  }
  return skill_trees.filter(isCorrect).length;
}
console.log(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]));

console.log('afdasfsdf'.split('').filter(a=> a==='a'));