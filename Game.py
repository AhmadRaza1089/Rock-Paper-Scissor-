import random
lis = ["rock", "paper", "scissor"]
while True:
    uchoicount = 0
    cchoicount = 0
    user = int(input("""Enter your number:
                1 Yes
                2 No|Exit \n"""))
    if user == 1:
        print("You have entered the game")
        for i in range(5):
            print(f"round no.{i+1}")
            uchoi = int(input("""Enter your choice:
                        1 rock
                        2 paper
                        3 scissor \n"""))
            if uchoi == 1:
                sele = "rock"
            elif uchoi == 2:
                sele = "paper"
            elif uchoi == 3:
                sele = "scissor"
            else:
                print("Invalid number")
                continue
            print("User choice:", sele)
            cchoi = random.choice(lis)
            print("Computer choice:", cchoi)
            #situation 
            if sele == cchoi:
                print("Draw")
                uchoicount += 1
                cchoicount += 1
            elif (sele == "paper" and cchoi == "rock") or \
                (sele == "rock" and cchoi == "scissor") or \
                (sele == "scissor" and cchoi == "paper"):
                print("You won this round")
                uchoicount += 1
            else:
                print("Computer won this round")
                cchoicount += 1
        # Final comparison score 
        if uchoicount > cchoicount:
            print("You won the game")
        elif cchoicount > uchoicount:
            print("Computer won the game")
        else:
            print("The game is a draw")
        print("User count:", uchoicount)
        print("Computer count:", cchoicount)
    else:
        print("Exit successfully")
        break
    
