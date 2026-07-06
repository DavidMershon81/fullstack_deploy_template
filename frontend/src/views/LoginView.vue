<script setup lang="ts">
import { useMutation } from '@tanstack/vue-query'
import { reactive, ref } from 'vue'
import { postLogin, type LoginCredentials } from '@/common/queries'
import { useAuthStore } from '@/common/auth'
import router from '@/router'

const authStore = useAuthStore()

const login_form = reactive<LoginCredentials>({
  username: '',
  password: ''
})

const { mutate:login, isPending:loginIsPending, isError:loginIsError, error:loginError } = useMutation({
  mutationFn: postLogin,
  onSuccess: data => { 
    console.log('login success!')
    login_form.username = ''
    login_form.password = ''
    authStore.saveToken(data.access_token)
    router.push('user_profile')
  },
  onError: error => { console.log('post company error! - error:' + error) }
})

</script>

<template>
  <main>
  <section>
    <form @submit.prevent="login(login_form)">
      <label>Username:
        <input type="text" v-model="login_form.username">
      </label>
      <label>Password:
        <input type="password" v-model="login_form.password">
      </label>
      <button type="submit">Login</button>
    </form>
    <br>
    <p v-if="loginIsPending">Posting Data...</p>
    <p v-if="loginIsError">error: {{loginError}}</p>
    <br>
    <p>No account yet? <RouterLink to="/register">Register</RouterLink></p>
  </section>
  <section>
    <label>Nobody wants to be logged in forever...</label>    
    <button @click.prevent="authStore.logout()">Logout</button>    
  </section>
  </main>
</template>

<style scoped>
@import '../assets/form_styles.css';
</style>

