<template>
  <div class="container">
    <b-list-group class="">
      <!-- 제목 -->
      <b-row class="tableHeader ">
        <b-col class='myCol' cols="2">작성자</b-col>
        <b-col class='myCol' cols="6">제목</b-col>
        <b-col class='myCol' cols="3">작성일</b-col>
        <b-col class='myCol' cols="1"><i class="fas fa-heart heart"></i></b-col>
      </b-row>
      <b-list-group-item v-if="isSelected" class="group" >
        <review-list-item  v-for="review in selected" :key="review.id"
        :review="review"
        >
      </review-list-item>
      </b-list-group-item >
      <b-list-group-item v-else class="group" >
        <review-list-item v-for="review in reviews" :key="review.id"
        :review="review"
        >
        </review-list-item>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
import axios from 'axios'

export default {
  components:{
    ReviewListItem,
  },
  data:function(){
    return{
      selected : null
    }
  },
  methods:{
    getReviews(){
      axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          return res.data
        }).catch(err=>{
          console.log(err)
        })
    }
  },
  props:{
    reviews: Array,
    movieId: {
      type: [Number,String],
      default:null,
      required:false
    }
  },
  mounted:function(){
    if(this.movieId=='null' || !this.movieId){
        this.selected=null
      }else{
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          this.selected = res.data
        })
      }
  },
  computed:{
    isSelected:function(){
      if(this.movieId=='null' || !this.movieId){
        return false
      }else{
        return true
      }
    }
  },
  watch:{
    movieId:function(){
      if(this.movieId=='null' || !this.movieId){
        this.selected=null
      }else{
        axios({
          method: 'get',
          url: `http://127.0.0.1:8000/server/community/movie/${this.movieId}/reviews/`
        }).then(res=>{
          this.selected = res.data
        })
      }
    }
  }
}

</script>

<style scoped>
.container{
  color: #808080;
}
.tableHeader{
  font-size: 20px;
  font-weight: 800;
  color: #808080;
  padding-bottom: 10px;
  border-bottom: #808080 solid 1px;
}
.myCol{
  text-align: center;
  font-size: 1.5rem;
} 
.heart{
  color: red
}
.group{
  background-color: #1b1b1b;
  padding-left: 0px;
  padding-right: 0px;
  padding-bottom: -10px;
}
.reviewTitle {
  font-size: 2rem;
}
</style>