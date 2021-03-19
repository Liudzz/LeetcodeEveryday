# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head) :
        pre = None
        mid = head
        next = mid.next
        while (mid != None):
            mid.next = pre
            pre = mid
            mid = next
            if next == None:
                return pre
            next = mid.next

    # class Solution:
#     def reverseList(head) :
#         if head == None:
#             return
#         pre = None
#         mid = head
#         a = head
#         while(mid != None):
#             a = mid
#             temp = mid.next
#             mid.next = pre
#             pre = mid
#             mid = temp
#         return a

if __name__ == "__main__":
    head = ListNode(1)
    a = ListNode(2)
    b = ListNode(3)
    head.next = a
    a.next = b
    i = head
    while (i != None):
        print(i.val)
        i = i.next


    p = Solution.reverseList(head)
    i = p
    while(i!=None):
        print(i.val)
        i=i.next
# class Solution:
#     def reverseList(head) :
#         if head == None:
#             return
#         pre = None
#         mid = head
#         a = head
#         while(mid != None):
#             a = mid
#             temp = mid.next
#             mid.next = pre
#             pre = mid
#             mid = temp
#         return a
