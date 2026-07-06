<script setup lang="ts">
import { useMutation } from '@tanstack/vue-query'
import { reactive, ref } from 'vue'
import { postRegister, type LoginCredentials } from '@/common/queries'

const register_form = reactive<LoginCredentials>({
  username: '',
  password: ''
})

const { mutate:register, isPending:registerIsPending, isError:registerIsError, error:registerError } = useMutation({
  mutationFn: postRegister,
  onSuccess: data => { 
    console.log('register success!')
    register_form.username = ''
    register_form.password = ''
    newUser.value = data.username
  },
  onError: error => { 
    console.log('error' + error) 
  }
})

const newUser = ref<string|null>(null);

</script>

<template>
  <main>
  <section>
    <h3>Create New Account</h3>
    <br>
    <form @submit.prevent="register(register_form)">
      <label>Username:
        <input type="text" v-model="register_form.username">
      </label>
      <label>Password:
        <input type="password" v-model="register_form.password">
      </label>
      <br>
      <button type="submit">Register</button>
    </form>
    <p v-if="registerIsPending">Posting Data...</p>
    <p v-if="registerIsError">error: {{registerError?.message}}</p>
    <p v-if="newUser">New User Created!</p>
  </section>
  </main>
</template>

<style scoped>
@import '../assets/form_styles.css';
</style>

