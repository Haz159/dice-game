import random
import time
from operator import itemgetter

def validate():
    validated = False
    while validated == False:
        choice = int(input("enter your choice (1 or 2):\n1) Log in\n2) sign up"))
        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            usernames_passwords = []
            file = open("userandpass.txt","r")
            for line in file:
                usernames_passwords.append(line.strip().split(","))
                 
            file.close()
            if [username, password] in usernames_passwords:
                print("Authentication success! you can continue")
                return username
                validated = True
            else:
                print("Error! username or password is incorrect, please try again")
                
        elif choice == 2:
            username = input("enter your desired username")
            password = input("enter your desired psasword")
            file = open("userandpass.txt", "a")
            file.write("\n")
            file.write(username + "," + password)
            file.close()
            print("account made.")

            

                

def play_game(p1_name, p2_name):
    p2_score = 0
    p1_score = 0
    
    for x in range(5):
        round_total = scoring()
        p1_score += round_total
        if p1_score < 0:
            p1_score = 0

        round_total = scoring()
        p2_score += round_total
        if p2_score < 0:
            p2_score = 0
        
        time.sleep(2)
        print("after round", x+1, p1_name, "is on: ", p1_score)
        print("after round", x+1, p2_name, "is on: ", p2_score)

    return p1_score, p2_score


def roll_dice():
    Die1 = random.randint(1, 6)
    Die2 = random.randint(1, 6)

    return Die1, Die2


def scoring():
    die1, die2 = roll_dice()
    score = die1 + die2
    if score % 2 == 0:
        score += 10
    else:
        score -= 5
    
    if die1 == die2:
        die3 = random.randint(1,6)
        score += die3

    return score


def judging(p1_name, p1_score, p2_name, p2_score):
    if p1_score > p2_score:
        return p1_name, p1_score
    elif p2_score > p1_score:
        return p2_name, p2_score
    else:
        winner_name, winner_score = overtime(p1_name, p1_score, p2_name, p2_score)
        return winner_name, winner_score


def overtime(p1_name, p1_score, p2_name, p2_score):
    print('''you will erach roll one dice until one person rolls a dice that is higher 
    than the other persons''')
    
    winner_found = False
    while winner_found == False:
        p1_die = random.randint(1,6)
        p2_die = random.randint(1, 6)
        if p1_die > p2_die:
            return p1_name, p1_score
            winner_found = True
        elif p1_die < p2_die:
            return p2_name, p2_score
            winner_found = True


def winners_file(winner_name, winner_score):
    leaderboard = open("winnersfile.txt", "a")
    leaderboard.write(str(winner_score) + "," + winner_name)
    leaderboard.write("\n")
    print("Your score has been saved")
    leaderboard.close()
    
    leaderboard = open("winnersfile.txt", "r")
    scores = leaderboard.readlines()
    unsortedScores = []
    for lines in scores:
        details = lines.strip("\n") 
        details = details.split(",")
        details[0] = int(details[0])
        unsortedScores.append(details)
    unsortedScores.sort(key = itemgetter(0), reverse=True)
    print("------------------------------------------------------------------")
    print("                      The top five scores are:                    ")
    print("------------------------------------------------------------------")
    print("1. "+str(unsortedScores[0][0]),"done by",str(unsortedScores[0][1]))
    print("2. "+str(unsortedScores[1][0]),"done by",str(unsortedScores[1][1]))
    print("3. "+str(unsortedScores[2][0]),"done by",str(unsortedScores[2][1]))
    print("4. "+str(unsortedScores[3][0]),"done by",str(unsortedScores[3][1]))
    print("5. "+str(unsortedScores[4][0]),"done by",str(unsortedScores[4][1]))

    leaderboard.close()



def main():
    print("-------WELCOME TO THE DICE GAME--------")
    print("-----------------USER 1----------------")
    p1_name = validate()
    print("-----------------USER 2----------------")
    p2_name = validate()

    p1_score, p2_score = play_game(p1_name, p2_name)

    winner_name, winner_score = judging(p1_name, p1_score, p2_name, p2_score)

    print(winner_name, "won with a score of: ", winner_score)

    winners_file(winner_name, winner_score)



main()
