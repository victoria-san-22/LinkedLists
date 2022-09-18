''' Author: Victoria Santos
    Program: linked_list_long.py
    Purpose: This program provides methods for analyzing
    or altering any given linked list. It has methods for
    determining if a given list is sorted, summing a list's
    int values, partitioning a list, returning every 
    fourth node from a given point, and returning a list of
    ordered pairs from two lists.
    Course: CSC 120 FA 001
'''

from list_node import ListNode

def is_sorted(head):
    ''' This function determines if a given linked list
        is sorted in ascending order. 

        Parameters: linked list (head)
        Return Value: True or False for whether or not
        the list is sorted
    '''   
    cur = head

    # none case
    if head is None:
        return 0
    # otherwise
    else:
        while cur.next is not None and cur.val <= cur.next.val:
            cur = cur.next

        if cur.next is None:
            return True
        else:
            return False


def list_sum(head):
    ''' This function takes the int values from a 
        linked list and returns the sum of those
        values.

        Parameters: linked list (head)
        Return Value: int sum
    '''   
    cur = head
    sum = cur.val

    if head is None:
        return 0
    else:
        while cur.next is not None:
            cur = cur.next
            sum += cur.val

    return sum


def partition_list(head):
    ''' This function takes a linked list and partitions
        it into different lists, each with alternating
        values from the original list.

        Parameters: linked list (head)
        Return Value: linked list 1 (head1), linked
        list 2 (head2)
    '''   
    head1 = head
    cur = head
    head2 = cur.next
    cur2 = head2

    while cur is not None and cur2 is not None \
        and cur.next.next is not None:
        cur.next = cur.next.next
        cur2.next = cur2.next.next
        cur = cur.next
        cur2 = cur2.next

    if cur.next is not None:
        cur.next = cur.next.next

    return head1, head2


def accordion_4(head, start_pos):
    ''' This function takes a linked list and returns
        an altered list of every fourth value from
        the given start point.

        Parameters: linked list (head), int start_pos
        Return Value: fourthed linked list (head)
    '''   

    # none case
    if head is None:
        return None

    # starting pointer
    counter = 0
    while counter < start_pos and head.next is not None:
        head = head.next
        counter += 1

    if counter != start_pos:
        head = None
        return head

    # every fourth
    counter = 0
    cur = head
    link_cur = head 
    last_fourth = None
    
    while cur is not None and cur.next is not None:
        cur = cur.next
        counter += 1

        if counter == 3 and cur.next is not None:
            link_cur.next = cur.next
            last_fourth = cur.next
            link_cur = link_cur.next
            cur = cur.next
            counter = 0
        
    last_fourth.next = None
    return head


def pair(list1, list2):
    ''' This function takes two linked lists and returns
        a linked list of tuples. Each tuple contains
        one value from list1 and one from list2 in the
        same orders as their respective lists. 

        Parameters: linked list 1 (head list1), linked
        list 2 (head list2)
        Return Value: linked list of tuples (head)
    '''   

    head = None
    new_cur = head
    cur = list1
    cur2 = list2
    start = 0

    # none case
    if list1 is None or list2 is None:
        return None

    # otherwise
    while cur.next is not None and cur2.next is not None:
        
        tup = (cur.val, cur2.val)
        if start == 0:
            head = ListNode(tup)
            new_cur = head
        else:
            new_cur.next = ListNode(tup)
            new_cur = new_cur.next

        cur = cur.next
        cur2 = cur2.next
        start += 1

    tup = (cur.val, cur2.val)
    new_cur.next = ListNode(tup)

    return head