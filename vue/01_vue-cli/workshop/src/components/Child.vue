<template>
  <div>
    <h1>Child</h1>
    <input type="text" @keypress="onChange">
    <p>appData: {{appData}}</p>
    <p>parentData: {{parentData}}</p>
  </div>
</template>

<script>
export default {
  name:"Child",
  props:{
    appData:String,
    parentData:String,
    childData:String,
  },
  methods:{
    onChange:function(event){
      console.log(event.target.value)
      this.$emit('onChildDataChange',event.target.value)
    }
  }
}
// 어떤 상황에서 자식 컴포넌트에 data를 쓰면 안되는가?
// 자식에서 발생하는 data인데, 부모가 쓰거나, 혹은 형제가 사용한다.
// 자식->부모로 data를 직접적으로 전달하는 것이 불가능

// 해결법 : 부모에 data를 만든다.
</script>

<style>

</style>