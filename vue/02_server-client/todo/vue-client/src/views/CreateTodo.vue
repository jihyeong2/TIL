<template>
  <form @submit="onSubmit">
    <input type="text" v-model="content">
    <button><b>+</b></button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateTodo',
  data(){
    return {
      content:'',
    }
  },
  methods:{
    onSubmit(event){
      event.preventDefault()
      axios({
        url:'http://127.0.0.1:8000/todos/',
        method:'POST',
        data:{
          content:this.content
        },
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then(()=>{
        this.$router.push({ name: 'TodoList' })
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>