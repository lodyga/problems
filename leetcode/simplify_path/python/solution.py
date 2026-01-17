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
        name = []

        for char in path + "/":
            if char == "/":
                if "".join(name) == "..":
                    if stack:
                        stack.pop()
                elif name and name != ["."]:
                    stack.append("".join(name))
                name = []
            else:
                name.append(char)

        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags:
            DS: stack, string
            A: built-in function
        """
        names = []
        
        for dir in path.split("/"):
            if dir == "" or dir == ".":
                continue
            elif dir == "..":
                if names:
                    names.pop()
            else:
                names.append(dir)
        
        return "/" + "/".join(names)


print(Solution().simplifyPath("/home/") == "/home")
print(Solution().simplifyPath("/home//foo/") == "/home/foo")
print(Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures")
print(Solution().simplifyPath("/../") == "/")
print(Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d")
print(Solution().simplifyPath("/a/../../b/../c//.//") == "/c")
print(Solution().simplifyPath("/.") == "/")
print(Solution().simplifyPath("/..hidden") == "/..hidden")
