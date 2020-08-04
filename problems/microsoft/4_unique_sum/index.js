const fourSum = (numbers, target) => {
  results = [];
  sums = {};
  const n = numbers.length;
  for (let i = 0; i < n; ++i) {
    for (let j = i + 1; j < n; ++j) {
      const current = numbers[i] + numbers[j];
      const rest = target - current;
      if (sums[rest] !== undefined) {
        let sum4 = [
          numbers[sums[rest][0]],
          numbers[sums[rest][1]],
          numbers[i],
          numbers[j],
        ];
        sum4.sort();
        if (!results.some((item) => equalTo(item, sum4))) {
          results = [...results, sum4];
        }
      }
    }

    for (let k = 0; k < i; ++k) {
      sums[numbers[i] + numbers[k]] = [i, k];
    }
  }

  return results;
};

const equalTo = (o1, o2) => {
  return (
    o1[0] === o2[0] && o1[1] === o2[1] && o1[2] === o2[2] && o1[3] === o2[3]
  );
};

console.log(fourSum([1, 1, -1, 0, -2, 1, -1], 0));

console.log(fourSum([3, 0, 1, -5, 4, 0, -1], 1));

console.log(fourSum([0, 0, 0, 0, 0], 0));
