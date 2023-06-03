class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1. 노드를 리스트에 담기
        nodes = []
        while head != None:
            nodes.append(head)
            head = head.next
        # 2. 홀수, 짝수 노드 나누기
        even = [nodes[i] for i in range(0,len(nodes),2)]
        odd = [nodes[i] for i in range(1,len(nodes),2)]

        # 3. 노드 참조 바꾸기
        nodes = even + odd
        nodes.append(None)
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        return nodes[0]