<template>
  <div style="margin-top : 5rem;" >
      <span class="slot-info d-flex flex-row tag-color" style="font-family: 'Hanna', sans-serif;" ># 강호 최강자 # 무림 협객!</span>      <swiper class="swiper" :options="swiperOption" style="margin-top : 2rem;">
        <swiper-slide v-for="movieEl in movie" :key="movieEl.id">
          <a href="" style="text-decoration:none;"  @click="move(movieEl.id)"><div class="slide-content" style=" margin :0rem 0.5rem;">
            <img :src="movieEl.poster_path" alt="" style="width: 15rem; height: 18rem;"> 
            <h5 class="recplat" style="width: 15rem;  padding : 0.5rem 0rem;">{{movieEl.title}}</h5> 
            <br>
          </div></a>
        </swiper-slide>
        
    

        <div class="swiper-pagination sp-custom" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>

  </div>
</template>

<script>
import Vue from 'vue'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import { CarouselPlugin } from 'bootstrap-vue'
import axios from 'axios'
Vue.use(CarouselPlugin)
export default {
  name: "Slot1",
  components: { 
        swiper,
    swiperSlide,

  },
  data() {
      return {
        movie : {},
        slide: 5,
        sliding: null,
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
          },
        }
      }
    },
      computed:{

  },
  methods: {
  onSlideStart() {
    this.sliding = true

  },
  onSlideEnd() {
    this.sliding = false
      
  },
  getRecData(){
    const keyword = [485,516,1001,630,1223,2330,3595,3594,3071,1313,3072]

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/server/movies/slot/`,
      data : {
        target : keyword}
      }).then(res=>{
        this.movie = res.data

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
}
}
</script>

<style>
  @import url(//fonts.googleapis.com/earlyaccess/hanna.css);

.slide-content:hover{
  transform:scale(1.05);
}
.recplat {
  background-color:#808080 !important;
  color:#1b1b1b !important;

font-family: 'Hanna', sans-serif;
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
.slot-info {
  font-family: 'Hanna', sans-serif;
  font-size: 2rem;
}
</style>