<template>
  <div id="app">
    <!-- Image and text -->
      <b-navbar class="mx-4 row" variant="#1b1b1b" type="#1b1b1b">
      <div class="col-3">
        <router-link to="/">
        <img src="../imgs/film-reel.png" class="d-inline-block" alt="Kitten" width="30px" style="filter: invert(100%);"/>
        <span class="btn fs-3 nav-font-color">MovieFriend</span>
        </router-link>
      </div>
      <div class="text-decoration-none col-7 menu">
        <router-link 
        class="btn  fs-5 nav-font-color" 
        to="/movies">Movies</router-link>
        <router-link 
        class="btn fs-5 nav-font-color" 
        to="/reviews">Reviews</router-link>
        <!-- 추천 시스템 라우터 -->
        <router-link class="btn fs-5 nav-font-color" to="/Recommend">Recommend</router-link>
      </div>
      <div class="col-2">
        <!-- 로그인 라우터 -->
        <span v-if="isLogin">
          <router-link class="btn fs-5 nav-font-color" @click.native="logout" to="#"><i class="far fa-user-circle profile"/>{{user}} Logout</router-link>
        </span>
        <span v-else>
          <button @click="$bvModal.show('modal-login')" class="btn fs-5 nav-font-color">Login</button>
          <b-modal centered id=modal-login class="moda" hide-footer hide-header>
            <div class="moda" id="login-modal">
              <p class="pTag">Login</p>
              <label :class="{'hovered':idHover}" class="label-id" for="username">I D : </label>
              <input v-model="credential.username" name="username" type="text"
              @mouseover="idHover=!idHover" @mouseleave="idHover=!idHover"
              >
              <br>
              <label :class="{'hovered':pwHover}" class="label-pw" for="password">PW : </label>
              <input v-model="credential.password" @keyup.enter="login" name="password" type="password"
              @mouseover="pwHover=!pwHover" @mouseleave="pwHover=!pwHover" 
              >
              <br>
            </div>
            <div class="btn-group">
              <button @click="login" class="btn-login">Login</button>
              <p @click='changeModal' class="p-signup">회원가입</p>
            </div>
          </b-modal>
          <b-modal centered id=modal-signup class="moda" hide-footer hide-header>
            <div class="moda" id="login-modal">
              <p class="pTag">Signup</p>
              <label :class="{'hovered':idHover}" class="label-id" for="username2">I D : </label>
              <input v-model="credential.username" name="username" type="text"
              @mouseover="idHover=!idHover" @mouseleave="idHover=!idHover"
              >
              <br>
              <label :class="{'hovered':pwHover}" class="label-pw" for="password2">PW : </label>
              <input v-model="credential.password" @keyup.enter="login" name="password2" type="password"
              @mouseover="pwHover=!pwHover" @mouseleave="pwHover=!pwHover" 
              >
              <br>
              <label :class="{'hovered':pwckHover}" class="label-pwck" for="passwordck">PWCHECK : </label>
              <input 
              id="pwck" 
              v-model="credential.passwordConfirmation" 
              name="passwordck" type="password" @mouseover="pwckHover=!pwckHover" @mouseleave="pwckHover=!pwckHover" 
              @keyup.enter="signup"
              >
              <br>
            </div>
            <div class="btn-group">
              <button @click="signup" class="btn-login">회원가입</button>
            </div>
        </b-modal>
        </span>
      </div>
      </b-navbar>
      <div><router-view @login="isLogin=true"/></div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'App',
  components:{
  },
  data : function() {
    return{
      idHover: false,
      pwHover: false,
      pwckHover: false,
      isLogin: false,
      credential:{
        username:null,
        password:null,
        passwordConfirmation:null,
      },
      user: null
    }
  },
  methods:{
    changeModal(){
      this.$bvModal.hide('modal-login')
      this.$bvModal.show('modal-signup')
    },
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
    },
    login(){
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/server/accounts/api-token-auth/',
        data: this.credential
      }).then(res=>{
        console.log(res)
        const jwt = res.data.token
        localStorage.setItem('jwt', jwt)
        localStorage.setItem('user', this.credential.username)
        this.user = this.credential.username
        this.isLogin = true
        this.$bvModal.hide('modal-login')
        alert("로그인 성공!")
      }).catch(err=>{
        console.log(err)
        alert('아이디 또는 비밀번호가 틀렸습니다.')
      })
    },
    signup(){
      axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/server/accounts/signup/',
          data: this.credential
      }).then((res)=>{
          alert(`${res.data.username} 가입성공!`)
          this.$bvModal.hide('modal-signup')
          this.$bvModal.show('modal-login')
      }).catch(err=>{
          alert('잘못된 가입정보 입니다.')
          console.log(err)
      })
    },
  },
  beforeCreate: function(){
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/server/movies/list/',
    }).then(res=>{
      // console.log(res)
      this.$store.dispatch("setMovies", res.data)
    }).catch(err=>{
      console.log(err)
    })
    axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/server/community/reviews/',
      }).then(res=>{
        this.$store.dispatch("setReviews", res.data)
      }).catch(err=>{
        console.log(err)
      })
  },
  created:function(){
    if (localStorage.getItem('jwt')) {
      this.user = localStorage.getItem('user')
      this.isLogin = true
    }
    else{
      this.isLogin = false
    }
  }
}
</script>
<style scoped>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #808080;
}
.menu{
  text-align: left;
}
.nav-font-color{
  color: #eee;
}
.moda{
  max-width: 100%;
  text-align: left;
  padding: 80px;
  padding-top: 40px;
  padding-bottom:10px;
  font-size: 20px;
}
.login-input{
  text-align: left;
}
#login-modal > input{
  margin: 10px;
  color: #808080;
  background-color: #1b1b1b;
  border: 1px #808080 solid;
  border-radius: 5px;
}
#login-modal > input:hover{
  max-width: 90%;
  margin: 10px;
  color: #808080;
  background-color: #1b1b1b;
  border: 1px #eee solid;
  border-radius: 5px;
}
.label-id:focus{
  max-width: 90%;
  margin: 10px;
  color: #808080;
  background-color: #1b1b1b;
  border: 1px #eee solid;
  border-radius: 5px;
}
.label-pw:focus{
  max-width: 90%;
  margin: 10px;
  color: #808080;
  background-color: #1b1b1b;
  border: 1px #eee solid;
  border-radius: 5px;
}
.label-id{
  letter-spacing: 1px;
  font-size: 25px;
}
.hovered{
  font-weight: 700;
  color: #eee;
  background-color: #1b1b1b;
}
.label-pw{
  font-size: 25px;
}
#pwck{
  height:35px;
  font-size: 25px;
}
#pwck{
  border: none;
}
.btn-group{
  display: flex;
  flex-direction: column;
  text-align: center;
  padding: 10px;
  max-width: 100%;
  max-height: 100%;
}
.btn-group > button{
  font-size: 20px;
  color: #808080;
  height: 40px;
  margin: 10px;
  border: 1px #1b1b1b solid;
  border-radius: 5px;
}
.btn-login{
  display: block;
  background-color: lightblue; 
}
.btn-login:hover{
  background-color: lightblue; 
  transform: scale(1);
  color : #eee;
}
.pTag{
  font-size: 50px;
  font-weight: 800;
}
.p-signup{
  font-size: 15px;
}
.p-signup:hover{
  color: #eee;
  cursor: pointer;
  transform: scale(1);
}
</style>
<style>
.modal-body{
  text-align: center;
  background-color: #1b1b1b !important;
}
#modal-login___BV_modal_content_, #modal-signup___BV_modal_content_{
  background-color: #1b1b1b !important;
}
.profile{
  margin-right: 10px;
}
</style>
