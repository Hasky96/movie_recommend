<template>
<div>
  <div>
  <div class="main-div">
    <div class="page-top">
      <div class="page-top-inner-wrap text-center">
        <h2 class="page-title ">추천 시스템</h2>
      </div>
    </div>
  <div class="mt-5 container ">
      
    </div >
      <transition name="fade">
      <div v-if="selected == null" class="d-flex justify-content-center">
        <a href="#"  @click="keyword" style="text-decoration:none; margin-right: 10rem;">
          <div class="recbox">
            <img src="..\assets\keypa.png" alt="" class="recpic2">
            <h2 class="rectitle">키워드 추천</h2>
            <div class="reccontent">
              <h4>선택한 키워드를 바탕으로</h4>
              <h4> 연관된 영화를 추천합니다.</h4>
            </div>
          </div>
        </a>
        <a href="#"  @click="title" style="text-decoration:none; margin-left: 2rem;">
          <div class="recbox" @click="title">
            <img src="..\assets\keyword2.png" alt="" class="recpic2">
            <h2 class="rectitle">유사도 추천</h2>
            <div class="reccontent">
              <h4> COS 유사도를 바탕으로 선택한 영화와</h4>
              <h4>  가장 비슷한 영화를 추천합니다.</h4>
            </div>
          </div>
        </a>
    </div>
    </transition>
    <transition name="fade">
    <div v-if="selected == 1">
      
      <div  class="d-flex justify-content-center">
      <b-button @click="keyword" class="m-3 mt-0 mb-2">키워드 추천</b-button>
      <b-button @click="title" class="m-3 mt-0 mb-2">타이틀 추천</b-button>
      </div>
      <transition name="fade">
              <recommend-detail style="margin-bottom : 30rem"></recommend-detail>
      </transition>
    </div>
    </transition>
    <transition name="fade">
    <div v-if="selected == 2">
      
      <div class="d-flex justify-content-center">
      <b-button @click="keyword" class="m-3 mt-0 mb-2">키워드 추천</b-button>
      <b-button @click="title" class="m-3 mt-0 mb-2">타이틀 추천</b-button>
      </div>
      <transition name="fade">
      <recommend-title style="margin-bottom : 30rem"></recommend-title>
      </transition>
    </div>
    </transition>
    </div>
    </div>
    <footer style="margin-top : 80rem; paddint-bottom : 5rem; fixed-bottom">
      <fotter></fotter>
    </footer>
  </div>
</template>

<script>
import RecommendDetail from '@/components/RecommendDetail.vue'
import RecommendTitle from '@/components/RecommendTitle.vue'
import Fotter from '../components/fotter.vue'

export default {
  name: "Recommend",
  components: {
    RecommendDetail,
    RecommendTitle,
    Fotter

  },
  data: function(){
      return {
        tryNum : 0,
        selected: null
      }
  },
  methods :{
    keyword : function() {
      this.selected = 1
    },
    title : function() {
      this.selected = 2
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      //pass
    } else {
      alert("로그인 해주세요!")
      this.$router.push({name: 'Login'})
    }
  }

}
</script>

<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
  height: 80vh;
}
.fade-enter {
  opacity: 0;
}
.fade-enter-active{
  transition: opacity 0.3s ease-in;
  }
.fade-leave-active {
  transition: opacity 0s ease-out;
}
.fade-leave-to {
   opacity: 0;

}
.recpic2 {
  width: 15rem; 
  height: 15rem;
  margin-top: 2rem;
  margin-bottom: 1rem;
}
.reccontent {
  margin: auto;
  color: white;
  font-family: 'Hanna', sans-serif;

}
.rectitle {
  margin-bottom: 1rem;
  color: white;
  font-family: 'Hanna', sans-serif;
}

.recbox {
  border: solid;
  border-color: white;
  border-radius: 20px;
  width: 25rem; 
  height: 28rem;
  background: #1b1b1b;
  opacity:0.9; 
  padding: 0.5  rem;
}
.page-top-inner-wrap {
    position: relative;
    max-width: 1240px;
    margin: 0px auto;
    text-align: left;
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
.ft-logo {
  margin :auto;
  margin-top: 1rem;
  width: 4rem;
}

</style>