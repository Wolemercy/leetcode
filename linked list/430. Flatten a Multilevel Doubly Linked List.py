# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        
        #edge case
        if not head:
            return head
        #use a stack; first in last out
        stack = [head]
        
        #create dummy node which will serve as flattened node
        dummy = Node()
        listNode = dummy
        temp = None
        while stack:
            node = stack.pop()
                
            if node.next:
                stack.append(node.next)

            if node.child:
                stack.append(node.child)
                node.child = None
            
            listNode.next = node
            listNode = listNode.next
            listNode.prev = temp
            
            temp = node
            
        return dummy.next
            
        
        
        
