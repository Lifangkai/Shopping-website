webpackJsonp([21],{511:function(t,e,n){n(754);var r=n(199)(n(660),n(788),"data-v-31175821",null);t.exports=r.exports},514:function(t,e,n){"use strict";function r(t){return"[object Array]"===L.call(t)}function o(t){return"[object ArrayBuffer]"===L.call(t)}function s(t){return"undefined"!=typeof FormData&&t instanceof FormData}function a(t){return"undefined"!=typeof ArrayBuffer&&ArrayBuffer.isView?ArrayBuffer.isView(t):t&&t.buffer&&t.buffer instanceof ArrayBuffer}function i(t){return"string"==typeof t}function u(t){return"number"==typeof t}function c(t){return void 0===t}function f(t){return null!==t&&"object"==typeof t}function d(t){return"[object Date]"===L.call(t)}function p(t){return"[object File]"===L.call(t)}function l(t){return"[object Blob]"===L.call(t)}function h(t){return"[object Function]"===L.call(t)}function m(t){return f(t)&&h(t.pipe)}function g(t){return"undefined"!=typeof URLSearchParams&&t instanceof URLSearchParams}function v(t){return t.replace(/^\s*/,"").replace(/\s*$/,"")}function b(){return("undefined"==typeof navigator||"ReactNative"!==navigator.product&&"NativeScript"!==navigator.product&&"NS"!==navigator.product)&&("undefined"!=typeof window&&"undefined"!=typeof document)}function y(t,e){if(null!==t&&void 0!==t)if("object"!=typeof t&&(t=[t]),r(t))for(var n=0,o=t.length;n<o;n++)e.call(null,t[n],n,t);else for(var s in t)Object.prototype.hasOwnProperty.call(t,s)&&e.call(null,t[s],s,t)}function w(){function t(t,n){"object"==typeof e[n]&&"object"==typeof t?e[n]=w(e[n],t):e[n]=t}for(var e={},n=0,r=arguments.length;n<r;n++)y(arguments[n],t);return e}function x(){function t(t,n){"object"==typeof e[n]&&"object"==typeof t?e[n]=x(e[n],t):e[n]="object"==typeof t?x({},t):t}for(var e={},n=0,r=arguments.length;n<r;n++)y(arguments[n],t);return e}function _(t,e,n){return y(e,function(e,r){t[r]=n&&"function"==typeof e?j(e,n):e}),t}var j=n(521),C=n(541),L=Object.prototype.toString;t.exports={isArray:r,isArrayBuffer:o,isBuffer:C,isFormData:s,isArrayBufferView:a,isString:i,isNumber:u,isObject:f,isUndefined:c,isDate:d,isFile:p,isBlob:l,isFunction:h,isStream:m,isURLSearchParams:g,isStandardBrowserEnv:b,forEach:y,merge:w,deepMerge:x,extend:_,trim:v}},515:function(t,e,n){"use strict";var r=n(514),o=n(532),s=n(522),a=n(539),i=n(537),u=n(518);t.exports=function(t){return new Promise(function(e,c){var f=t.data,d=t.headers;r.isFormData(f)&&delete d["Content-Type"];var p=new XMLHttpRequest;if(t.auth){var l=t.auth.username||"",h=t.auth.password||"";d.Authorization="Basic "+btoa(l+":"+h)}if(p.open(t.method.toUpperCase(),s(t.url,t.params,t.paramsSerializer),!0),p.timeout=t.timeout,p.onreadystatechange=function(){if(p&&4===p.readyState&&(0!==p.status||p.responseURL&&0===p.responseURL.indexOf("file:"))){var n="getAllResponseHeaders"in p?a(p.getAllResponseHeaders()):null,r=t.responseType&&"text"!==t.responseType?p.response:p.responseText,s={data:r,status:p.status,statusText:p.statusText,headers:n,config:t,request:p};o(e,c,s),p=null}},p.onabort=function(){p&&(c(u("Request aborted",t,"ECONNABORTED",p)),p=null)},p.onerror=function(){c(u("Network Error",t,null,p)),p=null},p.ontimeout=function(){c(u("timeout of "+t.timeout+"ms exceeded",t,"ECONNABORTED",p)),p=null},r.isStandardBrowserEnv()){var m=n(535),g=(t.withCredentials||i(t.url))&&t.xsrfCookieName?m.read(t.xsrfCookieName):void 0;g&&(d[t.xsrfHeaderName]=g)}if("setRequestHeader"in p&&r.forEach(d,function(t,e){void 0===f&&"content-type"===e.toLowerCase()?delete d[e]:p.setRequestHeader(e,t)}),t.withCredentials&&(p.withCredentials=!0),t.responseType)try{p.responseType=t.responseType}catch(e){if("json"!==t.responseType)throw e}"function"==typeof t.onDownloadProgress&&p.addEventListener("progress",t.onDownloadProgress),"function"==typeof t.onUploadProgress&&p.upload&&p.upload.addEventListener("progress",t.onUploadProgress),t.cancelToken&&t.cancelToken.promise.then(function(t){p&&(p.abort(),c(t),p=null)}),void 0===f&&(f=null),p.send(f)})}},516:function(t,e,n){"use strict";function r(t){this.message=t}r.prototype.toString=function(){return"Cancel"+(this.message?": "+this.message:"")},r.prototype.__CANCEL__=!0,t.exports=r},517:function(t,e,n){"use strict";t.exports=function(t){return!(!t||!t.__CANCEL__)}},518:function(t,e,n){"use strict";var r=n(531);t.exports=function(t,e,n,o,s){var a=new Error(t);return r(a,e,n,o,s)}},519:function(t,e,n){"use strict";var r=n(514);t.exports=function(t,e){e=e||{};var n={};return r.forEach(["url","method","params","data"],function(t){void 0!==e[t]&&(n[t]=e[t])}),r.forEach(["headers","auth","proxy"],function(o){r.isObject(e[o])?n[o]=r.deepMerge(t[o],e[o]):void 0!==e[o]?n[o]=e[o]:r.isObject(t[o])?n[o]=r.deepMerge(t[o]):void 0!==t[o]&&(n[o]=t[o])}),r.forEach(["baseURL","transformRequest","transformResponse","paramsSerializer","timeout","withCredentials","adapter","responseType","xsrfCookieName","xsrfHeaderName","onUploadProgress","onDownloadProgress","maxContentLength","validateStatus","maxRedirects","httpAgent","httpsAgent","cancelToken","socketPath"],function(r){void 0!==e[r]?n[r]=e[r]:void 0!==t[r]&&(n[r]=t[r])}),n}},520:function(t,e,n){"use strict";(function(e){function r(t,e){!o.isUndefined(t)&&o.isUndefined(t["Content-Type"])&&(t["Content-Type"]=e)}var o=n(514),s=n(538),a={"Content-Type":"application/x-www-form-urlencoded"},i={adapter:function(){var t;return void 0!==e&&"[object process]"===Object.prototype.toString.call(e)?t=n(515):"undefined"!=typeof XMLHttpRequest&&(t=n(515)),t}(),transformRequest:[function(t,e){return s(e,"Accept"),s(e,"Content-Type"),o.isFormData(t)||o.isArrayBuffer(t)||o.isBuffer(t)||o.isStream(t)||o.isFile(t)||o.isBlob(t)?t:o.isArrayBufferView(t)?t.buffer:o.isURLSearchParams(t)?(r(e,"application/x-www-form-urlencoded;charset=utf-8"),t.toString()):o.isObject(t)?(r(e,"application/json;charset=utf-8"),JSON.stringify(t)):t}],transformResponse:[function(t){if("string"==typeof t)try{t=JSON.parse(t)}catch(t){}return t}],timeout:0,xsrfCookieName:"XSRF-TOKEN",xsrfHeaderName:"X-XSRF-TOKEN",maxContentLength:-1,validateStatus:function(t){return t>=200&&t<300}};i.headers={common:{Accept:"application/json, text/plain, */*"}},o.forEach(["delete","get","head"],function(t){i.headers[t]={}}),o.forEach(["post","put","patch"],function(t){i.headers[t]=o.merge(a)}),t.exports=i}).call(e,n(200))},521:function(t,e,n){"use strict";t.exports=function(t,e){return function(){for(var n=new Array(arguments.length),r=0;r<n.length;r++)n[r]=arguments[r];return t.apply(e,n)}}},522:function(t,e,n){"use strict";function r(t){return encodeURIComponent(t).replace(/%40/gi,"@").replace(/%3A/gi,":").replace(/%24/g,"$").replace(/%2C/gi,",").replace(/%20/g,"+").replace(/%5B/gi,"[").replace(/%5D/gi,"]")}var o=n(514);t.exports=function(t,e,n){if(!e)return t;var s;if(n)s=n(e);else if(o.isURLSearchParams(e))s=e.toString();else{var a=[];o.forEach(e,function(t,e){null!==t&&void 0!==t&&(o.isArray(t)?e+="[]":t=[t],o.forEach(t,function(t){o.isDate(t)?t=t.toISOString():o.isObject(t)&&(t=JSON.stringify(t)),a.push(r(e)+"="+r(t))}))}),s=a.join("&")}if(s){var i=t.indexOf("#");-1!==i&&(t=t.slice(0,i)),t+=(-1===t.indexOf("?")?"?":"&")+s}return t}},524:function(t,e,n){"use strict";n.d(e,"h",function(){return s}),n.d(e,"j",function(){return a}),n.d(e,"f",function(){return i}),n.d(e,"d",function(){return u}),n.d(e,"m",function(){return et}),n.d(e,"a",function(){return nt}),n.d(e,"i",function(){return rt}),n.d(e,"c",function(){return ot}),n.d(e,"g",function(){return st}),n.d(e,"b",function(){return at}),n.d(e,"l",function(){return it}),n.d(e,"k",function(){return ut}),n.d(e,"e",function(){return ct});var r=n(525),o=n.n(r);o.a.defaults.withCredentials=!0;var s="http://127.0.0.1:8000",a=s+"/adminlist/media/admin/",i=s+"/businesslist/media/bussiness/",u=s+"/foodlist/media/food/",c=function(t){return o.a.post(s+"/api/userlogin/",t).then(function(t){return t.data})},f=function(t){return o.a.post(s+"/api/storelogin/",t).then(function(t){return t.data})},d=function(t){return o.a.post(s+"/api/adminlogin/",t).then(function(t){return t.data})},p=function(t){return o.a.post(s+"/api/userregister/",t).then(function(t){return t.data})},l=function(t){return o.a.post(s+"/api/storeregister/",t).then(function(t){return t.data})},h=function(t){return o.a.get(s+"/userlist/query/",{params:t}).then(function(t){return t.data})},m=function(t){return o.a.get(s+"/userlist/queryone/",{params:t}).then(function(t){return t.data})},g=function(t){return o.a.post(s+"/userlist/edit/",t).then(function(t){return t.data})},v=function(t){return o.a.post(s+"/userlist/delete/",t).then(function(t){return t.data})},b=function(t){return o.a.post(s+"/userlist/queryaddress/",t).then(function(t){return t.data})},y=function(t){return o.a.get(s+"/userlist/querywarn/",{params:t}).then(function(t){return t.data})},w=function(t){return o.a.post(s+"/userlist/addwarn/",t).then(function(t){return t.data})},x=function(t){return o.a.post(s+"/userlist/deletewarn/",t).then(function(t){return t.data})},_=function(t){return o.a.get(s+"/storelist/query/",{params:t}).then(function(t){return t.data})},j=function(t){return o.a.get(s+"/storelist/queryone/",{params:t}).then(function(t){return t.data})},C=function(t){return o.a.post(s+"/storelist/edit/",t).then(function(t){return t.data})},L=function(t){return o.a.post(s+"/storelist/delete/",t).then(function(t){return t.data})},A=function(t){return o.a.post(s+"/storelist/queryaddress/",t).then(function(t){return t.data})},E=function(t){return o.a.get(s+"/storelist/querywarn/",{params:t}).then(function(t){return t.data})},R=function(t){return o.a.post(s+"/storelist/addwarn/",t).then(function(t){return t.data})},q=function(t){return o.a.post(s+"/storelist/deletewarn/",t).then(function(t){return t.data})},S=function(t){return o.a.get(s+"/businesslist/query/",{params:t}).then(function(t){return t.data})},N=function(t){return o.a.post(s+"/businesslist/queryone/",t).then(function(t){return t.data})},O=function(t){return o.a.post(s+"/businesslist/edit/",t).then(function(t){return t.data})},k=function(t){return o.a.post(s+"/businesslist/delete/",t).then(function(t){return t.data})},T=function(t){return o.a.post(s+"/businesslist/create/",t).then(function(t){return t.data})},D=function(t){return o.a.get(s+"/foodlist/query/",{params:t}).then(function(t){return t.data})},B=function(t){return o.a.get(s+"/foodlist/querylist/",{params:t}).then(function(t){return t.data})},F=function(t){return o.a.post(s+"/foodlist/edit/",t).then(function(t){return t.data})},U=function(t){return o.a.post(s+"/foodlist/create/",t).then(function(t){return t.data})},P=function(t){return o.a.post(s+"/foodlist/delete/",t).then(function(t){return t.data})},z=function(t){return o.a.get(s+"/orderlist/query/",{params:t}).then(function(t){return t.data})},H=function(t){return o.a.post(s+"/orderlist/edit/",t).then(function(t){return t.data})},M=function(t){return o.a.post(s+"/orderlist/add/",t).then(function(t){return t.data})},I=function(t){return o.a.post(s+"/orderlist/delete/",t).then(function(t){return t.data})},W=function(t){return o.a.get(s+"/adminlist/query/",{params:t}).then(function(t){return t.data})},X=function(t){return o.a.get(s+"/adminlist/queryone/",{params:t}).then(function(t){return t.data})},$=function(t){return o.a.post(s+"/commentlist/busscomm/",t).then(function(t){return t.data})},J=function(t){return o.a.post(s+"/commentlist/foodcomm/",t).then(function(t){return t.data})},V=function(t){return o.a.post(s+"/commentlist/busscreate/",t).then(function(t){return t.data})},Q=function(t){return o.a.post(s+"/commentlist/foodcreate/",t).then(function(t){return t.data})},K=function(t){return o.a.post(s+"/shopcartlist/create/",t).then(function(t){return t.data})},G=function(t){return o.a.post(s+"/shopcartlist/edit/",t).then(function(t){return t.data})},Y=function(t){return o.a.post(s+"/shopcartlist/delete/",t).then(function(t){return t.data})},Z=function(t){return o.a.get(s+"/shopcartlist/query/",{params:t}).then(function(t){return t.data})},tt=function(t){return o.a.post(s+"/shopcartlist/alipay/",t).then(function(t){return t.data})},et={userLogin:c,storeLogin:f,adminLogin:d,userRegister:p,storeRegister:l},nt={userListAll:h,userListOne:m,userListEdit:g,userListDel:v,userListAddress:b,userListWarnQuery:y,userListWarnAdd:w,userListWarnDel:x},rt={storeListAll:_,storeListOne:j,storeListEdit:C,storeListDel:L,storeListAddress:A,storeListWarnQuery:E,storeListWarnAdd:R,storeListWarnDel:q},ot={bussinessListAll:S,bussinessListOne:N,bussinessEdit:O,bussinessDel:k,bussinessAdd:T},st={foodListAll:D,foodListQuery:B,foodListEdit:F,foodListDel:P,foodListAdd:U},at={orderListAll:z,orderListEdit:H,orderListAdd:M,orderListDel:I},it={AdminListAll:W,AdminListOne:X},ut={bussComm:$,foodComm:J,bussAdd:V,foodAdd:Q},ct={shopCartAdd:K,shopCartEdit:G,shopCartDel:Y,shopCartAll:Z,alipay:tt}},525:function(t,e,n){t.exports=n(526)},526:function(t,e,n){"use strict";function r(t){var e=new a(t),n=s(a.prototype.request,e);return o.extend(n,a.prototype,e),o.extend(n,e),n}var o=n(514),s=n(521),a=n(528),i=n(519),u=n(520),c=r(u);c.Axios=a,c.create=function(t){return r(i(c.defaults,t))},c.Cancel=n(516),c.CancelToken=n(527),c.isCancel=n(517),c.all=function(t){return Promise.all(t)},c.spread=n(540),t.exports=c,t.exports.default=c},527:function(t,e,n){"use strict";function r(t){if("function"!=typeof t)throw new TypeError("executor must be a function.");var e;this.promise=new Promise(function(t){e=t});var n=this;t(function(t){n.reason||(n.reason=new o(t),e(n.reason))})}var o=n(516);r.prototype.throwIfRequested=function(){if(this.reason)throw this.reason},r.source=function(){var t;return{token:new r(function(e){t=e}),cancel:t}},t.exports=r},528:function(t,e,n){"use strict";function r(t){this.defaults=t,this.interceptors={request:new a,response:new a}}var o=n(514),s=n(522),a=n(529),i=n(530),u=n(519);r.prototype.request=function(t){"string"==typeof t?(t=arguments[1]||{},t.url=arguments[0]):t=t||{},t=u(this.defaults,t),t.method=t.method?t.method.toLowerCase():"get";var e=[i,void 0],n=Promise.resolve(t);for(this.interceptors.request.forEach(function(t){e.unshift(t.fulfilled,t.rejected)}),this.interceptors.response.forEach(function(t){e.push(t.fulfilled,t.rejected)});e.length;)n=n.then(e.shift(),e.shift());return n},r.prototype.getUri=function(t){return t=u(this.defaults,t),s(t.url,t.params,t.paramsSerializer).replace(/^\?/,"")},o.forEach(["delete","get","head","options"],function(t){r.prototype[t]=function(e,n){return this.request(o.merge(n||{},{method:t,url:e}))}}),o.forEach(["post","put","patch"],function(t){r.prototype[t]=function(e,n,r){return this.request(o.merge(r||{},{method:t,url:e,data:n}))}}),t.exports=r},529:function(t,e,n){"use strict";function r(){this.handlers=[]}var o=n(514);r.prototype.use=function(t,e){return this.handlers.push({fulfilled:t,rejected:e}),this.handlers.length-1},r.prototype.eject=function(t){this.handlers[t]&&(this.handlers[t]=null)},r.prototype.forEach=function(t){o.forEach(this.handlers,function(e){null!==e&&t(e)})},t.exports=r},530:function(t,e,n){"use strict";function r(t){t.cancelToken&&t.cancelToken.throwIfRequested()}var o=n(514),s=n(533),a=n(517),i=n(520),u=n(536),c=n(534);t.exports=function(t){return r(t),t.baseURL&&!u(t.url)&&(t.url=c(t.baseURL,t.url)),t.headers=t.headers||{},t.data=s(t.data,t.headers,t.transformRequest),t.headers=o.merge(t.headers.common||{},t.headers[t.method]||{},t.headers||{}),o.forEach(["delete","get","head","post","put","patch","common"],function(e){delete t.headers[e]}),(t.adapter||i.adapter)(t).then(function(e){return r(t),e.data=s(e.data,e.headers,t.transformResponse),e},function(e){return a(e)||(r(t),e&&e.response&&(e.response.data=s(e.response.data,e.response.headers,t.transformResponse))),Promise.reject(e)})}},531:function(t,e,n){"use strict";t.exports=function(t,e,n,r,o){return t.config=e,n&&(t.code=n),t.request=r,t.response=o,t.isAxiosError=!0,t.toJSON=function(){return{message:this.message,name:this.name,description:this.description,number:this.number,fileName:this.fileName,lineNumber:this.lineNumber,columnNumber:this.columnNumber,stack:this.stack,config:this.config,code:this.code}},t}},532:function(t,e,n){"use strict";var r=n(518);t.exports=function(t,e,n){var o=n.config.validateStatus;!o||o(n.status)?t(n):e(r("Request failed with status code "+n.status,n.config,null,n.request,n))}},533:function(t,e,n){"use strict";var r=n(514);t.exports=function(t,e,n){return r.forEach(n,function(n){t=n(t,e)}),t}},534:function(t,e,n){"use strict";t.exports=function(t,e){return e?t.replace(/\/+$/,"")+"/"+e.replace(/^\/+/,""):t}},535:function(t,e,n){"use strict";var r=n(514);t.exports=r.isStandardBrowserEnv()?function(){return{write:function(t,e,n,o,s,a){var i=[];i.push(t+"="+encodeURIComponent(e)),r.isNumber(n)&&i.push("expires="+new Date(n).toGMTString()),r.isString(o)&&i.push("path="+o),r.isString(s)&&i.push("domain="+s),!0===a&&i.push("secure"),document.cookie=i.join("; ")},read:function(t){var e=document.cookie.match(new RegExp("(^|;\\s*)("+t+")=([^;]*)"));return e?decodeURIComponent(e[3]):null},remove:function(t){this.write(t,"",Date.now()-864e5)}}}():function(){return{write:function(){},read:function(){return null},remove:function(){}}}()},536:function(t,e,n){"use strict";t.exports=function(t){return/^([a-z][a-z\d\+\-\.]*:)?\/\//i.test(t)}},537:function(t,e,n){"use strict";var r=n(514);t.exports=r.isStandardBrowserEnv()?function(){function t(t){var e=t;return n&&(o.setAttribute("href",e),e=o.href),o.setAttribute("href",e),{href:o.href,protocol:o.protocol?o.protocol.replace(/:$/,""):"",host:o.host,search:o.search?o.search.replace(/^\?/,""):"",hash:o.hash?o.hash.replace(/^#/,""):"",hostname:o.hostname,port:o.port,pathname:"/"===o.pathname.charAt(0)?o.pathname:"/"+o.pathname}}var e,n=/(msie|trident)/i.test(navigator.userAgent),o=document.createElement("a");return e=t(window.location.href),function(n){var o=r.isString(n)?t(n):n;return o.protocol===e.protocol&&o.host===e.host}}():function(){return function(){return!0}}()},538:function(t,e,n){"use strict";var r=n(514);t.exports=function(t,e){r.forEach(t,function(n,r){r!==e&&r.toUpperCase()===e.toUpperCase()&&(t[e]=n,delete t[r])})}},539:function(t,e,n){"use strict";var r=n(514),o=["age","authorization","content-length","content-type","etag","expires","from","host","if-modified-since","if-unmodified-since","last-modified","location","max-forwards","proxy-authorization","referer","retry-after","user-agent"];t.exports=function(t){var e,n,s,a={};return t?(r.forEach(t.split("\n"),function(t){if(s=t.indexOf(":"),e=r.trim(t.substr(0,s)).toLowerCase(),n=r.trim(t.substr(s+1)),e){if(a[e]&&o.indexOf(e)>=0)return;a[e]="set-cookie"===e?(a[e]?a[e]:[]).concat([n]):a[e]?a[e]+", "+n:n}}),a):a}},540:function(t,e,n){"use strict";t.exports=function(t){return function(e){return t.apply(null,e)}}},541:function(t,e){/*!
 * Determine if an object is a Buffer
 *
 * @author   Feross Aboukhadijeh <https://feross.org>
 * @license  MIT
 */
t.exports=function(t){return null!=t&&null!=t.constructor&&"function"==typeof t.constructor.isBuffer&&t.constructor.isBuffer(t)}},660:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var r=n(524);e.default={data:function(){return{base:r.h,imgList:[r.h+"/media/lunbo/lunbo6.jpg",r.h+"/media/lunbo/015587554320db0000019ae910eee0.jpg@1280w_1l_2o_100sh.jpg",r.h+"/media/lunbo/01605a554320e10000019ae9299b20.jpg@1280w_1l_2o_100sh.jpg",r.h+"/media/lunbo/011abc554320e00000019ae9af49db.jpg@1280w_1l_2o_100sh.jpg",r.h+"/media/lunbo/01f760554320e10000019ae9c6a3c4.jpg@1280w_1l_2o_100sh.jpg"],currentDate:new Date}},computed:{username:function(){return this.$store.state.username}},mounted:function(){},methods:{}}},678:function(t,e,n){e=t.exports=n(484)(!1),e.push([t.i,'.allcover[data-v-31175821]{position:absolute;top:0;right:0}.ctt[data-v-31175821]{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%)}.tb[data-v-31175821]{position:absolute;top:50%;transform:translateY(-50%)}.lr[data-v-31175821]{position:absolute;left:50%;transform:translateX(-50%)}.userHome .el-carousel[data-v-31175821]{top:-10px;z-index:0}.userHome .el-carousel__item[data-v-31175821]{width:50%;height:100%}.lunbo[data-v-31175821]{width:100%;height:100%}.time[data-v-31175821]{font-size:13px;color:#999}.bottom[data-v-31175821]{margin-top:13px;line-height:12px}.button[data-v-31175821]{padding:0;float:right}.image[data-v-31175821]{width:100%;display:block}.clearfix[data-v-31175821]:after,.clearfix[data-v-31175821]:before{display:table;content:""}.clearfix[data-v-31175821]:after{clear:both}.web_title[data-v-31175821]{font-size:45px;color:#5a5a5a;margin-top:100px}.web_context[data-v-31175821]{margin-top:20px;font-size:20px;color:#777}.tuijian[data-v-31175821]{text-align:center}.tuijian img[data-v-31175821]{width:200px;height:200px;border-radius:50%}.tuijian h2[data-v-31175821]{margin-top:10px;font-size:30px;font-weight:600}.tuijian p[data-v-31175821]{margin-top:10px;font-size:15px}',""])},754:function(t,e,n){var r=n(678);"string"==typeof r&&(r=[[t.i,r,""]]),r.locals&&(t.exports=r.locals);n(485)("c2d9ffa8",r,!0)},788:function(t,e){t.exports={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"userHome"},[n("el-carousel",{attrs:{trigger:"click",height:"400px",type:"card"}},t._l(t.imgList,function(t){return n("el-carousel-item",{key:t},[n("img",{staticClass:"lunbo",attrs:{src:t}})])}),1),t._v(" "),n("div",{staticClass:"container"},[n("el-row",{staticClass:"row-bg",attrs:{type:"flex",justify:"space-around"}},[n("el-col",{staticClass:"tuijian",attrs:{span:6}},[n("img",{attrs:{src:"https://www.starbucks.com.cn/images/pages/tmall-1101-cn.jpg",alt:""}}),t._v(" "),n("h2",[t._v("双十一活动 速来抢购")]),t._v(" "),n("p",[t._v("更多精彩优惠，更多礼品，尽在双十一")])]),t._v(" "),n("el-col",{staticClass:"tuijian",attrs:{span:6}},[n("img",{attrs:{src:"https://www.starbucks.com.cn/images/pages/starbucks-design-studio-web-china.jpg",alt:""}}),t._v(" "),n("h2",[t._v("全球创意设计师平台")]),t._v(" "),n("p",[t._v("国际设计师顶尖制作，物美价廉等你取")])]),t._v(" "),n("el-col",{staticClass:"tuijian",attrs:{span:6}},[n("img",{attrs:{src:"https://www.starbucks.com.cn/images/pages/homepage-career-cn.jpg",alt:""}}),t._v(" "),n("h2",[t._v("淘宝美食 是在任性")]),t._v(" "),n("p",[t._v("星巴克欢迎你的到来")])])],1),t._v(" "),n("el-row",{staticClass:"row-bg",attrs:{type:"flex",justify:"space-around"}},[n("el-col",{attrs:{span:9}},[n("h2",{staticClass:"web_title"},[t._v("足不出户即可购买到你所喜欢的商品")]),t._v(" "),n("p",{staticClass:"web_context"},[t._v("\n          提供个人对个人的买卖平台有淘宝、易趣、拍拍等，另外还有许多提供其它\n          "),n("br"),t._v("各种各样商品出售的网站。\n        ")])]),t._v(" "),n("el-col",{attrs:{span:8}},[n("img",{attrs:{src:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573467094655&di=2b24f420f601628adf3604c6cb96d809&imgtype=0&src=http%3A%2F%2Fimg.mp.sohu.com%2Fupload%2F20170731%2F26ec9bd4e8f94219beb4c68512ef537a_th.png",alt:""}})])],1),t._v(" "),n("br"),t._v(" "),n("el-row",{staticClass:"row-bg",attrs:{type:"flex",justify:"space-around"}},[n("el-col",{attrs:{span:8}},[n("img",{attrs:{src:"http://img.mp.sohu.com/upload/20170731/1730037c3a2c44b3a5a34a4dd409e368_th.png",alt:""}})]),t._v(" "),n("el-col",{attrs:{span:9}},[n("h2",{staticClass:"web_title"},[t._v("可以货比三家，买到物美价廉的商品")]),t._v(" "),n("p",{staticClass:"web_context"},[t._v("\n          购物网址导航是指通过科学统筹的方法，对网友常用的购物网站进行对比，\n          "),n("br"),t._v("根据网站的规模、实力、信誉等进行排行，方便网友们快速找到自已购物所需要的网站\n        ")])])],1),t._v(" "),n("br"),t._v(" "),n("el-row",{staticClass:"row-bg",attrs:{type:"flex",justify:"space-around"}},[n("el-col",{attrs:{span:9}},[n("h2",{staticClass:"web_title"},[t._v("努力探寻更高意义上的导购原则和规范")]),t._v(" "),n("p",{staticClass:"web_context"},[t._v("\n          由于互联网在中国的迅猛发展，以及网上购物本身优势带来网购市场空前的繁荣，\n          "),n("br"),t._v("迫使众多卖家急需找到更多的展示平台为自己打开销量\n        ")])]),t._v(" "),n("el-col",{attrs:{span:8}},[n("img",{attrs:{src:"https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573467168530&di=8ec9eb7796466ea0069dc7acadd5d18a&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171012%2Fff01d81f159148428929638fed0fc167.jpeg",alt:""}})])],1)],1)],1)},staticRenderFns:[]}}});