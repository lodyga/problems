"use strict";
class Solution {
    twoSum(nums, target) {
        const numIdx = new Map();
        for (let idx = 0; idx < nums.length; idx++) {
            const num = nums[idx];
            const diff = target - num;
            if (numIdx.has(diff)) {
                return [numIdx.get(diff), idx];
            }
            else {
                numIdx.set(num, idx);
            }
        }
        return [];
    }
}
const solution = new Solution;
console.log(solution.twoSum([2, 7, 11, 15], 9));
