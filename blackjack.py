import time
from deck import Deck


class Blackjack:
    COLOR_CODES = {
    "black": 0,
    "red": 1,
}
    def __init__(self, num_players, num_decks):
        self.num_players = num_players
        self.num_decks = num_decks
        self.deck = Deck(num_decks)

    def hand_total(self, player_hand):
        total = 0
        for card in player_hand:
            if card.isdigit():
                total += int(card)
            elif card in ('J', 'Q', 'K'):
                total += 10
            elif card == 'A':
                if total >= 11:
                    total += 1
                else:
                    total += 11
        return total

    def show_hand(self, player_hand):
        def make_card(card):
            padding = ' ' * max(0, 3 - len(card))
            card_face = card if card.isdigit() else card.upper()[0]
            card_color = "red" if card_face in "JQK" else "black"
            return f"\033[{30+self.COLOR_CODES[card_color]}m|{padding}{card_face}{padding}|\033[0m"

        cards = [make_card(card) for card in player_hand]
        total = self.hand_total(player_hand)
        print(f"{' '.join(cards)}\n \n Total: {total}")




    def play(self):
        print("Welcome to Blackjack!")
        time.sleep(1)
        while True:
            print(len(self.deck))
            print(f"Suffling {self.num_decks} decks...")
            time.sleep(1)

            self.deck.shuffle()

            print("Dealing cards...")
            time.sleep(1)

            player_hand = [self.deck.deal(), self.deck.deal()]
            dealer_hand = [self.deck.deal(), self.deck.deal()]
            print("Player hand")
            self.show_hand(player_hand)
            time.sleep(1)
            print("Dealer hand")
            self.show_hand(dealer_hand[:1]+["?"])
            time.sleep(1)

            player_total = self.hand_total(player_hand)

            while player_total < 21:
                print("Would you like to hit or stand?")
                choice = input()

                if choice.lower() == "hit":
                    player_hand.append(self.deck.deal())
                    player_total = self.hand_total(player_hand)
                    self.show_hand(player_hand)
                    time.sleep(1)
                    print(f"Your total: {player_total}")
                    time.sleep(1)

                elif choice.lower() == "stand":
                    break

                else:
                    print("Invalid input. Please enter 'hit' or 'stand'.")
                    time.sleep(1)
                    continue

            if player_total > 21:
                print("You bust!")
                time.sleep(1)

            else:
                print(f"Your total: {player_total}")
                print(f"Dealer's total: {self.hand_total(dealer_hand)}")
                time.sleep(1)
                print("Dealer shows his hand!")
                self.show_hand(dealer_hand)
                time.sleep(1)

                while self.hand_total(dealer_hand) < player_total:
                    dealer_hand.append(self.deck.deal())
                    print("Dealer hits")
                    time.sleep(1)
                    print("Dealer hand")
                    self.show_hand(dealer_hand)
                    time.sleep(1)

                if self.hand_total(dealer_hand) > 21:
                    print("Dealer busts! You win!")
                elif player_total > self.hand_total(dealer_hand):
                    print("You win!")
                elif player_total < self.hand_total(dealer_hand):
                    print("You lose!")
                else:
                    print("It's a tie!")
                time.sleep(1)

            print("Would you like to play again?")
            choice = input()

            if choice.lower() != "yes":
                break

        print("Thanks for playing!")
        time.sleep(1)

if __name__ == "__main__":
    game = Blackjack(num_players= 1, num_decks=4)
    game.play()


