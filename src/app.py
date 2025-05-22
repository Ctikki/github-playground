# Initial version of the application
def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

def main():
    # Imagine this name comes from a config or user input
    user_name = "Alice"
    greet(user_name)

if __name__ == "__main__":
    main()
