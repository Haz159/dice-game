import random

def validate():
    validated = False
    while validated == False:
        username = input("enter your username")
        password = input("enter your password")
        userpass_list = []

        file = open("userandpass.txt", "r")

        for line in file:
            userpass_list.append(line.strip().split(","))

        if [username, password] in userpass_list:
            print("you can continue")
            validated = True
        else:
            print("error: your username and password do not match")

        file.close()


def play_game(p1_name, p2_name):
    for x in range(5):
        round_total = scoring()
        p1_score = p1_score + round_total

        round_total = scoring()
        p2_score = p2_score + round_total
        print("after round", x, p1_name, "scored: ", p1_score)
        print("after round", x, p2_name, "scored: ", p2_score)

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

    if score < 0:
        score = 0

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
    winners_list = []
    f = open("winnersfile.txt", "r+a")
    for line in f:
        winners_list.append(line.strip().split(","))
        winners_list.sort(key=lambda x: x[1])
    
    winners_list.append(winner_name, ",", winner_score)
    for x in winners_list:
        f.write(x)

    f.close()
    return winners_list

def main():
    p1_name = validate()
    print("now user 2")
    p2_name = validate()

    p1_score, p2_score = play_game(p1_name, p2_name)

    winner_name, winner_score = judging(p1_name, p1_score, p2_name, p2_score)

    print(winner_name, "won with a score of: ", winner_score)

    winners = winners_file(winner_name, winner_score)
    for x in range(5):
        print("the top 5 are: ", winners[x])



main()
