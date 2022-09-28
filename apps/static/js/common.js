
window.onload = () => {
  // toggleボタン
  let sidemenuToggle = document.getElementById('toggle')
  // メインコンテンツを囲むmain要素
  let page = document.getElementsByTagName('main')[0];
  // 表示状態 trueで表示中 falseで非表示
  let sidemenuStatus = true;
  // ボタンクリック時のイベント
  sidemenuToggle.addEventListener('click', () => {
    // 表示状態を判定
    if (sidemenuStatus) {
      page.style.cssText = 'margin-left: -230px'
      sidemenuStatus = false;
    } else {
      page.style.cssText = 'margin-left: 0px'
      sidemenuStatus = true;
    }
  })
}

