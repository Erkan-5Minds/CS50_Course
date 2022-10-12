def main():
    while True:
         change = input("How much change is owned: ")
         if change < 0:
            break
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
    
    while convertCents >= 1 == convertCents > 0:
        convertCents = convertCents - 1
        coins += 1
    
    print(f"%d\n", coins)
    
if __name__ == "__main__":
    main()
    