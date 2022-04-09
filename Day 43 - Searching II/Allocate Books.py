"""
Problem Description
Given an array of integers A of size N and an integer B.
The College library has N books. The ith book has A[i] number of pages.
You have to allocate books to B number of students so that the maximum number of pages allocated to a student is minimum.
A book will be allocated to exactly one student.
Each student has to be allocated at least one book.
Allotment should be in contiguous order, for example: A student cannot be allocated book 1 and book 3, skipping book 2.
Calculate and return that minimum possible number.

NOTE: Return -1 if a valid assignment is not possible.


Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 105


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return that minimum possible number.


Example Input
A = [12, 34, 67, 90]
B = 2


Example Output
113


Example Explanation
There are two students. Books can be distributed in following fashion :
1)  [12] and [34, 67, 90]
    Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
2)  [12, 34] and [67, 90]
    Max number of pages is allocated to student 2 with 67 + 90 = 157 pages
3)  [12, 34, 67] and [90]
    Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages
    Of the 3 cases, Option 3 has the minimum pages = 113.
"""

"""
Solution Approach
Here we will solve what has been discussed in the previous hint :

Problem statement: Given a fixed number of pages (V),  how many students do we need?
Solution :
   simple simulation approach
   intially Sum := 0
   cnt_of_student = 0
   iterate over all books:
        If Sum + number_of_pages_in_current_book > V :
                  increment cnt_of_student
                  update Sum
        Else:
                  update Sum
   EndLoop;
  


    fix range LOW, HIGH
    Loop until LOW < HIGH:
            find MID_point
            Is the number of students required to keep the max number of pages below MID < M? 
            IF Yes:
                update HIGH
            Else
                update LOW
    EndLoop;
"""
import math

class Solution:

    def books(self, A, B):

        l, h = max(A), sum(A)
        print(l, h)

        ans = math.inf
        while l <= h:
            maxPages = (l + h) // 2
            pageCount = 0
            child = 1
            for i in range(0, len(A)):
                if pageCount + A[i] > maxPages:
                    child += 1
                    pageCount = 0
                pageCount += A[i]

            if child <= B:
                ans = min(ans, maxPages)
                h = maxPages - 1
            else:
                l = maxPages + 1

        return -1 if ans == math.inf else ans