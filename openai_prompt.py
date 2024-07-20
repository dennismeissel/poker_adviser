import poker_analysis

class OpenAIPrompt:
    def __init__(self, game):
        self.game = game

    def generate_prompt(self):
        prompt = (
            f"You are an expert poker player and mathematician. Analyze the following game situation and determine "
            f"the action (raise, call, fold) that is most likely to lead to a win.\n\n"
            f"Number of players: {self.game.num_players}\n"
            f"Stage of the hand: {self.game.stage}\n"
            f"Your hand: {', '.join(map(str, self.game.hand.cards))}\n"
            f"Previous combinations: {self.format_previous_combinations(self.game.previous_combinations)}\n\n"
            f"Please provide a detailed explanation of your recommendation."
        )
        return prompt

    def format_previous_combinations(self, previous_combinations):
        formatted_combinations = []
        for hand in previous_combinations:
            formatted_combinations.append(', '.join(map(str, hand.cards)))
        return '; '.join(formatted_combinations)
