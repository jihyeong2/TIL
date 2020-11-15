<template>
  <div id="app">
    <SearchBar 
      :userInput="userInput"
      @changeUserInput="onChangeUserInput"
    />
    <VideoList :videos="videos" @onClick="onClick"/>
    <VideoDetail :selectedVideo="selectedVideo"/>
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import VideoDetail from './components/VideoDetail.vue'
import VideoList from './components/VideoList.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    SearchBar,
    VideoDetail,
    VideoList
  },
  data(){
    return {
      userInput:'',
      videos: [],
      selectedVideo: {},
    }
  },
  methods:{
    onChangeUserInput(input){
      this.userInput=input
      //유튜브 영상 검색하는 API 사용
      const API_URI='https://www.googleapis.com/youtube/v3/search'
      const API_KEY='AIzaSyD7RIzLQ_PlbzSaM_mEhaIMTubCzo8J9VI'
      if(this.userInput==='') return
      axios({
        url:API_URI,
        method:'GET',
        params:{
          key:API_KEY,
          part:'snippet',
          type:'video',
          q:this.userInput,
        }
      }).then(res=>{
        console.log(res.data)
        this.videos=res.data.items
      }).catch(err=>{
        console.log(err)
      })
    },
    onClick(video){
      this.selectedVideo=video
      console.log(this.selectedVideo)
    }
  },
  watch:{
    userInput(value){
      console.log(value)
      if(value === 'bad'){
        this.userInput=''
        alert('말조심!')
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
