# Program to explore different string functions in Python

def explore_string_functions():
    s = "  Hello, World!  "
    print(f"Original string: '{s}'")
    print(f"Uppercase: {s.upper()}")
    print(f"Lowercase: {s.lower()}")
    print(f"Title case: {s.title()}")
    print(f"Stripped: '{s.strip()}'")
    print(f"Left stripped: '{s.lstrip()}'")
    print(f"Right stripped: '{s.rstrip()}'")
    print(f"Replace 'World' with 'Python': {s.replace('World', 'Python')}")
    print(f"Split by comma: {s.split(',')}")
    print(f"Find 'World': {s.find('World')}")
    print(f"Count of 'l': {s.count('l')}")
    print(f"Is alpha: {s.isalpha()}")
    print(f"Is digit: {s.isdigit()}")
    print(f"Starts with '  He': {s.startswith('  He')}")
    print(f"Ends with '!  ': {s.endswith('!  ')}")

if __name__ == "__main__":
    explore_string_functions()
