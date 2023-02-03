class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        LIMIT = 2147483648
        negative = False
        if (dividend <= 0 and divisor > 0) or (dividend >= 0 and divisor < 0):
            negative = True
        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        output = 0
        stack = [(1, divisor)]
        print(stack[-1])
        while stack[-1][1] < dividend and count < 20:
            stack.append((stack[-1][0] + stack[-1][0], stack[-1][1] + stack[-1][1]))
            print(stack[-1])
            count += 1
        print(stack)

        cur = 0
        while len(stack) > 0 and cur < dividend:
            print(cur)
            if cur + stack[-1][1] <= dividend:
                output += stack[-1][0]
                cur += stack[-1][1]
            else:
                stack.pop()
            if output >= LIMIT - 1:
                break

        if negative:
            if output > LIMIT:
                return 0 - LIMIT
            return 0 - output
        if output > LIMIT - 1:
            return LIMIT - 1
        return output