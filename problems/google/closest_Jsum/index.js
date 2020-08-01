function closest_3sum_BF(nums, target) {
  //Brute force
  let minDistance = Infinity;
  let closest = null;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      for (let k = 0; k < nums.length; k++) {
        if (i != k && k != j && i != j) {
          const newSum = nums[i] + nums[j] + nums[k] - target;
          if (newSum < minDistance) {
            closest = [nums[i], nums[j], nums[k]];
            minDistance = newSum;
          }
        }
      }
    }
  }
  return closest;
}

function closest_3sum_O2(nums, target) {
  nums.sort()
  let minDistance = Infinity;
  let closest = null;
  for (let i = 0; i <= nums.length - 2; i++) {
    j = i + 1;
    k = nums.length - 1;

    while (k > j) {
      const newSum = Math.abs(nums[i] + nums[j] + nums[k] - target);
      if (newSum < minDistance) {
        closest = [nums[i], nums[j], nums[k]];
        minDistance = newSum;
      }
      if (newSum === 0) {
        return [nums[i], nums[j], nums[k]];
      }
      nums[i] + nums[j] + nums[k] - target > 0 ? k-- : j++;
    }
  }
  return closest;
}

console.log(closest_3sum_BF([2, 1, -5, 6, 7, 4], -1));

console.log(closest_3sum_O2([2, 1, -5, 3, 6, 7, 4], -1));
