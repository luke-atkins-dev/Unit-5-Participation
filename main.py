
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

def main():
    pass

if __name__ == "__main__":
    main()