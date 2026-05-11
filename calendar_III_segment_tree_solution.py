from collections import Counter

class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def update(self, start: int, end: int, left: int = 0, right: int = 100, idx: int = 1) -> None: #[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]
        #print("start =>", start, "end =>", end, "left =>", left, "right =>", right, "idx =>", idx)
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            print("start =>", start, "left =>", left, "right =>", right, "end =>", end)
            self.vals[idx] += 1
            self.lazy[idx] += 1
            #print("self.val[idx] =>", self.vals[idx], "self.lazy[idx] =>", self.lazy[idx], "idx =>", idx, )
            #print("vals_map =>", self.vals)
            #print("lazy_map =>", self.lazy)
        else:
            mid = (left + right)//2
            self.update(start, end, left, mid, idx*2)
            self.update(start, end, mid+1, right, idx*2 + 1)
            #print("idx =>", idx, "2 * idx =>", 2*idx, "2*idx + 1 =>", 2*idx + 1, "self.val[2*idx] =>", self.vals[2*idx], "self.val[2*idx + 1] =>", self.vals[2*idx + 1], "self.lazy[idx] =>", self.lazy[idx])
            #print("start =>", start, "left =>", left, "right =>", right, "end =>", end)
            self.vals[idx] = self.lazy[idx] + \
                max(self.vals[2*idx], self.vals[2*idx+1])
            #print("vals_map =>", self.vals)
            #print("lazy_map =>", self.lazy)

    def book(self, start: int, end: int) -> int: #[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]
        self.update(start, end-1)
        return self.vals[1]

result = MyCalendarThree()
print(result.book(10,20))
print(result.book(50,60))
print(result.book(10,40))
print(result.book(5,15))
print(result.book(5,10))
print(result.book(25,55))


