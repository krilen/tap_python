from multiply import multiplication_table



def main():
    for number in numbers:
        
        answers = multiplication_table(number, limit)
        
        print(f"Multiplication of {number}\n---------------------------")
        
        if answers: # 'bool(None)' -> False
        
            for l in range(1, limit+1):
                
                print(f" - {l} * {number} = {answers[l -1]} ")
        
        else:
            
            print(f" - Not possible to multiply")


        print("\n")

if __name__ == "__main__":
    
    numbers: list[int] = [2, 0, "6", 12, 23, 41, 96]
    limit: int = 12
    
    main()