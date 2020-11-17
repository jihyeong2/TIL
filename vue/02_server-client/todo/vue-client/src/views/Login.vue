<template>
  <form @submit="login">
    <label for="username">username : </label>
    <input type="text" id="username" v-model="username">
    <br>
    <label for="password">password : </label>
    <input type="password" id="password" v-model="password">
    <br>
    <button>Login</button>
  </form>
</template>

<script>
import Axios from 'axios'
export default {
  data(){
    return{
      username:'',
      password:'',
    }
  },
  methods:{
    login(event){
      event.preventDefault()
      Axios({
        url:'http://127.0.0.1:8000/accounts/api-token-auth/',
        method:'POST',
        data:{
          username:this.username,
          password:this.password
        }
      })
      .then((res)=>{
        console.log(res.data)
        localStorage.setItem('jwt',res.data.token)
        this.$emit('login')
        this.$router.push({name:'TodoList'})
      })
      .catch((err)=>{
        console.error(err)
      })
    }
  }
}
</script>

<style>

</style>