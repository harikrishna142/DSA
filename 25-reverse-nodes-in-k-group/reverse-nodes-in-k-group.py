# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverseLinkedList(head, k):
            prev, curr = None, head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group_start = group_end.next
            group_end.next = None
            reversed_group_start = reverseLinkedList(group_start, k)

            prev_group_end.next = reversed_group_start
            group_start.next = next_group_start

            prev_group_end = group_start
            length -= k

        return dummy.next