from graphics import *
import time                                           #importando time para diminuir a velocidade que as letras aparecem no dialogo.
import random as rd
#lista sprites
listasprite_costas = ['imgs/sprite_personagem/sprite1_costas.png','imgs/sprite_personagem/sprite2_costas.png','imgs/sprite_personagem/sprite3_costas.png']
listasprite_frente = ['imgs/sprite_personagem/sprite1_frente.png','imgs/sprite_personagem/sprite2_frente.png','imgs/sprite_personagem/sprite3_frente.png']
listasprite_esq = ['imgs/sprite_personagem/sprite1_esquerda.png','imgs/sprite_personagem/sprite2_esquerda.png','imgs/sprite_personagem/sprite3_esquerda.png','imgs/sprite_personagem/sprite4_esquerda.png','imgs/sprite_personagem/sprite5_esquerda.png']
listasprite_dir = ['imgs/sprite_personagem/sprite1.png','imgs/sprite_personagem/sprite2.png','imgs/sprite_personagem/sprite3.png','imgs/sprite_personagem/sprite4.png','imgs/sprite_personagem/sprite5.png']

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
        
def fase_jogo(win):
    background2=Image(Point(540,400),"imgs/floresta2.png")
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

    #---textooo---
    centrox_texto = (x1_dialogo + x2_dialogo) / 2
    centroy_texto = (y1 + y2) / 2
    caixa_dialogo.draw(win)

    teste='Você foi o escolhido para defender o C3\n Em um momento de fragilidade, quando os exames \n estão a beira de acontecer \n as criaturas da infernais querem as almas dos estudantes \n só você pode impedir isso Estudante!'
    teste_texto_atual=''
    Texto=Text(Point(centrox_texto,centroy_texto),'')
    Texto.setTextColor("white")
    Texto.draw(win)
    for letra in teste: #nesse loop inicia a caixa de texto de forma que as letras sejam desenhadas devagar.
        teste_texto_atual=teste_texto_atual+letra
        Texto.setText(teste_texto_atual)
        Texto.setTextColor("white")
        #time.sleep(0.05)
    
    win.getMouse()
    return "fase2"

def fase_jogo2(win):
    background_c3=Image(Point(540,400),"imgs/imagemc3inicio.png")
    background_c3.draw(win)
    #personagem=Image(Point(540,400),"imgs/sprite_personagem/sprite5.png")
    #personagem.draw(win)
    player_x= 540
    player_y= 400
    #sprite_atual.draw(win)
    sprite_atual =Image(Point(player_x,player_y),'imgs/sprite_personagem/sprite1_esquerda.png')
    sprite_atual.draw(win)
    ultima_tecla = ''
    andando = True
    cont = 0
    lista = listasprite_frente
    while andando:
        tecla=win.checkKey()
        if tecla == 'w':
            personagem.undraw()
            for i in listasprite_costas:
                p_costas = Image(Point(player_x,player_y), listasprite_costas[0])
                p_costas.move(0,-5)
                player_y=-5
                p_costas.draw(win)
        elif tecla == 'a':
            personagem.move(-5,0)
            player_x=-5
        elif tecla == 's':
            personagem.move(0,5)
            player_y=+5
        elif tecla == 'd':
            personagem.move(5,0)
            player_x=+5

def main ():
    win=GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)
    if telas == "fase1":
        fase_jogo(win)
    player = {
        "nome": 'nome_player',
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
        telas=fase_jogo(win)
    if telas == "fase2":
        telas = fase_jogo2(win)
    if telas == "fase3":
        fase_jogo3(win,player,inimigo_1)
    win.getMouse()
    
main()