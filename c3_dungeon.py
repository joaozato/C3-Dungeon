from graphics import *
import time  # importando time para diminuir a velocidade que as letras aparecem no dialogo.
import random as rd

# lista sprites
# VARIAVEIS GLOBAIS !!

player = {
        "nome": "nome_player",
        "vida_max": 100,
        "vida_atual": 100,
        "dano": 20,
        "pocao": 2,
        "dano especial":300,
    }

inimigo_1 = {"vida": 50, "dano": 5}

monstro_neutro = {
        "nome": "monstro_neutro",
        "vida_max": 200,
        "dano_normal": 10,
        "dano_especial": 20,
    }
prisco = {
        "dano":20,
        "vida_max":3000,
    }
cobra = {
        "dano":40,
        "vida_max":500
    }
larissa = {
        'dano':100,
        'vida_max':200
    }

inventarior = {"pocao_de_vida": 3, "espada": 1}

itens = {
    "pocao_de_vida": {
        "nome": "Poção de Vida",
        "tipo": "Consumível",
        "cura": 50,
        "desc": "Restaura os seus pontos de vida",
    },
    "espada": {"nome": "Espada", "tipo": "Arma", "dano": "15", "desc": "É uma espada =D !"},
}

listasprite_costas = [
    "imgs/sprite_personagem/sprite1_costas.png",
    "imgs/sprite_personagem/sprite2_costas.png",
    "imgs/sprite_personagem/sprite3_costas.png",
]
listasprite_frente = [
    "imgs/sprite_personagem/sprite1_frente.png",
    "imgs/sprite_personagem/sprite2_frente.png",
    "imgs/sprite_personagem/sprite3_frente.png",
]
listasprite_esq = [
    "imgs/sprite_personagem/sprite1_esquerda.png",
    "imgs/sprite_personagem/sprite2_esquerda.png",
    "imgs/sprite_personagem/sprite3_esquerda.png",
    "imgs/sprite_personagem/sprite4_esquerda.png",
    "imgs/sprite_personagem/sprite5_esquerda.png",
]
listasprite_dir = [
    "imgs/sprite_personagem/sprite1.png",
    "imgs/sprite_personagem/sprite2.png",
    "imgs/sprite_personagem/sprite3.png",
    "imgs/sprite_personagem/sprite4.png",
    "imgs/sprite_personagem/sprite5.png",
]


def menu(win):
    background1 = Image(Point(540, 400), "imgs/c3.png")  # imagem background do menu
    background1.draw(win)
    font = Image(
        Point(540, 200), "imgs/image-removebg-preview.png"
    )  # fonte utilizada para nome do jogo
    font.draw(win)
    botao_inicial = Rectangle(
        Point(430, 700), Point(630, 750)
    )  # retangulo de botão iniciar
    iniciar = Text(Point(530, 725), "Iniciar")
    iniciar.setSize(20)
    botao_inicial.setFill("orange")
    botao_inicial.draw(win)
    iniciar.draw(win)
    while True:  # enquanto for verdadeiro...
        click = win.getMouse()
        if (430 <= click.getX() <= 630) and (
            700 <= click.getY() <= 750
        ):  # se o usuario clicar no range do botão, então, é levado até o proximo cenário
            botao_inicial.undraw()  # quando ele clica, os botões anteriores e background são apagados levando a função de tela 1.
            iniciar.undraw()
            background1.undraw()
            font.undraw()
            return "fase1"


def inventario(win,player):  
    
    elemento_popup = []
    fundo = Rectangle(Point(50, 50), Point(350, 400))
    fundo.setFill("grey")
    fundo.draw(win)
    elemento_popup.append(fundo)

    y = 50
    titulo = Text(Point(200, 20), "Inventário")
    titulo.setSize(18)
    titulo.setStyle("bold")
    titulo.draw(win)
    elemento_popup.append(titulo)
    
    botoes_usar = {}
    
    for item_id,qnt in inventarior.items():
        if qnt <= 0:
            continue

        if y > 320:
            mensagem = Text(Point(200,350),'idk')
            mensagem.draw(win)
            elemento_popup.append(mensagem)
            break

        info = itens.get(item_id)

        if info:
            nome_completo = info['nome']
            descricao = info['desc']
            tipo = info['tipo']
            
            retangulo = Rectangle(Point(60, y - 15), Point(340, y + 40))
            retangulo.setFill("white")
            retangulo.setOutline("gray")
            retangulo.draw(win)
            elemento_popup.append(retangulo)

            texto_nome = Text(Point(150, y), f"{nome_completo} (x{qnt})")
            texto_nome.setSize(12)
            texto_nome.setStyle("bold")
            texto_nome.draw(win)
            elemento_popup.append(texto_nome)

            texto_desc = Text(Point(150, y + 20), descricao)
            texto_desc.setSize(10)
            texto_desc.draw(win)
            elemento_popup.append(texto_desc)
        
        if tipo == "Consumível":
            botao_x1, botao_y1 = 280, y - 10
            botao_x2, botao_y2 = 330, y + 10
                
            botao_usa = Rectangle(Point(botao_x1, botao_y1), Point(botao_x2, botao_y2))
            botao_usa.setFill("green")
            botao_usa.setOutline("darkgreen")
            botao_usa.draw(win)
            elemento_popup.append(botao_usa)
    
            texto_usar = Text(Point(305, y), "Usar")
            texto_usar.setSize(10)
            texto_usar.setStyle("bold")
            texto_usar.setTextColor("white")
            texto_usar.draw(win)
            elemento_popup.append(texto_usar)
            botoes_usar[item_id] = (botao_x1, botao_y1, botao_x2, botao_y2)
        y += 60
    botao_x1, botao_y1 = 150, 380
    botao_x2, botao_y2 = 250, 410
    
    botao_fecha = Rectangle(Point(botao_x1, botao_y1), Point(botao_x2, botao_y2))
    botao_fecha.setFill("red")
    botao_fecha.setOutline("darkred")
    botao_fecha.draw(win)
    elemento_popup.append(botao_fecha)
    
    texto_fechar = Text(Point(200, 395), "fechar")
    texto_fechar.setSize(12)
    texto_fechar.setStyle("bold")
    texto_fechar.setTextColor("white")
    texto_fechar.draw(win)
    elemento_popup.append(texto_fechar)

    while True:
        p = win.getMouse() 
        if botao_x1 <= p.getX() <= botao_x2 and botao_y1 <= p.getY() <= botao_y2:
            break

        item_usado = ""
        for item_id, (x1, y1, x2, y2) in botoes_usar.items():
            if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
                item_usado = item_id
                break
            
        if item_usado:
            inventarior[item_usado] -= 1
            cura = itens[item_usado].get("cura", 0)
            player['vida_atual'] += cura
            if player['vida_atual'] > player['vida_max']:
                player['vida_atual'] = player['vida_max']
            mensagem = f"usou essa merda de item ai: {itens[item_usado]['nome']} e curou {cura}"

            for item in elemento_popup:
                item.undraw()
            return inventario(win, player)
    
    for item in elemento_popup:
        item.undraw()

    

