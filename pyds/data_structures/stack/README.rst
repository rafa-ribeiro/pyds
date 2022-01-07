
Stack
=======

Implementação da estrutura de dados Stack ou Pilha
----------------------

Assim como uma lista, uma Pilha é utilizada para guardar coisas, mas diferentemente de uma Lista, a Pilha,
como o próprio nome diz, vai empilhando essas coisas uma sobre as outras.

A Pilha é uma estrutura de armazanemanto de dados que segue o seguinte princípio:

    "O último à entrar é o primeiro à sair"

Ou

    "O primeiro à entrar é o último à sair"

É muito comum vermos acrônimos (em inglês) para esse tipo de operação como LIFO ou FILO. É preciso
decorar esses termos? Não, não é, e você nem precisará se entender bem seu conceito.

**Como implementar uma pilha?**

Uma pilha pode ser implementada usando-se uma Lista ou alguma estrutura similar, no entanto devemos tomar alguns
cuidados ao manipular seus elementos

* A operação de adicionar um novo elemento à uma pilha é chamada de PUSH e esse novo elemento será sempre adicionado
à essa lista utilizada internamente pela pilha

* Já a operação de retirar da pilha, é chamada de POP, e ela sempre obtém e retira da pilha o último elemento
que havia sido inserido


**Onde usar uma estrutura de dados do tipo pilha? 🤔**

Uma pilha geralmente pode ser utilizada em situações em que se é preciso voltar ou acessar um estado anterior de algo,
por exemplo:

- Imagine que você está usando o computador para editar um texto ou fazer um desenho no paint, caso algo não saia como o
esperado, você pode simplesmenter dar um ctrl + z e logo seu texto ou desenho voltará para o estado anterior. Não sei
se um SO gerencia todas as operações do usuário exatamente assim, mas se me dissessem que é feito utilizando pilha, eu
acreditaria porque faz bastante sentido

- Ou ainda, se você gosta de jogar xadrez e está estudando movimentos num tabuleiro virtual, cada peça movida gera um
novo estado no tabuleiro e que é guardado numa pilha, assim é fácil dar um Pop no último movimento feito e voltar para
o estado anteior.

