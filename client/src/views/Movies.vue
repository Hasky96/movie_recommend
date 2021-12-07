<template>
  <div class="main-div">
    <section class="searchTab">
      <input class="search-input" @keyup.enter="search" v-model="keyword" type="text"><button @click="search" class="btn-search">검색</button>
    </section>
    <div class="movie-table">
      <movies-list
      :movies ="movies">
      </movies-list>
    </div>
    <div v-if="!keyword" class="pagination-div">
      <i v-if="pageStatus!='first'" @click="prePagination" class="fas fa-angle-left angle"></i>
      <span v-for="page in pages" :class="{'pagi-active':page==curPage}" :key="page" @click="getPages(page)" class="pagi" >{{page}}</span>
      <i v-if="pageStatus!='last'" @click="nextPagination" class="fas fa-angle-right angle"></i>
    </div>
  </div>
</template>

<script>
import MoviesList from '@/components/MoviesList.vue'
import axios from 'axios'
import _ from 'lodash'

export default {
  name: 'Movies',
  components: {
    MoviesList,
  },
  data : function(){
    return {
      keyword: "",
      movies:null,
      totalPage:null,
      curPage: 1,
      pages : [1, 2, 3, 4, 5],
      pageStatus: "first"
    }
  },
  methods:{
    reviewPage(movieId){
      this.$router.push({name: 'Review', params: {movieId: movieId}})
    },
    nextPagination(){
      let start = _.last(this.pages)+1
      let last = start+5
      if (_.range(start,last).includes(this.totalPage)){
        this.pages = _.range(start,this.totalPage+1)
        this.pageStatus="last"
      }else{
        this.pages = _.range(start,last)
        this.pageStatus="middle"
      }
      this.getPages(_.head(this.pages))
    },
    prePagination(){
      let last = _.head(this.pages)
      let start = last-5
      if(start<6){
        this.pages = [1,2,3,4,5]
        this.pageStatus="first"
      }else{
        this.pages= _.range(start,last)
        this.pageStatus="middle"
      }
      this.getPages(_.last(this.pages))
    },
    getPages(c){
      this.curPage = c
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/list/${c}/`
      }).then(res=>{
        this.movies = res.data
      }).catch(err=>{
        console.log(err)
      })
    },
    search(){
      axios({
          method : 'get',
          url: 'http://127.0.0.1:8000/server/movies/search/1/',
          params:{
            keyword : String(this.keyword)
          }
        }).then(res=>{
          console.log(res)
          this.movies = _.slice(res.data,0,8)
        }).catch(err=>{
          console.log(err)
      })
    }
  },
  computed:{
  },
  created:function(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/server/movies/list/totalpages/'
    }).then(res=>{
      this.totalPage=res.data.pages
      // console.log(res)
    })
    axios({
        method: 'get',
        url: `http://127.0.0.1:8000/server/movies/list/1/`
      }).then(res=>{
        // console.log(res)
        this.movies = res.data
      })
  }
}
</script>

<style scoped>
.main-div{
  margin-left: 10vw;
  margin-right:10vw;
}
.searchTab{
  width: 100%;
  text-align: center;
  padding: 5px;
  height: 7%;
}
.pagi{
  text-align: center;
  color: #eee;
  font-size: 30px;
  margin: 5px;
  padding-left: 5px;
  padding-right: 5px;
}
.pagi-active{
  border: #eee solid 1px;
  border-radius: 5px ;
}
.angle{
  font-size: 30px
}
.movie-table{
  text-align:center;
  height: 86%;
}
.search-input{
  border: #808080 1px solid;
  border-radius: 5px;
  margin: 5px;
  width: 40%;
}
.btn-search{
  background-color: #808080;
  border: #808080 1px solid;
  border-radius: 5px;
  color: #eee;
}
.pagination-div{
  height: 7%;
}
</style>
