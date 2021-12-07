<template>
  <div>

      <div class="casel">
        <b-carousel
        id="carousel-fade"
        v-model="slide"
        :interval="4000"
        controls
        fade
        indicators
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
      >
        <a href="#" @click="move1()"><b-carousel-slide
          img-src="https://blog.kakaocdn.net/dn/bCyVRA/btrl01k1Hoy/Uk9gobu3m0iwJ5rsZR71Kk/img.jpg"
        ></b-carousel-slide></a>

        <a href="#" @click="move2()"><b-carousel-slide 
        img-src="https://blog.kakaocdn.net/dn/uMH8H/btrl00zy4pS/vhlnrBlmCQVAKU6wmaYfJ1/img.jpg">
        </b-carousel-slide></a>

        <a href="#" @click="move3()"><b-carousel-slide 
        img-src="https://blog.kakaocdn.net/dn/boQlPa/btrl439IerO/hKgDaKojQkE5r6zMwnZawk/img.jpg">
        </b-carousel-slide></a>

        <a href="#" @click="move4()"><b-carousel-slide 
        img-src="https://blog.kakaocdn.net/dn/YjoP9/btrl6OxbfLv/x8l6RHPXNUksEgJcR8k58k/img.jpg">
        </b-carousel-slide></a>

        <a href="#" @click="move5()"><b-carousel-slide 
        img-src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FVfkYK%2Fbtrl1Xo5uki%2F29hXRYjYwCiW0GESyelyX0%2Fimg.jpg">
        </b-carousel-slide></a>
      </b-carousel>
  </div>
  <div class="container ">
    <br>
    <slot-1 class="slot"></slot-1>
    <slot-2 class="slot"></slot-2>
    <slot-3 class="slot"></slot-3>
    <slot-4 class="slot"></slot-4>
    <!-- 하부 슬라이더 들 -->
  
  </div>
<footer style="margin-top : 20rem; paddint-bottom : 5rem;">
      <fotter></fotter>
    </footer>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import Vue from 'vue'
import 'swiper/dist/css/swiper.css'
import { CarouselPlugin } from 'bootstrap-vue'
import Slot1 from '../components/main/slot1.vue'
import Slot2 from '../components/main/slot2.vue'
import Slot3 from '../components/main/slot3.vue'
import Slot4 from '../components/main/slot4.vue'
import Fotter from '../components/fotter.vue'

Vue.use(CarouselPlugin)
export default {
  name: "Home",
  components: { 
    Slot1,
    Slot2,
    Slot3,
    Slot4,
    Fotter
  },
  data() {
      return {
        slide: 2,
        sliding: null,
        swiperOption: {
          slidesPerView: 2,
          spaceBetween: 30,
          slidesPerGroup: 2,
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
  computed:{
    ...mapState(['movies'])
  },
  methods: {
  onSlideStart() {
    this.sliding = true
  },
  onSlideEnd() {
    this.sliding = false

  },
  move1(){
    this.$router.replace(`/movie/930/`)
    window.scrollTo(0,0)
    },
  move2(){
    this.$router.replace(`/movie/1/`)
    window.scrollTo(0,0)
    },
  move3(){
    this.$router.replace(`/movie/3640/`)
    window.scrollTo(0,0)
    },
  move4(){
    this.$router.replace(`/recommend/`)
    window.scrollTo(0,0)
    },
  move5(){
    this.$router.replace(`/movie/1208/`)
    window.scrollTo(0,0)
    },
}
}
</script>

<style scoped>

.slot {
  margin : 5rem 0rem;
}
.casel {
  margin : 0rem 19rem;
}
.carousel-fade .carousel-item {
    opacity: 0;
    transition-property: opacity;
    transform: none;
    display: block;
}
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}

</style>
<style >

</style>
