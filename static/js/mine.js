"use strict";

let data = [];
let h, w, bomb, count;
let startTime;
let timeoutId;
let TimeLeft;

const btn = document.getElementById("btn");
btn.addEventListener("click", init);

const text = document.getElementById("text");
const board = document.getElementById("board");
const bombCount = document.querySelector(".bombCount");
const result = document.getElementById("result");
const time = document.getElementById("time");
const lose_modal = document.getElementById('loseModal');
const win_modal = document.getElementById('winModal');

// 発表用のコード
const TestWin = document.getElementById("TestWin");
TestWin.addEventListener("click", Win);
function Win() {
  win_modal.style.display = 'block';
}

function init() {
  h = Number(document.getElementById("h").value);
  w = Number(document.getElementById("w").value);
  bomb = Number(document.getElementById("b").value);
  if (h * w - 9 < bomb) {
    result.textContent = "エラー：爆弾の数が正しく入力されていません。";
    return;
  }
  if (time.textContent !== "100") {
    result.textContent = "戻るボタンから一度戻ってください";
    return;
  }
  data = [];
  text.style.display = "none";
  board.innerHTML = "";
  board.style.pointerEvents = "auto";
  clearTimeout(timeoutId);
  result.textContent = "";
  count = bomb;
  bombCount.textContent = count;
  time.textContent = "100";
  for (let i = 0; i < h; i++) {
    const tr = document.createElement("tr");
    for (let j = 0; j < w; j++) {
      const td = document.createElement("td");
      td.addEventListener("click", leftClicked);
      td.addEventListener("contextmenu", rightClicked);
      tr.appendChild(td);
    }
    board.appendChild(tr);
  }
}

// 爆弾を設置
function putBomb() {
  for (let i = 0; i < bomb; i++) {
    while (true) {
      const y = Math.floor(Math.random() * h);
      const x = Math.floor(Math.random() * w);
      if (data[y][x] === 0) {
        data[y][x] = 1;
        break;
      }
    }
  }
}

// 左クリック マスを空ける
function leftClicked() {
  const y = this.parentNode.rowIndex;
  const x = this.cellIndex;
  if (this.className === "open" || this.className === "flag") {
    return;
  }

  // 一手目か確認
  if (!data.length) {
    startTime = Date.now();
    timer();
    for (let i = 0; i < h; i++) {
      data[i] = Array(w).fill(0);
    }
    for (let i = y - 1; i <= y + 1; i++) {
      for (let j = x - 1; j <= x + 1; j++) {
        if (i >= 0 && i < h && j >= 0 && j < w) {
          data[i][j] = -1;
        }
      }
    }
    putBomb();

  }

  // 爆弾を踏んだか判定
  if (data[y][x] === 1) {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (data[i][j] === 1) {
          board.rows[i].cells[j].classList.add("bomb");
        }
      }
    }
    board.style.pointerEvents = "none";
    result.textContent = "GAME OVER";
    clearTimeout(timeoutId);
    lose_modal.style.display = 'block';
    return;
  }

  let bombs = countBomb(y, x);
  if (bombs === 0) {
    open(y, x);
  } else {
    this.textContent = bombs;
    this.classList.add("open");
  }

  // クリア判定
  if (countOpenCell()) {
    for (let i = 0; i < h; i++) {
      for (let j = 0; j < w; j++) {
        if (data[i][j] === 1) {
          board.rows[i].cells[j].classList.add("clear");
          win_modal.style.display = 'block';
        }
      }
    }
    board.style.pointerEvents = "none";
    clearTimeout(timeoutId);
    return;
  }
}

// 右クリック 旗を置く
function rightClicked(e) {
  e.preventDefault();
  if (this.className === "open") {
    return;
  }
  this.classList.toggle("flag");
  if (this.className === "flag") {
    count--;
    bombCount.textContent = count;
  } else {
    count++;
    bombCount.textContent = count;
  }
}

// マスの周りの爆弾の数を数える
function countBomb(y, x) {
  let bombs = 0;
  for (let i = y - 1; i <= y + 1; i++) {
    for (let j = x - 1; j <= x + 1; j++) {
      if (i >= 0 && i < h && j >= 0 && j < w) {
        if (data[i][j] === 1) {
          bombs++;
        }
      }
    }
  }
  return bombs;
}

// マスを開く
function open(y, x) {
  for (let i = y - 1; i <= y + 1; i++) {
    for (let j = x - 1; j <= x + 1; j++) {
      if (i >= 0 && i < h && j >= 0 && j < w) {
        let bombs = countBomb(i, j);
        if (
          board.rows[i].cells[j].className === "open" ||
          board.rows[i].cells[j].className === "flag"
        ) {
          continue;
        }
        if (bombs === 0) {
          board.rows[i].cells[j].classList.add("open");
          open(i, j);
        } else {
          board.rows[i].cells[j].textContent = bombs;
          board.rows[i].cells[j].classList.add("open");
        }
      }
    }
  }
}

// 空いているマスを数える
function countOpenCell() {
  let openCell = 0;
  for (let i = 0; i < h; i++) {
    for (let j = 0; j < w; j++) {
      if (board.rows[i].cells[j].className === "open") {
        openCell++;
      }
    }
  }
  if (h * w - openCell === bomb) {
    return true;
  }
}


function timer() {
  const deff = new Date(Date.now() - startTime);
  const s = String(deff.getSeconds());
  const m = Number(deff.getMinutes()) * 60;

  // console.log(s);
  TimeLeft = 100 - Number(s) - m;
  // console.log(TimeLeft);
  time.textContent = `${TimeLeft}`;

  if (TimeLeft === 0) {
    board.style.pointerEvents = "none";
    result.textContent = "GAME OVER";
    clearTimeout(timeoutId);
    lose_modal.style.display = 'block';
    return;
  }
  timeoutId = setTimeout(() => {
    timer();
  }, 1000);
}

