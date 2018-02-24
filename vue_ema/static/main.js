import Vue from 'vue'

import axios from 'axios'
import router from './router'
import {store} from './store'
import Meta from 'vue-meta'





import Main from './Main.vue'

// Axios csrf settings
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'








Vue.use(Meta)


/* eslint-disable no-new */
new Vue({
  el: '#main',
  router,
  store,
  render: h => h(Main)
})
