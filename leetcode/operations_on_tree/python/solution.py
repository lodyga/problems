from collections import deque


class LockingTree:
    """
    Time complexity: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: queue, hash map, list, array
        A: BFS, iteration, level-order traversal
    """

    def __init__(self, parent: list[int]):
        self.parent = parent  # [-1, 0, 0, 1, 1, 2, 2]
        # val = 0: unlocked, val > 0: locked by `val` user id
        self.locked_by = [0] * len(parent)  # [0, 0, 0, 0, 5, 0, 0]
        # {0: [1, 2], 1: [3, 4], 2: [5, 6]}
        self.child = {p: [] for p in parent[1:]}

        for c in range(1, len(parent)):
            p = parent[c]
            self.child[p].append(c)

    def lock(self, num: int, user: int) -> bool:
        if self.locked_by[num]:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Check if node or any of its ancesters are locked.
        num_copy = num
        while num_copy != -1:
            if self.locked_by[num_copy]:
                return False
            num_copy = self.parent[num_copy]

        # Check descendants.
        locked_counter = 0
        queue = deque([num])

        while queue:
            node = queue.popleft()

            if self.locked_by[node]:
                self.locked_by[node] = 0
                locked_counter += 1

            if node in self.child:
                queue.extend(self.child[node])

        if locked_counter > 0:
            self.locked_by[num] = user

        return locked_counter > 0


lockingTree = LockingTree([-1, 0, 0, 1, 1, 2, 2])
print((lockingTree.lock(2, 2)) == True)
print((lockingTree.unlock(2, 3)) == False)
print((lockingTree.unlock(2, 2)) == True)
print((lockingTree.lock(4, 5)) == True)
print((lockingTree.upgrade(0, 1)) == True)
print((lockingTree.lock(0, 1)) == False)
