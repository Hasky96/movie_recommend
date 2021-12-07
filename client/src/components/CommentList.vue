<template>
  <div>
  <div class="comment " v-for="comment in commentList" :key="comment.id" style="margin: 1rem 0rem;">
    <span class="user">{{comment.user.username}}</span>
    <span class="mx-2">-</span>
    <span class="commenttext">{{comment.content}}</span>
    <b-button v-if="check(comment.user.username)" @click="deleteComment(comment.id)" class="btnsize">삭제</b-button>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {

  props:{
    reviewId: Number,
    comments: Array
  },
  data:function(){
    return {
      user:null,
      newComments:null,
    }
  },
  computed:{
    commentList(){
      if (this.newComments){
        return this.newComments
      }else{
        return this.comments
      }
    },
  },
  methods : {
    check(username){
      if(this.user==username){
        return true
      }else{
        return false
      }
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteComment(id) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/server/community/comments/${id}/del/`,
        headers: this.setToken()
        }).then(()=>{
          // console.log(res)
          axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/review/${this.reviewId}/comments/`,
          }).then(res=>{
            // console.log(res)
            this.newComments=res.data
          })
        }).catch(err=>{
          console.log(err)
          alert('권한이 없습니다.')
        })
    }
  },
  created(){
    this.user = localStorage.getItem('user')
  }
}
</script>

<style scoped>
.comment{
  padding-top: 0.5em;
  padding-bottom: 0.5em;
  width : 100%;
  margin: 0px;
}
.user{
  padding: 0.5em;
  border: #eee solid 1px;
  border-radius: 0.7em;
}
.commenttext{
  padding: 0.5em;
  border: #eee solid 1px;
  border-radius: 0.7em;
}
.line{
  font-size: 1.5em;
}
.btnsize {
  width: 4rem;
  height: 2rem;
  font-size: 0.7rem;
  margin-left: 1rem;
}
</style>