def fase_jogo(win,player):


    background2 = Image(Point(540, 400), "imgs/floresta2.png")
    background2.draw(win)
    ponto_central = Point(140, 675)
    # retratoo

    foto_retrato = Image(ponto_central, "imgs/principal_menor.png")
    largura_retrato = foto_retrato.getWidth()
    altura_retrato = foto_retrato.getHeight()

    # calculo pra conseguir encaixar o sprite na caixa

    x1 = 140 - (largura_retrato / 2)  # centro - metade do tamanho
    y1 = 675 - (altura_retrato / 2)
    x2 = 140 + (largura_retrato / 2)
    y2 = 675 + (altura_retrato / 2)

    x1_dialogo = x2 + 20  # x2 onde o retrato termina + 20px de espaço
    x2_dialogo = 1030  # x fixo


    caixa_retrato = Rectangle(Point(x1, y1), Point(x2, y2))
    caixa_retrato.draw(win)
    caixa_retrato.setFill("black")
    foto_retrato.draw(win)
    caixa_dialogo = Rectangle(Point(x1_dialogo, y1), Point(x2_dialogo, y2))
    caixa_dialogo.setFill("black")

    # ---textooo---
    centrox_texto = (x1_dialogo + x2_dialogo) / 2
    centroy_texto = (y1 + y2) / 2
    caixa_dialogo.draw(win)

    teste = "Você foi o escolhido para defender o C3\n Em um momento de fragilidade, quando os exames \n estão a beira de acontecer \n as criaturas da infernais querem as almas dos estudantes \n só você pode impedir isso Estudante!"
    teste_texto_atual = ""
    Texto = Text(Point(centrox_texto, centroy_texto), "")
    Texto.setTextColor("white")
    Texto.draw(win)

    for (
        letra
    ) in (
        teste
    ):  # nesse loop inicia a caixa de texto de forma que as letras sejam desenhadas devagar.
        if win.checkMouse():  # se houve click enqt ta mosttando o texto
            Texto.setText(teste)  # se sim mostra o texto completo e para d mostra
            break
        teste_texto_atual = teste_texto_atual + letra
        Texto.setText(teste_texto_atual)
        Texto.setTextColor("white")
        time.sleep(0.05)

    while True:
        click = win.getMouse()
        mx = click.getX()
        my = click.getY()
        if (x1_dialogo <= mx <= x2_dialogo) and (
            y1 <= my <= y2
        ):  # qnd clica passa o texto
            break
    return "fase2"


def fase_jogo2(win,player):  #onde o boneco anda pelo mapa

    LARGURA_MAX = 1080
    ALTURA_MAX = 800

    background_c3 = Image(Point(540, 400), "imgs/background.png")
    background_c3.draw(win)

    # personagem=Image(Point(540,400),"imgs/sprite_personagem/sprite5.png")
    # personagem.draw(win)
    player_x = 540
    player_y = 400
    # sprite_atual.draw(win)

    sprite_atual = Image(
        Point(player_x, player_y), "imgs/sprite_personagem/sprite1_esquerda.png"
    )
    sprite_atual.draw(win)

    ultima_tecla = ""
    andando = True
    cont = 0
    lista = listasprite_frente
    while andando:
        tecla = win.checkKey()
        if tecla == 'f':            #tive que colocar o botão de teste aqui em cima, caso contrário não abre o cenário de batalha
                return 'fase3'
        if tecla == "w" or tecla == "s" or tecla == "d" or tecla == "a":
            sprite_atual.undraw()

            if tecla != ultima_tecla:
                cont = 0
                ultima_tecla = tecla
            if tecla == "a":
                player_x = player_x - 5
                lista = listasprite_esq
            elif tecla == "d":
                player_x = player_x + 5
                lista = listasprite_dir

            # caralho NAO PARA DE DAR INDEX OUT OF RANGEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE

            if cont >= len(lista):
                cont = 0

            sprite_novo = lista[cont]
            sprite_atual = Image(Point(player_x, player_y), sprite_novo)
            sprite_atual.draw(win)
            cont += 1
        time.sleep(0.10)

        if player_x < 0:
            background_c3.undraw()
            sprite_atual.undraw()
            #novo_x = LARGURA_MAX - 50
            #novo_y = player_y
            return "fase4"  #andando para a esquerda vai direto para a batalha da cobra python
        
        elif player_x > LARGURA_MAX:
            background_c3.undraw()
            sprite_atual.undraw()
            #novo_x = 50 
            #novo_y = player_y
            return "fase3"#("fase3", 50, player_y) #leva para a batalha contra AED

