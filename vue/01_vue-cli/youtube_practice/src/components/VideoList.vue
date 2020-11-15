<template>
  <div>
    <ul>
      <VideoItem
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @onClick="onClick"
      />
    </ul>
  </div>
</template>

<script>
import VideoItem from '@/components/VideoItem.vue'
export default {
  components:{
    VideoItem,
  },
  props:{
    videos:Array
  },
  methods:{
    onClick(video){
      // console.log(video)
      this.$emit('onClick',video)
    }
  }
}
</script>

<style>

</style>