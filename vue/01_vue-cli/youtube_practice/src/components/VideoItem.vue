<template>
  <div>
    <li @click="onClick">
      <img :src="youtubeURL" alt="thumbnail" width="320" height="180" >
      <span>{{youtubeTitle}}</span>
    </li>
  </div>
</template>

<script>
import _ from 'lodash'
export default {
  props:{
    video:Object
  },
  computed:{
    youtubeURL(){
      return this.video.snippet.thumbnails.medium.url
    },
    youtubeTitle(){
      return _.unescape(this.video.snippet.title)
    }
  },
  methods:{
    onClick() {
      this.$emit('onClick',this.video)
    }
  }
}
</script>

<style>

</style>