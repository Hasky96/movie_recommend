<template>
  <div id="main-div">
    <!--이미지-->
    <section class="imgSection">
      <img :src="movie.poster_path" alt="poster" id="imgTag" >
    </section>
    <section class="contentSection">
      <p id="titleTag">{{movie.title}}</p>
      <p id="dateTag">{{movie.release_date}} 개봉</p>
      <p id="dateTag">{{genres_String}}</p>
      <p id="rankTag"> <i class="fas fa-star star"/> <span style="filter: contrast(10%);">{{movie.vote_average}}</span></p>
      <p id="contentTag">{{movie.overview}}</p>
      <p></p>
    </section>
    <section class="recommendTag" style="margin-top : 3rem;">
          <div class="recommend-div">
          <br>
          <h2 style="margin-top : 2rem;">추천 영화</h2>
          <div class="container" style="margin-top : 2rem">
              <swiper class="swiper" :options="swiperOption">
                <swiper-slide  v-for="movie in movies" :key="movie.id">
                  <div class="slide-content" style=" margin :0rem 0.5rem;" @click="move(movie[2])">
                      <img :src="movie[1]" alt="" style="width: 15rem; height: 18rem;"> 
                    <h5 class="recplat" style="width: 15rem;  padding : 0.5rem 0rem;">{{ movie[0] }}</h5> 
                    <br>
                  </div>
                </swiper-slide>
                <div class="swiper-pagination sp-custom" slot="pagination"></div>
                <div class="swiper-button-prev" slot="button-prev"></div>
                <div class="swiper-button-next" slot="button-next"></div>
              </swiper>
          </div>
        </div>
    </section>
    <section class="community">
      <nav>
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button class="nav-link active" id="nav-comment-tab" data-bs-toggle="tab" data-bs-target="#nav-comment" type="button" role="tab" aria-controls="nav-comment" aria-selected="true">Comments</button>
          <button class="nav-link" id="nav-review-tab" data-bs-toggle="tab" data-bs-target="#nav-review" type="button" role="tab" aria-controls="nav-review" aria-selected="false">Reviews</button>
        </div>
      </nav>
        <div class="tab-content" id="nav-tabContent">
          <div class="tab-pane fade show active oneline" id="nav-comment" role="tabpanel" aria-labelledby="nav-comment-tab">
            <movie-comment class="comment-tab"
            :comments="movie.comment_set"
            :movieid="movie.id"
            >
            </movie-comment>
          </div>
          <div class="tab-pane fade" id="nav-review" role="tabpanel" aria-labelledby="nav-review-tab">
            <review-list class="review"
            :movieId="movie.id"
            ></review-list>
          </div>
        </div>
    </section>
   <footer style="margin-top : 20rem; paddint-bottom : 5rem;">
      <fotter></fotter>
    </footer>
  </div>
</template>

<script>
import axios from 'axios'
import MovieComment from '@/components/MovieComment.vue'
import ReviewList from '@/components/ReviewList.vue'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import Fotter from '../components/fotter.vue'

