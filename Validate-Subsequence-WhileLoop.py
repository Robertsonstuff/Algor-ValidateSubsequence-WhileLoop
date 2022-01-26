# while loop - O(n) Time, O(1) space

def ValidateSequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        # loop through if the index of arrIdx is less than the length of the array(8) AND is the seqIdx is less than the length of the sequence(4). Meaning both of the arrIdx and the seqIdx is less than the length of array and sequence. If these values are not the case, return(line11)
        if array[arrIdx] == sequence[seqIdx]: #if first number is found (if 5 == 1) (go to line 9)increment 1 to the next sequence. In this case it isn't so it then goes to (line 10) and add 1 index integer in the array (1 == 1).
            seqIdx += 1 
        arrIdx += 1 #increment 1 sequence
    return seqIdx == len(sequence)
    # this will return a boolean once the while loop has met both requirements on (line 6).

result = ValidateSequence([5,1,22,25,6,-1,8,10],[1,6,-1,10])
print(result)