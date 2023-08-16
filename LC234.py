class Solution:
    def __init__(self):
        self.left = None
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        return self.traverse(head)

    def traverse(self,right):
        if right is None:
            return True
        res = self.traverse(right.next)
        res = res and (right.val == self.left.val)
        self.left = self.left.next
        return res
