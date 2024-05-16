
Documentação do Código
Este documento descreve a estrutura, funcionamento e propósito do código Python desenvolvido para processar uma imagem e realizar algumas operações de análise, incluindo contagem de cores, detecção de objetos e cálculo de superfície de água.

1. Introdução
O código foi projetado para trabalhar com imagens no formato RGB e realizar as seguintes operações:

Contagem de cores presentes na imagem.
Registro de objetos específicos, como meteoros, estrelas e água.
Cálculo da superfície da água na imagem.
Detecção de meteoros acima da superfície da água.
O código foi estruturado em várias funções para facilitar a manutenção e compreensão.

2. Funcionalidades
2.1. getColor(image, x, y)
Esta função retorna a cor RGB de um pixel específico na imagem.

2.2. addColor(cor, margem)
Esta função é responsável por adicionar uma cor ao dicionário de cores, com uma margem de erro especificada.

2.3. calcularSuperficie(nivelAgua, largura, obj_img, corAgua)
Esta função calcula a superfície da água na imagem, identificando os pixels que correspondem à cor da água e registrando suas coordenadas em uma lista.

2.4. registroDeCores(altura, largura, obj_img, margem, corAgua, corMeteoro, corEstrela)
Esta função realiza o registro de cores presentes na imagem, contando a quantidade de ocorrências de cada cor e registrando as posições de objetos específicos, como meteoros e estrelas.

2.5. imprimirResultado(coresOrdenadas)
Esta função imprime os resultados da contagem de cores, exibindo a quantidade de ocorrências de cada cor na imagem.

2.6. calcularMeteorosAcimaDaAgua()
Esta função calcula a quantidade de meteoros que estão acima da superfície da água, com base nas coordenadas registradas anteriormente.

2.7. main()
A função principal do código, responsável por coordenar todas as operações e imprimir os resultados finais.

3. Variáveis Globais
3.1. meteoros
Lista que armazena as coordenadas dos meteoros presentes na imagem.

3.2. estrelas
Lista que armazena as coordenadas das estrelas presentes na imagem.

3.3. nivelAgua
Variável que armazena a altura da superfície da água na imagem.

3.4. meteorosAcimaDaAgua
Lista que armazena as coordenadas dos meteoros que estão acima da superfície da água.

3.5. superficie
Lista que armazena as coordenadas dos pixels que compõem a superfície da água na imagem.

3.6. cores
Dicionário que armazena as cores presentes na imagem e o número de ocorrências de cada uma.

4. Execução do Código
Para executar o código, basta chamar a função main().

