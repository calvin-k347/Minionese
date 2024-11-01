import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import Home from './components/Home.vue'
import Syntax from './components/syntax.vue'
const routes = [
  { path: '/', component: Home },
  { path: '/syntax', component: Syntax}
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})
createApp(App)
.use(router)
.mount('#app')

