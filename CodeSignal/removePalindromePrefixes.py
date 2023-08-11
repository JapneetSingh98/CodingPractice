def solution(s):
    if s == "":
        return ""
    for i in range(len(s)):
        if s[:len(s) - i] == s[len(s)-i-1::-1]:
            if i == len(s) - 1:
                return
            else:
                print("-", s[len(s)-i:])
                return solution(s[len(s)-i:])
            