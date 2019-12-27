import Vue from 'vue'
import Vuex from 'vuex'
// import {getAdminInfo} from '@/api/getData'

Vue.use(Vuex)

const state = {
	username: sessionStorage.getItem("username"),
	storeinfo: sessionStorage.getItem("storeinfo"),
	userroot: sessionStorage.getItem("userroot"),
	admininfo: sessionStorage.getItem("admininfo"),
	userinfo: sessionStorage.getItem("userinfo"),
	explain: `普通用户只能编辑修改
			管理员可以编辑修改删除`,
	isShowShop: sessionStorage.getItem("isShowShop"),
}

const mutations = {
	setUserName(state, message) {
		state.username = message
	},
	setStoreInfo(state, message) {
		// sessionStorage.setItem("userinfo",JSON.stringify(message))
		// state.userinfo = JSON.parse(sessionStorage.getItem("userinfo"))
		state.storeinfo = message
	},
	setAdminInfo(state, message) {
		state.admininfo = message
	},
	setUserInfo(state,message) {
		state.userinfo = message
	},
	setUserRoot(state, message) {
		state.userroot = message
	},
	setExplain(state, message) {
		state.explain = message
	},
	setIsShow(state,message) {
		state.isShowShop = message
	}
}

const actions = {
	// async getAdminData({commit}){
	// 	try{
	// 		const res = await getAdminInfo()
	// 		if (res.status == 1) {
	// 			commit('saveAdminInfo', res.data);
	// 		}else{
	// 			throw new Error(res.type)
	// 		}
	// 	}catch(err){
	// 		// console.log(err.message)
	// 	}
	// }
	setUserRootAsync(context, message) {
		context.commit('increment', message)
	}
}

export default new Vuex.Store({
	state,
	actions,
	mutations,
})
