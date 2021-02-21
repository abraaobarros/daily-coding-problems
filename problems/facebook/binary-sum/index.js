function sum_binary(bin1, bin2) {
  let query = 0;
  let sum = "";
  for (let i = 0; i <= bin1.length || i <= bin2.length; i++) {
    [result, query] = sum_digit(
      bin1[bin1.length - i - 1],
      bin2[bin2.length - i - 1],
      query
    );
    sum = `${result}${sum}`;
  }
  return sum;
}

function sum_digit(char1, char2, query) {
  const bin1 = parseBin(char1);
  const bin2 = parseBin(char2);
  return [(bin1 + bin2 + query) % 2, bin1 + bin2 + query >= 2 ? 1 : 0];
}

function parseBin(char) {
  if (!char) return 0;
  return parseInt(char);
}

console.log(sum_binary("11101", "1011"));
