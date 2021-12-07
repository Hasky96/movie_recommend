<template>
    <div class="col-sm-3 p-2 movieContainer" >
      <div class="poster-movie" @click="$router.push({path:`/movie/${movieId}/`})">
        <div class="imgDiv">
          <img class="imgTag" :class="{'imgTag-hover':ishover}" :src="movie.poster_path" alt="">
        </div>
        <div class="movieContent" @mouseover="ishover=true" @mouseleave="ishover=false">
          <h4 class="fw-bold">{{movie.title}}</h4>
          <p>{{movie.release_date}}</p>
          <p>{{genres_String}}</p>
          <p class="vote"><i class="fas fa-star starTag"/> {{movie.vote_average}}</p>
        </div>
      </div>
    </div >
</template>

<script>
import axios from 'axios'

export default {
  name : 'MovieListItem',
  props:{
    movie: Object,
    movieId:Number
  },
  data(){
    return{
      genres: [],
      ishover: false,
    }
  },
  methods:{
  },
  mounted(){
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/server/movies/${this.movieId}/genres/`,
    }).then(res=>{
      this.genres = res.data
    })
  },
  computed:{
    genres_String(){
      let str = ""
      this.genres.forEach(p => str+=p.name+" ")
      return str
    },
  },
  watch:{
    movieId:function(){
      axios({
       method: 'get',
       url: `http://127.0.0.1:8000/server/movies/${this.movieId}/genres/`,
     }).then(res=>{
       // console.log(res)
       this.genres = res.data
     })
    }
  }

}
</script>

<style scoped>
.movieContent{
  position: absolute;
  top: 0;
  text-align: left;
  color: white;
  opacity: 0%;
  width: 100%;
  height: 100%;
  z-index: 2;
  padding: 30px;
}
.movieContent:hover{
  transition-duration: 1s;
  opacity: 100%;
}
.movieContainer{
  height: 100%;
}
.poster-movie{
  position: relative;
  background-color: black;
  align-items: center;
  height: 100%;
  padding: 0px;
  margin: 0px;
}
.imgDiv{
  display: flex;
  overflow: hidden;
  height: 100%;
}
.imgTag-hover{
  opacity: 20%;
  transition-duration: 0.5s;
}
.imgTag{
  overflow: hidden;
  width: 100%;
  height: auto;
}
.starTag{
  color: gold;
  font-size: 30px;
}
.vote{
  font-size: 30px;
}

</style>