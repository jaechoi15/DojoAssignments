# Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.

from random import randint

def coinToss():
    print "Starting the program..."
    for toss in range (0, 51):
        coin_flip = randint(1,100)
        head_toss = 0
        tail_toss = 0
        if coin_flip > 49:
            head_toss += 1
            print "Attempt #" + str(toss) + ": Throwing a coin..." + "It's heads!" + " ... Got " + str(head_toss) + " head(s) so far and " + str(tail_toss) + " tail(s) so far"
        else:
            tail_toss += 1
            print "Attempt #" + str(toss) + ": Throwing a coin..." + "It's tails!" + " ... Got " + str(head_toss) + " head(s) so far and " + str(tail_toss) + " tail(s) so far"
    print "Ending the program, thank you!"

coinToss()