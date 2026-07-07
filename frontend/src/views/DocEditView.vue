<script setup lang="ts">
import * as Y from 'yjs'
import { WebsocketProvider } from 'y-websocket'
import { ref, watch, computed } from 'vue'

const ydoc = new Y.Doc()
const text_area_contents = ref('')
const roomname = 'test_room'
const ytext = ydoc.getText('text')

const provider = ref<WebsocketProvider|null>(null)


if(provider.value === null) {
  let apiURL:string = (import.meta.env.DEV ? import.meta.env.VITE_API_URL_DEV : import.meta.env.VITE_API_URL_PROD).replace('http://', '').replace('https://', '')
  provider.value = new WebsocketProvider(
    //'wss://demos.yjs.dev/ws', // use the public ws server
    `ws://${apiURL}/doc/ws`,
    roomname,
    ydoc
  )
}

let syncing_from_ydoc = false

// ydoc -> ref
ytext.observe(() => {
  syncing_from_ydoc = true
  text_area_contents.value = ytext.toString()
  syncing_from_ydoc = false
})

// ref -> ydoc
watch(text_area_contents, (new_value) => {
  if (syncing_from_ydoc) return
  ydoc.transact(() => {
    ytext.delete(0, ytext.length)
    ytext.insert(0, new_value)
  })
})

</script>

<template>
  <main>
    <section>
      <h2>Edit Document</h2>
      <textarea v-model="text_area_contents">

      </textarea>
      <p>{{ text_area_contents }}</p>
    </section>
  </main>
</template>

<style scoped>
@import '../assets/form_styles.css';
</style>

