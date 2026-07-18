def chatbot():
    print("Hello! I am your AI assistant.")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name}!\n")

    while True:
        
        mood = input("How are you feeling today? (good/bad/neutral): ").strip().lower()
        print("")  

        if mood == "good":
            print("That's fantastic to hear! Positive vibes are the best.")
            
            hobby = input("What hobby or activity makes you happiest? ")
            print(f"Wow, {hobby} sounds like a lot of fun!")

        elif mood == "bad":
            print("I am so sorry to hear that. I hope your day gets better soon.")
            
            distraction = input("What is your favorite activity to do when you want to relax? ")
            print(f"Doing some {distraction} sounds like a peaceful way to unwind.")

        elif mood == "neutral":
            print("A balanced day is a good day. Steady and calm!")
            
            activity = input("Are there any interesting activities you are planning to try later? ")
            print(f"That sounds interesting! Good luck with {activity}.")
        else:
            print("I didn't quite catch that mood, but I hope you are doing well!")

        print("")  

        choice = input("Would you like to keep chatting? (yes/no): ").strip().lower()
        print("-" * 40)  

        if choice != "yes" and choice != "y":
            break

    print(f"\nThank you for chatting with me today, {name}! Have a wonderful rest of your day. Goodbye!")

if __name__ == "__main__":
    chatbot()
