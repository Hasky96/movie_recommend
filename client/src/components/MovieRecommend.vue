<template>
  <div>
        <br>
  <h2 style="margin-top : 2rem;">추천 영화</h2>
  <div class="container" style="margin-top : 2rem">
        <swiper class="swiper" :options="swiperOption">
          <!-- div로 감싸고, 크기 조절하면 될 듯 -->
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[0]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[0] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[1]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[1] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[2]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[2] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[3]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[3] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[4]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[4] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[5]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[5] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[6]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[6] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[7]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[7] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[8]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[8] }}</p> <br></div></swiper-slide>
        <swiper-slide ><div style=" margin :0rem 0.5rem;"><img :src="this.movieList.pp[9]" alt="" style="width: 15rem; height: 18rem;"><p class="recplat" style="width: 15rem;">{{ this.movieList.title[9] }}</p> <br></div></swiper-slide>
        <div class="swiper-pagination" slot="pagination"></div>
        <div class="swiper-button-prev" slot="button-prev"></div>
        <div class="swiper-button-next" slot="button-next"></div>
      </swiper>
    </div>

  </div>
</template>

<script>
 import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
import axios from 'axios'

 export default {
    name: 'movierecommend',
    title: 'Scrollbar',
    components: {
      Swiper,
      SwiperSlide
    },
    data() {
      return {
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
        },
      movie: {},
      movieList : null,
      number : 1,

      
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
  },

    created:function(){
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
                this.movieList = res.data
              }).catch(err=>{
                console.log(err)
              })
    }).catch(err=>{
      console.log(err)
    })
    }

  }
</script>
