<h1>Resumo:</h1>
O código foi estruturado em várias funções para facilitar a manutenção e compreensão.

Adicionei uma margem de erro ao capturar as cores para que não tenha várias cores semelhantes com nomes diferentes.
Registrei a imagem como uma matriz com ajuda da biblioteca OpenCv e percorri a matriz iterando cada pixel e armazenando as informações de acordo com as cores referidas.
Note que essa é a parte mais custosa do algoritmo, tendo uma complexidade de O(altura *largura) da imagem que muitas vezes será uma complexidade quadrática.
A seguir, o código irá imprimir as informações, assim respondendo a primeira e a segunda pergunta.

Para responder a terceira, comparei a lista de coordenadas relativa aos meteoros e comparei com a lista referente a área de superfície da água.
A área de superfície da água foi calculada considerando a altura do nível do ar constante. Assim, uma vez encontrado o nível da água, não precisei iterar todos os outros milhares de pixels.
assim, calculei a superfície da água considerando a altura fixa levando assim uma complexidade linear de O(n) onde n é referente a largura da imagem.

A complexidade de tempo do código é dominada pelas operações de iteração sobre os pixels da imagem e das coordenadas dos objetos. A complexidade de espaço depende principalmente do número de cores únicas e do número de objetos presentes na imagem para serem armazenados no dicionário de cores. Em geral, a complexidade do código é razoável para imagens de tamanho moderado, mas pode aumentar significativamente com o aumento do tamanho da imagem ou do número de objetos presentes nela.
<h1>Documentação do Código</h1>
Este documento descreve a estrutura, funcionamento e propósito do código Python desenvolvido para processar uma imagem e realizar algumas operações de análise, incluindo contagem de cores, detecção de objetos e cálculo de superfície de água.

<h2>1. Introdução</h2>
Recebi um desafio para criar um algoritmo que recebe uma imagem e conta alguns objetos inseridos nela.
O código foi projetado para trabalhar com imagens no formato RGB e realizar as seguintes operações:

Contagem de cores presentes na imagem.
Registro de objetos específicos, como meteoros, estrelas e água.
Cálculo da superfície da água na imagem.
Detecção de meteoros acima da superfície da água.
O código foi estruturado em várias funções para facilitar a manutenção e compreensão.

<h2>2. Funcionalidades</h2>
<h3>2.1. getColor(image, x, y)</h3>
Esta função retorna a cor RGB de um pixel específico na imagem.

<h3>2.2. addColor(cor, margem)</h3>
Esta função é responsável por adicionar uma cor ao dicionário de cores, com uma margem de erro especificada.

<h3>2.3. calcularSuperficie(nivelAgua, largura, obj_img, corAgua)</h3>
Esta função calcula a superfície da água na imagem, identificando os pixels que correspondem à cor da água e registrando suas coordenadas em uma lista.

<h3>2.4. registroDeCores(altura, largura, obj_img, margem, corAgua, corMeteoro, corEstrela)</h3>
Esta função realiza o registro de cores presentes na imagem, contando a quantidade de ocorrências de cada cor e registrando as posições de objetos específicos, como meteoros e estrelas.

<h3>2.5. imprimirResultado(coresOrdenadas)</h3>
Esta função imprime os resultados da contagem de cores, exibindo a quantidade de ocorrências de cada cor na imagem.

<h3>2.6. calcularMeteorosAcimaDaAgua()</h3>
Esta função calcula a quantidade de meteoros que estão acima da superfície da água, com base nas coordenadas registradas anteriormente.

<h3>2.7. main()</h3>
A função principal do código, responsável por coordenar todas as operações e imprimir os resultados finais.

<h2>3. Variáveis Globais</h2>
<h3>3.1. meteoros</h3>
Lista que armazena as coordenadas dos meteoros presentes na imagem.

<h3>3.2. estrelas</h3>
Lista que armazena as coordenadas das estrelas presentes na imagem.

<h3>3.3. nivelAgua</h3>
Variável que armazena a altura da superfície da água na imagem.

<h3>3.4. meteorosAcimaDaAgua</h3>
Lista que armazena as coordenadas dos meteoros que estão acima da superfície da água.

<h3>3.5. superficie</h3>
Lista que armazena as coordenadas dos pixels que compõem a superfície da água na imagem.

<h3>3.6. cores</h3>
Dicionário que armazena as cores presentes na imagem e o número de ocorrências de cada uma.

<h2>4. Execução do Código</h2>
Certifique-se que você adicionou as bibliotecas necessárias: OpenCv, Numpy e Matplotilib
Para executar o código, basta chamar a função main().

