function solution(p) {
  function isCorrect(text){
    let s=[];
    for(let i=0; i<text.length; i++){
      if(text[i]==='(') s.push(text[i]);
      else{
        if(s.length==0) return false;
        s.pop();
      }
    }
      return s.length==0 ? true : false;
  }
  function bracket(text){
    if(text==='') return text;
    let u='',v='';
    let openCnt=0, closeCnt=0, idx;
    for(idx=0; idx<text.length; idx++){
      if(text[idx]=='('){
        openCnt++;
      }
      else{
        closeCnt++;
      }
      if(openCnt==closeCnt){
        u=text.slice(0,idx+1);
        v=text.slice(idx+1,text.length);
        break;
      }
    }
    if(isCorrect(u)){
      return u+bracket(v);
    }
    else{
      return '('+bracket(v)+')'+u.slice(1,u.length-1).split("").map(x=>x==='('?')':'(').join("");
    }
  }
  return bracket(p);
}