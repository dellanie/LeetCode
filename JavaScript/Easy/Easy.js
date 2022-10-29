//length Of Last Word
//spliting the sentence into words.Then finding the length of the last array using -1.
var lengthOfLastWord = function(s) {
    var words = s.trim().split(" ")
    return words[words.length - 1].length     
};

//Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

var mySqrt = function(x) {
    var s1 =Math.sqrt(x)
    return Math.floor(s1)
};
