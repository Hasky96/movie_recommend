<template>
  <div style="margin-bottom: 10rem;">
    <comment-new
    :reviewId="reviewId"
    @refresh="refresh"
    ></comment-new>
    <comment-list
    :reviewId="reviewId"
    :comments="propdata"
    ></comment-list>
  </div>
</template>

<script>
import axios from 'axios'
import CommentNew from '@/components/CommentNew.vue'
import CommentList from '@/components/CommentList.vue'

export default {
  components:{
    CommentNew,
    CommentList
  },
  props:{
    reviewId:Number, 
    comments: Array
  },
  data:function(){
    return{
      new_comments:null
    }
  },
  computed:{
    propdata:function(){
      if(this.new_comments){
        return this.new_comments
      }else{
        return this.comments
      }
    }
  },
  methods:{
    refresh:function(){
      axios({
        method: 'GET',
        url: `http://127.0.0.1:8000/server/community/review/${this.reviewId}/comments/`
      }).then(res=>{
        console.log(res)
        this.new_comments = res.data
      }).catch(err=>{
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>