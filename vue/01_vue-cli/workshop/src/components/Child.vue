<template>
  <div>
    <h1>Child</h1>
    <input type="text" @keyup="onChildDataChange">
    <p>appData: {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
  </div>
</template>

<script>
export default {
  props:{
    appData: {
      type: String,
    },
    parentData: {
      type: String,
    },
  },
  methods: {
    onChildDataChange(event){
      this.$emit('onChildDataChange', event.target.value)
    }
  },
}
</script>

<style>

</style>