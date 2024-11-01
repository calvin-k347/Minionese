import { createMemoryHistory, createRouter } from 'vue-router'

import Home from './components/Home.vue'
import Syntax from './components/Syntax.vue'
const routes = [
  { path: '/', component: Home },
  { path: '/syntax', component: Syntax}
]
const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

export default router;