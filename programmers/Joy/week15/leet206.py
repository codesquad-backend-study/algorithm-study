class Solution:
    def reverseList(self, head: Optional[ListNoteBook]) -> Optional[ListNode]:
        # nodes = []
        # while head != None:
        #     nodes.append(head)
        #     head = head.next
        # nodes.reverse()
        # nodes.append(None)
        # for i in range(len(nodes)-1):
        #     nodes[i].next = nodes[i+1]
        # return nodes[0]

        prev = None
        curr = head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev