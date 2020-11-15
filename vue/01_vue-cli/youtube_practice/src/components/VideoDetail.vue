<template>
  <div v-if="isPossible">
    <iframe :src="selectedURI" frameborder="0" width="400" height="320"></iframe>
  </div>
</template>

<script>
export default {
  props:{
    selectedVideo:Object
  },
  computed:{
    selectedURI(){
      const videoId=this.selectedVideo.id.videoId
      console.log(videoId)
      return `https://www.youtube.com/embed/${videoId}`
    },
    isPossible(){
      // return Object.keys(this.selectedVideo).length>0 ? true : false
      for(const key in this.selectedVideo){
        return true
      }
      return false
    }
  }
}
</script>

<style>

</style>