print("Let's play 'Rock-Paper-Scissor Game'")

#get input from user 
print("1. Rock\n2. Paper\n3. Scissior")

score1 = 0
score2 = 0

x="yes"
while(x != "no"):
    player1 = int(input("Player 1 \nPlease enter choice: "))

    player2 = int(input("Player 2 \nPlease enter choice: "))

    if(player1 < 1 or player1 > 3):
        print("Invalid choice of player 1")
    elif(player2 < 1 or player2 > 3):
        print("Invalid choice of player 2")
    elif(player1 == player2):
        print("No one won")
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 1 and player2 == 2):
        print("Congratulations! Player 2 won")
        score2 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 1 and player2 == 3):
        print("Congratulations! Player 1 won")
        score1 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 2 and player2 == 1):
        print("Congratulations! Player 2 won")
        score2 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 2 and player2 == 3):
        print("Congratulations! Player 2 won")
        score2 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 3 and player2 == 1):
        print("Congratulations! Player 1 won")
        score1 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
    elif(player1 == 3 and player2 == 2):
        print("Congratulations! Player 2 won")
        score2 += 1
        print("Player 1 score: ",score1)
        print("Player 2 score: ",score2)
        
    print("Do you want to continue the game?")

    x = input("Enter 'yes' or 'no': ")
    x = x.lower()
    if(x == "no"):
        print("Player 1 final score: ",score1)
        print("Player 2 final score: ",score2)
