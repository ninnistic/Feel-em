# feelem

## Project setup

1. vue project 생성 `vue create feelem`
2. Vue 2 선택
3. 필수 라이브러리 설치 
*  `vue add vuex`
*  `npm i vuex-persistedstate`
*  `vue add router` - history mode [yes] 선택
*  `vue add vuetify`
*  `npm install vue bootstrap-vue bootstrap`
```
// main.js에 추가 
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.use(BootstrapVue)
```

*  `npm install buefy`
   
```
// main.js에 추가
import Vue from 'vue';
import Buefy from 'buefy';
import 'buefy/dist/buefy.css';

Vue.use(Buefy);
```


* `npm add vue-js-modal`

```
// main.js에 추가
import VModal from 'vue-js-modal'
Vue.use(VModal)
```



## 생각해볼 문제
여러 libraries를 사용하는 까닭에 syntax가 겹치는 문제 발생할 수도 있다.