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
