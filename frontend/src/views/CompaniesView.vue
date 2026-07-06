<script setup lang="ts">
import { useQuery, useMutation } from '@tanstack/vue-query'
import { reactive } from 'vue'
import { getCompanies, postCompany  } from '@/common/queries'

//this is used for the form state, it's synced using the v-model commands in the template
const form = reactive({
  name: ''
})

//useQuery for syncing the get request to the companies
const { isPending:getIsPending, isError:getIsError, data:companies, error:getError, refetch } = useQuery({
  queryKey: ['companies'],
  queryFn: getCompanies
})

//useMutation for posting the data of a new company (also can be used for update, delete and other stage change requests)
const { mutate, isPending:postIsPending, isError:postIsError, error:postError } = useMutation({
  mutationFn: postCompany,
  onSuccess: data => { 
    console.log('company created! data:' + data)
    //clear the form
    form.name = ''
    //refresh data
    refetch()
  },
  onError: error => { console.log('post company error! - error:' + error) }
})

</script>

<template>
  <main>
    <section>
      <h2>Add Company</h2>
      <form @submit.prevent="mutate(form.name)">
        <label>Name:
          <input type="text" v-model="form.name">
        </label>
        <button type="submit">Submit</button>
      </form>
      <p v-if="postIsPending">Sending...</p>
      <p v-if="postIsError">error: {{postError}}</p>
    </section>
    <section>
      <h2>Companies</h2>
      <p v-if="getIsPending">Loading...</p>
      <p v-if="getIsError">error: {{getError}}</p>
      <ul v-else="">
        <li v-for="company in companies" :key="company.id">{{ company.name }}</li>
      </ul>
    </section>
  </main>
</template>

<style scoped>
@import '../assets/form_styles.css';
@import '../assets/box_list_styles.css';
    
</style>
