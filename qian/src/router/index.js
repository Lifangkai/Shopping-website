import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

// 登陆注册模块
const login = r => require.ensure([], () => r(require('@/page/login')), 'login');
// 管理员模块
const manage = r => require.ensure([], () => r(require('@/page/manage/manage')), 'manage');
const userList = r => require.ensure([], () => r(require('@/page/manage/userList')), 'userList');
const storeList = r => require.ensure([], () => r(require('@/page/manage/storeList')), 'storeList');
const adminList = r => require.ensure([], () => r(require('@/page/manage/adminList')), 'adminList');
const visitor = r => require.ensure([], () => r(require('@/page/manage/visitor')), 'visitor');
const vueEdit = r => require.ensure([], () => r(require('@/page/manage/vueEdit')), 'vueEdit');
const adminSet = r => require.ensure([], () => r(require('@/page/manage/adminSet')), 'adminSet');
const explain = r => require.ensure([], () => r(require('@/page/manage/explain')), 'explain');
// 商家模块
const store = r => require.ensure([], () => r(require('@/page/store/store')), 'store');
const shopList = r => require.ensure([], () => r(require('@/page/store/shopList')), 'shopList');
const addShop = r => require.ensure([], () => r(require('@/page/store/addShop')), 'addShop');
const foodList = r => require.ensure([], () => r(require('@/page/store/foodList')), 'foodList');
const addGoods = r => require.ensure([], () => r(require('@/page/store/addGoods')), 'addGoods');
const orderList = r => require.ensure([], () => r(require('@/page/store/orderList')), 'orderList');
const storeInfo = r => require.ensure([], () => r(require('@/page/store/storeInfo')), 'storeInfo');
// 用户模块
const user = r => require.ensure([], () => r(require('@/page/user/user')), 'user');
const userHome = r => require.ensure([], () => r(require('@/page/user/userHome')), 'userHome');
const goodAll = r => require.ensure([], () => r(require('@/page/user/goodAll')), 'goodAll');
const goodClass = r => require.ensure([], () => r(require('@/page/user/goodClass')), 'goodClass');
const goodList = r => require.ensure([], () => r(require('@/page/user/goodList')), 'goodList');
const foodInfo = r => require.ensure([], () => r(require('@/page/user/foodInfo')), 'foodInfo');
const shopCart = r => require.ensure([], () => r(require('@/page/user/shopCart')), 'shopCart');
const userOrder = r => require.ensure([], () => r(require('@/page/user/userOrder')), 'userOrder');
const userInfo = r => require.ensure([], () => r(require('@/page/user/userInfo')), 'userInfo');
const applyText = r => require.ensure([], () => r(require('@/page/user/applyText')), 'applyText');
// 404
const notPage = r => require.ensure([], () => r(require('@/page/404')), 'notPage');


const routes = [
	{
		path: '/login',
		component: login
	},
	{
		path: '/',
		redirect: '/userHome'
	},
	{
		path: '/',
		component: manage,
		name: '',
		children: [
			{
				path: '/visitor',
				component: visitor,
				meta: {
					title:'用户分布',
					auth:true
				},
			},
			{
				path: '/userList',
				component: userList,
				meta: {
					title: '用户列表',
					auth: true
				}
			},
			{
				path: '/storeList',
				component: storeList,
				meta: {
					title: '商家列表',
					auth: true
				}
			},
			{
				path: '/adminList',
				component: adminList,
				meta: {
					title: '管理员列表',
					auth: true
				}
			},
			{
				path: '/vueEdit',
				component: vueEdit,
				meta: {
					title: '文本编辑',
					auth: true
				}
			},
			{
				path: '/adminSet',
				component: adminSet,
				meta: {
					title: '管理员设置',
					auth: true
				}
			},
			{
				path: '/explain',
				component: explain,
				meta: {
					title: '说明',
					auth: true
				}
			}
		]
	},
	{
		path: '/',
		component: store,
		name: '',
		children: [
			{
				path: '/shopList',
				component: shopList,
				meta: {
					title: '店铺详情',
					auth: true
				}
			},
			{
				path: '/addShop',
				component: addShop,
				meta: {
					title: '添加商铺',
					auth: true
				}
			},
			{
				path: '/foodList',
				component: foodList,
				meta: {
					title: '食品列表',
					auth: true
				}
			},
			{
				path: '/addGoods',
				component: addGoods,
				meta: {
					title: '添加商品',
					auth: true
				}
			},
			{
				path: '/orderList',
				component: orderList,
				meta: {
					title: '订单列表',
					auth: true
				}
			},
			{
				path: '/storeInfo',
				component: storeInfo,
				meta: {
					title: '个人信息',
					auth: true
				}
			}
		]
	},
	{
		path: '/',
		component: user,
		name: '',
		children: [
			{
				path: '/userHome',
				component: userHome,
				meta: {
					title: '用户首页',
					auth: false
				}
			},
			{
				path: '/goodList',
				component: goodList,
				meta: {
					title: '商品列表',
					auth: false
				}
			},
			{
				path: '/goodAll',
				component: goodAll,
				meta: {
					title: '所有商品',
					auth: false
				}
			},
			{
				path: '/goodClass',
				component: goodClass,
				meta: {
					title: '商品分类',
					auth: false
				}
			},
			{
				path: '/foodInfo',
				name:"商品详情",
				component: foodInfo,
				meta: {
					title: '商品详情',
					auth: false
				}
			},
			{
				path: '/shopCart',
				component: shopCart,
				meta: {
					title: '购物车详情',
					auth: true
				}
			},
			{
				path: '/applyText',
				component: applyText,
				meta: {
					title: '支付详情',
					auth: true
				}
			},
			{
				path: '/userOrder',
				component: userOrder,
				meta: {
					title: '用户订单',
					auth: true
				}
			},
			{
				path: '/userInfo',
				component: userInfo,
				meta: {
					title: '用户信息',
					auth: true
				}
			}
		]
	},
	{
		path: '*',
		component: notPage
	}
]

export default new Router({
	routes,
	mode: 'history',
	strict: process.env.NODE_ENV !== 'production',
})
