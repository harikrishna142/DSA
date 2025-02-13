class Solution:
    def rotateRight(self, head, k):
        if not head:
            return None
        n, temp = 1, head
        while temp.next:
            n += 1
            temp = temp.next
        k %= n
        temp.next = head
        for _ in range(n - k):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        return new_head