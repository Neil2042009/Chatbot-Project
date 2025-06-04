#
name = input("Welcome to the Subject-Based Encouragement Chatbot, please enter your name: ")
print(name)
subject = input("What is your favourite subject?(For example, math, chemistry, computer science, biology, geography, business, robot, )")

def get_response(subject):
    if subject == "math":
        print(name, "it's awesome that you like math!It builds strong logical thinking.")
        print("Famous figure: Issac Newton - he helped invent calculus")