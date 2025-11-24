from graphics import *
import time 
def menu (win):
    background1= Image(Point(540,400),"imgs/c3.png")
    background1.draw(win)
    font=Image(Point(540,200),"imgs/image-removebg-preview.png")
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
            background1.undraw()
            font.undraw()
            return "fase1"
    


def fase_jogo(win):
    background2=Image(Point(540,400),"imgs/principal.png")
    background2.draw(win)
    caixa_dialogo=Rectangle(Point(260,580),Point(730,750))
    caixa_dialogo.setFill("orange")
    caixa_dialogo.draw(win)
    teste='Você foi o escolhido para defender o C3\n Em um momento de fragilidade, quando os exames \n estão a beira de acontecer \n as criaturas da infernais querem as almas dos estudantes \n só você pode impedir isso Estudante!'
    teste_texto_atual=''
    Texto=Text(Point(500,650),'')
    Texto.draw(win)
    for letra in teste:
        teste_texto_atual=teste_texto_atual+letra
        Texto.setText(teste_texto_atual)
        time.sleep(0.05)
    




def main ():
    win=GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)
    if telas == "fase1":
        fase_jogo(win)
    win.getMouse()
    win.close()
main()
