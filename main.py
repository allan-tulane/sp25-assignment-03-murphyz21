import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    # If length of first string is empty, return length of second string
    if (S == ""):
        return (len(T))
    # If second string is empty, return length of first string
    elif (T == ""):
        return (len(S))
    else:
        # If first characters match, move to the next character
        if (S[0] == T[0]):
            return (MED(S[1:], T[1:]))
        # Else, take the minimum of the three possible options and add 1 for the operation
        else:
            return (1 + min(MED(S, T[1:]), MED(S[1:], T)))

def fast_MED(S, T, MED={}):
    # if result is like already there just return it
    if (S, T) in MED:
        return MED[(S, T)]
    # If T is empty return length of S
    if T == "":
        return len(S)
    # If S is empty return length of T
    if S == "":
        return len(T)

    # If the first characters match, move to next character
    elif S[0] == T[0]:
        MED[(S, T)] = fast_MED(S[1:], T[1:], MED)
    # Else calculate cost for insertion and deletion and take minimum
    else:
        insert_cost = fast_MED(S, T[1:], MED)  
        delete_cost = fast_MED(S[1:], T, MED)  
        
        # Store the result: add 1 for the operation (insert or delete) and take the minimum cost
        MED[(S, T)] = 1 + min(insert_cost, delete_cost)
    # Return stored result for the pair
    return MED[(S, T)]

def fast_align_MED(S, T, MED={}):
    # TODO - keep track of alignment
    # if result is already compute
    if (S, T) in MED:
        return MED[(S, T)]

    # If T is empty add S with -
    if T == "":
        MED[(S, T)] = (S, "-" * len(S))
        return MED[(S, T)]
    # If S is empty add T with -
    elif S == "":
        MED[(S, T)] = ("-" * len(T), T)
        return MED[(S, T)]

    # If first characters match, just align and move to the next characters
    if S[0] == T[0]:
        align_S, align_T = fast_align_MED(S[1:], T[1:], MED)
        MED[(S, T)] = (S[0] + align_S, T[0] + align_T)
    # Else, Calculate the alignment for inserton and deletion
    else:
        insertion_S, insertion_T = fast_align_MED(S, T[1:], MED)
        deletion_S, deletion_T = fast_align_MED(S[1:], T, MED)

        # Calculate lengths of insertion and deletions
        insertion_C = 1 + len(insertion_S)
        deletion_C = 1 + len(deletion_S)

        # If insertion is cheaper or equal add the gap to S and move forward in T
        if insertion_C <= deletion_C:
            MED[(S, T)] = ("-" + insertion_S, T[0] + insertion_T)
        # Else, do it the otheer way (add gap to T and move forward in S)
        else:
            MED[(S, T)] = (S[0] + deletion_S, "-" + deletion_T)
    # Return final alignment
    return MED[(S, T)]