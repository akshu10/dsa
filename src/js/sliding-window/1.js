/**
 * Max sum of size K
 *
 * ([2, 1, 5, 1, 3, 2], 3) → 9
 * Constraints: 1 ≤ k ≤ nums.length ≤ 10^5, values may be negative.
 * Target: O(n), O(1) space. If you find yourself re-summing the window each step, that's the thing to fix.
 *
 */

function maxSubarraySum(nums, k) {
  let windowSum = 0,
    maxSubArraySum = 0;

  for (let j = 0; j < k; j++) windowSum += nums[j];

  // Doing this prevents the first window value from being thrown away. (Take first window value into account)
  maxSubArraySum = windowSum;

  for (let i = 0; i + k < nums.length; i++) {
    windowSum = windowSum - nums[i] + nums[k + i];
    maxSubArraySum = Math.max(windowSum, maxSubArraySum);
  }

  return maxSubArraySum;
}

console.log("MAX subarray sum: ", maxSubarraySum([2, 1, 5, 1, 3, 2], 3));
console.log("MAX subarray sum: ", maxSubarraySum([1, 4, 5], 3));
