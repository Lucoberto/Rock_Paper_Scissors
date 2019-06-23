import random, sys
menuac="menu"
R='\033[31m'
G='\033[32m'
C='\033[36m'
P='\033[35m'
O='\033[33m'
W='\033[0m'
#menu para acceder a todo el resto de el juego
def menu():
    global menuac
    print(R+'['+O+'+'+R+'] '+C+'Options.'+W)
    print(R+'['+O+'1'+R+'] '+C+'Play.'+W)
    print(R+'['+O+'2'+R+'] '+C+'credits.'+W)
    print(R+'['+O+'3'+R+'] '+C+'Exit.'+W)
    op=input(O+"choose an option: "+W)
    if op == "play":
        menuac="your_turn"
    elif op == "credits":
        menuac="credits_"
    elif op == "exit":
        sys.exit()
#el jugador elije una de las opciones entre piedra papel o tijera 
def your_turn():
    global menuac,op
    print(R+'['+O+'+'+R+'] '+C+'Actions.'+W)
    print(R+'['+O+'1'+R+'] '+C+'Scissors.'+W)
    print(R+'['+O+'2'+R+'] '+C+'Rock.'+W)
    print(R+'['+O+'3'+R+'] '+C+'Paper.'+W)
    op = input(O+"choose your action: "+W)
    if op == "scissors":
        menuac="RPS"
    elif op == "rock":
        menuac="RPS"
    elif op == "paper":
        menuac="RPS"


#se almazena la decision de el jugador
op=""
#segenera uno entre los tres ascii art al azar y se compara con la decision del jugador
def RPS():
    global menuac,op
    rock="""
        _______
    ---'   ____)
          (_____)
          (_____)
           (____)
    ---.__(___)
    """


    paper="""
        _______
    ---'    ____)_
            ______)_
             _______)
            _______)
    ---.__________)
    """


    scissors="""
        _______
    ---'   ____)__
            ______)
           ________)
          (____)
    ---.__(___)
    """
#elije uno al azar
    lista=[scissors, paper, rock]
    decision=random.choice(lista)
#consecuencia tijera
    if op == "scissors" and decision == rock:
        print(rock)
        print(R+'You loses because of a '+P+'Rock'+W)
        menuac="your_turn"
    elif op == "scissors" and decision == paper:
        print(paper)
        print(O+'You won'+R+' killing '+O+'a '+P+'Paper'+W)
        menuac="your_turn"
    elif op == "scissors" and decision == scissors:
        print(scissors)
        print(G+'It seems to have been a draw'+W)
        menuac="your_turn"
# Consecuencia roca
    elif op == "rock" and decision == scissors:
        print(scissors)
        print(O+'You won'+R+' killing '+O+'a '+P+'Scissors'+W)
        menuac="your_turn"
    elif op == "rock" and decision == paper:
        print(paper)
        print(R+'You loses because of a '+P+'Paper'+W)
        menuac="your_turn"
    elif op == "rock" and decision == rock:
        print(rock)
        print(G+'It seems to have been a draw'+W)
        menuac="your_turn"
#Consecuencia de papel
    elif op == "paper" and decision == scissors:
        print(scissors)
        print(R+'You loses because of a '+P+'Scissors'+W)
        menuac="your_turn"
    elif op == "paper" and decision == paper:
        print(paper)
        print(G+'It seems to have been a draw'+W)
        menuac="your_turn"
    elif op == "paper" and decision == rock:
        print(rock)
        print(O+'You won'+R+' killing '+O+'a '+P+'Rock'+W)
        menuac="your_turn"

def credits_():
    global menuac
    print(O+'Developed by '+C+'@Lucoberto'+W)
    print(O+'Thanks to '+C+'@wynand1004 '+O+'for the '+P+'ASCII art'+W)
    print("")
    print(R+'['+O+'+'+R+'] '+C+'Options.'+W)
    print(R+'['+O+'3'+R+'] '+C+'Return.'+W)
    op=input(O+"choose an option: "+W)
    if op == "return":
        menuac="menu"






def func():
    try:
        while True:
            if menuac == "menu":
                menu()
            elif menuac == "RPS":
                RPS()
            elif menuac == "your_turn":
                your_turn()
            elif menuac == "credits_":
                credits_()
    except KeyboardInterrupt:
        sys.exit()
if __name__=="__main__":
	func()