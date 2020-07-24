#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  a = 0                   # variable a is set to zero
    while (a < n * n * n):  # while loop run while constant n times three is run, giving O(n)
      a = a + n * n         # a is assigned multiplication and addition of constants



b)  sum = 0                 # variable sum is assigned the value of zero
    for i in range(n):      # for loop creates a quasilinear time complexity of O(n log n) because of nested while loop
      j = 1                 # variable j is set to 1
      while j < n:          # while loop runs for every j creating an 0(n)
        j *= 2              # the variable j doubles at each iteration, which cuts the iteration time by 0.5
        sum += 1            # sum is incremented to prevent an infinite loop


c)  def bunnyEars(bunnies):             # definition of bunnyEars defined
      if bunnies == 0:                  # if statement to check on the input value
        return 0                        # return 0 when input is 0

      return 2 + bunnyEars(bunnies-1)   # return produces an O(n), as the time needed will depend on the size of the input

## Exercise II


