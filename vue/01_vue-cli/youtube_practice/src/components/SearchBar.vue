<template>
  <div>
    <input type="text" :value="userInput" @change="onChange">
  </div>
</template>

<script>
export default {
  props:{
    userInput:String,
  },
  methods:{
    onChange(event){
      this.$emit('changeUserInput',event.target.value)
    }
  }
}
</script>

<style>

</style>