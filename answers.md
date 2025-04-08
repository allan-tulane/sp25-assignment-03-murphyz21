# CMPS 2200 Assignment 3
## Answers

**Name:**__Zoe Murphy_______________________


Place all written answers from `assignment-03.md` here for easier grading.

**1a)** Given a $N$ dollars, state a greedy algorithm for producing
as few coins as possible that sum to $N$.
    Start with a list of empty coins. 
    When N (the amount of coins) is greater than 0
        Look for the biggest 2^k that is less than or equal to N
        subtract 2^k from N
        add the coin value 2^k to that initial list
    return the list

**1b)** Prove that this algorithm is optimal by proving the greedy
  choice and optimal substructure properties.
    This algorithm has a greedy choice because it's choosing the largest possible coin that doesn't exceed the remaining amount. All the coins are powers of 2 and a smaller combo of coins would require more coins than just taking the largest one, so it's efficient. 
    It has an optimal substructure because taking the largest coin and subtracting it from the total creates a smaller version of the same problem over and over. 

**1c)** What is the work and span of your algorithm?
    O(log(n)) work and O(log n) span

**2a)** You realize the greedy algorithm you devised above doesn't
  work in Fortuito. Give a simple counterexample that shows that the
  greedy algorithm does not produce the fewest number of coins.
    You could have coins that are worth 1, 5, and 7 dollars and you want 10 dollars. 
    The greedy algorithm would do the 7 dollar coin and then three 1 dollar coins. (4 coins total)
    It'd be better to just do two 5 dollar coins.

**2b)** Since you paid attention in Algorithms class, you realize that
  while this problem does not have the greedy choice property it does
  have an optimal substructure property. State and prove this
  property.
    This has optimal substructure because we have to solve the smaller coin problems first. The subproblems have to be solved first. 
    You can like find the minimum coins needed for amount N by adding one coin k to the optimal solution N - k. This shows that N depends on the solutions to the smaller subproblems. 

  **2c)** Use this optimal substructure property to design a
  dynamic programming algorithm for this problem. If you used top-down
  or bottom-up memoization to avoid recomputing solutions to
  subproblems, what is the work and span of your approach?
    You can have a list that looks at the minimum coins needed from 0 - N
    Then for each N, check the coins and update the list with the smallest number of coins needed
    then return the list

    work is O(n*k) because N is like the target amount and k is the number of coins and we're checking each coin for each amount up to N

    span is O(n) cause it's like proportional to the number of amounts N
