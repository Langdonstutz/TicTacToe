# Prototype.py
# TicTacToe
# By Langdon and Mike De La Cruz
from graphics import *
from random import *

already_moved = False
#Window Runs when the Game Finishes
def restart():
    global DetectTie
    win = GraphWin("Prototype", 600, 600)
    win.setBackground("blanched almond")
    win.setCoords(0,0,600,600)
    winlos = Text(Point(300,450),'')
    if DetectTie == 9:
        FinalMessage = Text(Point(300,500),'Game ends In a Tie')
    else:
        FinalMessage = Text(Point(300,500),Symbol+' Won the Game')
        if Symbol == 'X':
            winlos = Text(Point(300,450),'You Won The Game!')
        else:
            winlos = Text(Point(300,450),'You Lost The Game! Try Again')
    playagn = Text(Point(300,300),'Do you want to play again?')
    yes = Rectangle(Point(100,100),Point(200,200))
    yestext = Text(Point(150,150),'Yes')
    notext = Text(Point(450,150),'No')
    no = Rectangle(Point(400,100),Point(500,200))

    restartbuttons = [playagn, yes, yestext, notext, no, FinalMessage, winlos]
    for i in restartbuttons:
        i.draw(win)
    while True:
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        #Yes
        if 100<x<200 and 100<y<200:
            return False
            win.close()
        #No
        if 400<x<500 and 100<200:
            exit()  

def startmenu():
    global win
    win = GraphWin("Prototype", 600, 600)
    win.setBackground("blanched almond")
    win.setCoords(0,0,600,600)
    
    #Create buttons
    Welcome = Text(Point(300,500),'Welcome to Tic Tac Toe!')
    Wdific = Text(Point(300,320),'Select a Difficulty')

    easybot = Rectangle(Point(100,100),Point(200,200))
    mediumbot = Rectangle(Point(250,100),Point(350,200))
    hardbot = Rectangle(Point(400,100),Point(500,200))
    labelE = Text(Point(150,150),'Easy')
    labelM = Text(Point(300,150),'Medium')
    labelH = Text(Point(450,150),'Hard')
    global Button
    Button = [easybot, mediumbot, hardbot, labelE, labelM, labelH, Welcome, Wdific]

    for i in Button:
        i.draw(win)
    
    #If buttons clicked, select difficulty
    while True:
        global already_moved
        global difficulty
        click = win.getMouse()
        x = click.getX()
        y = click.getY()
        #Easy
        if 100<x<200 and 100<y<200:
            win.close()
            difficulty = 'easy'
            already_moved = False
            main()
            return False
        #Medium
        if 250<x<350 and 100<200:
            difficulty = 'medium'
            win.close()
            already_moved = False
            main()
            return False
        #Hard
        if 400<x<500 and 100<200:
            win.close()
            difficulty = 'hard'
            already_moved = False
            main()
            return False

