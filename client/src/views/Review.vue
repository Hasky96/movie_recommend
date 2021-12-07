<template>
  <div>
  <div class="main-div" >
    <div class="page-top">
      <div class="page-top-inner-wrap text-center">
        <h2 class="page-title ">리뷰 리스트</h2>
      </div>
    </div>
    <div class="container recboxs">
    <review-list
    v-model='movieId'
    :reviews="reviews"
    :movieId="movieId"
    ></review-list>
    
    <br>
    <hr>
    <div class="d-flex flex-row justify-content-between">
      <select v-model="movieId" >
        <option value="null">리뷰를 확인 할 영화를 선택해주세요</option>
        <option v-for="title in moviesTitles" :key="title.id" :value="title.id">{{title.title}}</option>
      </select>
      <b-button @click="$router.push({name: 'ReviewCreate'})" >new Review</b-button>
    </div>
    </div>
    </div>
  <footer style="margin-top : 20rem; paddint-bottom : 5rem;">
        <fotter></fotter>
    </footer>
  <!-- {{reviews}} -->
  </div>
</template>

<script>
import _ from 'lodash'
import ReviewList from '@/components/ReviewList.vue'
// import {mapState} from 'vuex'
import Fotter from '../components/fotter.vue'
import axios from 'axios'
// import axios from 'axios'

export default {
  name: "Reviews",
  components:{
    ReviewList,
    Fotter
  },
  data:function(){
    return{
      reviews: [],
      movies:[],
      movieId : null,
    }
  }, 
  methods:{
  },
  computed:{
    // ...mapState(['reviews']),
    moviesTitles(){
      let arr = []
      this.reviews.forEach(x => {arr.push(x.movie_info)});
      return _.uniqBy(arr, 'id')
    }
  },
  watch:{
    id: function(){
      alert(this.id)
    }
  },
  mounted(){
     axios({
        method : 'get',
        url: 'http://127.0.0.1:8000/server/community/reviews/',
      }).then(res=>{
        console.log(res)
        this.reviews = res.data
      }).catch(err=>{
        console.log(err)
      })
  }
}
</script>

<style>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
.recboxs {
  /* border-radius: 20px; */
  opacity:0.9; 
  margin-top: 3rem;
  padding:2rem;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}
.page-title {
    font-size: 3rem;
    line-height: 36px;
    color: rgb(255, 255, 255);
    font-family: 'Hanna', sans-serif;
    font-weight: 400;
}
.page-top {
  background: #1b1b1b;
  padding: 40px 0px;
  text-align: left;
  margin: 0 auto;

}
</style>