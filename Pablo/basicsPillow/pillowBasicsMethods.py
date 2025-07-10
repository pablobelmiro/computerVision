from PIL import Image
import os

print(os.getcwd())

#Ajustando diretório das imagens
BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, "..", 'imgs')

#função só pra poder juntar o caminho com arquivo
def in_file(file):
    return os.path.join(PATH, file)

image = Image.open(in_file('kasongo_top_block.jpg'))


#FUNÇÕES BÁSICAS

#format - formato da imagem
print(f'Formato da imagem: {image.format}') 

#mode - mode de coloração da imagem
print(f'Modo de coloração da imagem: {image.mode}')

#size - Dimensões da imagem
print(f'Dimensões da imagem: {image.size}')
print(f'Largura da imagem: {image.width}')
print(f'Altura da imagem: {image.height}')


image.show()

#Resize - Redimensionando a imagem
#Recebe como parâmetro uma tupla com a nova largura e altura
image_resized = image.resize(size=(800, 600))
image_resized.show()

#crop - Recortando a imagem
#Recebe como parâmetro uma tupla com as coordenadas do retângulo a ser recortado
#x, y do ponto inicial do corte
#tem que lembrar que a imagem sempre começa no ponto (0, 0)
#eixo x aumenta para a direita e eixo y aumenta para baixo
image_cropped = image.crop(box=(100, 100, 400, 400))
image_cropped.show()


#transpose - Transpondo a imagem
#Recebe como parâmetro uma constante que define a transposição
#tem que dar uma pesquisada nas constantes disponíveis na doc
#https://pillow.readthedocs.io/en/latest/reference/Image.html#PIL.Image.Image.transpose
image_transposed = image.transpose(method=Image.ROTATE_270)
image_transposed.show()