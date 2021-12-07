<template>
  <div class="container">
    <h1 class="rectitle" style="margin-top : 1rem; padding-top:1rem;">추천 타이틀 페이지 입니다.</h1>
    <div >
    <b-form-input type="text" name="" id="" v-model.trim="titleGet" class="" @keyup.enter="titleSend"  placeholder="영화 제목을 입력해 주세요" style="width : 30rem; margin : auto;  margin-bottom : 0.5rem;">  </b-form-input>
    <b-button  @click="titleSend"  class="m-2" style="margin:auto;">제목 전송!</b-button>
    </div>

    <span style="font-size: 20px; color: rgb(164,219,214);font-family: 'Hanna', sans-serif;margin: 10px;">
            영화정보는 네이버에 검색된 결과가 나옵니다.
          </span>
    <br>
    <div class="container"   style="margin-bottom: 10rem; margin-top: 2.5rem;">
      <transition-group name="fade">
      <div v-for="movieEl in movieList" :key="movieEl">
        <b-container class="bv-example-row text-center" style="margin: -0.5rem;" >
          <b-row >
            <b-col cols="1"  style="margin: auto;">
              <p class="reccontent">{{movieEl[0]}}</p>
            </b-col>
            <b-col cols="6" class="reccontent"  style="margin: auto;">{{movieEl[1]}}</b-col>
            <b-col cols="3" class="reccontent"  style="margin: auto;">{{movieEl[2]}}</b-col>
            <b-col cols="2" class="reccontent"   style="margin: auto;">
              <a v-if="movieEl[0] != '순번'" :href="movieEl[3]" target='_blank'>  <b-button  class="reccontent">이동</b-button></a>
                <p v-if="movieEl[0] == '순번'" class="reccontent">{{movieEl[3]}}</p>
            </b-col>
          </b-row>
        </b-container>
        <hr>
      </div>
       </transition-group>
    </div>
 
<!-- </div> -->
</div>
</template>

<script>
import axios from 'axios'
export default {
  name : 'RecommendTitle',
  data: function(){
      return {
        titleGet : null,
        recoGet : null,
        loding : 0,
        infoChaser : null,
        tempMovie : null,
        number : 1,
        movieList : null,
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
    titleSend  : function() {
      const Keyword = {
        titleGet: this.titleGet,
      }
      if (Keyword.titleGet == null){
        alert('영화제목을 입력해 주세요')
      }else {
      if (Keyword.titleGet) {
        this.loding = 1
        axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/recommend/title/',
        data: Keyword,
        headers: this.setToken()
        }).then(res=>{
          
          if (res.data.state == true) {
            this.recoGet = res.data.Veclist1.title

            const movie_list = [['순번' ,'제목', '유사도','영화링크']]
            var line_score =110/(res.data.Veclist1.score[0]+res.data.Veclist1.score[1])
            var step;
            
            for (step = 0; step < 20; step++) {
              var score = res.data.Veclist1.score[step] * line_score
              Math.ceil(score)
              movie_list.push([this.number,res.data.Veclist1.title[step], `${score.toFixed(2)} %`,`https://movie.naver.com/movie/search/result.naver?query=${res.data.Veclist1.title[step]}&section=all`])
              this.number += 1
            } 
            this.movieList = movie_list
            this.number = 1
          }else{
            alert('검색된 제목이 없습니다! 다른 제목을 넣어주세요~')
          }
          this.loding = 2
        }).catch(err=>{
          console.log(err)
        })
      }
      }
    },
  
  }
}
</script>

<style >
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
.reccontent {
  margin: auto;
  color: #dddddd;
  font-family: 'Hanna', sans-serif;

}
.rectitle {
  margin-bottom: 1rem;
  color: #dddddd;
  font-family: 'Hanna', sans-serif;
}

</style>