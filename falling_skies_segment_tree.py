class SegmentTree(object):
    def __init__(self, N, update_fn, query_fn):
        self.N = N
        self.H = 1
        while 1 << self.H < N:
            self.H += 1

        self.update_fn = update_fn
        self.query_fn = query_fn
        self.tree = [0] * (2 * N)
        self.lazy = [0] * N

    def _apply(self, x, val):#[[1,2],[2,3],[6,1]]
        self.tree[x] = self.update_fn(self.tree[x], val)
        print("apply_function =>", "tree =>", self.tree, "x =>", x, "val =>", val)
        if x < self.N:
            self.lazy[x] = self.update_fn(self.lazy[x], val)
            print("apply_function =>", self.lazy, "x =>", x, "val =>", val)

    def _pull(self, x):#[[1,2],[2,3],[6,1]]
        while x > 1:
            x //= 2
            self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2 + 1])
            self.tree[x] = self.update_fn(self.tree[x], self.lazy[x])
            print("pull_function =>", "tree =>", self.tree, "x =>", x, "self.lazy[x] =>", self.lazy[x])

    def _push(self, x):#[[1,2],[2,3],[6,1]]
        for h in range(self.H, 0, -1):
            y = x >> h
            print("push_function =>", "y =>", y, "x =>", x, "h =>", h, "self.lazy[y] =>", self.lazy[y])
            if self.lazy[y]:
                self._apply(y * 2, self.lazy[y])
                self._apply(y * 2+ 1, self.lazy[y])
                self.lazy[y] = 0

    def update(self, L, R, h):#[[1,2],[2,3],[6,1]]
        L += self.N
        R += self.N
        print("update_function","L =>", L, "R =>", R)
        L0, R0 = L, R
        while L <= R:
            if L & 1:
                print("update_function","L =>", L, "h =>", h)
                self._apply(L, h)
                L += 1
            if R & 1 == 0:
                print("update_function","R =>", R, "h =>", h)
                self._apply(R, h)
                R -= 1
            L //= 2; R //= 2
        self._pull(L0)
        self._pull(R0)

    def query(self, L, R):#[[1,2],[2,3],[6,1]]
        L += self.N
        R += self.N
        print("query function =>","L =>", L, "R =>", R)
        self._push(L); self._push(R)
        ans = 0
        while L <= R:
            if L & 1:
                print("query function =>","L =>", L, "tree =>", self.tree)
                ans = self.query_fn(ans, self.tree[L])
                L += 1
            if R & 1 == 0:
                print("query function =>", "R =>", R, "tree =>", self.tree)
                ans = self.query_fn(ans, self.tree[R])
                R -= 1
            L //= 2; R //= 2
        return ans

class Solution(object): #[[1,2],[2,3],[6,1]]
    def coord (self, positions):
        coords_set = set()
        for (left, right) in positions:
            l = left
            r = left + (right - 1)
            coords_set.add(l)
            coords_set.add(r)
        coords = sorted(coords_set)
        index = {v: i for i, v in enumerate(coords)}
        print("index =>", index)
        return index

    def fallingSquares(self, positions):
        #Coordinate compression
        index = self.coord(positions)

        tree = SegmentTree(len(index), max, max)
        best = 0
        ans = []
        for left, size in positions:
            L, R = index[left], index[left + size - 1]
            s = tree.query(L, R)  # query once, store it
            print("tree.query(L, R) =>", s)
            h = s + size
            tree.update(L, R, h)
            best = max(best, h)
            ans.append(best)

        return ans

result = Solution()
print(result.fallingSquares([[1,2],[2,3],[6,1]]))