export default {
  components: { 
    MovieComment,
    ReviewList,
    swiper,
    swiperSlide,
    Fotter
  },
  name: 'MovieDetail',
  data:function(){
    return {
      model: null,
      genres: {},
      movie: {},
      movieList : [],
      number : 1,
    swiperOption: {
          slidesPerView: 5,
          spaceBetween: 30,
          slidesPerGroup: 5,
          loop: true,
          loopFillGroupWithBlank: true,
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        }
    }
  },
  methods : {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getRecData(){
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/${this.$route.params.movieId}/genres/`,
        }).then(res=>{
          this.genres = res.data
        })
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/${this.$route.params.movieId}/info/`,
        }).then(res=>{
          this.movie = res.data
          axios({
            method: 'get',
            url: `http://127.0.0.1:8000/server/recommend/${res.data.id}/detail/`,
            headers: this.setToken(),
            }).then(res=>{
              // console.log(res)
              this.movieList = res.data
              const movie_list = []
              var step;
              for (step = 0; step < 24; step++) {
                movie_list.push([res.data.title[step], res.data.pp[step], res.data.pk[step]])
              } 
              this.movieList = movie_list
              }).catch(err=>{
                console.log(err)
              })
        }).catch(err=>{
          console.log(err)
        })
    },
    move(id){
      if(id!=this.$route.params.movieId){
        this.$router.replace(`/movie/${id}/`)
        this.getRecData()
        window.scrollTo(0,0)
      }
    }
  },
  created:function(){
    this.getRecData()
  },
  computed:{
    genres_String(){
      let str = ""
      this.genres.forEach(p => str+=p.name+" ")
      return str
    },
    movies:function(){
      const id = this.$route.params.movieId
      return this.movieList.filter( movie => movie[2] != id)
    }
  }
}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);
#main.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
.imgSection{
  height: 40vw;
  margin-top: 0.5em;
  background:black;
}
#imgTag{
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.contentSection{
  /*  */
}
#titleTag{
  font-size: 25px;
  letter-spacing: 0.2px;
  margin: 3vh 10vw;
  margin-bottom: 0px;
  text-align: left;
  color: #808080;
}
#dateTag{
  font-size: 13px;
  letter-spacing: 0.2px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
}
#rankTag{
  font-size: 34px;
  letter-spacing: 0.2px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
}
.star{
  color: gold;
}
#contentTag{
  font-size: 1rem;
  letter-spacing: 0.3px;
  text-align: left;
  margin-left: 10vw;
  margin-right: 10vw;
  color: #808080;
  height: 400px;
  overflow: auto;
}
#contentTag::-webkit-scrollbar{
  width : 1px;
  background-color:#1b1b1b;
  border: white 1px solid;
}
#contentTag::-webkit-scrollbar-thumb{
  border-radius: 3px;
  background-color:#A5A5A5;
}
#contentTag::-webkit-scrollbar-track{
  background-color:#1b1b1b;
}
.community{
  margin-top: 3em;
  margin-left: 10vw;
  margin-right: 10vw;
  background-color:#1b1b1b;
}
.recommendTag{
   /* 임시 어딘지 보라고 넣어논 border */
  background: #1b1b1b;
  height: 500px;
  margin-left: 10vw;
  margin-right: 10vw;
}
.review{
  padding: 20px;
  padding-left: 30px;
  padding-right: 30px;
}
.swiper-button-next,
.swiper-button-prev, 
.swiper-container-rtl .swiper-button-prev,
.swiper-container-rtl .swiper-button-next{
    fill: #000;
}
.recplat {
  background-color:#808080 !important;
  color:#1b1b1b !important;

font-family: 'Hanna', sans-serif;
}
.slide-content:hover{
  transform:scale(1.05);
}
.comment-tab{
  height: 700px;
}
.recommend-div{
  height: 500px;
}
.tab-content{
  height: 800;
}


</style>
<style>
.active{
  background-color:#808080 !important;
  color:#1b1b1b !important;
}
#nav-comment-tab, #nav-review-tab{
  color: #808080;
  text-align: center  !important;
}
.tab-pane{
  background-color: #1b1b1b !important;
}

.swiper-pagination-bullet-active {
  background-color: #000;
}
</style>
<style lang="scss" scoped>
.swiper-button-next, .swiper-container-rtl .swiper-button-prev .swiper-button-prev {
filter : hue-rotate(180deg) brightness(200%) contrast(10%);
fill: white;
--swiper-theme-color: #ffffff;
}
.swiper-button-prev , .swiper-container-rtl .swiper-button-prev .swiper-button-prev {
filter : hue-rotate(180deg) brightness(200%) contrast(10%);
fill: white;
--swiper-theme-color: #ffffff;
}
.swiper-pagination-bullet{
  opacity: 1;
  border: white solid 1px;
  background-color: transparent;
}
.swiper-pagination-bullet-active {
  background-color: #000;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}

</style>