
def get_age() -> int:
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
    age = get_age

if __name__ == "__main__":
    main()