<template>
  <b-row @click="$router.push({path:`/review/${review.id}`})" class="review">
    <b-col cols="2" class="reviewWord">{{review.user.username}}</b-col>
    <b-col cols="6" class="reviewWord">{{review.title}}</b-col>
    <b-col cols="3" class="reviewWord">{{review.created_at| moment("from", "now")}}</b-col>
    <b-col cols="1" class="reviewWord">{{review.like_users|count}}</b-col>
  </b-row>
</template>

<script>
export default {
  props:{
    review : Object
  },
  filters:{
    count: function(arr){
      return arr.length
    }
  },
}
</script>

<style scoped>
.review{
  padding-bottom : 10px;
  
}
.review:hover{
  border: #eff solid 1px;
  background: #eee;
  cursor: pointer;
  transform: scale(1.01);
}
.reviewWord {
  color: #a7a7a7;
  font-size: 1rem;
}
</style>