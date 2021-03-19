# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(head,left: int, right: int) :
        i = 1
        p = head
        leftbefore,leftdata,rightdata,rightafter = None, None, None, None
        while p != None:
            if i == left - 1:
                leftbefore = p
            elif i == left:
                leftdata = p
            elif i== right:
                rightdata = p
            p = p.next
            i += 1
        if rightdata == None:
            rightafter = None
        else:
            rightafter = rightdata.next
        rightdata.next = None
        leftdata,rightdata = reverseList(leftdata)
        leftbefore.next = leftdata
        rightdata.next = rightafter
        return head



def reverseList(head):
    if head == None:
        return
    pre = None
    mid = head
    a = head
    while(mid != None):
        a = mid
        temp = mid.next
        mid.next = pre
        pre = mid
        mid = temp
    return a,head
