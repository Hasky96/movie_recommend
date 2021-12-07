<template>
<div>
    <div class="container-sm" v-if="movies" style="height: 100%;">
      <div class="row" style="height: 30vh;">
        <movies-list-item style="height: 100%;"
        v-for="movie in movies" :key=movie.id
        :movie="movie.fields"
        :movieId="movie.pk"
        >
        </movies-list-item>
      </div>
    </div>
    <section v-else>
      <h3>아직 영화정보가 없습니다.</h3>
    </section>
  </div>

</template>

<script>
import MoviesListItem from '@/components/MoviesListItem.vue'

export default {
  name: "MovieList",
  components:{
    MoviesListItem,
  },
  data : function(){
    return {
    }
  },
  props:{
    movies : Array
  },
  methods:{
  },
}
</script>

<style>
</style>