def whoIsWin(cells,turn):
    # ternary operator
    player="Player 1" if turn==True else "Player 2"
    if cells[7]==cells[8]==cells[9]!=0:
        print("The winner is "+player)
        return True
    elif cells[4]==cells[5]==cells[6]!=0:
        print("The winner is "+player)
        return True
    elif cells[1]==cells[2]==cells[3]!=0:
        print("The winner is "+player)
        
        return True
    elif cells[3]==cells[5]==cells[7]!=0:
        print("The winner is "+player)
        return True
    elif cells[1]==cells[5]==cells[9]!=0:
        print("The winner is "+player)
        return True
    elif cells[1]==cells[4]==cells[7]!=0:
        print("The winner is "+player)
        return True
    elif cells[2]==cells[5]==cells[8]!=0:
        print("The winner is "+player)
        return True
    elif cells[3]==cells[6]==cells[9]!=0:
        print("The winner is "+player)
        return True
    
    else:
        return False
    
    
def printCells(cells):
    print("-----------------------")
    for i in range(1,10):
        if  cells[i]==0:
            print("|_|",end='')
        elif cells[i]==1:
            print('|X|',end='')
        elif cells[i]==2:
            print('|O|',end='')
        if i==3 or i==6:
            print("\n")
    
def main():
    cells=['',0,0,0,0,0,0,0,0,0]
    counter=0;
    isXTurn=True
    while(counter<9):
        printCells(cells)
        
        print("\n")
        print("Player Turn:"+"Player 1" if isXTurn==True else "Player 2")
        try:
                
            loc=int(input("Enter input from 1 to 9:-"))
            if(loc>=0 and loc<=9):
                if(cells[loc]==0):
                    cells[loc]=1 if isXTurn==True else 2
                    counter+=1
                    if(whoIsWin(cells,isXTurn)==True):
                        print("Game over!")
                        printCells(cells)
                        break
                    
                    isXTurn=not isXTurn
                else:
                    print("Enter valid location please this location taken before")
            else:
                print("Invalid input")
        except ValueError:
            print("please enter a number")
    if counter==9:
        print("Game over! NoBody win")
        printCells(cells)
    print("\n")
    restart=input("Do you want restart this game(y/n):-")
    if restart=="Y" or restart=="y":
        
        main()


if __name__=="__main__":
    main()
    
