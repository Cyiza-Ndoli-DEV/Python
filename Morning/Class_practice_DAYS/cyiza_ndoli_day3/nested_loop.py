
# nested loops

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")


#start with the outer loop

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")  #that end thing will prevent the cursor from
                              #moving to the next line since we have 2 prints6 
    print()