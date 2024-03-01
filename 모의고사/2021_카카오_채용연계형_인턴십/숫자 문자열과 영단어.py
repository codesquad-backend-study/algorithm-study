def solution(s):
    number_dict = {"zero": '0', "one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8',
                   "nine": '9'}

    buf = ""
    ans = ""
    for ch in s:
        if ch.isdigit():
            ans += ch
        else:
            buf += ch

        if buf in number_dict:
            ans += number_dict[buf]
            buf = ""

    return int(ans)
