import argparse
import random

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("insight", type=int, help="Insight check rolled by player.")
    parser.add_argument("intimidation", type=int, help="Intimidation check rolled by player.")
    parser.add_argument("deception", type=int, help="Deception check rolled by player.")
    parser.add_argument("hours", type=int, help="Number of hours to gamble.")
    parser.add_argument("gold", type=int, help="Amount of gold being bet.")
    parser.add_argument("-gph", type=int, default=25, help="Gold that is reserved for bet per hour. Default is 25.")
    parser.add_argument("-m", "--modifier", type=int, default=5, help="Difficulty modifier for location. Default is 5")
    args = parser.parse_args()
    return args

def is_roll_success(roll, dc):
    if (roll >= dc):
        print("Success!")
        return True
    print("Fail ... ")
    return False

def determine_gold_earned(success, gold_bet):
    print ("Total successes: {0}".format(str(success)))
    if (success == 0):
        return -2 * gold_bet
    if (success == 1):
        return -1 * gold_bet / 2
    if (success == 2):
        return gold_bet + gold_bet / 2
    if (success == 3):
        return gold_bet * 2

def main():
    args = get_args()
    total_betting_gold = args.gold
    for i in range(args.hours):
        print("Gambling hour: {0}".format(str(i)))
        insightDc = args.modifier + random.randint(1,10) + random.randint(1,10)
        intimidationDc = args.modifier + random.randint(1,10) + random.randint(1,10)
        deceptionDc = args.modifier + random.randint(1,10) + random.randint(1,10)
        success = 0
        print("Insight roll: {0}, Insight DC: {1}".format(str(args.insight), str(insightDc)))
        success = success + 1 if is_roll_success(args.insight, insightDc) else success
        print("Intimidation roll: {0}, Insight DC: {1}".format(str(args.intimidation), str(intimidationDc)))
        success = success + 1 if is_roll_success(args.intimidation, intimidationDc) else success
        print("Deception roll: {0}, Insight DC: {1}".format(str(args.deception), str(deceptionDc)))
        success = success + 1 if is_roll_success(args.deception, deceptionDc) else success
        gold_earned = determine_gold_earned(success, args.gph)
        print("Gold earned from the hour: {0}".format(str(gold_earned)))
        total_betting_gold += gold_earned
        print ("Total gold: {0}".format(str(total_betting_gold)))
    print("Final result from gambling: {0}".format(str(total_betting_gold)))

if __name__ == "__main__":
    main()