import axios from 'axios';
// import { getCookie } from "../page/comm_func.js";

// 让axios携带cookie
axios.defaults.withCredentials = true;

export const base = 'http://127.0.0.1:8000';

const Axios = axios.create({
    baseURL: base,
    headers: {
        // 'X-CSRFToken': this.$cookies.get("csrftoken")
    }
})

// 请求管理员图片地址
export const adminImageUrl = `${base}/adminlist/media/admin/`
// 请求商家图片地址
export const bussinessImageUrl = `${base}/businesslist/media/bussiness/`
// 请求食品图片地址
export const foodImageUrl = `${base}/foodlist/media/food/`

// 用户登陆
export const userLogin = params => { return Axios.post(`${base}/api/userlogin/`, params).then(res => res.data) };
// 商家登陆
export const storeLogin = params => { return Axios.post(`${base}/api/storelogin/`, params).then(res => res.data) };
// 管理员登陆
export const adminLogin = params => { return Axios.post(`${base}/api/adminlogin/`, params).then(res => res.data) };
// 用户注册
export const userRegister = params => { return Axios.post(`${base}/api/userregister/`, params).then(res => res.data) };
// 商家注册
export const storeRegister = params => { return Axios.post(`${base}/api/storeregister/`, params).then(res => res.data) };
// 退出登录
export const loginOut = params => { return Axios.get(`${base}/api/loginout/`, {params:params}).then(res => res.data) };
// 所有用户数据
export const userListAll = params => { return Axios.get(`${base}/userlist/query/`, { params: params }).then(res => res.data) };
// 单个用户数据
export const userListOne = params => { return Axios.get(`${base}/userlist/queryone/`, { params: params }).then(res => res.data) };
// 修改用户数据
export const userListEdit = params => { return Axios.post(`${base}/userlist/edit/`, params).then(res => res.data) };
// 删除用户数据
export const userListDel = params => { return Axios.post(`${base}/userlist/delete/`, params).then(res => res.data) };
// 用户分布数量统计
export const userListAddress = params => { return Axios.post(`${base}/userlist/queryaddress/`, params).then(res => res.data) };
// 查询用户预警
export const userListWarnQuery = params => { return Axios.get(`${base}/userlist/querywarn/`, { params: params }).then(res => res.data) };
// 添加用户预警
export const userListWarnAdd = params => { return Axios.post(`${base}/userlist/addwarn/`, params).then(res => res.data) };
// 删除用户预警
export const userListWarnDel = params => { return Axios.post(`${base}/userlist/deletewarn/`, params).then(res => res.data) };
// 所有商家数据
export const storeListAll = params => { return Axios.get(`${base}/storelist/query/`, { params: params }).then(res => res.data) };
// 单个商家数据
export const storeListOne = params => { return Axios.get(`${base}/storelist/queryone/`, { params: params }).then(res => res.data) };
// 修改商家数据
export const storeListEdit = params => { return Axios.post(`${base}/storelist/edit/`, params).then(res => res.data) };
// 删除商家信息
export const storeListDel = params => { return Axios.post(`${base}/storelist/delete/`, params).then(res => res.data) };
// 商家分布数量统计
export const storeListAddress = params => { return Axios.post(`${base}/storelist/queryaddress/`, params).then(res => res.data) };
// 查询商家预警
export const storeListWarnQuery = params => { return Axios.get(`${base}/storelist/querywarn/`, { params: params }).then(res => res.data) };
// 添加商家预警
export const storeListWarnAdd = params => { return Axios.post(`${base}/storelist/addwarn/`, params).then(res => res.data) };
// 删除商家预警
export const storeListWarnDel = params => { return Axios.post(`${base}/storelist/deletewarn/`, params).then(res => res.data) };
// 所有店铺数据
export const bussinessListAll = params => { return Axios.get(`${base}/businesslist/query/`, { params: params }).then(res => res.data) };
// 单个店铺数据
export const bussinessListOne = params => { return Axios.post(`${base}/businesslist/queryone/`, params).then(res => res.data) };
// 修改店铺数据
export const bussinessEdit = params => { return Axios.post(`${base}/businesslist/edit/`, params).then(res => res.data) };
// 删除店铺数据
export const bussinessDel = params => { return Axios.post(`${base}/businesslist/delete/`, params).then(res => res.data) };
// 添加店铺数据
export const bussinessAdd = params => { return Axios.post(`${base}/businesslist/create/`, params).then(res => res.data) };
// 所有商品数据
export const foodListAll = params => { return Axios.get(`${base}/foodlist/query/`, { params: params }).then(res => res.data) };
// 搜索商品数据
export const foodListQuery = params => { return Axios.get(`${base}/foodlist/querylist/`, { params: params }).then(res => res.data) };
// 修改商品数据
export const foodListEdit = params => { return Axios.post(`${base}/foodlist/edit/`, params).then(res => res.data) };
// 添加商品数据
export const foodListAdd = params => { return Axios.post(`${base}/foodlist/create/`, params).then(res => res.data) };
// 删除商品数据
export const foodListDel = params => { return Axios.post(`${base}/foodlist/delete/`, params).then(res => res.data) };
// 所有订单数据
export const orderListAll = params => { return Axios.get(`${base}/orderlist/query/`, { params: params }).then(res => res.data) };
// 修改订单数据
export const orderListEdit = params => { return Axios.post(`${base}/orderlist/edit/`, params).then(res => res.data) };
// 添加订单数据
export const orderListAdd = params => { return Axios.post(`${base}/orderlist/add/`, params).then(res => res.data) };
// 删除订单数据
export const orderListDel = params => { return Axios.post(`${base}/orderlist/delete/`, params).then(res => res.data) };
// 所有管理员数据
export const AdminListAll = params => { return Axios.get(`${base}/adminlist/query/`, { params: params }).then(res => res.data) };
// 单个管理员数据
export const AdminListOne = params => { return Axios.get(`${base}/adminlist/queryone/`, { params: params }).then(res => res.data) };
// 单个商家评论数据
export const bussComm = params => { return Axios.post(`${base}/commentlist/busscomm/`, params).then(res => res.data) };
// 单个食品评论数据
export const foodComm = params => { return Axios.post(`${base}/commentlist/foodcomm/`, params).then(res => res.data) };
// 添加商家评论数据
export const bussAdd = params => { return Axios.post(`${base}/commentlist/busscreate/`, params).then(res => res.data) };
// 添加食品评论数据
export const foodAdd = params => { return Axios.post(`${base}/commentlist/foodcreate/`, params).then(res => res.data) };
// 添加购物车
export const shopCartAdd = params => { return Axios.post(`${base}/shopcartlist/create/`, params).then(res => res.data) };
// 修改购物车
export const shopCartEdit = params => { return Axios.post(`${base}/shopcartlist/edit/`, params).then(res => res.data) };
// 删除购物车
export const shopCartDel = params => { return Axios.post(`${base}/shopcartlist/delete/`, params).then(res => res.data) };
// 查询购物车
export const shopCartAll = params => { return Axios.get(`${base}/shopcartlist/query/`, { params: params }).then(res => res.data) };
// 支付宝支付
export const alipay = params => { return Axios.post(`${base}/shopcartlist/alipay/`, params).then(res => res.data) };

