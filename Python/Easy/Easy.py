#length Of Last Word
#spliting the sentence into words.Then finding the length of the last array using -1.
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.length = s.strip().split()
        track_list=[]
        track_list = self.length
        last_word = track_list[-1]
        return len(last_word)