//数组去重
export const array_remove_repeat = (a) => { // 去重
    let r = [];
    for (let i = 0; i < a.length; i++) {
        let flag = true;
        let temp = a[i];
        for (let j = 0; j < r.length; j++) {
            if (temp === r[j]) {
                flag = false;
                break;
            }
        }
        if (flag) {
            r.push(temp);
        }
    }
    return r;
}

//判断是否是空对象
export const isEmptyObject = (a) => {
    let t;
    for (t in a)
        return !1;
    return !0;
}

//对象深拷贝
export const deepClone = (obj) => {
    let objClone = Array.isArray(obj) ? [] : {};
    if (obj && typeof obj === "object") {
        let key;
        for (key in obj) {
            if (obj.hasOwnProperty(key)) {
                //判断ojb子元素是否为对象，如果是，递归复制
                if (obj[key] && typeof obj[key] === "object") {
                    objClone[key] = deepClone(obj[key]);
                } else {
                    //如果不是，简单复制
                    objClone[key] = obj[key];
                }
            }
        }
    }
    return objClone;
}

// 创建唯一id
export const createId = () => {
    return Math.random()
        .toString(36)
        .slice(2);
}

// 获取cookie
export const getCookie = (cname) => {
    debugger
    var name = cname + "=";
    var ca = document.cookie.split(';');
    console.log("获取cookie,现在循环")
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        console.log(c)
        while (c.charAt(0) == ' ') c = c.substring(1);
        if (c.indexOf(name) != -1) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

// 获取元素距离左边浏览器距离
export const getOffsetLeft = (obj) => {
    var tmp = obj.offsetLeft;
    var node = obj.offsetParent;
    while (node != null) {
        tmp += node.offsetLeft;
        node = node.offsetParent;
    }
    return tmp;
};
// 获取元素距离上边浏览器距离
export const getOffsetTop = (obj) => {
    var tmp = obj.offsetTop;
    var node = obj.offsetParent;
    while (node != null) {
        tmp += node.offsetTop;
        node = node.offsetParent;
    }
    return tmp;
};