let api = {
    userLogin,
    storeLogin,
    adminLogin,
    userRegister,
    storeRegister,
    loginOut
}

let user = {
    userListAll,
    userListOne,
    userListEdit,
    userListDel,
    userListAddress,
    userListWarnQuery,
    userListWarnAdd,
    userListWarnDel
}

let store = {
    storeListAll,
    storeListOne,
    storeListEdit,
    storeListDel,
    storeListAddress,
    storeListWarnQuery,
    storeListWarnAdd,
    storeListWarnDel
}

let business = {
    bussinessListAll,
    bussinessListOne,
    bussinessEdit,
    bussinessDel,
    bussinessAdd
}

let food = {
    foodListAll,
    foodListQuery,
    foodListEdit,
    foodListDel,
    foodListAdd
}

let order = {
    orderListAll,
    orderListEdit,
    orderListAdd,
    orderListDel
}

let admin = {
    AdminListAll,
    AdminListOne
}

let comment = {
    bussComm,
    foodComm,
    bussAdd,
    foodAdd
}

let shopcart = {
    shopCartAdd,
    shopCartEdit,
    shopCartDel,
    shopCartAll,
    alipay
}

export {
    api,
    user,
    store,
    business,
    food,
    order,
    admin,
    comment,
    shopcart
}