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
    background2=Image(Point(540,400),"imgs/floresta.png")
    background2.draw(win)
    ponto_central = Point(140,675)
    #retratoo
    foto_retrato = Image(ponto_central, "imgs/principal_menor.png")
    largura_retrato = foto_retrato.getWidth()
    altura_retrato = foto_retrato.getHeight()

    #calculo pra conseguir encaixar o sprite na caixa

    x1 = 140 - (largura_retrato / 2) # centro - metade do tamanho
    y1 = 675 - (altura_retrato / 2)
    x2 = 140 + (largura_retrato / 2)
    y2 = 675 + (altura_retrato / 2)

    x1_dialogo = x2 + 20 #x2 onde o retrato termina + 20px de espaço
    x2_dialogo = 1030 #x fixo


    caixa_retrato = Rectangle(Point(x1,y1), Point(x2,y2))
    caixa_retrato.draw(win)
    caixa_retrato.setFill("black")
    foto_retrato.draw(win)
    caixa_dialogo=Rectangle(Point(x1_dialogo,y1),Point(x2_dialogo,y2))   
    caixa_dialogo.setFill("black")
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

