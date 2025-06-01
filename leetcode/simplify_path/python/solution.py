class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: stack
        """
        stack = []
        word = ""

        for char in path + "/":
            if char == "/":
                if word == "..":
                    if stack:
                        stack.pop()
                elif word and word != ".":
                    stack.append(word)
                word = ""
            else:
                word += char
        
        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Time complexity: O(n)
        Auxiliary space complexity: O(n)
        Tags: built-in function
        """
        clean_dirs = []
        
        for dir in path.split("/"):
            if not dir or dir == ".":
                continue
            elif dir == "..":
                if clean_dirs:
                    clean_dirs.pop()
            else:
                clean_dirs.append(dir)
        
        return "/" + "/".join(clean_dirs)


print(Solution().simplifyPath("/home/") == "/home")
print(Solution().simplifyPath("/home//foo/") == "/home/foo")
print(Solution().simplifyPath("/home/user/Documents/../Pictures") == "/home/user/Pictures")
print(Solution().simplifyPath("/../") == "/")
print(Solution().simplifyPath("/.../a/../b/c/../d/./") == "/.../b/d")
print(Solution().simplifyPath("/a/../../b/../c//.//") == "/c")
print(Solution().simplifyPath("/.") == "/")
print(Solution().simplifyPath("/..hidden") == "/..hidden")