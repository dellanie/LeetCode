#length Of Last Word
#spliting the sentence into words.Then finding the length of the last array using -1.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.length = s.strip().split()
        track_list=[]
        track_list = self.length
        last_word = track_list[-1]
        return len(last_word)
#Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

class Solution2:
    def mySqrt(self, x: int) -> int:
        s1 = math.isqrt(x)
        return s1

#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
#https://blog.devgenius.io/leetcode-83-remove-duplicates-from-sorted-list-get-solution-with-images-ddfa56b191f
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
         if head == None or head.next == None:
            return head
         list = head
        
         while(list.next!=None):
             if list.val == list.next.val:
                 list.next = list.next.next
             else:
                 list = list.next
        
         return head