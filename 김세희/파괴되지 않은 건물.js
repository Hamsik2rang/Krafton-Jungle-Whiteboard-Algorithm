function solution(board, skill) {
  var answer = 0;
  const rowCnt = board.length;
  const colCnt = board[0].length;
  const damage = Array.from(Array(rowCnt), () => new Array(colCnt).fill(0));
  for (let [type, r1, c1, r2, c2, degree] of skill) {
    if (type === 1) {
      //공격
      damage[r1][c1] -= degree;
      if (r2 < rowCnt - 1) {
        damage[r2 + 1][c1] += degree;
      }
      if (c2 < colCnt - 1) {
        damage[r1][c2 + 1] += degree;
      }
      if (r2 < rowCnt - 1 && c2 < colCnt - 1) {
        damage[r2 + 1][c2 + 1] -= degree;
      }
    } else {
      //회복
      damage[r1][c1] += degree;
      if (r2 < rowCnt - 1) {
        damage[r2 + 1][c1] -= degree;
      }
      if (c2 < colCnt - 1) {
        damage[r1][c2 + 1] -= degree;
      }
      if (r2 < rowCnt - 1 && c2 < colCnt - 1) {
        damage[r2 + 1][c2 + 1] += degree;
      }
    }
  }

  //damage 누적합 구하기
  for (let i = 0; i < rowCnt; i++) {
    for (let j = 0; j < colCnt; j++) {
      if (i > 0) {
        damage[i][j] += damage[i - 1][j];
      }
    }
  }
  for (let i = 0; i < rowCnt; i++) {
    for (let j = 0; j < colCnt; j++) {
      if (j > 0) {
        damage[i][j] += damage[i][j - 1];
      }
    }
  }
  const result = board.map((r, ridx) => {
    return r.map((c, cidx) => (c += damage[ridx][cidx]));
  });

  ans = 0;
  for (let i = 0; i < rowCnt; i++) {
    for (let j = 0; j < colCnt; j++) {
      if (result[i][j] > 0) ans += 1;
    }
  }

  return ans;
}
