import numpy as np
import cv2

def showImage(image):
  from matplotlib import pyplot as plt
  plt.imshow(image)
  plt.show()

def getColor(image, x, y):
  return [image.item((y, x, 0)), image.item((y, x, 1)), image.item((y, x, 2)) ]

def addColor(cor, margem):
  for i in cores.keys():
    tupla = (abs(cor[0] - i[0]), abs(cor[1] - i[1]), abs(cor[2] - i[2]))
    if tupla[0] < margem and tupla[1] < margem and tupla[2] < margem:
      cores[i] += 1
      return
  cores[cor] = 1
      
def calcularSuperficie(nivelAgua, largura, obj_img, corAgua):
  for x in range(largura):
    if tuple(getColor(obj_img, x, nivelAgua)) == corAgua:
      superficie.append(x)

def registroDeCores(altura, largura, obj_img, margem, corAgua, corMeteoro, corEstrela):
  for y in range(altura):
    for x in range(largura):
      cor = tuple(getColor(obj_img, x, y))
      addColor(cor, margem)
      if cor == (corMeteoro):
        #registro da posicao do meteoro
        meteoros.append((x, y))
      elif cor == (corEstrela):
        #registro da posicao da estrela
        estrelas.append((x, y))
      elif cor == (corAgua):
        #registro da posicao da agua
        if getColor(obj_img, x, y-1) != (0, 0, 255):
          #nao existem estrelas e meteoros abaixo da agua
          return y
                   
def imprimirResultado(coresOrdenadas):
  print("\n")
  for cor in coresOrdenadas:
    string = "Cor: " + str(cor)
    tab = 30 - len(string)
    espacos = " " * tab
    print(string, espacos , " Quantidade: ", coresOrdenadas[cor])

def calcularMeteorosAcimaDaAgua():
    for meteoro in meteoros:
      if meteoro[0] in superficie:
        meteorosAcimaDaAgua.append(meteoro)

# lista com as coordenadas de x compativeis com a cor da agua
# *********************
# * variaveis globais *
# *********************
meteoros = []
estrelas = []
nivelAgua = -1
meteorosAcimaDaAgua = []
superficie = []
cores = {}

def main():
  # *********************
  # **** variaveis ******
  # *********************

  # path: caminho da imagem
  path = "./img/imagem.png"
  # margem de erro para considerar a cor igual
  # min = 0, max = 255 quanto menor a margem mais precisao na coleta de cores
  margem = 30
  # carregamento da imagem
  obj_img = cv2.imread(path)
  obj_img = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
  #dimensoes da imagem
  altura, largura, canais_de_cor = obj_img.shape
  #cores para a busca
  corAgua = (0, 0, 255) 
  corMeteoro = (255, 0, 0)
  corEstrela = (255, 255, 255)

  # informacoes da imagem
  print("Dimensões da imagem: Largura = ", largura, " Altura = ", altura, " Canais = ", canais_de_cor)
  print("\n")

  # contagem de cores e registro dos objetos
  nivelAgua = registroDeCores(altura, largura, obj_img, margem, corAgua, corMeteoro, corEstrela)
  
  #ordenar cores para imprimir o resultado da contagem
  coresOrdenadas = dict(sorted(cores.items(), key=lambda item: item[1], reverse=True))
  print("Quantidade de cores: ", len(cores), " margem: ", margem, " pixels")
  imprimirResultado(coresOrdenadas)
  print("Quantidade de pixels computados: ", altura * largura)
  print("\n")
  print("Stars white (255, 255, 255) = ", coresOrdenadas[corEstrela])
  print("Meteors Red (255, 0, 0) = ", coresOrdenadas[corMeteoro])
  print("Water Blue ", corAgua, " = ", coresOrdenadas[corAgua])


  # meteoros que vao cair na agua
  if nivelAgua == -1:
    print("Nivel da agua nao encontrado")
    return -1
  print("Nivel da agua = ", nivelAgua, " pixels")
  calcularSuperficie(nivelAgua, largura, obj_img, corAgua) 
  #debug print("Superficie: ", superficie)

  calcularMeteorosAcimaDaAgua()
  print("Meteoros acima da agua = ", len(meteorosAcimaDaAgua))
  #debug print("Meteoros acima da agua: ", meteorosAcimaDaAgua)

  #exibir imagem
  showImage(obj_img)
  return 0

main()