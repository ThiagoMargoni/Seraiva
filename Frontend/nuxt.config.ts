// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  typescript: {
    typeCheck: true
  },
  plugins: ['~/plugins/pinia.ts'],
  modules: [
    'nuxt-primevue',
    '@sidebase/nuxt-auth',
    '@nuxtjs/tailwindcss',
    'nuxt-icon'
  ],
  primevue: {
    components: {
      include: ['Button']
    }
  },
  css: [
    'primeicons/primeicons.css',
    '~/assets/global.scss',
    'vue3-toastify/dist/index.css'
  ],
  auth: {
    baseURL: 'http://localhost:8000',
    provider: {
      type: 'local',
      endpoints: {
        signIn: { path: '/token/login', method: 'post' },
        signOut: { path: '/token/logout', method: 'post' },
        signUp: { path: '/users/', method: 'post' },
        getSession: { path: '/users/me', method: 'get' },
      },
      token: { signInResponseTokenPointer: '/auth_token', type: 'Token' },
      pages: { login: '/user/login' },
      sessionDataType: {
        results: 'Array'
      }
    }
  }
})