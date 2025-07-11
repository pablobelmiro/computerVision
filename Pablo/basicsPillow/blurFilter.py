from PIL import Image, ImageFilter
import os
import numpy as np

print(os.getcwd())

#Ajustando diretório das imagens
BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, "..", 'imgs')

#função só pra poder juntar o caminho com arquivo
def in_file(file):
    return os.path.join(PATH, file)

image = Image.open(in_file('old_builds.jpg'))
#image.show()

#ENTENDENDO FILTRO CONVOLUCIONAL
#conceito matemático
#é como um filtro com 2 características:

#1. é um filtro linear => cálculo do novo valor de um pixel a partir de uma combinação linear(somas e multiplicações)
#é como uma média ponderado dos pixels mais próximos

#2. Espacialmente invariante => se comporta nas regiões da imagem, da mesma maneira, não importanto o ponto da imagem

#filtro box => Os pesos da média ponderada são iguais(1/q) 
#efeito de borramento
#é o espalhamento da quantidade de luz em um sensor(câmera)

#Imagem(MATRIZ) => filtro convolucional(KERNEL matriz) => Nova imagem com a média ponderada dos pixels vizinhos
#um filtro se comporta da mesma maneira em diferentes canais
#o deslocamento de centro são mais fáceis de manipular
#no caso de bordas, alguma métrica precisa ser implementada, utilizando geralmente padding ou utilizando os valores mais próximos

def show_vertical(image1, image2):
    joinedImage = Image.fromarray(np.vstack(np.array(image1), np.array(image2)))

#implementando utilizando pillow
#utilizar os métodos ImageFilter -> modo BoxBlur
#configurar o radius para configurar a "vizinhança" do pixel
def show_box_blur(image, r=10):
    filtered = image.filter(ImageFilter.BoxBlur(r))

    return filtered

filteredImage = show_box_blur(image,10)
filteredImage.show()

#ATIVIDADE - FAZER FILTRO BOX NA MÃO MANIPULANDO MATRIZES
