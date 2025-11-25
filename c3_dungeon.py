from graphics import *
import time                                           #importando time para diminuir a velocidade que as letras aparecem no dialogo.
def menu (win):
    background1= Image(Point(540,400),"imgs/c3.png")    #imagem background do menu
    background1.draw(win)           
    font=Image(Point(540,200),"imgs/image-removebg-preview.png")  #fonte utilizada para nome do jogo
    font.draw(win)
    botao_inicial=Rectangle(Point(430,700),Point(630,750))   #retangulo de botão iniciar
    iniciar=Text(Point(530,725),"Iniciar")
    iniciar.setSize(20)
    botao_inicial.setFill("orange")
    botao_inicial.draw(win)
    iniciar.draw(win)
    while True:                                   #enquanto for verdadeiro...
        click = win.getMouse()
        if (430 <= click.getX() <= 630) and (700 <= click.getY() <=750):  #se o usuario clicar no range do botão, então, é levado até o proximo cenário
            botao_inicial.undraw()                                          #quando ele clica, os botões anteriores e background são apagados levando a função de tela 1.
            iniciar.undraw()
            background1.undraw()
            font.undraw()
            return "fase1"
    


def fase_jogo(win):         #quando encerra a funçao de menu anterior, vem para cá.
    background2=Image(Point(540,400),"imgs/principal.png")                  #novo background é desenhado
    background2.draw(win)                                                       
    caixa_dialogo=Rectangle(Point(260,580),Point(730,750))          #nova caixa de dialogo
    caixa_dialogo.setFill("orange")
    caixa_dialogo.draw(win)
    teste='Você foi o escolhido para defender o C3\n Em um momento de fragilidade, quando os exames \n estão a beira de acontecer \n as criaturas da infernais querem as almas dos estudantes \n só você pode impedir isso Estudante!'
    teste_texto_atual=''
    Texto=Text(Point(500,650),'')
    Texto.draw(win)
    for letra in teste: #nesse loop inicia a caixa de texto de forma que as letras sejam desenhadas devagar.
        teste_texto_atual=teste_texto_atual+letra
        Texto.setText(teste_texto_atual)
        time.sleep(0.05)
        
    




def main ():
    win=GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)
    player = {
        "nome": nome_player,
        "vida_max": 100,
        "vida_atual": 100,
        "dano": 15,
        "pocao": 2
    }
    inimigo_1 = {
        "vida":50,
        "dano":5
    }
    Prisco = {
        "nome": "Prisco",
        "vida_max": 200,
        "dano_normal":10,
        "dano_especial":20,

    }

    if telas == "fase1":
        fase_jogo(win,player,inimigo_1)
    if telas == "fase2":
        fase_jogo2(win,player,inimigo_1,Prisco)
    win.getMouse()
    win.close()
main()
