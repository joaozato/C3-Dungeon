from graphics import *

def menu (win):
    background1= Image(Point(540,400),"imgs\c3.png")
    background1.draw(win)
    font=Image(Point(540,200),"imgs\image-removebg-preview.png")
    font.draw(win)
    botao_inicial=Rectangle(Point(430,700),Point(630,750))
    iniciar=Text(Point(530,725),"Iniciar")
    iniciar.setSize(20)
    botao_inicial.setFill("orange")
    botao_inicial.draw(win)
    iniciar.draw(win)
    while True:
        click = win.getMouse()
        if (430 <= click.getX() <= 630) and (700 <= click.getY() <=750):
            botao_inicial.undraw()
            iniciar.undraw()
            return "fase1"
        
    


def main ():
    win= GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)
    if telas == "fase1":
        fase_jogo(win)
    win.close()
main()