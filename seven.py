#Approach
#Initialize the jar with 10 candies (maximum capacity).
#Read the number of candies requested by the customer.
#Validate the input:
#If the requested candies are less than or equal to 0 or greater than the available candies, print "INVALID INPUT" and display the current number of candies.
#Otherwise:
#Deduct the requested candies from the jar.
#Display the number of candies sold.
#After the sale, if the remaining candies are less than or equal to 5, refill the jar to its maximum capacity (10 candies).
#Display the updated number of candies available in the jar.

capacity = 10
minimum = 5
candies = capacity
order = int(input())
if order <= 0 or order > candies:
  print("Invalid Input")
  print("Number of candies left:", candies)
else:
  candies -= order
  print("Mumber of candies sold:" , order)
  if candies <= minimum:
    candies = capacity
  print("Number of candies left:", candies)
