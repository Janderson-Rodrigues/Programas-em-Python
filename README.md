O programa implementa a Torres de Hanói , um problema clássico matemático e de recursão. Ele move uma pilha de discos de uma torre de origem para uma torre de destino, seguindo regras específicas:

Somente um disco pode ser movido por vez.
Um disco maior nunca pode ser colocado sobre um disco menor.
Os discos devem estar sempre em uma das três torres.
Descrição do funcionamento:
1. Estrutura do código:
mover_disco(origem, destino)

Remova o último disco da torre de origem e adicione na torre de destino.
imprimir_torres(torre_A, torre_B, torre_C)

Exibe o estado atual das torres após cada entrega.
torres_de_hanoi_recursivo(num_disco, origem, destino, auxiliar)

Resolva o problema recursivamente.
Se houver apenas um disco, ele é movido diretamente para o destino.
Caso contrário:
Mover (n-1) discos da torre de origem para a torre auxiliar.
Mova o disco maior diretamente para o destino.
Mover os (n-1) discos da torre auxiliar para a torre de destino.
2. Inicialização das torres e execução:
A torre A inicia com todos os discos ordenados.
As torres B e C são vazias.
A função torres_de_hanoi_recursivoé chamada para resolver o problema.
Erros e ajustes necessários:
Erro de digitação em num_dsico→ deve sernum_disco
Referências incorretas a torre_A, torre_B, torre_Cdentro da função recursiva
A função recebe as torres como argumentos, então a referência global não funciona corretamente.
Deve-se imprimir as partições locais recebidas pela função.



#Programa Validação CPF


Este programa em Python tem a finalidade de validar um número de CPF (Cadastro de Pessoas Físicas) confo

Descrição do funcionamento:
Limpeza dos caracteres

Remover todos os caracteres não numéricos, permitindo que
Verificação da quantidade de dígitos

O CPF deve conter exatamente 11 dígitos . SeFalse.
Verificação de repetição de números

CPFs com todos os dígitos iguais (exemplo: "111.111.111-11
Cálculo do primeiro dígito selecionado

Utiliza
O resultado é somado e dividido por 11. Se o resto for menor que 2 , o dígito0 . Caso contrário11 menos ou resto .
Verificação do primeiro dígito selecionado

O valor calculado é comparado ao primeiro dígito selecionado do CPF original. Se forem diferentes, a função retorna False.
Cálculo do segundo dígito selecionado

O processo é semelhante ao primeiro cálculo, mas agora envolve os 10 primeiros dígitos (incluindo o primeiro dígito selecionado ou recém-verificado).
Verificação do segundo dígito selecionado

O segundo dígito selecionado é comparado ao original. Se forem diferentes, a função retorna False.
Retorno do resultado

Se todas as etapas foram atendidas corretamente, a função retorna True, indicando que o CPF é válido.
Exemplo de uso:
O código inclui um teste com o CPF "123.456.789-09". Ele imprime no console se o CPF é válido ou inválido.

Esse programa pode ser utilizado em aplicações que desativam validação de CPF, como cadastros de usuários em sistemas financeiros, plataformas de e-commer.
