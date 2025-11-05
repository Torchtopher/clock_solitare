import pydealer
from tqdm import trange
total_wins = 0

def check_win(clock):
    win = True
    for stack in clock:
        if stack.size != 0:
            win = False
    return win
NUM_TRIALS = 100000

for i in trange(NUM_TRIALS):
    deck = pydealer.Deck()
    deck.shuffle(1)

    clock = []   # 0 is center (king), 1 is Ace, going up to
    #print(deck.cards)

    for i in range(13):
        #print(i)
        stack = pydealer.Stack()
        stack.add(deck.deal(4))
        clock.append(stack)
        #print(stack)

    #print(deck.cards)

    running = True
    current_idx = 0 # start at king
    while running:
        card = clock[current_idx].deal(1).cards
        #print()
        #print(type(card))
        if len(card) == 0: # this means no more face down cards in this stack
            win = check_win(clock)
            break
        #print(card[0].value)
        val = card[0].value 
        if val == "Ace":
            current_idx = 1
        elif val == "King":
            current_idx = 0
        elif val == "Jack":
            current_idx = 11
        elif val == "Queen":
            current_idx = 12
        else:
            current_idx = int(val)
    #print(f"You {'won' if win else 'lost'}")
    total_wins += win

print(f"Win percentage {total_wins / NUM_TRIALS}")
print(f"1/13 {round(1/13, 3)}")