import os
import random
import json
import logging
from dotenv import load_dotenv
from poker_analysis import Card, Hand, Game
from openai_prompt import OpenAIPrompt
from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Load the OpenAI API key from the .env file
load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

class RandomGameGenerator:
    def __init__(self):
        self.suits = ['hearts', 'diamonds', 'clubs', 'spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.stages = ['pre-flop', 'flop', 'turn', 'river']

    def generate_random_hand(self):
        cards = random.sample([Card(rank, suit) for rank in self.ranks for suit in self.suits], 2)
        return Hand(cards)

    def generate_random_previous_combinations(self):
        previous_combinations = [
            Hand(random.sample([Card(rank, suit) for rank in self.ranks for suit in self.suits], 2))
            for _ in range(random.randint(1, 5))
        ]
        return previous_combinations

    def generate_random_game(self):
        num_players = random.randint(2, 9)
        stage = random.choice(self.stages)
        hand = self.generate_random_hand()
        previous_combinations = self.generate_random_previous_combinations()
        return Game(num_players, stage, hand, previous_combinations)

class OpenAICaller:
    def __init__(self, game):
        self.game = game

    def call_openai(self):
        prompt_generator = OpenAIPrompt(self.game)
        prompt = prompt_generator.generate_prompt()

        # Define the prompt template
        prompt_template = PromptTemplate(
            template="""You are an assistant that analyzes poker games.
                        Here is the game information: {game_info}
                        Please provide a concise and clear analysis of the game.
                        After the analysis, provide a decision code for the action to be taken (e.g., call, raise, fold).
                        The answer must finish with the format "decision_code:x", where x is the code.""",
            input_variables=["game_info"]
        )
        
        # Format the prompt with the game information
        prompt_data = prompt_template.format(game_info=prompt)
        
        # Log the prompt data
        logging.info(f"Prompt data sent to OpenAI: {prompt_data}")

        # Using LangChain to create the OpenAI LLM and call it
        llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")
        response = llm.invoke(prompt_data).content
        
        return response

def main():
    random_game_generator = RandomGameGenerator()
    game = random_game_generator.generate_random_game()
    print(f"Generated Game: {game}")

    openai_caller = OpenAICaller(game)
    result = openai_caller.call_openai()
    print(f"OpenAI Response: {result}")

if __name__ == "__main__":
    main()
