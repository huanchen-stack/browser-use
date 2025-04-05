import asyncio

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from browser_use import Agent

load_dotenv()

# Initialize the model
llm = ChatOpenAI(
	model='gpt-4o',
	temperature=0.0,
)
# task = 'Locate a recipe for vegan chocolate chip cookies with over 60 reviews and a rating of at least 4.5 stars on Allrecipes.'
# task = 'Find the Return Policy for Mens Rhinestone Skull Graphic Shirt on Amazon. Color: Black, Size: XX-Large. If Free return is avaliable, tell me how to return this item.'
# task = 'Search Apple for the accessory Smart Folio for iPad and check the closest pickup availability next to zip code 90038.'
# task = 'Find the article \"What is climate change? A really simple guide\" and use it to answer what human activities are causing climate change.'
# task = "Find the Customer Service on the Booking website, browse the questions about cancellation, and tell me 'how do I know whether my booking has been cancelled'."
# task = "Look up the pronunciation and definition of the word \"sustainability\" on the Cambridge Dictionary."
# task = "Give me the headline on nytimes.com"
# task = 'Find the first airbnb listing in New York City with a rating of at least 4.5 stars and a price of $100 or less.'
# task = 'Find The Most Popular Recipes of the 1960s, noting the recipe name, preparation time and total time of the second recipe in this collection.'
# task = "If we assume all articles published by Nature in 2020 (articles, only, not book reviews/columns, etc) relied on statistical significance to justify their findings and they on average came to a p-value of 0.04, how many papers would be incorrect as to their claims of statistical significance? Round the value up to the next integer. You may start from https://www.nature.com/nature/articles?year=2020"
task = "According to github, when was Regression added to the oldest closed numpy.polynomial issue that has the Regression label in MM/DD/YY?"

# task = "give me today's nba scores from espn homepage"
agent = Agent(task=task, llm=llm)


async def main():
	await agent.run()


if __name__ == '__main__':
	asyncio.run(main())
