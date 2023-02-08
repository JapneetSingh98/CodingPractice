class Solution:
    def countAndSay(self, n: int) -> str:
        output = "1"
        for i in range(2, n + 1):
            n_str = output
            output = ""
            cur = n_str[0]
            count = 0

            for char in n_str:
                if cur == char:
                    count += 1
                else:
                    output = output + str(count) + cur
                    cur = char
                    count = 1

            output = output + str(count) + cur
            print(output)

        return output