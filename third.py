def check_brackets(expression):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    
    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if stack == [] or brackets[char] != stack.pop():
                return "Несиметрично"
    
    return "Симетрично" if not stack else "Несиметрично"

def main():
    expression = input("Введіть рядок з дужками: ")
    result = check_brackets(expression)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()