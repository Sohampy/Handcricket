import random

def cricket():
    uwon=open("Userwon.txt","r")
    cwon=open("Compwon.txt","r")
    Draw=open("Draw.txt","r")
    def bat():
        global batingtr
        ctr=1
        batr=[]
        batingtr=0
        print("User is now BATTING")
        while ctr<13:
            us=input(f"User Batting: {ctr} ball =>")
            if us.isdigit()==False or int(us)>=7:
                print("ONLY ENTER A NUMBER BETWEEN (0/6)")
                print("¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦  ")
            elif us.isdigit():
                user=int(us)
                comp=random.randint(1,6)
                if user!=comp:
                    print("Computer choosed:",comp)
                    batr.append(user)
                    batingtr=sum(batr)
                    print("Runs scored:",batingtr)
                    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    ctr+=1
                elif user==comp:
                    print("Computer choosed:",comp)
                    print("Runs scored:",batingtr)
                    print("YOU ARE OUT...YOU SCORED ",batingtr,"RUNS")
                    break
            
        ball()


    def ball():
        global balingtr
        balingtr=0
        ctr2=1
        balltr=[]
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print("User is now BALLING")
        print("Computer has a traget of ",batingtr,"runs")
        while ctr2<13:
            usb=input(f"User balling: {ctr2} ball =>")
            if usb.isdigit()==False or int(usb)>=7:
                print("ONLY ENTER A NUMBER BETWEEN (0/6)")
                print("¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦ ¦  ")
            elif usb.isdigit():
                user=int(usb)
                comp=random.randint(0,6)
                if user!=comp:
                    print("Computer choosed:",comp)
                    balltr.append(comp)
                    balingtr=sum(balltr)
                    print("Runs scored:",balingtr)
                    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                    ctr2+=1
                    while balingtr<=batingtr:
                        print()
                        break
                    else:
                        print(cwon.read())
                        input()
                        break
                elif user==comp:
                    if balingtr==batingtr:
                        print("Computer choosed:",comp)
                        print("Runs scored:",balingtr)
                        print("COMPUTER IS OUT")
                        print(Draw.read())    
                    else:
                        print("Computer choosed:",comp)
                        print("Runs scored:",balingtr)
                        print("COMPUTER IS OUT")
                        print("_______________________________")
                        print("Runs Scored By the User:",batingtr)
                        print("Runs scored By th computer:",balingtr)
                        print(uwon.read())
                        input()
                        break
        else:
            print(uwon.read())
    bat()

title=open("Title.txt","r")
print(title.read())
cricket()




        




 





    

