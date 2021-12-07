<template>
<div >
<div class="main-div">
  <div class="page container grayborder" style="margin : auto; margin-bottom : 10rem;">
    <header class="hea grayborder">
      <p id="back" @click="$router.push({name:'Review'})"  style="margin-top : 1rem;" >리뷰></p>
      <h2 class="my-0 pb-0 reviewTitle"  style="">{{review.title}}</h2>
      
      <div class="py-0 mt-2"  >
      
      <div class="d-flex justify-content-between">
        <div>
          <span >작성자 : {{user}}</span>
          <br>
          <span >{{review.created_at|moment("from", "now")}}</span>
          <p class="my-0 " >별점 : {{review.rank}}</p>           
        </div>
        
        <div class="d-flex justify-content-end">
          <!-- user 정보가 리뷰 작성자 정보랑 일치 하면?? -->
          <div v-if="usercheck()"> 
          <button class="p-0 fs-6 text-light btn btnsize bg-danger" @click="deletes">delete</button>
          <button class="p-0 fs-6 text-light btn btnsize bg-info" @click="edit">update</button>
          </div>
          <div class="likediv">
            <button @click="like" :class="[this.liked ? 'fas':'', 'far']" class="btnheart fa-heart heart" style="" ></button> 
            <!-- 버튼 사이즈 조절하기 -->
            <span class="like">{{this.likes}}</span>
          </div>
        </div>
        </div>
      </div>
    </header>
    <hr>
    <section class="sec">
      <div class="row grayborder">
        <div class="col-4 p-0 text-center">
          <img :src="movie.poster_path" alt="" width="100%" style="margin: 0px; padding: 0.1em;">
          <div class="col">
          <h5 class="fw-bold">{{movie.title}}</h5>
          <span style="font-size: 0.9em">개봉 일자 : {{movie.release_date}}</span>  
        </div>
        </div>
        <div class="grayborder reviewContent col">
          <h5>{{review.content}}</h5>
        </div>
      </div>
    </section>
    <footer class="foot grayborder" >
      <comment
      :reviewId="review.id"
      :comments="review.comment_set"
      ></comment>
    </footer>
  </div>
  </div>
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Comment.vue'

export default {
  components: { 
    Comment ,
  },
  name: "ReviewDetail",
  data: function(){
    return {
      review: [],
      liked:null,
      movie: [],
      user : "",
      likes : null,
    }
  },
  created:function(){
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/accounts/liked-reviews/`,
        headers: this.setToken()
        }).then(res=>{
          const id = this.$route.params.reviewId
          // console.log(res.data.like_reviews)
          const list= res.data.like_reviews
          list.forEach(x=>{
            if(x.id == id){
              this.liked = true
              return
            }
          })
        }).catch(err=>{
          console.log(err)
        })
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/`,
    }).then(res=>{
      // console.log(res)
      this.review = res.data
      this.likes = this.review.like_users.length
      this.user = res.data.user.username
      axios({
        method: 'get',
        url : `http://127.0.0.1:8000/server/movies/${res.data.movie.id}/info/`,
      }).then(res=>{
        this.movie = res.data
      }).catch(err=>{
        console.log(err)
      })
    }).catch(err=>{
      console.log(err)
    })
    
  },
  methods : {
    usercheck(){
      const user = localStorage.getItem("user")
      if (user != this.user){
        return false
      }else{
        return true
      }
    },
    edit(){
      this.$router.push({path:`/review/${this.review.id}/update/`})
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    like() { 
      this.liked = !this.liked
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/like/`,
        headers: this.setToken()
        }).then(res=>{
          this.likes = res.data.review
        }).catch(err=>{
          console.log(err)
        })
    },
    update() {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/updel/`,
        headers: this.setToken()
        }).then(res=>{
          console.log(res)
        }).catch(err=>{
          console.log(err)
        })
    },
    deletes() {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/updel/`,
        headers: this.setToken()
        }).then(()=>{
          axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/server/community/reviews/',
          }).then(res=>{
          this.$store.dispatch("setReviews", res.data)
          return this.$router.push({name:'Review'})
          }).catch(err=>{
          console.log(err)
          })
        }).catch(err=>{
          console.log(err)
        })
    },
  },
  beforeRouteLeave(to, from, next) {
    if (this.canLeaveSite){// 
    }
    else{
      next();
    }
  }
}
</script>

<style scoped>
.main-div{
  margin-bottom: 10rem;
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
div{
  margin : 0px
}
*{
  padding: 2px;
  margin: 10px;
  text-align: left;
}
.page{

}
.hea{
  padding: 2px;
  height: 10%;
  position: relative;
}
.sec{
  padding: 2px;
  height: 70%;
  position: relative;
}
.foot{
  padding: 1em;
}
#back{
  margin-bottom: 0px;
  margin-top: 0px;
  color: #03c75a;
  font-size: 0.7rem;
}
#back{
  cursor: pointer;
}
.grayborder{
  background: #202020;
}
.reviewTitle{
  height: 3rem;
   overflow: auto;
   font-weight: 900;

   margin-bottom: 1rem;

}
.reviewContent{
  height: 25rem;
  overflow: auto;
  padding-top: 1rem;
  font-size: 1em;
  font-weight: 700;
}
.btnsize {
  width: 4rem;
  height: 2rem;
}
.btnheart {
  margin: 0px;
  padding: 0px;
  color: red;
  font-size: 1.5rem;
  border: none;
  background-color: #202020;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}
.like{
  font-size: 1.5rem;
  margin-left: 0.5rem;
}
.likediv{
  padding-top: 0.77rem;
}

</style>