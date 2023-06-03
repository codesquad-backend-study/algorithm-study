class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 노드를 리스트에 담기
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
        # 2. 노드 순서 바꾸기
        if len(nodes) >= 2:
            for i in range(0,len(nodes)-1,2):
                tmp = nodes[i]
                nodes[i] = nodes[i+1]
                nodes[i+1] = tmp
        # 3. 노드 참조 바꾸기
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]