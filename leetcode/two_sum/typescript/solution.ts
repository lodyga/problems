class Solution {
    twoSum(nums: number[], target: number): number[] {
        const numIdx = new Map<number, number>();

        for (let idx: number = 0; idx < nums.length; idx++) {
            const num: number = nums[idx];
            const diff: number = target - num;

            if (numIdx.has(diff)) {
                return [numIdx.get(diff)!, idx];
            }
            else {
                numIdx.set(num, idx);
            }
        }

        return [];
    }
}

const solution = new Solution;
console.log(solution.twoSum([2, 7, 11, 15], 9))