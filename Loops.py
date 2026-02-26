# Loops are a way to repeat code right away.
# loops will continue to run until the condition is false. While true, the loop will continue to run.\
laps = 1
endRace = 6

while laps <= endRace:
    print("I am in in the race on lap ", laps + 1)
    laps = laps + 1
if laps == 3:
    print("I am halfway there")
laps = laps + 1
print("I have finished the race")
counter = 0
list = ["Apple", "Banana", "Pear", "Orange"]
while counter < len(list):
    print(list[counter])
    counter = counter + 1
print ("end of list")