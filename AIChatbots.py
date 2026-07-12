import re, random
from colorama import Fore, init

init(autoreset=True)

destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "New York", "Paris"],
}


jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Why do travelvers always feel warm? Because they have a lot of hot spots!",
]


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def recommend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities?")
    preference = input(Fore.GREEN + "You: ").strip().lower()
    preference = normalize_input(preference)

    if preference in destinations:
        suggestions = random.choice(destinations[preference])
        print(Fore.CYAN + f"TravelBot: How about? {suggestions}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (yes/no)")
        answer = input(Fore.GREEN + "You: ").strip().lower()

        if answer == "yes":
            print(Fore.CYAN + "TravelBot: Great! Have a wonderful trip!")
        elif answer == "no":
            print(Fore.RED + "TravelBot: Let's try another.")
            recommend()
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have that type of destination.")
            recommend()
            


