from PIL import Image
import os

print(os.getcwd())

#Ajustando diretório das imagens
BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, "..", 'imgs')

#função só pra poder juntar o caminho com arquivo
def in_file(file):
    return os.path.join(PATH, file)

image = Image.open(in_file('kasongo_top_block_2.jpg'))
#image.show()


#convertendo pra preto e branco na unha e no PURO
#entendendo que a imagem é uma matriz de pixels
#e cada pixel é uma tupla com os valores RGB
#é como se fosse uma imagem em escala de cinza
#mas com os valores de cinza sendo a média dos valores RGB
print(image.getpixel((0, 0)))
print(image.getpixel((150, 150)))
print(image.getpixel((1230, 1230)))
print(image.getpixel((500, 300)))

#transformando com média simples
w, h = image.size #primeiro tem que pegar as dimensões da imagem
grayImageSimpleAverage = Image.new("RGB", (w, h))


#quando a colocamos as 3 coordenadas de cor iguais, temos um pixel em escala de cinza
#Podemos decompor uma cor com uma parte que é o brilho(iluminação) e outra parte que é a cor
#essencialmente a escala é apenas uma informação de brilho e não de cor
#informação de luminância
#temos 3 valores e precisamos convertê-los para um único valor de brilho
#usando a média simples dos valores RGB parar isso
#podemos também usar outras fórmulas, como a média ponderada

#CONVERTENDO UTILIZANDO MÉDIA SIMPLES
#primeiro percorre todas as colunas da imagem
print("----------- utilizando média simples")
for x in range(w):
    #percorrendo todas as linhas da imagem
    for y in range(h):
        #capturando pixel atual
        pixel = image.getpixel((x,y))
        print(f'pixel atual: {pixel}')
        #calculando a luminância
        luminancia = (pixel[0] + pixel[1] + pixel[2]) // 3
        print(f'luminancia atual: {luminancia}')
        #adicionando o pixel na imagem em escala de cinza
        grayImageSimpleAverage.putpixel((x,y), (luminancia, luminancia, luminancia))

#disponibilizando imagem
grayImageSimpleAverage.show()


#ENTENDENDO MELHOR COMO FUNCIONA A ESCALA DE CINZA:
#O principal componente para transformação para escala de cinza vem do verde em segundo lugar o vermelho
#e o terceiro do azul

#fazendo a média ponderada para poder fazer a transformação da escala de cinza
grayImagePondAverage = Image.new("RGB", (w,h))
for w in range(w):
    for y in range(h):
        pixel = image.getpixel((x,y))
        lum = int(0.3*pixel[0] + 0.59*pixel[1] + 0.11*pixel[2])
        grayImagePondAverage.putpixel((x,y), (lum. lum, lum))

grayImagePondAverage.show()
