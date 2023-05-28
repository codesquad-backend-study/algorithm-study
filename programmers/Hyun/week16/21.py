# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        while list1 != None:
            nodes.append((list1.val, list1))
            list1 = list1.next

        while list2 != None:
            nodes.append((list2.val, list2))
            list2 = list2.next

        nodes.sort(key=lambda x: x[0])

        if not nodes:
            return None

        head = nodes[0][1]
        tmp = nodes[0][1]
        for _, node in nodes[1:]:
            tmp.next = node
            tmp = tmp.next

        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val):                # list1 이 가리키는 노드는 무조건 작은 값이다.
            list1, list2 = list2, list1

        if list1:                                                       # 재귀 종료조건 : list1 이 None인 경우 재귀함수의 호출이 끝난다.
            list1.next = self.mergeTwoLists(list1.next, list2)              # list1.next를 재귀적으로 정한다.

        return list1                                                    # 현재 list1 이 가리키는 (작은 값) 노드를 반환한다.
