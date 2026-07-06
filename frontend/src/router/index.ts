import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import UserProfileView from '@/views/UserProfileView.vue'
import RegisterView from '@/views/RegisterView.vue'
import CompaniesView from '@/views/CompaniesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/companies',
      name: 'companies',
      component: CompaniesView,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
    },
    {
      path: '/user_profile',
      name: 'user_profile',
      component: UserProfileView,
    },
  ],
})

export default router
