def clear() -> None:
    """Clear the terminal."""
    print("\033[H\033[2J", end="", flush=True)
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidder = {}
left = True


def winner_finder(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        



while left:
    name = input("Enter your name: ")
    bid = int(input("Enter your bidding amout: $"))
    bidder[name] = bid
    wanna_continue = input("Is any bidder left? type 'yes' or 'no' ")
    if wanna_continue == "no":
        left = False
        winner_finder(bidder)
    elif wanna_continue == 'yes':
        clear()


        



