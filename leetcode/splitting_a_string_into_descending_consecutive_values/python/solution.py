class Solution:
    def splitString(self, text: str) -> bool:
        """
        Time complexity: O(2^n)
        Auxiliary space complexity: O(n)
        Tags:
            A: backtracking with pruning
        """
        N = len(text)

        def backtrack(start_idx: int, prev_num: int, has_split: bool) -> bool:
            if start_idx == N:
                return has_split

            num = 0

            for idx in range(start_idx, N):
                digit = int(text[idx])
                num = num*10 + digit

                is_prev_valid = start_idx == 0 or prev_num - 1 == num
                
                # pruning
                # if start_idx != 0 and num >= prev_num:
                #     break

                if (
                    is_prev_valid
                    and backtrack(idx + 1, num, start_idx != 0)
                ):
                    return True

            return False

        return backtrack(0, 0, False)


print(Solution().splitString("1234") == False)
print(Solution().splitString("050043") == True)
print(Solution().splitString("9080701") == False)
print(Solution().splitString("1") == False)
print(Solution().splitString("21") == True)
print(Solution().splitString("021") == True)
print(Solution().splitString("201") == True)
print(Solution().splitString("0090089") == True)
print(Solution().splitString("001") == False)
print(Solution().splitString("64424509442147483647") == False)
