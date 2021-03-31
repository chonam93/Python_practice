def is_palindrome(word):
    check = []
    for i in range(len(word)):
        if word[i] == word[len(word) - i - 1]:
            check += "0"
        else:
            check += "1"

    total = 0
    for i in check:
        check_num = int(i)
        total += check_num

    if total == 0:
        return True
    else:
        return False
# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))