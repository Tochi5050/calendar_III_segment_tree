from typing import List
class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n

    def query(self, l, r):
        print("query", "l =>", l, "r =>", r)
        l += self.n
        r += self.n
        print("query", "l += self.n =>",  l, "r += self.n=>", r)
        ans = 0
        while l < r:
            print("query", "l =>", l, "r =>", r, "ans =>", ans, "tree =>", self.tree)
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])
            l >>= 1
            r >>= 1
        return ans




    def update(self, i, val):
        print("update", "i =>", i, "val =>", val)
        i += self.n
        print("update", "i += self.n =>", i)
        self.tree[i] = val
        print("update", "i =>", i, "tree =>", self.tree)
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])
            print("update", "i =>", i, "tree =>", self.tree)


class Solution:
    def lengthOfLIS(self, A: List[int], k: int) -> int: #[4,2,1,4,3,4,5,8,15]
        n, ans = max(A), 1
        seg = SEG(n)
        for a in A:
            print("a =>", a)
            a -= 1
            print(f"seg.query_outer a - 1=> {a} , k=> {k}, max(0, a - k) => max(0, {a} - {k}) = {max(0, a - k)}")
            premax = seg.query(max(0, a - k), a)
            ans = max(ans, premax + 1)
            print("seg.update_outer =>", "a - 1=>", a, "premax =>", premax)
            seg.update(a, premax + 1)
        return ans

result = Solution()
print(result.lengthOfLIS([4,2,1,4,3,4,5,8,15], 3))