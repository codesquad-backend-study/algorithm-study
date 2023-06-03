class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 1. 노드를 리스트에 담기
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
        # 2. 리스트 뒤집기
        left = left - 1
        head = nodes[:left]
        tmp = nodes[left:right]
        tail = nodes[right:]
        tmp.reverse()

        nodes = head + tmp + tail
        # 3. 노드 참조 바꾸기
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]