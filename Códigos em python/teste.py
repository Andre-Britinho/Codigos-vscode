import random

vida_monstro = 100
sua_vida = 100
bool = True

print("Vida do monstro = {}".format(vida_monstro))
print("Vida do jogador = {}".format(sua_vida))
print("\n")

while(bool):
    joga_dado = input("Pressione d para jogar o dado: ")
    
    if(joga_dado == 'd'):
        dado = random.randrange(1,21)
        print("Você tirou {} no dado".format(dado))
        
        #Dado com valor = a 20
        if(dado == 20):
            ataque = input("Pressione a para atacar: ")
            if(ataque == 'a'):
                #seu ataque e dano no monstro
                seu_dano_ataque = random.randrange(10,21)
                print("O dano do seu ataque é = {}".format(seu_dano_ataque))
                vida_monstro -= seu_dano_ataque
                print("Vida do monstro = {}".format(vida_monstro))
                
                #ataque do monstro e dano em você
                dano_ataque_monstro = random.randrange(1,5)
                print("O dano do ataque do monstro é = {}".format(dano_ataque_monstro))
                sua_vida -= dano_ataque_monstro
                print("Sua vida é = {}".format(sua_vida))
                print("\n")
                
                if(vida_monstro <= 0 and sua_vida <= 0):
                    print("Você e o monstro morreram")      
                elif(vida_monstro <= 0):
                    print("Você derrotou o monstro")
                    bool = False
                elif(sua_vida <= 0):
                    print("Você morreu")
                    bool = False
                
        #Dado com valor entre 12 e 19
        elif(dado >= 12 and dado <= 19):
            ataque = input("Pressione a para atacar: ")
            if(ataque == 'a'):
                #seu ataque e dano no monstro
                seu_dano_ataque = random.randrange(6,21)
                print("O dano do seu ataque é = {}".format(seu_dano_ataque))
                vida_monstro -= seu_dano_ataque
                print("Vida do monstro = {}".format(vida_monstro))
                
                #ataque do monstro e dano em você
                dano_ataque_monstro = random.randrange(1,13)
                print("O dano do ataque do monstro é = {}".format(dano_ataque_monstro))
                sua_vida -= dano_ataque_monstro
                print("Sua vida é = {}".format(sua_vida))
                print("\n")
                
                if(vida_monstro <= 0 and sua_vida <= 0):
                    print("Você e o monstro morreram")      
                elif(vida_monstro <= 0):
                    print("Você derrotou o monstro")
                    bool = False
                elif(sua_vida <= 0):
                    print("Você morreu")
                    bool = False
                
        #Dado com valor entre 2 e 11
        elif(dado >= 2 and dado <= 11):
            ataque = input("Pressione a para atacar: ")
            if(ataque == 'a'):
                #seu ataque e dano no monstro
                seu_dano_ataque = random.randrange(1,13)
                print("O dano do seu ataque é = {}".format(seu_dano_ataque))
                vida_monstro -= seu_dano_ataque
                print("Vida do monstro = {}".format(vida_monstro))
                
                #ataque do monstro e dano em você
                dano_ataque_monstro = random.randrange(6,21)
                print("O dano do ataque do monstro é = {}".format(dano_ataque_monstro))
                sua_vida -= dano_ataque_monstro
                print("Sua vida é = {}".format(sua_vida))
                print("\n")
                
                if(vida_monstro <= 0 and sua_vida <= 0):
                    print("Você e o monstro morreram")      
                elif(vida_monstro <= 0):
                    print("Você derrotou o monstro")
                    bool = False
                elif(sua_vida <= 0):
                    print("Você morreu")
                    bool = False
                
        #dado com valor  = a 0    
        else:
            ataque = input("Pressione a para atacar: ")
            if(ataque == 'a'):
                #seu ataque e dano no monstro
                seu_dano_ataque = random.randrange(1,5)
                print("O dano do seu ataque é = {}".format(seu_dano_ataque))
                vida_monstro -= seu_dano_ataque
                print("Vida do monstro = {}".format(vida_monstro))
                    
                #ataque do monstro e dano em você
                dano_ataque_monstro = random.randrange(10,21)
                print("O dano do ataque do monstro é = {}".format(dano_ataque_monstro))
                sua_vida -= dano_ataque_monstro
                print("Sua vida é = {}".format(sua_vida))
                print("\n")
                    
                if(vida_monstro <= 0 and sua_vida <= 0):
                    print("Você e o monstro morreram")      
                elif(vida_monstro <= 0):
                    print("Você derrotou o monstro")
                    bool = False
                elif(sua_vida <= 0):
                    print("Você morreu")
                    bool = False
