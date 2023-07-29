# 내장함수 sort() 사용
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    node_list = []
    while cur:
        node_list.append(cur.val)
        cur = cur.next

    node_list.sort()

    cur = head
    for val in node_list:
        cur.val = val
        cur = cur.next

    return head

# 병합정렬 사용
def mergeTwoList(self, list1, list2) -> ListNode:
    if list1 and list2:
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoList(list1.next, list2)

    return list1 or list2

def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not (head and head.next):
        return head

    # 런너 기법(중간 노드를 찾는다)
    half, slow, fast = None, head, head
    while fast and fast.next:
        half = slow
        slow = slow.next
        fast = fast.next.next
    half.next = None

    # 재귀로 모두 분할
    list1 = self.sortList(head)
    list2 = self.sortList(slow)

    # 정렬하며 병합
    return self.mergeTwoList(list1, list2)
