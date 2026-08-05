#Approach
#Read the weight of the clothes.
#Validate the input:
#If the weight is less than 0, print "INVALID INPUT".
#If the weight is greater than 7000, print "OVERLOADED".
#If the input is valid, determine the washing time based on the weight:
#0 grams → 0 minutes
#1 to 2000 grams → 25 minutes
#2001 to 4000 grams → 35 minutes
#4001 to 7000 grams → 45 minutes
#Print the estimated washing time in the required format:
#Time Estimated: <time> minutes

weight = int(input())

if weight < 0:
    print("INVALID INPUT")
elif weight > 7000:
    print("OVERLOADED")
elif weight == 0:
    print("Time Estimated: 0 minutes")
elif weight <= 2000:
    print("Time Estimated: 25 minutes")
elif weight <= 4000:
    print("Time Estimated: 35 minutes")
else:
    print("Time Estimated: 45 minutes")