#AQUI É AS FUNÇOES DOS MAPAS! 

    #AQUI VOU ADD MESMA LOGICA DA FASE 2, SOQ MUDANDO BACKGROUNDS

def fase_jogo3(win, player, inimigo_1):  #batalha contra aed
    #CONSTRUÇÃO DO CENÁRIO, SPRITES DOS PERSONAGENS QUE VÃO SER UTILIZADOS NAS VERIFICAÇÕES NO CENÁRIO INICIAL

    background3 = Image(Point(540, 400), "imgs/floresta.png")                     #construção da interface e cenário
    personagem_batalha=Image(Point(150,500),"imgs/personagem_combate.png")        #sprite personagem em pose neutra de batalha
    personagem_batalha2=Image(Point(500,500),"imgs/personage_combate_2.png")      #sprite personagem em pose de ataque
    personagem_sofrendo=Image(Point(150,500),'imgs/personagem_sofrendo.png')      #sprite de dano do protagonista
    monstro_neutro=Image(Point(750,500),"imgs/monstro_neutro.png")                #sprite do monstro neutro
    monstro_sofrendo=Image(Point(750,500),'imgs/monstro_sofrendo.png')                #sprite do monstro de dano
    monstro_ataque=Image(Point(300,500),'imgs/monstro_ataque.png')                #sprite ataque monstro
    coracao_inimigo_vivo = Image(Point(900, 100), "imgs/coracao_aliado.png")      #sprite do coração do inimigo enquanto vivo
    coracao_inimigo_morto=Image(Point(900,100),'imgs/coracao_inimigo.png')        #sprite do coração morto
    coracao = Image(Point(150, 100), "imgs/coracao_aliado.png")                   #sprite do coração aliado                   
    prisco_face=Image(Point(245,725),'imgs/prisco_face.png')                      #rosto do mestre prisco

    #CONSTRUÇÃO DAS CAIXAS DE DIALOGO, ICONES DE INTERFACE E VARIAVEIS DE HP

    caixa_dialogo2=Rectangle(Point(320,650),(Point(740,800)))                     #caixa de dialogo
    caixa_dialogo2.setFill('black')                                               #cor da caixa
    texto_batalha=Text(Point(530,725),"Sua primeira batalha começa aqui,\n prepare-se!\n Aperte 1 para ataque normal, e 2 para ataque especial \n.")
    texto_batalha.setFill("white")                                                #cor do texto dentro dela
    HP = Text(Point(905, 100), f"{inimigo_1['vida']}")                            #variavel de hp do inimigo que será utilizada na tela
    HP.setFill("White")                                                           #setando a cor do texto da variavel
    HP.setSize(20)                                                                #o tamanho
    HP_personagem = Text(Point(155, 100), f"{player['vida_atual']}")              #variavel da vida do player que sera utilizada na tela
    HP_personagem.setFill("White")                                                #cor do texto da variavel
    HP_personagem.setSize(20)                                                     #tamanho
    efeito_dano=Image(Point(600,500),'imgs/efeito_dano.png')                      #sprite de dano acionado quando ataca o inimigo
    ataque_icon = Image(Point(230,100),'imgs/Attack.png')                         #icone de ataque na interface
    ataque_icon_ativo=Image(Point(230,100),'imgs/Attack_ativo.png')               #icone de ataque ativado quando o jogador aperta a tecla
    power_icon_ativado=Image(Point(290,100),'imgs/Power_ativado.png')             #icone de ataque forte ativado quando o jogador aperta a tecla
    power_icon= Image(Point(290,100),'imgs/Power.png')                            #icone de ataque power na interface

    #DESENHO DAS VARIAVEIS NA TELA

    background3.draw(win)                                                         
    coracao_inimigo_vivo.draw(win)                                               
    HP_personagem.draw(win)
    monstro_neutro.draw(win)                                                        
    coracao.draw(win)                                       #DESENHA TODAS AS VARIAVEIS DO BLOCO ACIMA
    prisco_face.draw(win)                                                           
    HP.draw(win)                                                                
    ataque_icon.draw(win)
    power_icon.draw(win)
    caixa_dialogo2.draw(win)
    texto_batalha.draw(win)
    personagem_batalha.draw(win)  


    
    
    # INICIALIZAÇÃO DO COMBATE                                                  #spawn do personagem
    win.getMouse()                                                                  #aguarda o click do mouse
    texto_batalha.undraw()
    caixa_dialogo2.undraw()        #é apagado os sprites anteriores para o inicio da batalha.
    prisco_face.undraw()                                         
    especial_count=1                                                            #contador de especial durante a batalha
    while player["vida_atual"]>0 or inimigo_1["vida"]>0:                        #loop para batalha
        tecla=win.getKey()
        turno_player=True
        #condição se o jogador utiliza a primeira skill de luta
        if tecla=='f':
            return 'fase4'
        if tecla == 'i':
            inventario(win,player)
            HP_personagem.undraw()
            HP_personagem = Text(Point(155, 100), f"{player['vida_atual']}")              #variavel da vida do player que sera utilizada na tela
            HP_personagem.setFill("White")                                                #cor do texto da variavel
            HP_personagem.setSize(20) 
            #monstro_neutro.undraw()
            #personagem_batalha.undraw()
            continue
        if tecla == '1' and turno_player== True:                                #jogador ataca
            ataque_icon_ativo.draw(win)                                         #espada em cima da interface pisca sinalizando que está ativa
            time.sleep(0.9)                                                     #delay até ela desaparecer
            ataque_icon_ativo.undraw()                                          #ela desaparece
            personagem_batalha.undraw()                                         #sprite de personagem neutro desaparece
            personagem_batalha2.draw(win)                                       #sprite de ataque do personagem aparece
            efeito_dano.draw(win)                                               #efeito de ataque   
            monstro_neutro.undraw()                                             #sprite monstro neutro some
            monstro_sofrendo.draw(win)                                              #monstro sofre o dano com o sprite aparecendo
            time.sleep(0.7)                                                     #pequeno delay 
            monstro_sofrendo.undraw() 
            personagem_batalha2.undraw()
            monstro_neutro.draw(win)
            personagem_batalha.draw(win)                                                #sprite do monstro desaparece
            inimigo_1['vida'] = inimigo_1['vida'] - player['dano']                          #recebe a variavel de dano
        #condição se o jogador aperta o super poder
        if tecla == '2' and turno_player == True:   # falta deixar a permissão pra só um ataque especial, se colocar o jogo buga por redesenhar uma imagem, já que essa verificação é pulada, ele ignora e vai direto pro else.p
            monstro_neutro.undraw()
            personagem_batalha.undraw()                                       #código para o super especial
            power_icon_ativado.draw(win)
            personagem_batalha2.draw(win)
            monstro_sofrendo.draw(win)
            time.sleep(0.9)
            monstro_sofrendo.undraw()
            power_icon_ativado.undraw()
            inimigo_1["vida"] = inimigo_1['vida'] - player['dano especial']
            HP.undraw()
            HP = Text(Point(905, 100), f"{inimigo_1['vida']}")
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)
            player["vida_atual"]= player["vida_atual"]-inimigo_1["dano"]
            especial_count -=1
        #condição se o inimigo morre

        if inimigo_1["vida"] <= 0:
            coracao_inimigo_vivo.undraw()
            coracao_inimigo_morto.draw(win)
            HP.undraw()                                                        #aqui o hp é atualizado, 
            HP=Text(Point(905,100),f'{inimigo_1['vida']}')                     #do inimigo
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)                                                        #faz a verificação mais importante, se for menor que zero, o monstro morre e a batalha nao continua
            monstro_neutro.undraw()                                             #animação de morte do monstro
            efeito_dano.undraw()                                                #efeito some
            monstro_morto=Image(Point(750,500),'imgs/monstro_morto.png')        #mais declarações de variaveis de imagens
            monstro_morto2=Image(Point(750,500),'imgs/monstro_morto2.png')
            monstro_morto.draw(win)                                             #sprite do monstro morrendo
            time.sleep(0.8)                                                     #delay antes dele fechar os olhos e morrer
            monstro_morto.undraw()
            monstro_morto2.draw(win)
            time.sleep(0.2)
            personagem_batalha2.undraw()
            personagem_batalha.draw(win)
        #aqui usamos um ELSE porquê é impossivel do jogador morrer para esse inimigo, ele é a batalha mais fácil. 
        #CASO A VIDA NÃO CHEGUE A ZERO A BATALHA CONTINUA E O MONSTRO ATACA <-- ??
        monstro_neutro.draw(win)                                        #monstro volta a ser neutro
        HP.undraw()                                                     #aqui o hp é atualizado, 
        HP=Text(Point(905,100),f'{inimigo_1['vida']}')                  #do inimigo
        HP.setFill("White")
        HP.setSize(20)
        HP.draw(win)
        print(inimigo_1['vida'])                                        #printa na tela
        time.sleep(0.3) #delay para animação             
        efeito_dano.undraw()                        
        personagem_batalha2.undraw()
        personagem_batalha.draw(win)                                    
        time.sleep(0.7)                                                 #delay antes do monstro atacar
        monstro_neutro.undraw()
        monstro_ataque.draw(win)                                        #monstro ataca
        personagem_batalha.undraw()
        personagem_sofrendo.draw(win)                                   #personagem recebe dano
        time.sleep(0.9)                                                 #delay para animação de dano do monstro
        monstro_ataque.undraw()
        monstro_neutro.draw(win)
        personagem_sofrendo.undraw()
        personagem_batalha.draw(win)
        time.sleep(0.2)                                         
        player["vida_atual"]= player["vida_atual"]-inimigo_1["dano"]       #aqui fica a impressão do dano logo após o personagem executar
        HP_personagem.undraw()                                             #uma ação
        HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
        HP_personagem.setFill("White")
        HP_personagem.setSize(20)
        HP_personagem.draw(win)                                            #hp do personagem aparece na tela atualizado
        if inimigo_1["vida"] <=0 or player["vida_atual"] <= 0:
            break
    #aqui serão 'des'desenhadas as coisas do cenário quando o jogador clicar com o mouse
    win.getMouse()
    background3.undraw()
    #personagem_batalha.undraw()
    monstro_neutro.undraw() 
    HP.undraw()
    HP_personagem.undraw()
    coracao.undraw()
    coracao_inimigo_vivo.undraw()
    ataque_icon.undraw()
    power_icon.undraw()
    return 'fase2'             #levando a fase 4 (agora vai levar ao cenario de transição)
