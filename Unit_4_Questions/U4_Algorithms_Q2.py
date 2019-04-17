# Write a recursive function called repeatStrings(string, num) that returns a concatenation of the string repeated num
# times. If num = 0, the function should return an empty string


def repeatStrings(string, num):
    if num == 0:
        return ""
    if num > 0:
        return repeatStrings(string, num - 1) + string



print(repeatStrings("Hello", 0))
print(repeatStrings("Hello", 8))
