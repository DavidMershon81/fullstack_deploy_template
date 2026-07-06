<script setup lang="ts">
import { useQuery } from '@tanstack/vue-query'
import { getUser } from '@/common/queries'

const { isPending:getIsPending, isError:getIsError, data:user, error:getError, refetch } = useQuery({
  queryKey: ['user'],
  queryFn: getUser
})

</script>

<template>
  <main>
    <section>
    <h2>User Profile</h2>
      <section v-if="user">
        <p>username: {{ user.username }}</p>
        <p>Not much of a personality yet, but we can improve that later</p>
      </section>
      <section v-if="!user">
        <p v-if="getIsPending">Loading...</p>
        <p v-if="getIsError">error: {{ getError }}</p>
      </section>
    </section>
  </main>
</template>

<style scoped>
@import '../assets/form_styles.css';
</style>

