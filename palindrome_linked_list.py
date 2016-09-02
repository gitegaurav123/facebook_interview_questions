# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def reverse_linked_list(head):
    if head == None:
        return None
    prev = None
    current = head
    nextt = head.next
    while(nextt):
        current.next = prev
        prev = current
        current = nextt
        nextt = nextt.next
    current.next = prev
    return current

def print_linked_list(head):
    current = head
    while(current):
        print current.val, '->',
        current = current.next
    print None

def cut_linked_list_in_half(head):
    # print 'Cutting the linked_list.'
    if head == None or head.next == None:
        print 'Head or head.next is None'
        return head,head
    elif head.next.next == None:
        temp = head.next
        head.next = None
        return head,temp
    else:
        fast = head
        slow = head
        not_done = True
        while(not_done):
            print fast.val, slow.val
            fast = fast.next.next
            if fast.next == None:
                temp = slow.next
                slow.next = None
                slow = temp.next
                not_done = False
            elif fast.next.next == None:
                slow = slow.next
                temp = slow.next
                slow.next = None
                slow = temp
                not_done = False
            else:
                slow = slow.next
        return head, slow
        
def similar_linked_list(head1,head2):
        if head1 == head2 == None:
            return True
        current1 = head1
        current2 = head2
        while(True):
            # print current1.val, current2.val
            if head1 == None and head2 != None:
                return False
            elif head1 != None and head2 == None:
                return False
            elif current1.val == current2.val:
                    current1 = current1.next
                    current2 = current2.next
                    if current1 == None and current2 == None:
                        return True

            else:
                return False
        
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        # print_linked_list(head)
        head1, head2 = cut_linked_list_in_half(head)
        # print_linked_list(head1)
        # print_linked_list(head2)
        head2 = reverse_linked_list(head2)
        return similar_linked_list(head1, head2)
        
