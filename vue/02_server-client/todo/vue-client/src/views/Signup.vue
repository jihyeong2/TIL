<template>
  <form @submit="signup">
    <label for="username">username : </label>
    <input type="text" id="username" v-model="username">
    <br>
    <label for="password">password : </label>
    <input type="password" id="password" v-model="password">
    <br>
    <label for="passwordConfirm">passwordConfirm : </label>
    <input type="password" id="passwordConfirm" v-model="passwordConfirm">
    <br>
    <button>Signup</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  data(){
    return{
      username:'',
      password:'',
      passwordConfirm:'',
    }
  },
  methods:{
    signup(event){
      event.preventDefault()
      if(this.password!=this.passwordConfirm){
        alert('비밀번호가 일치하지 않습니다.')
        this.password=''
        this.passwordConfirm=''
      }
      else{
        axios({
          method:'POST',
          url:'http://127.0.0.1:8000/accounts/signup/',
          data:{
            'username':this.username,
            'password':this.password,
            'passwordConfirm':this.passwordConfirm
          }
        })
        .then(()=>{
          alert('회원가입이 완료되었습니다.')
          this.$router.push({name:'Login'})
        })
        .catch((err)=>{
          console.error(err)
          console.dir(err)
          // 이미 사용된 이름에 대해 에러메세지 띄우고 싶으면
          // err 객체 참조해서 조건 만들 것.
        })
      }
    }
  }
}
</script>

<style>

</style>