def main():
    # Dictionary of string operations
    oper_dict = {
        'lower': lambda s: s.lower(),
        'upper': lambda s: s.upper(),
        'len': lambda s: str(len(s)),
        'reverse': lambda s: s[::-1]
    }

    # Get input from user
    word = input("Enter word: ")
    operation = input("Enter operation name (lower, upper, len, reverse): ")

    # Find the action selected by get and run it
    action = oper_dict.get(operation, lambda s: 'Unknown operation')
    result = action(word)

    print(result)


# Example usage
if __name__ == "__main__":
    main()
