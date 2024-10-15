from collections import deque

def is_palindrome(s):
    d = deque([ch.lower() for ch in s if ch.isalnum()])
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

def main():
    test_string = input("Введіть рядок: ")
    if is_palindrome(test_string):
        print(f"'{test_string}' є паліндромом.")
    else:
        print(f"'{test_string}' не є паліндромом.")

if __name__ == "__main__":
    main()
