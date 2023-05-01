import App from './App.vue'
import { createSSRApp } from 'vue'
import { createPinia } from "pinia";
const pinia = createPinia();

export function createApp() {
  const app = createSSRApp(App)
  app.use(pinia)
  return {
    app
  }
}
