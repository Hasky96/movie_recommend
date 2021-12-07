<template>
<div>
<div class="container">
  <div class="page-top">
      <div class="page-top-inner-wrap text-center">
        <h2 class="page-title recalltitle">리뷰 수정</h2>
      </div>
    </div>
  <div>
    <label for="reviewTitle"> </label>
    <b-input v-model="title" name="reviewTitle" type="text" placeholder="제목을 입력해 주세요"></b-input>
      <br>
    
    <div class="d-flex justify-content-between">
      <div class="movie-title">
      <label for="movieTitle"></label>
      <input  type="text"  @click="$bvModal.show('modal-movie')" name="movieTitle" :value='movieTitle' readonly placeholder="영화를 검색해 주세요"> 
      <b-button v-b-modal.modal-movie>영화검색</b-button>
      <b-modal id=modal-movie ok-title="확인" ok-only>
        <div>
          <input type="text" v-model="search" placeholder="영화제목을 입력하세요" style="width: 100%">
          <section style="overflow: auto; height: 500px;">
            <div class="movieItem p-2" v-for="movie in searchList" :key="movie.id" @click="setSearch(movie.pk , movie.fields.title)">
              <img :src="movie.fields.poster_path" height="100px" alt="">
              <section class="sec1">
                <p class="fs-5">{{movie.fields.title}}</p> 
                <p style="text-align: end;">개봉일{{movie.fields.release_date}}</p>
              </section>
            </div>
          </section>
        </div>
      </b-modal>
      </div>
      <div style="margin-right : 10rem;">
        <p style="margin-bottom : -1rem;">당신이 생각하는 영화 별점은?</p>
        <div class="rate">
          <input v-model="rankString" type="radio" id="star5" name="rate" value="5" />
          <label  for="star5" title="text">5 stars</label>
          <input v-model="rankString" type="radio" id="star4" name="rate" value="4" />
          <label for="star4" title="text">4 stars</label>
          <input v-model="rankString" type="radio" id="star3" name="rate" value="3" checked/>
          <label for="star3" title="text">3 stars</label>
          <input v-model="rankString" type="radio" id="star2" name="rate" value="2" />
          <label for="star2" title="text">2 stars</label>
          <input v-model="rankString" type="radio" id="star1" name="rate" value="1" />
          <label for="star1" title="text">1 star</label>
        </div>
      </div>

    </div>
    
    <label for="reviewContent"></label>
    <b-textarea v-model="content" 
    style="resize:none"
    name="reviewContent" type="textarea" cols="50" rows="10" placeholder="리뷰를 입력해 주세요"></b-textarea>
    <br>
    <b-button @click="$router.go(-1)" variant="outline-danger"  style="margin-right : 1rem;">취소</b-button>
    <b-button @click="create" variant="outline-success" >작성하기</b-button>
  </div>
  </div>
<footer style="margin-top : 20rem; paddint-bottom : 5rem;">
     <fotter></fotter>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import Fotter from '../components/fotter.vue'

export default {
  name: 'ReviewCreate',
  components : {
    Fotter
  },
  data:function(){
    return {
      searchList: null,
      search: null,
      movieTitle: null,
      movieId: null,
      rankString:"",
      title: null,
      content: null,
    }
  },
  computed:{
    rankInt : function(){
      return parseInt(this.rankString)
    }
  },
  watch:{
    search: function(){
      axios({
        method : 'get',
        url: 'http://127.0.0.1:8000/server/movies/search/1/',
        params:{
          keyword : String(this.search)
        }
      }).then(res=>{
        console.log(res)
        this.searchList = res.data
      }).catch(err=>{
        console.log(err)
      })
    },
  },
  methods:{
    setSearch(id, title){
      this.movieId = id
      this.movieTitle = title
      this.$bvModal.hide('modal-movie')
      // document.querySelector('#movieTitle').setText(title)

    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },

    create(){
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/updel/`,
        data: {
          title : this.title,
          content : this.content,
          rank: this.rankInt,
        },
        headers: this.setToken()
      }).then(()=>{
        axios({
          method: 'get',
          url: 'http://127.0.0.1:8000/server/community/reviews/',
        }).then(res=>{
          this.$store.dispatch("setReviews", res.data)
          return this.$router.push({path:`/review/${this.$route.params.reviewId}/`})
        }).catch(err=>{
          console.log(err)
          alert('입력값이 올바르지 않습니다.')
        })
      }).catch(err=>{
        console.log(err)
        alert('입력값이 올바르지 않습니다.')
      })
    }
  },
  beforeCreate(){
    const uUserInfo = localStorage.getItem("user")
    // 작성자와 페이지 접속한 사람이 같은지?
    axios({
      method : 'get',
      url: `http://127.0.0.1:8000/server/community/review/${this.$route.params.reviewId}/`
    }).then(res=>{
      // console.log(res)
      const data = res.data
      const uUserCheck = data.user.username
      if(uUserCheck != uUserInfo){
        alert("권한이 없습니다.")
        this.$router.go(-1)
      }else{
        this.movieTitle = data.movie.title
        this.movieId = data.movie.id
        this.rankString = data.rank
        this.title = data.title
        this.content = data.content
      }
    })
  },
  mounted: function () {
      axios({
        method : 'get',
        url: 'http://127.0.0.1:8000/server/movies/search/1/',
        params:{
          keyword : String("")
        }
      }).then(res=>{
        this.searchList = res.data
      }).catch(err=>{
        console.log(err)
      })
  },
}
</script>

<style scoped>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
.sec1{
  display: inline-block; 
  height: 100%;
  width:70%;
}

.movieItem:hover{
  cursor:pointer;
  background: #eee;
}

.rate {
  text-align: center;
  display: inline-block;
  margin: 0 auto;
  /* float: left; */
  height: 46px;
  padding: 0 10px;
}
.rate:not(:checked) > input {
  position:absolute;
  top:-9999px;
}
.rate:not(:checked) > label {
  float:right;
  width:1em;
  overflow:hidden;
  white-space:nowrap;
  cursor:pointer;
  font-size:30px;
  color:#ccc;
}
.rate:not(:checked) > label:before {
  content: '★ ';
}
.rate > input:checked ~ label {
  color: gold;    
}
.rate:not(:checked) > label:hover,
.rate:not(:checked) > label:hover ~ label {
  color: gold;  
}
.rate > input:checked + label:hover,
.rate > input:checked + label:hover ~ label,
.rate > input:checked ~ label:hover,
.rate > input:checked ~ label:hover ~ label,
.rate > label:hover ~ input:checked ~ label {
  color: gold;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}
.movie-title{
  text-align: left;
  width: 50%;
}
.movie-title>input{
  width: 50%;
  margin-right: 20px;
}
.btn-review{
  margin: 20px
}

</style>