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

//Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
//https://javascript.plainenglish.io/removing-duplicates-from-a-sorted-linked-list-c9e0e62d2c96
var deleteDuplicates = function(head) {
    //set current node to be the head of the list
    let current = head;
    //run until we are at the end of the list
    while(current !== null && current.next !== null){
        //checks to see if the current value and the next value are the same
        if (current.val === current.next.val){
            //skips over the dupicate and the next value becomes 2x next
            current.next = current.next.next
            //current value and the next value are not the same
        }else{
            //moves to the next node on the list to run through tthe next while again
            current = current.next
        }
    }
    //return linked list with no duplicates
    return head
};