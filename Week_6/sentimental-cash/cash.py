def main():
    try:
      change = int(input("How much change is owed: "))
    except change < 0:
      print("Error change has to be greater then 0!")
      exit()

    convertCents = round(change * 100)
    coins = 0

    while convertCents >= 25:
        convertCents = convertCents - 25
        coins += 1
    
    while convertCents >= 10:
        convertCents = convertCents - 10
        coins += 1
    
    while convertCents >= 5:
        convertCents = convertCents - 5
        coins += 1
    
    while convertCents >= 1:
        convertCents = convertCents - 1
        coins += 1
    
    print(coins)
    
if __name__ == "__main__":
    main()
