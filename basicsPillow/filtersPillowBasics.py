from PIL import Image
import os

print(os.getcwd())

#Ajustando diretório das imagens
BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, 'imgs')

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
grayImage = Image.new("RGB", (w, h))

#for x in range(w):