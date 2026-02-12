
"""
Name: Stage of Life Calculator
Purpose: Calculates stage of life for the age input
Author: Luke Atkins
Starter Code: No starter code used
Date: 2/11/2026
License: MIT
"""

def get_age() -> int:
    """Forces the user to enter a valid integer representing their age between 0 and 200"""
    res = input("Enter age: ")
    try:
        res = int(res)
    except Exception:
        print("invalid input")
        return get_age()
    
    if res <= 0 or res > 200:
        print("invalid age")
        return get_age()

    return res

def get_stage(age: int) -> str:
    """Returns the current stage of life as a string"""
    stage = ""
    if age <= 2:
        stage = 'baby'
    elif age < 4:
        stage = 'toddler'
    elif age >= 4 and age < 13:
        stage = 'kid'
    elif age >= 13 and age < 20:
        stage = 'teenager'
    elif age >= 20 and age < 65:
        stage = 'adult'
    elif age >= 65:
        stage = 'elder'
    
    return stage

def main():
    """Programs main entry. Does not take in command line args"""
    age = get_age()
    stage = get_stage(age)
    print(f'the person is a {stage}')
    input('Enter another age? (y/n): ') == 'y' and main()

if __name__ == "__main__":
    main()