'''
No geral dentro da função 3, ocorre um loop que define toda a batalha, com loops de animações, já que o jogo funciona
em turnos, o que acontece é a aparição das animações, com os delays setados para dar a impressão de movimento, e
que o jogador consiga visualizar o que está acontecendo com calma, existe um if no meio para verificar a vida do inimigo, já
que antes havia um bug que o inimigo mesmo com a vida <0 , acabava te batendo e não morrendo, isso foi resolvido com uma verificação
que caso contrário for falsa, continua a batalha.
'''

def fase_jogo4 (win,player,cobra): # batalha cobra
    #realiza declaração de variaveis que serão usadas
    #aqui são declaradas o cenário, personagem e inimigo.
    background4=Image(Point(540,400),"imgs/background4.png")                           #construção da interface e cenário
    cobraimg=Image(Point(750,500),'imgs/cobra.png')
    personagem_batalha=Image(Point(150,500),"imgs/personagem_combate.png")          
    personagem_batalha2=Image(Point(500,500),"imgs/personage_combate_2.png")
    personagem_batalha3=Image(Point(500,500),"imgs/personagem_ataque_espada.png")
    personagem_sofrendo=Image(Point(150,500),'imgs/personagem_sofrendo.png')
    personagem_morto=Image(Point(150,500),'imgs/personagem_morto.png')
    personagem_morto2=Image(Point(150,500),'imgs/personagem_morto2.png')
    prisco_face=Image(Point(245,725),'imgs/prisco_face.png')
    cobra_ataque=Image(Point(400,500),'imgs/cobra_ataque.png')
    cobra_dano=Image(Point(750,500),'imgs/cobra_dano.png')
    cobra_morrendo=Image(Point(300,500),'imgs/cobra_morrendo.png')
    cobra_morrendo2=Image(Point(300,500),'imgs/cobra_morrendo2.png')


    #declara os icones como barras de HP aliada e inimiga, as caixas de dialogo e o texto da batalha

    ataque_icon = Image(Point(230,100),'imgs/Attack.png')
    ataque_icon_ativo=Image(Point(230,100),'imgs/Attack_ativo.png')                     #desenha os icones
    power_icon_ativado=Image(Point(290,100),'imgs/Power_ativado.png')
    power_icon= Image(Point(290,100),'imgs/Power.png')                                  #spawn do personagem
    coracao=Image(Point(150,100),'imgs/coracao_aliado.png')
    coracao_inimigo_morto=Image(Point(900,100),'imgs/coracao_inimigo.png')
    coracao_inimigo_vivo=Image(Point(900,100),"imgs/coracao_aliado.png")
    HP=Text(Point(905,100),f'{cobra['vida_max']}')
    HP.setFill("White")
    HP.setSize(20)
    HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
    HP_personagem.setFill("White")
    HP_personagem.setSize(20)
    caixa_dialogo2=Rectangle(Point(320,650),(Point(740,800)))
    caixa_dialogo2.setFill('black')
    texto_batalha=Text(Point(530,725),'Sua segunda batalha, agora contra o \n segundo maior inimigo do estudante,\n o Python!')
    texto_batalha.setFill("white")

    #a partir daqui desenha as variaveis

    background4.draw(win)
    personagem_batalha.draw(win)
    cobraimg.draw(win)
    caixa_dialogo2.draw(win)
    prisco_face.draw(win)
    texto_batalha.draw(win)
    HP.draw(win)                                                                #desenha os hps
    HP_personagem.draw(win)
    coracao_inimigo_vivo.draw(win)
    coracao.draw(win)
    ataque_icon.draw(win)
    power_icon.draw(win)


    # define o que vai sumir antes de começar a batalha.
    win.getMouse()           
    prisco_face.undraw()
    texto_batalha.undraw()
    caixa_dialogo2.undraw()
    while player['vida_atual'] >0 and cobra['vida_max'] >0:
        tecla=win.getKey()
        #botao de atalho de teste para ir para a próxima fase, o jogador não deve apertar
        if tecla=='f':
            return 'fase5'
        if tecla == 'i':
            inventario(win,player)
            continue
        #ataque comum
        if tecla == '1' and player['vida_atual']> 0:                            #jogador ataca
            ataque_icon_ativo.draw(win)                                         #espada em cima da interface pisca sinalizando que está ativa
            time.sleep(0.9)                                                     #delay até ela desaparecer
            ataque_icon_ativo.undraw()                                          #ela desaparece
            personagem_batalha.undraw()                                         #sprite de personagem neutro desaparece
            personagem_batalha3.draw(win)                                       #sprite de ataque do personagem aparece                                               #efeito de ataque   
            cobraimg.undraw()                                                   #sprite monstro neutro some
            cobra_dano.draw(win)                                                #monstro sofre o dano com o sprite aparecendo
            time.sleep(0.7)                                                     #pequeno delay 
            cobra_dano.undraw()                                                 #sprite do monstro desaparece
            cobra['vida_max'] = cobra['vida_max'] - player['dano']              #recebe a variavel de dano
            #aqui fazemos o loop do poder 2, o mais forte do personagem
        if tecla == '2' and player['vida_atual']>0:                             # falta deixar a permissão pra só um ataque especial, se colocar o jogo buga por redesenhar uma imagem, já que essa verificação é pulada, ele ignora e vai direto pro else.p
            cobraimg.undraw()
            personagem_batalha.undraw()                                         #código para o super especial
            power_icon_ativado.draw(win)
            personagem_batalha3.draw(win)
            cobra_dano.draw(win)
            time.sleep(0.9)
            cobra_dano.undraw()
            power_icon_ativado.undraw()
            cobra["vida_max"] = cobra['vida_max'] - player['dano especial']
            HP.undraw()
            HP = Text(Point(905, 100), f"{cobra['vida_max']}")
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)
            player["vida_atual"]= player["vida_atual"]-cobra["dano"]
        
        #verificação da vida maxima do oponente      
        if cobra["vida_max"] <= 0:
            coracao_inimigo_vivo.undraw()
            coracao_inimigo_morto.draw(win)
            HP.undraw()                                                        #aqui o hp é atualizado, 
            HP=Text(Point(905,100),f'{cobra['vida_max']}')                     #do inimigo
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)                                                        #faz a verificação mais importante, se for menor que zero, o monstro morre e a batalha nao continua
            cobraimg.undraw()                                                   #animação de morte do monstro                                           
            cobra_morrendo=Image(Point(750,500),'imgs/cobra_morrendo.png')        #mais declarações de variaveis de imagens
            cobra_morrendo2=Image(Point(750,500),'imgs/cobra_morrendo2.png')
            cobra_morrendo.draw(win)                                             #sprite do monstro morrendo
            time.sleep(0.8)                                                     #delay antes dele fechar os olhos e morrer
            cobra_morrendo.undraw()
            cobra_morrendo2.draw(win)
            time.sleep(0.2)
            personagem_batalha3.undraw()
            personagem_batalha.draw(win)
            win.getMouse()
            return 'fase5'  #caso o jogador o mate, retornamos para a proxima fase
            
        
        #batalha continua caso o jogador não mate a cobra ou nao seja morto                                                             
        cobraimg.draw(win)                                              #monstro volta a ser neutro
        HP.undraw()                                                     #aqui o hp é atualizado, 
        HP=Text(Point(905,100),f'{cobra['vida_max']}')                  #do inimigo
        HP.setFill("White")
        HP.setSize(20)
        HP.draw(win)
        print(cobra['vida_max'])                                        #printa na tela
        time.sleep(0.3)                                                 #delay para animação                                    
        personagem_batalha3.undraw()
        personagem_batalha.draw(win)                                    
        time.sleep(0.7)                                                 #delay antes do monstro atacar
        cobraimg.undraw()
        cobra_ataque.draw(win)                                          #monstro ataca
        personagem_batalha.undraw()
        personagem_sofrendo.draw(win)                                   #personagem recebe dano
        time.sleep(0.9)                                                 #delay para animação de dano do monstro
        cobra_ataque.undraw()
        cobraimg.draw(win)
        personagem_sofrendo.undraw()
        personagem_batalha.draw(win)
        time.sleep(0.2)                                         
        player["vida_atual"]= player["vida_atual"]-cobra["dano"]       #aqui fica a impressão do dano logo após o personagem executar
        HP_personagem.undraw()                                             #uma ação
        HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
        HP_personagem.setFill("White")
        HP_personagem.setSize(20)
        HP_personagem.draw(win)       

        #verificação caso o jogador morra 
        if player['vida_atual'] <= 0:
            personagem_sofrendo.undraw()
            personagem_batalha3.undraw()
            personagem_batalha.undraw()
            personagem_morto.draw(win)
            time.sleep(0.7)
            personagem_morto.undraw()
            personagem_morto2.draw(win)
            texto_fim= Text(Point(540,400),'VOCÊ PERDEU \n CLIQUE PARA TENTAR NOVAMENTE')
            texto_fim.setSize(30)
            texto_fim.setTextColor('red')
            texto_fim.setStyle('bold')
            texto_fim.draw(win)
            win.getMouse()
            #da a opção do jogador clicar na tela para reiniciar, o cenário é resetado e as variáveis também.
            texto_fim.undraw()
            personagem_morto2.undraw()
            background4.undraw()
            cobraimg.undraw()
            HP.undraw()
            HP_personagem.undraw()
            coracao.undraw()
            coracao_inimigo_morto.undraw()
            coracao_inimigo_vivo.undraw()
            ataque_icon.undraw()
            power_icon.undraw()
            player['vida_atual']=100
            cobra['vida_max']=500
            return 'fase4'
        