def main ():
    global Symbol

    # Create the main design
    win = GraphWin("Prototype", 600, 600)
    win.setBackground("blanched almond")

    Horizontal_Line1 = Line(Point(0,200), Point(600, 200)).draw(win)
    Horizontal_Line1.setWidth(6)

    Vertical_Line1 = Line(Point(200, 0), Point(200, 600)).draw(win)
    Vertical_Line1.setWidth(6)

    Horizontal_Line2 = Line(Point(0, 400), Point(600, 400)).draw(win)
    Horizontal_Line2.setWidth(6)

    Vertical_Line2 = Line(Point(400, 0), Point(400, 600)).draw(win)
    Vertical_Line2.setWidth(6)

    # Create X and O Functions

    def X_Object ():
        Line1 = Line(Point(230, 230), Point(370, 370))
        Line1.setWidth(12)

        Line2 = Line(Point(230, 370), Point(370, 230))
        Line2.setWidth(12)

        return Line1, Line2
    
    def O_Object (X, Y):
        Create_Circle = Circle(Point(X, Y), 75)
        Create_Circle.setWidth(12)

        return Create_Circle
    
    # Box to reference placeholders and determine wins
    Boxes = list(range(9))
    Symbol = "X" # default 
    # 0, 1, 2
    # 3, 4, 5
    # 6, 7, 8

    # Declare the winner here!
    def check_winner():
        global Symbol 
        if Boxes[0] == Symbol and Boxes[3] == Symbol and Boxes[6] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[1] == Symbol and Boxes[4] == Symbol and Boxes[7] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[2] == Symbol and Boxes[5] == Symbol and Boxes[8] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[0] == Symbol and Boxes[4] == Symbol and Boxes[8] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[2] == Symbol and Boxes[4] == Symbol and Boxes[6] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[0] == Symbol and Boxes[1] == Symbol and Boxes[2] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[3] == Symbol and Boxes[4] == Symbol and Boxes[5] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"
        elif Boxes[6] == Symbol and Boxes[7] == Symbol and Boxes[8] == Symbol:
            print(Symbol, "won!")
            time.sleep(1)
            return "yield"

    # Optimize Player's Interactive Mouseclick
    def Player_Interactive_Mode(MX1, MY2, BoxNum):
            # Box 1 is > 0, < 200, > 0, < 200, Box[0] == 0, L1/L2 = (-200, -200)  
            if Boxes[BoxNum] != "X" and Boxes[BoxNum] != "O":
                L1, L2 = X_Object() # L1, L2 represent the lines that make up X
                L1.move(MX1, MY2)
                L2.move(MX1, MY2)
                L1.draw(win)
                L2.draw(win)
                Boxes[BoxNum] = "X"
                return check_winner()
            else:
                return "Occupied"

    def boxchecker(BoxNum):
        if Boxes[BoxNum] == "X" or Boxes[BoxNum] == "O":
            return "Occupied"
        else: 
            return "Open"
            
    # A.I First Design
    def Computer_Interactive_Mode(difficulty):
        global Symbol
        global already_moved
        if difficulty == 'easy':
            print("easy")
            Num = randrange(1, 9)
            return Num
        if difficulty == 'medium':
            if boxchecker(4) == 'Open':
                print("medium")
                Num = 5
            elif already_moved != True:  # If the center is not available and we haven't moved yet
                firstmove = [0, 2, 6, 8]
                g = choice(firstmove)
                while boxchecker(g) != 'Open':
                    g = choice(firstmove)
                Num = g+1
                already_moved = True  # Set already_moved to True after the first move
            else:  # If we have already moved once
                Num = randrange(0, 9)  # Choose a random move
            print(Num)
            return Num
        if difficulty == 'hard':
            #Check to win game
            for i in range(9):
                if boxchecker(i) == 'Open':
                    Boxes[i] = "O"
                    Symbol = 'O'
                    if check_winner() == 'yield':
                        Boxes[i] = i
                        Num = i+1
                        Symbol = 'O'
                        return Num
                    Boxes[i] = i
            #Check to Block a Loss
            for i in range(9):
                if boxchecker(i) == 'Open':
                    Boxes[i] = "X"
                    Symbol = 'X'
                    if check_winner() == 'yield':
                        Boxes[i] = i
                        Num = i+1
                        Symbol = 'O'
                        return Num
                    Boxes[i] = i    
            Num = randrange(1, 9)
            Symbol = 'O'
            return Num
            
    # Initiate Gameplay
    global DetectTie
    DetectTie = 0
    for i in range(9999999):
         

        for values in Boxes: # Tie Detector Method
            if type(values) == str:
                DetectTie = DetectTie + 1
        
        if DetectTie == 9: # Tie Detector Method
            print("Tie!")
            break
        else:
            print(DetectTie, "detect")
            DetectTie = 0

        # Below is Player and Computer Interactions
        if Symbol == "X":
            Mouse = win.getMouse()
            #Box 1
            if Mouse.getX() > 0 and Mouse.getX() < 200 and Mouse.getY() > 0 and Mouse.getY() < 200:
                check = Player_Interactive_Mode(-200, -200, 0)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue # This stops the current iteration/loop and goes back to the start to reloop
                Symbol = "O" # if there isn't a win from you switch the symbol to O not 0
            #Box 2
            elif Mouse.getX() > 200 and Mouse.getX() < 400 and Mouse.getY() > 0 and Mouse.getY() < 200:
                Symbol = "X"
                check = Player_Interactive_Mode(0, -200, 1)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 3
            elif Mouse.getX() > 400 and Mouse.getX() < 600 and Mouse.getY() > 0 and Mouse.getY() < 200:
                Symbol = "X"
                check = Player_Interactive_Mode(200, -200, 2)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 4
            elif Mouse.getX() > 0 and Mouse.getX() < 200 and Mouse.getY() > 200 and Mouse.getY() < 400:
                Symbol = "X"
                check = Player_Interactive_Mode(-200, 0, 3)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 5
            elif Mouse.getX() > 200 and Mouse.getX() < 400 and Mouse.getY() > 200 and Mouse.getY() < 400:
                Symbol = "X"
                check = Player_Interactive_Mode(0, 0, 4)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 6
            elif Mouse.getX() > 400 and Mouse.getX() < 600 and Mouse.getY() > 200 and Mouse.getY() < 400:
                Symbol = "X"
                check = Player_Interactive_Mode(200, 0, 5)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 7
            elif Mouse.getX() > 0 and Mouse.getX() < 200 and Mouse.getY() > 400 and Mouse.getY() < 600:
                Symbol = "X"
                check = Player_Interactive_Mode(-200, 200, 6)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 8
            elif Mouse.getX() > 200 and Mouse.getX() < 400 and Mouse.getY() > 400 and Mouse.getY() < 600:
                Symbol = "X"
                check = Player_Interactive_Mode(0, 200, 7)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
            #Box 9
            elif Mouse.getX() > 400 and Mouse.getX() < 600 and Mouse.getY() > 400 and Mouse.getY() < 600:
                Symbol = "X"
                check = Player_Interactive_Mode(200, 200, 8)
                if check == "yield":
                    win.close()
                    break
                elif check == "Occupied":
                    continue 
                Symbol = "O"
        #AI's turn starts here below
        elif Symbol == "O":
            BoxNum = Computer_Interactive_Mode(difficulty)
            if BoxNum == 1 and Boxes[0] != "O" and Boxes[0] != "X":
                Boxes[0] = "O"
                c1 = O_Object(100, 100)
                c1.draw(win)
                Symbol = "O"
                
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 2 and Boxes[1] != "O" and Boxes[1] != "X":
                Boxes[1] = "O"
                c1 = O_Object(300, 100)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 3 and Boxes[2] != "O" and Boxes[2] != "X":
                Boxes[2] = "O"
                c1 = O_Object(500, 100)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 4 and Boxes[3] != "O" and Boxes[3] != "X":
                Boxes[3] = "O"
                c1 = O_Object(100, 300)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 5 and Boxes[4] != "O" and Boxes[4] != "X":
                Boxes[4] = "O"
                c1 = O_Object(300, 300)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 6 and Boxes[5] != "O" and Boxes[5] != "X":
                Boxes[5] = "O"
                c1 = O_Object(500, 300)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 7 and Boxes[6] != "O" and Boxes[6] != "X":
                Boxes[6] = "O"
                c1 = O_Object(100, 500)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                
                Symbol = "X"
            elif BoxNum == 8 and Boxes[7] != "O" and Boxes[7] != "X":
                Boxes[7] = "O"
                c1 = O_Object(300, 500)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"
            elif BoxNum == 9 and Boxes[8] != "O" and Boxes[8] != "X":
                Boxes[8] = "O"
                c1 = O_Object(500, 500)
                c1.draw(win)
                Symbol = "O"
                check = check_winner()
                if check == "yield":
                    win.close()
                    break
                Symbol = "X"

#Main function
startmenu()
while True:
    restart()
    startmenu()
