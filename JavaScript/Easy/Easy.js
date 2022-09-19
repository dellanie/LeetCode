//length Of Last Word
//spliting the sentence into words.Then finding the length of the last array using -1.
var lengthOfLastWord = function(s) {
    var words = s.trim().split(" ")
    return words[words.length - 1].length     
};