def fase_jogo5(win,player,prisco,larissa):
    #declaração de variaveis de cenário e sprites
    background_final=Image(Point(540,400),'imgs/batalha_final.png')
    evil_prisco=Image(Point(750,500),'imgs/evil_prisco.png')
    evil_prisco_ataque=Image(Point(750,500),'imgs/evil_prisco_attack.png')
    evil_prisco_morte=Image(Point(750,500),'imgs/evil_prisco_fraco.png')
    evil_prisco_morte2=Image(Point(750,500),'imgs/evil_prisco_morto.png')
    evil_prisco_dano=Image(Point(750,500),'imgs/prisco_dano.png')
    personagem_batalha=Image(Point(150,500),"imgs/personagem_combate.png")          
    personagem_batalha2=Image(Point(500,500),"imgs/personage_combate_2.png")
    personagem_batalha3=Image(Point(500,500),"imgs/personagem_ataque_espada.png")
    personagem_sofrendo=Image(Point(150,500),'imgs/personagem_sofrendo.png')
    personagem_morto=Image(Point(150,500),'imgs/personagem_morto.png')
    personagem_morto2=Image(Point(150,500),'imgs/personagem_morto2.png')
    larissa_ataque=Image(Point(890,500),'imgs/larissa_ataque.png')
    larissa_super=Image(Point(890,500),'imgs/larissa_super.png')
    larissa_dano=Image(Point(280,500),'imgs/larissa_dano.png')
    
    #Caixas de dialogos

    caixa_dialogo2=Rectangle(Point(320,650),(Point(740,800)))                     #caixa de dialogo
    caixa_dialogo2.setFill('black')                                               #cor da caixa
    texto_batalha=Text(Point(530,725),"Eu lamento muito informar a você \n que eu estou do lado das criaturas algoritmicas\n vocês todos irão reprovar!")
    texto_batalha.setFill("white")
    texto_batalha2=Text(Point(530,725),'Não se preocupa estudante!\n to aqui pra te ajudar\n, a larissa do JS vai acabar com o velhote!')    
    texto_batalha2.setFill("white")
    prisco_dialogo=Image(Point(230,725),'imgs/evil_prisco_dialogo.png')
    personagem_assustado=Image(Point(20,725),'imgs/personagem_assustado.png')
    larissa_dialogo=Image(Point(230,680),'imgs/larissa_dialogo.png')
    larissa_batalha=Image(Point(280,500),'imgs/larissa_neutra.png')
    larissa_voando=Image(Point(280,300),'imgs/larissa_voando.png')
    


    #Icones
    ataque_icon = Image(Point(230,100),'imgs/Attack.png')
    ataque_icon_ativo=Image(Point(230,100),'imgs/Attack_ativo.png')                     #desenha os icones
    power_icon_ativado=Image(Point(290,100),'imgs/Power_ativado.png')
    power_icon= Image(Point(290,100),'imgs/Power.png')                                  #spawn do personagem
    coracao=Image(Point(150,100),'imgs/coracao_aliado.png')
    coracao_inimigo_morto=Image(Point(900,100),'imgs/coracao_inimigo.png')
    coracao_inimigo_vivo=Image(Point(900,100),"imgs/coracao_aliado.png")
    HP=Text(Point(905,100),f'{prisco['vida_max']}')
    HP.setFill("White")
    HP.setSize(20)
    HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
    HP_personagem.setFill("White")
    HP_personagem.setSize(20)

    #primeira cena    com um tom de humor, dialogo do prisco dizendo que está do lado do mal
    background_final.draw(win)
    prisco_dialogo.draw(win)
    caixa_dialogo2.draw(win)
    texto_batalha.draw(win)
    evil_prisco.draw(win)
    personagem_batalha.draw(win)

    win.getMouse()

    #segunda cena            #onde a larissa aparece dizendo que vai te salvar e te ajudar
    prisco_dialogo.undraw()
    texto_batalha.undraw()
    personagem_assustado.draw(win)
    texto_batalha2.draw(win)
    larissa_dialogo.draw(win)
    win.getMouse()

    #terceira cena       #cena da larissa chegando voando 
    
    larissa_voando.draw(win)
    time.sleep(0.5)
    larissa_voando.undraw()
    larissa_batalha.draw(win)

    #quarta cena que leva pra batalha

    win.getMouse()
    larissa_dialogo.undraw()
    caixa_dialogo2.undraw()
    texto_batalha2.undraw()
    HP.draw(win)                                                                #desenha os hps
    HP_personagem.draw(win)
    coracao_inimigo_vivo.draw(win)
    coracao.draw(win)
    ataque_icon.draw(win)
    power_icon.draw(win)

    while player['vida_atual'] >0 and prisco['vida_max']>0:
        tecla=win.getKey()
        if tecla == '1' and player['vida_atual']> 0:                                #jogador ataca
            ataque_icon_ativo.draw(win)                                         #espada em cima da interface pisca sinalizando que está ativa
            time.sleep(0.9)                                                     #delay até ela desaparecer
            ataque_icon_ativo.undraw()                                          #ela desaparece
            personagem_batalha.undraw()  
            larissa_batalha.undraw()                                       #sprite de personagem neutro desaparece
            personagem_batalha3.draw(win)                       
            larissa_ataque.draw(win)                #sprite de ataque do personagem aparece                                               #efeito de ataque   
            evil_prisco.undraw()                                             #sprite monstro neutro some
            evil_prisco_dano.draw(win)                                              #monstro sofre o dano com o sprite aparecendo
            time.sleep(0.7)           
            larissa_ataque.undraw()                                         #pequeno delay 
            evil_prisco_dano.undraw()
            larissa_batalha.draw(win)
            prisco['vida_max'] = prisco['vida_max'] - player['dano']
            prisco['vida_max'] = prisco['vida_max'] - larissa['dano']      
        if tecla == '2' and player['vida_atual']>0:   # falta deixar a permissão pra só um ataque especial, se colocar o jogo buga por redesenhar uma imagem, já que essa verificação é pulada, ele ignora e vai direto pro else.p
            evil_prisco.undraw()
            personagem_batalha.undraw()
            larissa_batalha.undraw()                                         #código para o super especial
            power_icon_ativado.draw(win)
            personagem_batalha3.draw(win)
            larissa_super.draw(win)
            evil_prisco_ataque.draw(win)
            time.sleep(0.9)
            evil_prisco_ataque.undraw()
            power_icon_ativado.undraw()
            larissa_super.undraw()
            larissa_batalha.draw(win)
            prisco["vida_max"] = prisco['vida_max'] - player['dano especial']
            HP.undraw()
            HP = Text(Point(905, 100), f"{prisco['vida_max']}")
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)
            player["vida_atual"]= player["vida_atual"]-prisco["dano"]
        if prisco["vida_max"] <= 0:
            coracao_inimigo_vivo.undraw()
            coracao_inimigo_morto.draw(win)
            HP.undraw()                                                        #aqui o hp é atualizado, 
            HP=Text(Point(905,100),f'{prisco['vida_max']}')                     #do inimigo
            HP.setFill("White")
            HP.setSize(20)
            HP.draw(win)                                                        #faz a verificação mais importante, se for menor que zero, o monstro morre e a batalha nao continua
            evil_prisco.undraw()                                                   #animação de morte do monstro                                           
            evil_prisco_morte.draw(win)                                             #sprite do monstro morrendo
            time.sleep(0.8)                                                     #delay antes dele fechar os olhos e morrer
            evil_prisco_morte.undraw()
            evil_prisco_morte2.draw(win)
            time.sleep(0.2)
            personagem_batalha3.undraw()
            personagem_batalha.draw(win)
            win.getMouse()

        evil_prisco.draw(win)                                        #monstro volta a ser neutro
        HP.undraw()                                                     #aqui o hp é atualizado, 
        HP=Text(Point(905,100),f'{prisco['vida_max']}')                  #do inimigo
        HP.setFill("White")
        HP.setSize(20)
        HP.draw(win)
        print(prisco['vida_max'])                                        #printa na tela
        time.sleep(0.3) #delay para animação                                    
        personagem_batalha3.undraw()
        personagem_batalha.draw(win)                                    
        time.sleep(0.7)                                                 #delay antes do monstro atacar
        evil_prisco.undraw()
        evil_prisco_ataque.draw(win)                                        #monstro ataca
        personagem_batalha.undraw()
        larissa_batalha.undraw()
        personagem_sofrendo.draw(win)
        larissa_dano.draw(win)                                   #personagem recebe dano
        time.sleep(0.9)                                                 #delay para animação de dano do monstro
        evil_prisco_ataque.undraw()
        evil_prisco.draw(win)   
        personagem_sofrendo.undraw()
        larissa_dano.undraw()
        personagem_batalha.draw(win)
        larissa_batalha.draw(win)
        time.sleep(0.2)                                         
        player["vida_atual"]= player["vida_atual"]-prisco["dano"]       #aqui fica a impressão do dano logo após o personagem executar
        HP_personagem.undraw()                                             #uma ação
        HP_personagem=Text(Point(155,100),f"{player['vida_atual']}")
        HP_personagem.setFill("White")
        HP_personagem.setSize(20)
        HP_personagem.draw(win)        
        if player['vida_atual'] <= 0:
            personagem_sofrendo.undraw()
            personagem_batalha3.undraw()
            personagem_batalha.undraw()
            personagem_morto.draw(win)
            time.sleep(0.7)
            personagem_morto.undraw()
            personagem_morto2.draw(win)
            texto_fim= Text(Point(540,400),'VOCÊ PERDEU \n CLIQUE PARA TENTAR NOVAMENTE')
            texto_fim.setSize(30)
            texto_fim.setTextColor('red')
            texto_fim.setStyle('bold')
            texto_fim.draw(win)
            win.getMouse()
            
            texto_fim.undraw()
            personagem_morto2.undraw()
            background_final.undraw()
            evil_prisco.undraw()
            HP.undraw()
            HP_personagem.undraw()
            coracao.undraw()
            coracao_inimigo_morto.undraw()
            coracao_inimigo_vivo.undraw()
            ataque_icon.undraw()
            power_icon.undraw()
            player['vida_atual']=100
            prisco['vida_max']=3000
            return 'fase5'

    #SEGUE A MESMA LÓGICA DA FASE ANTERIOR, POR ISSO NÃO COLOQUEI TANTAS DESCRIÇÕES    


def main ():
    win=GraphWin('C3 Dungeon', 1080, 800)
    telas=menu(win)

   
    while True:

        # ATENÇAO PRA NAO CHAMAR DUAS VZS
        if telas == "fase1":
            telas = fase_jogo(win,player)
        elif telas == "fase2":
            telas = fase_jogo2(win,player)
        elif telas == "fase3":
            telas = fase_jogo3(win, player, inimigo_1)
        elif telas == 'fase4':
            telas = fase_jogo4(win,player,cobra)
        elif telas == 'fase5':
           telas = fase_jogo5(win,player,prisco,larissa)

main()
