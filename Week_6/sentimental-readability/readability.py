import cs50

def main():
    while True:
        input = cs50.get_string('Text: ')
        index = 0
        alphabets = 0
        digits = 0
        special = 0
        words = 1
        sentences = 0
        
        if (input):
            for i in range(len(input)):
                if (input[i].isalpha()):
                    alphabets += 1
                elif (input[i].isnumeric()):
                    digits += 1
                elif (input[i] == ' ' and input[i + 1]):
                    words += 1
                elif (input[i] == '?' or input[i] == '!' or input[i] == '.'):
                    sentences += 1
                else:
                    special += 1

            L = float(alphabets / words * 100)

            S = float(sentences / words * 100)

            index = round((float)(0.0588 * L - 0.296 * S - 15.8))
            
            if (index >= 16):
                print('Grade 16+')
            elif (index < 1):
                print('Before Grade 1')
            else:
                print('Grade ', index)

            break
    if __name__ == "__main__":
      main()
