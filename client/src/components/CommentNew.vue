<template>
  <div class="row comment">
    <input v-model="content" class="inp col-11" type="text" @keyup.enter="write">
    <button @click="write" class="btn col-1 p-0">작성</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data:function(){
    return{
      content:null
    }
  },
  props:{
    reviewId: Number
  },
  methods:{
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    write(){
      axios({
        method: 'POST',
        url:`http://127.0.0.1:8000/server/community/review/${this.reviewId}/comment/`,
        data: {content: this.content},
        headers: this.setToken()
      }).then(()=>{
        this.content = null
        this.$emit('refresh')
      }).catch(err=>{
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
.comment{
  height: 4em;
}
.inp{
  border: 1px black solid;
  border-radius: 0%;  
}
.btn{
  text-align: center;
  border: 1px black solid;
  background: #aaa;
  border-radius: 0%;
  font-size: 1em;
  font-weight: 700;
}
</style>