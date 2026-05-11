from _pyrepl.commands import end
from typing import List

class Node:
    def __init__(self, start: int, end: int, X: List[int]) -> None:
        self.start, self.end = start, end
        self.total = 0
        self.count = 0
        self._left = None
        self._right = None
        self.X = X

    @property
    def mid(self):
        return (self.start + self.end) // 2

    @property
    def left(self):
        print("left_function", "count =>", self.count, "total =>", self.total)
        self._left = self._left or Node(self.start, self.mid, self.X)
        return self._left

    @property
    def right(self):
        print("right_function", "count =>", self.count, "total =>", self.total)
        self._right = self._right or Node(self.mid, self.end, self.X)
        return self._right

    def update(self, i: int, j: int, val: int, des) -> int:
        print("update_function", "start =>", self.start, "end =>", self.end, "val =>", val, "i =>", i, "j =>", j)
        if i >= j: return 0
        if self.start == i and self.end == j:
            print("update_function", "count =>", self.count, "val =>", val)
            self.count += val
        else:
            self.left.update(i, min(self.mid, j), val, "left")
            self.right.update(max(self.mid, i), j, val, "right")

        if self.count > 0:
            print("update_function", "end =>", self.end, "start", self.start, "count =>", self.count)
            self.total = self.X[self.end] - self.X[self.start]
            print("update_function", "total =>", self.total, "des =>", des)
        else:
            print("update_function", "des =>", des, "self.left.total =>", self.left.total, "self.right.total =>", self.right.total, "count =>", self.count)
            self.total = self.left.total + self.right.total
            print("update_function", "total =>", self.total, "des =>", des, "self.left.total =>", self.left.total, "self.right.total =>", self.right.total)

        return self.total


class Solution: #[[0,0,2,2],[1,0,2,3],[1,0,3,1]]
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 1, -1
        events = []

        X = set()
        for x1, y1, x2, y2 in rectangles:
            if (x1 < x2) and (y1 < y2):
                events.append((y1, OPEN, x1, x2))
                events.append((y2, CLOSE, x1, x2))
                X.add(x1)
                X.add(x2)
        events.sort()

        X = sorted(X)
        print("X =>", X)
        x_index = {x: i for i, x in enumerate(X)}
        print("X_index =>", x_index)
        active = Node(0, len(X) - 1, X)
        ans = 0
        cur_x_sum = 0
        cur_y = events[0][0]
        print("events =>", events)

        for y, typ, x1, x2 in events:
            ans += cur_x_sum * (y - cur_y)
            #print("ans =>", ans, "x1 =>", x1, "x2 =>", x2)
            cur_x_sum = active.update(x_index[x1], x_index[x2], typ, des = "start")
            print("cur_x_sum =>", cur_x_sum)
            cur_y = y

        return ans % (10 ** 9 + 7)

result = Solution()
print(result.rectangleArea([[0,0,2,2],[1,0,2,3],[1,0,3,1]]))