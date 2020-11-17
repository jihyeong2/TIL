<template>
  <div>
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input type="checkbox" :checked="todo.completed" @click="updateTodo(todo)">
        <span @click="updateTodo(todo)">{{ todo.content }}</span>
        <button @click="deleteTodo(todo.id)"><b>X</b></button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios'
// const  SERVER_URL = process.env.VUE_APP_SERVER_URL
export default {
  name: 'TodoList',
  data() {
    return {
      todos: [],
    }
  },
  methods:{
    updateTodo(todo){
      axios({
        url:`http://127.0.0.1:8000/todos/${todo.id}/`,
        method:'PUT',
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
        data:{
          ...todo,
          completed:!todo.completed,
        }
      })
      .then((res)=>{
        console.log(res)
        todo.completed=res.data.completed
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    deleteTodo(id){
      axios({
        url:`http://127.0.0.1:8000/todos/${id}/`,
        method:'DELETE',
        headers:{
          Authorization: `JWT ${localStorage.getItem('jwt')}`
        },
      })
      .then((res)=>{
        this.todos=this.todos.filter((todo)=>{
          return todo.id != res.data.id
        })
      })
      .catch((err)=>{
        console.log(err)
      })
    }
  },
  created() {
    // todos를 api를 찔러서 가져와서
    // data의 todos에 할당해준다
    // 가져오는 척을 할겁니다
    axios({
      url:'http://127.0.0.1:8000/todos',
      method:'GET',
      headers:{
        Authorization: `JWT ${localStorage.getItem('jwt')}`
      },
    })
    .then((res)=>{
      this.todos=res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  },
}
</script>

<style>

</style>