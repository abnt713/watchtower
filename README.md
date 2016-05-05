# Watchtower
The last stand against the darkness

## Sobre ##
*Nota: Este é um projeto em sua primeira fase de desenvolvimento. Be gentle*

Sabedoria é poder, principalmente a sabedoria que todos desejam mas ninguém possui.
Sabedoria do que existe além dos véus que cobrem nosso mundo, sabedoria daqueles
que se escondem nas sombras.

É perigoso negligenciar as trevas, principalmente quando temos pessoas
inocentes envolvidas. Nunca se sabe quando a próxima bruxa vai atacar,
quando o próximo uivo brilhará contra o luar, quando o próximo fantasma irá
consumar sua vingança. Mas, é por isso que estamos aqui. Somos os vigilantes
silenciosos. Somos aqueles que todos conhecem e subestimam, mas que, na calada da
noite e envoltos nos braços da escuridão, agimos como um faról na neblina. Somos
o homem na esquina, somos a senhora da casa ao lado, somos os pedestres nas calçadas.

Somos os guardiões. Somos Watchtower.

## Projeto ##
Este projeto foi desenvolvido para a disciplina de Programação Distribuída,
oferecida pela Universidade Federal do Rio Grande do Norte. Foi nos dada a tarefa
de criar um Jokenpo que funcionasse a partir de RMI. Em vista disso, comecei a
trabalhar no Watchtower (inclusive tem Jokenpo no meio... mais ou menos)

## Instalação ##
### Debian based ###

**Dependencias**:
- Python 3 (incompatível com Python 2)
- Pip

**Instruções**

- Baixe a última release
- Uma vez na pasta do projeto, use o comando ```pip install -r requirements.txt```
para instalar as dependências do projeto
- Abaixo as instruções para executar o projeto

### Windows ###
*Coming soon (?)*

## Execução ##
1. Vá até a pasta do projeto
2. Execute o arquivo ```server.sh```
3. Execute o comando ```python guardian.py```

## Sobre o jogo ##
Watchtower é um jogo sobre conduzir um purge com sucesso. Purge é uma cerimônia de purificação realizada sobre uma região. A purge requer que o grardião conheça seu inimigo antes de atacá-lo, por isso as pistas da equipe de investigação são tão importantes.

#### Criaturas ####
Todas as criaturas no projeto terão uma espécie e um elemento associado. A espécie e o elemento apresentam traços e fraquezas únicas, as quais devem ser exploradas pelo guardião. Você pode pesquisar mais a respeito
de monstros e tipos que já conheça pelo comando ```python codex.py <elemento> <criatura>```

#### Preparação ####
Na primeira parte do jogo, o usuário deve selecionar ver as pistas deixadas pela entidade e
coletadas pelo time de investigação. Em seguida, você deve identificar os pontos
fortes e fracos da criatura em questão. Faça isso utilizando o codex. Você deve selecionar:
* Material da arma
* Local do purge
* Amuleto
* Poção
* Ato de invocação
* Ato de banimento

Assim que selecionados os itens acima, começa a fase de batalha

#### Batalha ####
Será mostrado ao jogador seus erros e acertos com relação à criatura e, em seguida,
começa o jogo de Jokenpo. É possível utilizar três tipos de ataque:
**corporal**, **arcano** e **prece**. Seu oponente também irá utilizar um desses movimentos,
sendo que a ordem de vitória é:
**corporal** -> **prece** -> **arcano** -> **corporal** ...

## Créditos ##
~ Desenvolvido por Alison de Araújo Bento
