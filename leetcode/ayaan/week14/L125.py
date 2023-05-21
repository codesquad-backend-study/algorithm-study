def is_palindrome(s):
    alphabet_string = ""
    s = s.lower()
    for ch in s:
        if ch.isalpha() or ch.isnumeric():
            alphabet_string += ch
    if alphabet_string == alphabet_string[::-1]:
        print("true")
    else:
        print("false")

import collections
def is_palindrome2(s):
    str_list = collections.deque()
    for ch in s:
        if ch.isalnum():
            str_list.append(ch.lower())

    while len(str_list) > 1:
        if str_list.popleft() != str_list.pop():
            return False
    return True

import re
def is_palindrome3(s):
    s = re.sub("[^0-9A-z]", "", s)
    s = s.lower()

    return s == s[::-1]

is_palindrome3("A man, a plan, a canal: Panama")
