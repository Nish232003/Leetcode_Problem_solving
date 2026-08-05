# Approach

#Read the oxygen levels of all 3 trainees for 3 rounds (total 9 inputs).
#Validate each oxygen value.
#If any value is less than 1 or greater than 100, print "INVALID INPUT" and terminate.
#Calculate the average oxygen level of each trainee over the three rounds.
#Round each average value to the nearest integer.
#Find the highest average oxygen level.
#If the highest average is less than 70, print "All trainees are unfit".
#Otherwise, print the trainee number(s) whose average oxygen level is equal to the highest average.

totals = [0, 0, 0]

for i in range(9):
    oxygen = int(input())

    if oxygen < 1 or oxygen > 100:
        print("INVALID INPUT")
        exit()

    totals[i % 3] += oxygen

averages = []

for total in totals:
    averages.append(round(total / 3))

maximum = max(averages)

if maximum < 70:
    print("All trainees are unfit")
else:
    for i in range(3):
        if averages[i] == maximum:
            print("Trainee Number :", i + 1)
