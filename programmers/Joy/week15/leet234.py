from tkinter.tix import ListNoteBook
from typing import Optional
from collections import deque

class Solution:
    def isPalindrome(self, head: Optional[ListNoteBook]) -> bool:

        nums = []
        curr = head

        while curr != None:
            nums.append(curr.val)
            curr = curr.next

        nums = deque(nums)

        while len(nums) > 1 :
            if nums.popleft() == nums.pop():
                continue
            else:
                return False
        return True