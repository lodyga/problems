# Decode Ways
https://leetcode.com/problems/decode-ways/description/

You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

<b>Example 1:</b>\
Input: s = "12"\
Output: 2\
Explanation:\
"12" could be decoded as "AB" (1 2) or "L" (12).


<b>Example 2:</b>\
Input: s = "226"\
Output: 3\
Explanation:\
"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


<b>Example 3:</b>\
Input: s = "06"\
Output: 0\
Explanation:\
"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.