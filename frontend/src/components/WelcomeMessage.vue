import { LoginCredentials } from '../common/queries';
<script setup lang="ts">
defineProps<{
  msg: string
}>()
</script>

<template>
  <div class="greetings">
    <h1 class="highlight_color">{{ msg }}</h1>
      <h3>This starter project comes complete with these useful features to get us started</h3>
      <ul>
        <li><span>Company</span> and <span>User</span> test models</li>
        <li>Test <span>GET</span> and <span>POST</span> routes</li>
        <li><span>JWT</span> token based auth system with <span>login</span> and <span>registration</span> pages</li>
        <li><span>Protected</span> route to pull info on the current user</li>
        <li>Frontend forwards <span>unauthenticated / expired users</span> back to the login page</li>
      </ul>
  </div>
</template>

<style scoped>
@import '../assets/box_list_styles.css';

h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
  text-align: left;
}

span {
  color: var(--vt-c-highlight-color-main);
}


</style>
