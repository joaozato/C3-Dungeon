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
        
def inventario (win): #funçao apenas da janela, criar outra funçao pra armazenar os itens
    win_inv = GraphWin("Inventário",400,400)
    win_inv.setBackground("grey")
    aviso = Text(Point(200, 380), "Clique para fechar")
    aviso.draw(win_inv)
    win_inv.getMouse()
    win_inv.close()

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

    #inventariobotao

    altura = 40
    margem = 10

    inv_y2 = y1 - margem
    inv_y1 = inv_y2 - altura

    
    inventario_button = Rectangle(Point(x1,inv_y1),Point(x2,inv_y2))
    inventario_button.setFill("orange")
    inventario_button.draw(win)
    centrox_inv = (x1 + x2) / 2 #msm coisa
    centroy_inv = (inv_y1 + inv_y2) / 2 #USAR ESTES CALCULOS PRA PEGAR O CENTRO DOS TEXTOS OK!
    inventario_texto = Text(Point(centrox_inv,centroy_inv),'Inventário')
    inventario_texto.setSize(20)
    inventario_texto.draw(win)
#cuucucucucucucucuc

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
        if win.checkMouse(): #se houve click enqt ta mosttando o texto
            Texto.setText(teste) #se sim mostra o texto completo e para d mostra 
            break 
        teste_texto_atual=teste_texto_atual+letra
        Texto.setText(teste_texto_atual)
        Texto.setTextColor("white")
        time.sleep(0.05)

    while True:
        click = win.getMouse()
        mx = click.getX()
        my = click.getY()
        if (x1 <= mx <= x2) and (inv_y1 <= my <= inv_y2):
            inventario(win) #pega a funçao
            #nao ta chamando.
        elif (x1_dialogo <= mx <= x2_dialogo) and (y1 <= my <= y2): #qnd clica passa o texto
            break
    return "fase2"

def fase_jogo2(win):
    background_c3=Image(Point(540,400),'imgs/fundo2.png')
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
        if tecla == 'w' or tecla == 's' or tecla == 'd' or tecla == 'a':
            sprite_atual.undraw()

            if tecla != ultima_tecla:
                cont = 0
                ultima_tecla = tecla
            if tecla == 'w':
                player_y = player_y - 5
                lista = listasprite_costas
                #sprite_novo = listasprite_costas[cont]
            elif tecla == 's':
                player_y = player_y + 5
                lista = listasprite_frente
                #sprite_novo = listasprite_frente[cont]
            elif tecla == 'a':
                player_x = player_x - 5
                lista = listasprite_esq
            elif tecla == 'd':
                player_x = player_x + 5
                lista = listasprite_dir

            #caralho NAO PARA DE DAR INDEX OUT OF RANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

            if cont >= len(lista):
                cont = 0

            sprite_novo = lista[cont]
            sprite_atual =Image(Point(player_x,player_y),sprite_novo)
            sprite_atual.draw(win)
            cont += 1
        time.sleep(0.10)

def fase_jogo3(win,player,inimigo_1):
    background3=Image(Point(540,400),"imgs/floresta.png")
    background3.draw(win)
    personagem_batalha=Image(Point(150,500),"imgs/sprite_personagem/sprite2.png")
    personagem_batalha.draw(win)
    prisco=Image(Point(700,500),"imgs/PRISCO.png")
    prisco.draw(win)
    caixa_dialogo2=Rectangle(Point(350,700),(Point(700,750)))
    caixa_dialogo2.setFill('black')
    caixa_dialogo2.draw(win)
    texto_batalha=Text(Point(530,725),"Sua primeira batalha começa aqui,\n prepare-se!")
    texto_batalha.setFill("white")
    texto_batalha.draw(win)
    win.getMouse()
    texto_batalha.undraw()
    caixa_dialogo2.undraw()
    coracao=Image(Point(150,100),'imgs/coracao_aliado.png')
    HP=Text(Point(905,100),f'{inimigo_1['vida']}')
    HP.setFill("White")
    HP.setSize(20)
    coracao_inimigo=Image(Point(900,100),"imgs/coracao_inimigo.png")
    coracao.draw(win)
    coracao_inimigo.draw(win)
    HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
    HP_personagem.setFill("White")
    HP_personagem.setSize(20)
    HP_personagem.draw(win)
    HP.draw(win)
    while player["vida_atual"]>0 or inimigo_1["vida"]>0:
        tecla=win.getKey()
        turno_player=True
        if tecla == '1' and turno_player== True:
            inimigo_1['vida'] = inimigo_1['vida'] - player['dano']
            print(inimigo_1['vida'])
            HP.undraw()
            HP=Text(Point(905,100),f'{inimigo_1['vida']}')
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)
        if inimigo_1["vida"] <=0:
            break            

def main ():
    win=GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)
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