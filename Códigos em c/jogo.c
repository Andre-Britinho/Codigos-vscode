#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void comecoDeJogo(){
    printf("Voce eh chamado para investigar uma antiga loja que havia sido invadida na noite passada.\n");
    printf("Chegando na loja voce se depara com um ambiente escuro, janelas quebradas, portas rangendo.\n");
    printf("Entrando, voce percebe manchas de sangue nas paredes e chao e ao final das manchas uma criatura.\n");
    printf("A criatura esta parada e voce tenta uma abordagem silenciosa para acabar com ela.\n");
    printf("Derrota-la vai ajudar a entender a situacao sobre a noite passada.\n");
    printf("\n");    
}

void fimDeJogo(){
    printf("Vasculhando o cadaver da criatura voce um mapa e um nome.\n");
    printf("ALCHEMAX, localizada em um lugar entre montanhas.\n");
    printf("O nome nao eh estranho e voce tem uma leve ideia de onde pode ser esse lugar.\n");
    printf("Enquanto esta se arrumando para sair da loja, voce escuta barulhos estranhos no telhado.\n");
    printf("Voce se depara com mais criaturas perto de voce e uma delas consegue entrar.\n");
    printf("CONTINUA.\n");

}

void verificaDado(int rolagem){
    if(rolagem == 20){
        printf("Cada passo que voce da em direcao a criatura eh o mais preciso e silencioso possivel.\n");
        printf("Voce tira sua faca da bainha e enfia na nuca da criatura que nem fazia ideia que voce estava la.\n");
        printf("\n");
    }

    else if(rolagem >= 12 && rolagem <= 19){
        printf("Voce tenta o seu melhor para nao chamar a atencao da criatura mas quando voce saca sua arma a criatura se levanta.\n");
        printf("Ela te ataca mas nao acerta em cheio, voce se recupera, dispara e elimina a criatura.\n");
        printf("\n");
    }

    else if(rolagem >=2 && rolagem <= 11){
        printf("Ao tentar se aproximar voce deixa cair uma moeda de seu bolso.\n");
        printf("A criatura, mesmo apos o barulho, aparenta estar imovel.\n");
        printf("Ao se abaixar para pegar a moeda, a criatura parte com tudo para cima de voce, arrancando um braco na investida.\n");
        printf("Voce grita de dor e no reflexo dispara contra ela, matando-a.\n");
        printf("\n");
        printf("Voce perde bastante sangue, deixando um rastro ao sair da loja\n");
        printf("Voce esta com bastante dor e se apoia em um carro para recuperar as forcar e seguir em frente.\n");
        printf("Sua visao esta meio enevoada, sem conseguir distinguir as coisas que estao ao redor.\n");
        printf("Voce avista uma pessoa se aproximando e pede ajuda.\n");
        printf("Ao se aproximar voce identifica um som familiar, que tinha escutado a pouco tempo.\n");
        printf("CONTINUA.\n");
        printf("\n");
    }

    else{
        printf("Ao ver a criatura voce se sente extremamente nervoso e tenta disparar mas voce erra.\n");
        printf("A criatura ao ouvir o disparo rapidamente se levanta e num piscar de olhos te ataca com toda forca possivel.\n");
        printf("Voce grita ao cair lentamente, sem uma das pernas e um pedaco do braco.\n");
        printf("Ela pisa no meio da sua barriga, ruge muito alto e solta um ataque que arranca sua cabeca.\n");
        printf("Fim de jogo.\n");
    }
}

int main(){
    comecoDeJogo();  

    char dado;
    printf("Rode o dado: ");
    scanf(" %c", &dado);
    printf("\n");

    int segundos = time(0);
    srand(segundos);
    int numerogrande = rand();

    int rolagem = numerogrande % 21;
    
    if(rolagem == 0){
        rolagem += 1;
    }

    if(dado == 'd'){
        printf("Resultado do dado = %d\n", rolagem);
    }

    printf("\n");

    verificaDado(rolagem);
    
    if(rolagem >= 12 && rolagem <= 20){
        fimDeJogo();
    }
}