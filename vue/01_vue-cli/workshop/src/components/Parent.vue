<template>
  <div>
    <h1>Parent</h1>
    <input type="text" @keyup="onChange">
    <p>appData: {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <Child
      :appData="appData"
      :parentData="parentData"
      @onChildDataChange="onChildDataChange"
    />
  </div>
</template>

<script>
import Child from './Child.vue'
export default {
  components:{
    Child,
  },
  // props: ['appData',], 이렇게도 가능!
  props:{
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
    childData: {
      type: String,
    },
  },
  methods: {
    onChange: function(event){
      // 부모가 달아둔 onParentDataChange라는 이벤트 발생시킴
      // 발생시키면서 인자 전달
      this.$emit('onParentDataChange', event.target.value)
    },
    onChildDataChange(childData) {
      this.$emit('onChildDataChange', childData)
    }
  }
}
</script>

<style>

</style>