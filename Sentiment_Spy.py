import sys
import time
from textblob import TextBlob
from colorama import Fore, Style, init

init(autoreset=True)

conversation_history = []
sentiment_counters = {"positive": 0, "neutral": 0, "negative": 0}

def show_processing_animation():
    """Displays a simple spy-themed loading animation."""
    animation = ["[Spying on text...]", "[Analyzing intelligence...]", "[Decoding emotions...]"]
    print(Fore.CYAN + "Incoming transmission... ", end="", flush=True)
    for frame in animation:
        sys.stdout.write(Fore.MAGENTA + f"{frame} ")
        sys.stdout.flush()
        time.sleep(0.5)
        sys.stdout.write('\b' * (len(frame) + 1))
    print("\n" + Style.RESET_ALL)


def analyze_sentiment(text):
    """Analyzes text sentiment and updates global metrics."""
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        category = "positive"
        color = Fore.GREEN
        strength = "Strong" if polarity > 0.5 else "Moderate"
    elif polarity < 0:
        category = "negative"
        color = Fore.RED
        strength = "Strong" if polarity < -0.5 else "Moderate"
    else:
        category = "neutral"
        color = Fore.YELLOW
        strength = "Neutral"

    conversation_history.append({"text": text, "category": category, "score": round(polarity, 2)})
    sentiment_counters[category] += 1

    print(color + f"» Analysis: {category.upper()} ({strength} sentiment)")
    print(color + f"» Polarity Score: {round(polarity, 2)}\n")


def execute_command(command):
    """Handles chatbot system commands."""
    global conversation_history, sentiment_counters
    cmd = command.lower().strip()
    
    if cmd == "summary":
        print(Fore.BLUE + "\n=== SENTIMENT CURRENT SUMMARY ===")
        for key, value in sentiment_counters.items():
            print(f"• {key.capitalize()}: {value}")
        print("=================================\n")
        
    elif cmd == "reset":
        conversation_history = []
        sentiment_counters = {"positive": 0, "neutral": 0, "negative": 0}
        print(Fore.LIGHTRED_EX + "System memory wiped clean. All logs and counters reset.\n")
        
    elif cmd == "history":
        print(Fore.BLUE + "\n=== CONVERSATION LOGS ===")
        if not conversation_history:
            print("No entries recorded yet.")
        for idx, entry in enumerate(conversation_history, 1):
            print(f"{idx}. [{entry['category'].upper()}] (Score: {entry['score']}) -> \"{entry['text']}\"")
        print("=========================\n")
        
    elif cmd == "help":
        print(Fore.LIGHTWHITE_EX + "\n--- AVAILABLE COMMANDS ---")
        print("• summary : Check current running sentiment counts.")
        print("• reset   : Wipe all conversation data and scores.")
        print("• history : View your input log history during this session.")
        print("• help    : View this command list guide.")
        print("• exit    : Stop chatbot and save final session file.\n")


def get_valid_name():
    """Prompts and validates the user's name."""
    while True:
        name = input("Agent, please enter your name: ").strip()
        if name.isalpha():
            return name
        print(Fore.RED + "Access Denied. Name must only contain alphabetic letters. Try again.")


def generate_final_report(username):
    """Generates a text report and exports it to a text file."""
    report_title = f"=== SENTIMENT ANALYSIS REPORT FOR {username.upper()} ==="
    border = "=" * len(report_title)
    
    report_content = (
        f"{border}\n"
        f"{report_title}\n"
        f"{border}\n"
        f"Positive Messages : {sentiment_counters['positive']}\n"
        f"Neutral Messages  : {sentiment_counters['neutral']}\n"
        f"Negative Messages : {sentiment_counters['negative']}\n"
        f"{border}\n"
        f"Total Logged Input lines: {len(conversation_history)}\n"
    )
    
    print(Fore.CYAN + "\n" + report_content)
    
    filename = f"{username}_sentiment_analysis.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_content)
        print(Fore.GREEN + f"Report successfully encrypted and saved to file: '{filename}'")
    except IOError:
        print(Fore.RED + "Error: Could not write file summary to disc.")


def main():
    print(Fore.CYAN + "==================================================")
    print(Fore.CYAN + "   Welcome to the Secret Sentiment Chatbot HQ")
    print(Fore.CYAN + "==================================================")
    
    username = get_valid_name()
    print(Fore.GREEN + f"\nWelcome Agent {username}!")
    print("Type any text sentence below to analyze its psychological sentiment.")
    print("Type 'help' to review special commands or 'exit' to quit.\n")

    commands = {"summary", "reset", "history", "help"}

    while True:
        user_input = input(Fore.LIGHTWHITE_EX + f"[{username}] > ").strip()
        
        if not user_input:
            continue
            
        if user_input.lower() == "exit":
            print(Fore.LIGHTYELLOW_EX + "\nTerminating active safe-line session...")
            generate_final_report(username)
            print(Fore.CYAN + "Goodbye, Agent.")
            break
            
        elif user_input.lower() in commands:
            execute_command(user_input)
            
        else:
            show_processing_animation()
            analyze_sentiment(user_input)


if __name__ == "__main__":
    main()
