<template>
  <div>
    <h1>App</h1>
    <input type="text" v-model="appData" >
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <!-- onParentDataChange라는 이름의 이벤트리스너를 달아둠 -->
    <!-- Parent에서 해당 이벤트 발생시키면 내가 필요한 일(onParentDataChange) 함 -->
    <Parent 
      :appData="appData"
      :parentData="parentData"
      :childData="childData"
      @onParentDataChange="onParentDataChange"
      @onChildDataChange="onChildDataChange"
    />
  </div>
</template>

<script>
import Parent from './components/Parent.vue'

export default {
  name:'App',
  components:{
    Parent,
  },
  data: function (){
    return {
      appData:'',
      parentData: '',
      childData: '',
    }
  },
  methods:{
    // onParentDataChange 이벤트 발생시 해야될 일
    // 이벤트 발생 시 인자 전달 받는 것 가능
    onParentDataChange: function(parentData){
      this.parentData = parentData
    },
    onChildDataChange: function(childData){
      this.childData = childData
    },
  }
}
</script>

<style>

</style>