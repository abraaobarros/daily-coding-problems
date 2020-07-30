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
          }
        }
      }
    }
  }
  return closest;
}

console.log(closest_3sum_BF([2, 1, -5, 4], -1));
