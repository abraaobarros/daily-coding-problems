function integer_to_roman(num) {
  const numbers = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
  };
  let roman = "";
  while (num > 0) {
    const nearestNumber = Object.keys(numbers)
      .reverse()
      .find((i) => i <= num);
    num = num - nearestNumber;
    roman = roman + numbers[nearestNumber];
  }
  return roman;
}

console.log(integer_to_roman(1494));
