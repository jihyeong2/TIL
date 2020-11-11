<template>
  <div>
    <h1>App</h1>
    <input type="text" v-model="appData">
    <p>appData:{{appData}}</p>
    <p>parentData:{{parentData}}</p>
    <p>childData: {{childData}}</p>
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
import Parent from '@/components/Parent.vue'
export default {
  name:'App',
  components:{
    Parent,
  },
  data: function(){
    return {
      appData:'',
      parentData:'',
      childData:'',
    }
  },
  methods:{
    onParentDataChange: function(parentData){
      this.parentData=parentData
    },
    onChildDataChange: function(childData){
      this.childData=childData
    }
  }
}
</script>

<style>

</style>