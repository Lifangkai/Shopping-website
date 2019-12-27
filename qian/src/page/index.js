var wH = window.innerHeight;
var wW = window.innerWidth;

export const generateStars = (n) => {
  let login_page = document.getElementById('login_page')
  // let login_page = document.body
  for (var i = 0; i < n; i++) {
    var div = document.createElement('div');
    div.className = i % 20 == 0 ? 'star star--big' : i % 9 == 0 ? 'star star--medium' : 'star';
    // random everywhere!
    div.setAttribute('style', 'top:' + Math.round(Math.random() * wH) + 'px;left:' + Math.round(Math.random() * wW) + 'px;animation-duration:' + (Math.round(Math.random() * 3000) + 3000) + 'ms;animation-delay:' + Math.round(Math.random() * 3000) + 'ms;');
    // console.log(document.getElementById('login_page'))
    login_page.appendChild(div);
  }
  // console.log(login_page)
};

// generateStars(150);