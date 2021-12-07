<template>
  <div  class="container">
    <h1 class="rectitle" style="margin-top : 1rem; padding-top:1rem;"  v-if="tryNum != 3 ">키워드 추천 페이지 입니다!</h1>
    <!-- 키워드 입력  -->

    <b-form-input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 0 " @keyup.enter="onB"  placeholder="키워드를 입력해 주세요" class="keyword-input-button" style="width : 30rem; margin : auto;"></b-form-input>
    <b-form-input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 1 " @keyup.enter="onC"  placeholder="키워드를 입력해 주세요" class="keyword-input-button" style="width : 30rem; margin : auto;"></b-form-input>
    <b-form-input  type="text" name="" id="" v-model.trim="inputKeyword" v-if="tryNum == 2 " @keyup.enter="onD"  placeholder="키워드를 입력해 주세요" class="keyword-input-button" style="width : 30rem; margin : auto;"></b-form-input>
    <br>
    <b-button v-if="tryNum == 0" @click="onB"  style="margin : auto;">첫번째 전송</b-button>
    <b-button v-if="tryNum == 1" @click="onC"  style="margin : auto;">두번째 전송</b-button>
    <b-button v-if="tryNum == 2" @click="onD"  style="margin : auto;">세번째 전송</b-button>
    <b-button v-if="tryNum == 4" @click="reset"  variant="danger" style="margin-top : -2rem;">리셋</b-button>

    <!-- if 로 첫번째, 두번째 ,세번째 키워드 넣을 수 있도록 하고, 이후에는 연관 키워드 선택하기 or 그냥 키워드 입력하기로 할 수 있도록 -->
    <transition name="fade">
      <div v-if="tryNum == 1">
        <h2  class="rectitle">첫번째 키워드 {{ firstKeyword }}에 대한 연관 키워드 입니다.</h2>
        <div class="keyword-container">
          <div @click='onC(vec)' class="keyword" v-for="vec in firstData" :key="vec.id">
              {{vec}}
          </div>
        </div>
      </div>
    </transition>
    <transition name="fade">
      <div v-if="tryNum == 2">
        <h2  class="rectitle">첫번째 키워드 {{ firstKeyword }}</h2>
        <h2 class="rectitle">두번째 키워드 {{ secoundKeyword }}에 대한 연관 키워드 입니다.</h2>
        <div class="keyword-container">
          <div @click='onD(vec)' class="keyword" v-for="vec in secoundData" :key="vec.id">
              {{vec}}
          </div>
        </div>
      </div>
    </transition> 
    <transition name="fade">
      <div v-if="tryNum == 3">
        <div v-if="loding == 0">
        <h1  class="rectitle">선택하신 키워드는 다음과 같습니다.</h1>
        <p class="reckeyword" style="margin-bottom: 1rem;">첫번째 키워드 : {{firstKeyword}}</p>
        <p class="reckeyword" style="margin-bottom: 1rem;">두번째 키워드 : {{secoundKeyword}}</p>
        <p class="reckeyword" style="margin-bottom: 1rem;">세번째 키워드 : {{thirdKeyword}}</p>
        <b-button  @click="reset" style="margin-bottom:1rem;" variant="danger">리셋</b-button>
        <b-button v-if="tryNum == 3" @click="getMovie" style="margin-left:2rem; margin-bottom:1rem;"  variant="success">키워드 전송!</b-button>
        
        </div>
      </div>
    </transition>
   <transition name="fade" >
    <img src="..\assets\loding.gif" alt="" v-if="loding == 1" class="imgsize">
    </transition>
    <transition name="fade" >
    <div v-if="tryNum == 4" class="container">
      <div v-if="loding == 2" class="">
          <span style="font-size: 20px; color: rgb(164,219,214);font-family: 'Hanna', sans-serif;margin: 10px;">
            영화정보는 네이버에 검색된 결과가 나옵니다.
          </span>
        <hr>
          <div v-for="movieEl in movieList" v-bind:key="movieEl">
            <b-container class="bv-example-row text-center" style="margin: -0.5rem;" >
              <b-row   >
                <b-col cols="1" class="reccontent" style="margin: auto;">{{movieEl[0]}}</b-col>
                <b-col cols="4" class="reccontent" style="margin: auto;">{{movieEl[1]}}</b-col>
                <b-col cols="5" class="reccontent" style="margin: auto;">{{movieEl[2]}}</b-col>
                <b-col cols="1" class="reccontent" style="margin: auto;">
                  <a target="_blank" v-if="movieEl[0] != '순번'" :href="movieEl[3]">  <b-button  style="margin: auto;">이동</b-button></a>
                    <p v-if="movieEl[0] == '순번'" style="margin: auto;">{{movieEl[3]}}</p>
                  </b-col>
              </b-row>
            </b-container>
            <hr>
          </div>
        
      </div>
    </div>
  </transition>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name :'RecommendKeyword',
  data: function(){
      return {
        tryNum : 0,
        firstData: null,
        firstKeyword : null,
        inputKeyword : null,
        secoundKeyword: null,
        secoundData : null,
        thirdData : null,
        thirdKeyword : null,
        movieData : null,
        reviewData : null,
        loding :0 ,
        number : 1,
        movieList : null,
        keywordTitle : null,
        show: true
      }
    },
  methods :{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    onB : function(){
      
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      if (Keyword.inputKeyword) {
        
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          if (res.data.state == true){
          this.loding = 1
          this.firstData = res.data.Veclist1
          this.firstKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    onC : function(word){
      this.inputKeyword ??=word
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      if (Keyword.inputKeyword) {
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          this.loding = 1 
          if (res.data.state == true){
          this.secoundData = res.data.Veclist1
          this.secoundKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    onD : function(word){
      this.inputKeyword ??=word
      const Keyword = {
        inputKeyword: this.inputKeyword,
      }
      if (this.inputKeyword == null){
        alert('빈 키워드는 입력하실 수 없습니다!')
        this.loding = 0
      } else{
      
      if (Keyword.inputKeyword) {
        this.loding = 1
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
         if (res.data.state == true){
          this.thirdData = res.data.Veclist1
          this.thirdKeyword = res.data.first_keyword
          this.tryNum += 1
          this.inputKeyword = null
          this.loding = 0
          } else {
            alert('다른 키워드를 입력해 주세요!')
            this.loding = 0
          }
        }).catch(err=>{
          console.log(err)
        })
      }}
    },
    getMovie : function(){
      this.loding = 1
      const keyWordData = {
        firstData : this.firstData,
        firstKeyword : this.firstKeyword,
        secoundData: this.secoundData,
        secoundKeyword : this.secoundKeyword,
        thirdData : this.thirdData,
        thirdKeyword : this.thirdKeyword,
      }
      axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/server/recommend/movie/',
      data: keyWordData,
      headers: this.setToken()
      }).then(res=>{
        this.movieData = res.data.movie_list
        const movie_list = [['순번' ,'제목', '사용자 리뷰','영화링크']]

        var step;
        for (step = 0; step < 20; step++) {
          movie_list.push([this.number,res.data.movie_list.영화명[step], res.data.movie_list.리뷰[step],`https://movie.naver.com/movie/search/result.naver?query=${res.data.movie_list.영화명[step]}&section=all`])
          this.number += 1
        } 
        this.movieList = movie_list
        this.tryNum += 1
        this.loding = 2
        this.number = 1
      }).catch(err=>{
        console.log(err)
        this.loding = 2
      })
      
    },
    reset : function() {
      this.loding = 0
      this.tryNum = 0
    } 
    }
    
  }
  
  
</script>
<style scoped>
.keyword-container{
  margin-top: 30px;
  position: relative;
  width: 100%
}
.keyword{
  font-family: 'Hanna', sans-serif;
  font-size:20px;
  margin: 2%;
  text-align: center;
  padding: 10px;
  display: inline-block;
  background-color: #adb5bd;
  color: #1b1b1b;
  border: solid #adb5bd 1px;
  border-radius: 10px;
  width: 16%;
}
.keyword:hover{
  transform: scale(1.1);
  cursor: pointer;
}
</style>
<style scoped>
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);
.fade-enter {
  opacity: 0;
}
.fade-enter-active{
  transition: opacity 1s ease-in;
  }
.fade-leave-active {
  transition: opacity 0.2s ease-out;
}
.fade-leave-to {
   opacity: 0;

}
.keyword-input-button {
  height: 2rem;
  width: 10rem;
}
.reccontent {
  margin: auto;
  color: #dddddd;
  font-family: 'Hanna', sans-serif;

}
.reckeyword {
  margin: auto;
  color: #dddddd;
  font-family: 'Hanna', sans-serif;
  font-size: 2rem;
}
.rectitle {
  margin-bottom: 1rem;
  color: #dddddd;
  font-family: 'Hanna', sans-serif;
}
.imgsize {
  margin-top: 5rem;
  width: 20rem;
  height: 20rem;
}
</style>