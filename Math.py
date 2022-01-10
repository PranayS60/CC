import math


class Math:
    def countDigits(self, num):
        count = 0

        while num > 0:
            num = int(num / 10)
            count += 1
        return count

    def quadraticRoots(self, a, b, c):
        res = []
        d = b ** 2 - 4 * a * c
        if d < 0:
            res.append(-1)
        else:
            D = math.sqrt(d)
            res.append((-b + D)/(2*a))
            res.append((-b - D)/(2*a))
        return res

    def greyConverter(self, n):
        ##Your code here
        bs = bin(n)
        bs = bs[2:]
        res = 0
        for i, bit in enumerate(bs):
            if i == 0:
                res = int(bit)
                continue
            res = res * 2 + (int(bit) ^ int(bs[i - 1]))
        return res
