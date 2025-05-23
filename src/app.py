import datetime

# Initial version of the application
ENABLE_GREETING = True

def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

def main():
    # Imagine this name comes from a config or user input
    user_name = "Alice"
    if ENABLE_GREETING:
        greet(user_name)

def say_goodbye():
    """Prints a farewell message."""
    print("Goodbye!")

def show_time():
    """Displays the current time."""
    # This is a simulated hotfix change
    now = datetime.datetime.now()
    print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
    show_time()
    say_goodbye()
