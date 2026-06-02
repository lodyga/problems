class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, string
            A: built-in function
        """
        stack = []
        entries = path.split("/")

        for entry in entries:
            if entry in ".":
                continue
            elif entry == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(entry)

        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, string
            A: iteration
        """
        stack = []
        entry = []

        for char in path + "/":
            if char == "/":
                if "".join(entry) in ".":
                    pass
                elif "".join(entry) == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append("".join(entry))

                entry = []

            else:
                entry.append(char)

        return "/" + "/".join(stack)


print(Solution().simplifyPath("/home/") == "/home")
print(Solution().simplifyPath("/home//foo/") == "/home/foo")
print(Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures")
print(Solution().simplifyPath("/../") == "/")
print(Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d")
print(Solution().simplifyPath("/a/../../b/../c//.//") == "/c")
print(Solution().simplifyPath("/.") == "/")
print(Solution().simplifyPath("/..hidden") == "/..hidden")
print(Solution().simplifyPath("/a//b////c/d//././/..") == "/a/b/c")
