def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print('Error: Please enter numeric values only.')
    else:
        return f"The result of the division is {result:.1f}"

def main():
    numb1 = input('Enter numerator: ')
    numb2 = input('Enter denominator: ')
    result = safe_divide(numb1, numb2)
    if result is not None:
        print(f"The result of the division is {result:.1f}")

if __name__ == "__main__":
    main()


    
              