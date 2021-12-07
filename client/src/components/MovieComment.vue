<template>
<div class="">
  <div class="px-5">
    <div class="newDiv row g-0 mb-3 d-flex justify-content-evenly">
      <div class="col-3 star-select" style="width : 5rem;">
        <select v-model="rankString" class="star star-select" name="" id="">
          <option class="star" value="1">★</option>
          <option value="2">★★</option>
          <option value="3">★★★</option>
          <option value="4">★★★★</option>
          <option value="5">★★★★★</option>
        </select>

      </div>
      <span class="col-7"><input v-model="content" type="text" @keyup.enter="write"></span><span class="col-2"><button @click="write">작성</button></span>
    </div>
    <div class="comments-list" >
      <article class="comment  px-5 " v-for="comment in commentss" :key="comment.id" >
        <span v-if="comment" class="content">{{comment.user.username}}</span>
        <span v-if="comment" class="text- mx-4 content"> : </span>
        <span v-if="comment" class="content">{{comment.content}}</span>
        <i v-if="comment" class="fas fa-star star ms-5"/> <span class="rank">{{comment.rank}}</span>
        <b-button v-if="user==comment.user.username" @click="deleteComment(comment.id)" class="btnsize" variant="outline-secondary">삭제</b-button>
      </article>
    </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  props:{
    comments: Array,
    movieid:Number
  },
  data:function(){
    return{
      newComments: null,
      content: null,
      rankString:"3",
      user:null,
    }
  },
  computed:{
    rankInt : function(){
      return parseInt(this.rankString)
    },
    commentss: function(){
      if(this.newComments){
        return this.newComments
      }else{
        return this.comments 
      }
    }
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    write(){
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/server/movies/${this.movieid}/comment_create/`,
        data: {
          content : this.content,
          rank: this.rankInt,
        },
        headers: this.setToken()
      }).then(()=>{
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/movies/${this.movieid}/comments/`,
        }).then(res=>{
          this.newComments = res.data.comment_set
          this.content = ''
        }).catch(err=>{
          console.log(err)
        })
      }).catch(err=>{
        console.log(err)
      })
    },
    deleteComment(id) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/server/movies/comments/${id}/del/`,
        headers: this.setToken()
        }).then(()=>{
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/server/movies/${this.movieid}/comments/`,
          }).then(res=>{
            this.newComments = res.data.comment_set
            this.content = ''
          }).catch(err=>{
            console.log(err)
          })
          // console.log(res)
        }).catch(err=>{
          console.log(err)
        })
    },
  },
  created(){
    this.user = localStorage.getItem('user')
  }
}
</script>

<style scoped>
.container{
  align-content: center;
  text-align: left;
  margin: 0px;
  padding: 0px;
  background-color: #1b1b1b;
  width: 100%;
  max-width: 100%;
}
.comments-list{
  overflow: auto;

}
.newDiv{
  top: 20px;
  margin: 0px;
  margin-top: 10px;
}
.newDiv > span > input{
  background: #1b1b1b;
  border: 1px #808080 solid;
  border-radius: 5px;
  font-size: 20px;
  color: #808080;
  width: 100%;
  padding-right: 0px;
}
.newDiv > span > button{
  background: #1b1b1b;
  color: #808080;
  border: 1px #808080 solid;
  border-radius: 5px;
  height: 40px;
  width: 100%;
}
.star{
  color: gold;
}
.comment{
  text-align: left;
  background-color: #1b1b1b;
  color: #808080;
  font-size: 1.5rem;
  border: 1px #808080 solid;
  border-radius: 5px;
  margin-top : 1rem;
  
}
.rank{
  font-size: 1.5rem;
}
.text-{
  font-size: 2rem;
}
.content{
  margin-left: 20px;
}
.star-select{
  -webkit-appearance: none;
  font-size: 22px;
  background-color: #1b1b1b;
  border: none;
}
.btnsize {
  width: 4rem;
  height: 2rem;
  font-size: 0.7rem;
  margin-left: 1rem;
  margin-bottom: 0.5rem;
}

</style>