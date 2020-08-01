function reshape_matrix(mat, x, y) {
  if (x * y != mat.length * mat[0].length) {
    return;
  }
  const flat = mat.reduce((i, acc) => [...i, ...acc]);
  let mReshaped = [];
  for (let i = 0; i < y; i++) {
    const row = mReshaped.push(flat.slice(i * x, x * (i + 1)));
  }
  return mReshaped;
}

console.log(
  reshape_matrix(
    [
      [1, 2, 5],
      [3, 4, 3],
    ],
    6,
    1
  )
);
