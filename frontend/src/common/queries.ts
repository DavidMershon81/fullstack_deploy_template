import axios from 'axios'
import { useAuthStore } from './auth'
import router from '@/router'

export interface Company {
  id: number
  name: string
}

export interface TokenInfo {
  access_token: string
  token_type: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface User {
  username: string
}

const apiURL:string = import.meta.env.DEV ? import.meta.env.VITE_API_URL_DEV : import.meta.env.VITE_API_URL_PROD
const api = axios.create({ baseURL: apiURL })


//this allows the JWT auth token to be automatically passed to routes that require it
api.interceptors.request.use(config => {
  const authStore = useAuthStore()
  if(authStore.isAuthenticated) {
    config.headers.Authorization = `Bearer ${authStore.token}`
  }
  return config
})

//logout and forward the user to the login page if their token is rejected by the server
api.interceptors.response.use(
  response => response,
  error => {
    const authStore = useAuthStore()
    if(error.response?.status === 401) {
      authStore.logout()
      router.push('/login')
    }
    return Promise.reject(error)
  }
)

export const getCompanies = async (): Promise<Company[]> => {
  const response = await api.get('/companies')
  return response.data
}

export const postCompany = async (company_name: string): Promise<Company> => {
  const response = await api.post('/companies', { name: company_name })
  return response.data
}

export const postLogin = async (credentials : LoginCredentials): Promise<TokenInfo> => {
  const form = new URLSearchParams()
  form.append('username', credentials.username)
  form.append('password', credentials.password)
  const response = await api.post('/login', form)
  return response.data
}

export const postRegister = async (credentials : LoginCredentials): Promise<User> => {
  const form = new URLSearchParams()
  form.append('username', credentials.username)
  form.append('password', credentials.password)
  const response = await api.post('/register', form)
  return response.data
}

export const getUser = async (): Promise<User> => {
  const response = await api.get('/users/me')
  return response.data
}