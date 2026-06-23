class Solution:
    def calculate(self, s: str) -> int:
        total = prev = num = i = 0
        op = "+"
        n = len(s)
        while i <= n:
            ch = s[i] if i < n else "+"

            if ch == " ":
                i += 1
                continue
            
            elif ch.isdigit():
                num = num * 10 + int(ch)
            
            else:
                if op == "+":
                    total += prev
                    prev = num
                elif op == "-":
                    total += prev
                    prev = -num
                elif op == "*":
                    prev *= num
                else:
                    if prev < 0 :
                        prev = -(-prev // num)
                    else:
                        prev //= num
                op = ch
                num = 0
            i += 1

        total += prev
        return total
        