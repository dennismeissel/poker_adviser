class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def __repr__(self):
        return f"Hand({self.cards})"

class Game:
    def __init__(self, num_players, stage, hand, previous_combinations):
        self.num_players = num_players
        self.stage = stage
        self.hand = hand
        self.previous_combinations = previous_combinations

    def __repr__(self):
        return f"Game(num_players={self.num_players}, stage='{self.stage}', hand={self.hand}, previous_combinations={self.previous_combinations})"
