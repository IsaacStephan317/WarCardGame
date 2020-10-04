import random

#variables
jack = 11
queen = 12
king = 13
ace = 14

deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king, ace, ace, ace ,ace]
#the commented deck is used to test ties
#deck = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
my_score = 0
opp_score = 0

#the two player lists
my_list = []
opponent_list = []

#functions created
#shuffles the list so that it is random just like a card game
def shuffle():
    random.shuffle(deck)

#
def deal_cards():
    for i in range(52):
        if i%2 == 1:
            my_list.append(deck[i])
        elif i%2 == 0:
            opponent_list.append(deck[i])

#functions that change numerical values to their face card equivalent
def face():
    if my_list[rounds-1] == 11:
        print "Your card is: Jack"
    if my_list[rounds-1] == 12:
        print "Your card is: Queen"    
    if my_list[rounds-1] == 13:
        print "Your card is: King"
    if my_list[rounds-1] == 14:
        print "Your card is: Ace"

def opp_face():
    if opponent_list[rounds-1] == 11:
        print "The opponent's card is: Jack"
    if opponent_list[rounds-1] == 12:
        print "The opponent's card is: Queen"    
    if opponent_list[rounds-1] == 13:
        print "The opponent's card is: King"
    if opponent_list[rounds-1] == 14:
        print "The opponent's card is: Ace"

#had to make a second version that works with the for loop when players tie
def face2():
    if my_list[rounds-(i + 2)] == 11:
        print "Your card is: Jack"
    if my_list[rounds-(i + 2)] == 12:
        print "Your card is: Queen"    
    if my_list[rounds-(i + 2)] == 13:
        print "Your card is: King"
    if my_list[rounds-(i + 2)] == 14:
        print "Your card is: Ace"

def opp_face2():
    if opponent_list[rounds-(i + 2)] == 11:
        print "The opponent's card is: Jack"
    if opponent_list[rounds-(i + 2)] == 12:
        print "The opponent's card is: Queen"    
    if opponent_list[rounds-(i + 2)] == 13:
        print "The opponent's card is: King"
    if opponent_list[rounds-(i + 2)] == 14:
        print "The opponent's card is: Ace"

#another one for maxnumb
def face_max():
    if maxnumb == 11:
        print "The highest card is: Jack"
    if maxnumb == 12:
        print "The highest card is: Queen"    
    if maxnumb == 13:
        print "The highest card is: King"
    if maxnumb == 14:
        print "The highest card is: Ace"
        
#starting the game
play = input("do you want to play? (yes or no)")

    
while play != "yes":
        if play == "no":
            print "That's too bad"
            break
        print "incorrect input!"
        play = input("do you want to play? (yes or no)")

#beginning variables and lists
rounds = 26

ind = 0
tie = []
sum = 0
indices = []

#main code of program
while play == "yes":
    if play == "no":
        print "Thanks for playing!"
        break
    shuffle()
    deal_cards()
    while rounds > 0:
        print""
        if my_list[rounds-1] <= 10:
            print "Your card is" + ": " + str(my_list[rounds-1])
        elif my_list[rounds-1] >= 11:
            face()
        if opponent_list[rounds-1] <= 10:    
            print "The opponent's card is" + ": " + str(opponent_list[rounds-1])
        elif opponent_list[rounds-1] >= 10:
            opp_face()
        #code for player winning
        if my_list[rounds-1] > opponent_list[rounds-1]:
            print "You won the hand!"
            my_score = my_score + 1
        #code for opponent winning    
        if my_list[rounds-1] < opponent_list[rounds-1]:
            print "You lost the hand"
            opp_score = opp_score + 1
        #algorithim for a tie
        if my_list[rounds-1] == opponent_list[rounds-1]:
            if rounds <=3:
                print "It's a tie"
                break
            print "War!"
            #tells players what the cards are and adds each card to a list (tie)
            for i in range(3):
                if my_list[rounds-(i + 2)] <= 10:
                    print "Your card is" + ": " + str(my_list[rounds-(i + 2)])
                elif my_list[rounds-(i + 2)] >= 11:
                    #checks for a face card and prints the name rather than the numerical value
                    face2()
                if opponent_list[rounds-(i + 2)] <= 10:    
                    print "The opponent's card is" + ": " + str(opponent_list[rounds-(i + 2)])
                elif opponent_list[rounds-(i + 2)] >= 11:
                    opp_face2()
                tie.append(my_list[rounds-(i + 2)])
                tie.append(opponent_list[rounds-(i + 2)])
            #the max number is found from the card list and the list is checked for multiple occurances of that max value    
            maxnumb = max(tie)
            for i in tie:
                if i == maxnumb:
                    sum = sum + ind
                    indices.append(ind)
                ind = ind +1    
            #results for all possible outcomes
            if len(indices) == 2 and sum % 2 == 1:
                print "It's a tie"
                rounds = rounds-3
            elif len(indices) == 3:
                if indices == [0, 2, 4]:
                    print "You won the hand!"
                    my_score = my_score + 4
                elif indices == [1, 3, 5]:
                    print "You lost the hand"
                    opp_score = opp_score + 4
                else:
                    print "its a tie"
                rounds = rounds-3    
            elif len(indices) >= 4:
                print "It's a tie"
                rounds = rounds-3
            else:
                if maxnumb <= 10:
                    print "The highest card is: " + str(maxnumb)
                elif maxnumb >= 11:
                    face_max()
                owner = tie.index(maxnumb)
                if owner%2 == 1:
                    print "You lost the hand"
                    opp_score = opp_score + 4
                    rounds = rounds-3
                elif owner%2 == 0:
                    print "You won the hand!"
                    my_score = my_score + 4
                    rounds = rounds-3
            ind = 0        
            sum = 0        
            tie = []
            indices = []
        print""    
        if rounds > 0:
            play_hand = input("Press enter to play the next hand")
        rounds = rounds - 1   
    #determines who won based on score variables    
    if my_score > opp_score:
        print""
        print "You won the game!"
        print""
    elif my_score < opp_score:
        print""
        print "You lost the game"
        print""
    else:
        print ""
        print "It's a tie game!"
        print""
    #asks the user if they want to play again    
    play = input("do you want to play again? (yes or no)")
    while play != "yes":
        if play == "no":
            print ""
            print "Thanks for playing!"
            break
        print "incorrect input!"
        play = input("do you want to play? (yes or no)")
    #resets the values for the lists and variables    
    my_list = []
    opponent_list = []
    rounds = 26
    my_score = 0
    opp_score = 0
