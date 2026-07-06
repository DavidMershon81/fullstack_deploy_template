import { defineStore } from "pinia"
import { ref, computed } from 'vue'

export const useAuthStore = defineStore('auth', () => {
    const token_param = 'access_token'
    const token = ref<string | null>(localStorage.getItem(token_param))
    const isAuthenticated = computed(() => token.value != null)

    const init = () => {
        token.value = localStorage.getItem(token_param)
    }

    const saveToken = (newToken:string) => {
        token.value = newToken
        localStorage.setItem(token_param, newToken)
    }

    const logout = () =>  {
        token.value = null
        localStorage.removeItem(token_param)
    }

    return { init, isAuthenticated, saveToken, logout, token }
})