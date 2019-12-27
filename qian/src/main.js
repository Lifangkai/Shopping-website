import 'babel-polyfill'
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import App from './App'
import router from './router'
import store from './store/'
import SlideVerify from 'vue-monoplasty-slide-verify';
import VueCookies from 'vue-cookies'

// 路由跳转之前
router.beforeEach((to, from, next) => {
	// console.log(to)
	// to 表示将要跳转到的组件(目标组件)
	// console.log(from);//(源组件)

	// next 是一个函数
	// next()
	// next() 进入下一个组件的钩子函数
	// next(false)
	// next(false) 阻止跳转  中断导航
	// next("/login") 
	// next("/login") 进入指定的组件的钩子函数
	if (to.meta.auth) {//判断是否需要登录
		if (sessionStorage.getItem("username") !== null) {
			next();
		} else {
			next({
				path: "/login",
				query: {
					redirect: to.fullPath
				}
			});
		}
	} else {
		next();
	}
})

Vue.config.productionTip = false;

Vue.use(SlideVerify);
Vue.use(ElementUI);
Vue.use(VueCookies)

new Vue({
	el: '#app',
	router,
	store,
	template: '<App/>',
	components: { App }
})
