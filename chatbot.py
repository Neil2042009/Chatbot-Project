from openai import OpenAI
import random


OPEN_AI_KEY = "API key"  # Replace with your actual OpenAI key


# Predefined trailblazers list
trailblazers = [
   "Katherine Johnson - Helped NASA with space missions using math.",
   "Alan Turing - Cracked codes in WWII and invented computing.",
   "Kimberly Bryant - Founded Black Girls Code.",
   "Ada Lovelace - First computer programmer.",
   "Elon Musk - Tech entrepreneur behind SpaceX and Tesla."
]


# Initialize OpenAI client
client = OpenAI(api_key=OPEN_AI_KEY)


print("Welcome to the Empowerment Chatbot!")


# User input
name = input("What's your name? ")
subject = input("What's your favorite subject? ")
tech = input("Are you interested in technology? (yes/no): ")


# Encouragement based on subject
print(f"\nNice to meet you, {name}!")
subject = subject.lower()


if subject == "science":
   print("You have a mind for discovery! Keep exploring science.")
elif subject == "art":
   print("Your creativity can change the world!")
elif subject == "math":
   print("You think logically and solve real problems—awesome!")
elif subject in ["english", "language arts"]:
   print("Words have power, and you can use them to inspire!")
elif subject == "history":
   print("Understanding the past helps build a better future!")
elif subject in ["music", "band"]:
   print("Your rhythm and harmony bring joy to the world!")
elif subject in ["computer science", "programming", "coding"]:
   print("You’re building the future—one line of code at a time!")
elif subject in ["physical education", "pe", "sports"]:
   print("Strong body, strong mind! Keep moving forward!")
elif subject in ["geography"]:
   print("Exploring the world starts with understanding it!")
elif subject in ["drama", "theatre"]:
   print("Your voice and stories can move hearts!")
else:
   print("Every subject has value. Keep learning and growing!")




# Encouragement based on tech interest
if tech.lower() == "yes":
   print("Technology is the future, and you can be part of it!")
else:
   print("That’s okay! Stay curious and open to new things.")


# Random trailblazer from list
print("\nHere’s someone inspiring you should know about:")
print(random.choice(trailblazers))


# ChatGPT-suggested trailblazer
print("\nLet’s ask ChatGPT to suggest another inspiring person...")


completion = client.chat.completions.create(
   model="gpt-4o-mini",
   messages=[
       {"role": "system", "content": "You are a friendly Canadian. All your responses should be in Canadian slang."},
       {"role": "user", "content": "Tell me about a trailblazer in tech or science who can inspire high school students."}
   ]
)


print("ChatGPT says:")
print(completion.choices[0].message.content.strip())




