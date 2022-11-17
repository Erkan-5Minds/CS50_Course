def main():
    try:
       change = int(input("How much change is owed: "))
    except change < 0:
      print("Error: Change has to be greater then 0!")
      exit()

    convert_cents = round(change * 100)
    coins = 0

    while convert_cents >= 25:
        convert_cents = convert_cents - 25
        coins += 1
    
    while convert_cents >= 10:
        convert_cents = convert_cents - 10
        coins += 1
    
    while convert_cents >= 5:
        convert_cents = convert_cents - 5
        coins += 1
    
    while convert_cents >= 1:
        convert_cents = convert_cents - 1
        coins += 1
    
    print(coins)
    
if __name__ == "__main__":
    main()
