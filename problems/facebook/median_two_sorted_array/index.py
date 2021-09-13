# median of two sorted array


def median_sorted_array(nums1, nums2):

  # nums1 => [..., leftX | rightX, ...] nums2 => [..., leftY | rightY, ...]

  def _is_median(leftX, rightX, leftY, rightY):
      return leftX <= rightY and leftY <= rightX

  def _is_left_partition(leftX, rightX, leftY, rightY):
      return leftX > rightY

  def _median(total_len,leftX, rightX, leftY, rightY):
      if total_len % 2 ==0:
          return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
      else:
          return max(leftX, leftY)

  def _median_one(nums):
      n = len(nums)
      if n % 2 == 0:
          return (nums[n//2-1]+nums[n//2]) / 2
      else:
          return nums[n//2]

  def _min(nums, partition):
      if not nums or partition == len(nums):
          return float('Inf')
      else:
          return nums[partition]

  def _max(nums, partition):
      if not nums or partition == 0:
          return float('-Inf')
      else:
          print(nums, partition)
          return nums[partition-1]

  total_len = len(nums1)+len(nums2)
  if len(nums1)==0:
      return _median_one(nums2)
  if len(nums2)==0:
      return _median_one(nums1)
  if total_len==0:
      return 0
  if len(nums1) > len(nums2):
      return median_sorted_array(nums2, nums1)
  lo, hi = 0, len(nums1)

  while hi>=lo:
      partX = (lo+hi)//2
      partY = (total_len+1)//2 - partX

      leftX = _max(nums1, partX)
      rightX = _min(nums1, partX)

      leftY = _max(nums2, partY)
      rightY = _min(nums2, partY)

      if _is_median(leftX, rightX, leftY, rightY):
          return _median(total_len, leftX, rightX, leftY, rightY)

      if _is_left_partition(leftX, rightX, leftY, rightY):
          hi = partX-1
      else:
          lo = partX+1

  return -1