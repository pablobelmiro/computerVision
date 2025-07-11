from PIL import Image
import os

print(os.getcwd())

#Ajustando diretório das imagens
BASE_DIR = os.path.dirname(__file__)
PATH = os.path.join(BASE_DIR, "..", 'imgs')

#função só pra poder juntar o caminho com arquivo
def in_file(file):
    return os.path.join(PATH, file)

image = Image.open(in_file('city_china.jpg'))
#image.show()


#FUNDAMENTOS FILTRO DE SOBEL:
#Dentro de uma imagem temos regiões mais uniformes(lisas) de cores ou regiões com variações
#regiões com variações nos tons são regiões de fronteiras com objetos ou delta de textura
#esse é um "conceito" de aresta no mundo real
#no conceito matemático de aresta, utilizamos a DERIVADA
#intuição pra isso: "O quando que uma função está variando"
#exemplo derivada 0(onde não importa onde o eixo x estará, o y sempre será um valor constante ou mesmo valor)
#a derivada permite uma "noção" do quanto uma função varia
#na imagem, a variação entrega as arestas/contornos

#FUNDAMENTOS GRADIENTE
#forma de medir a variação em uma imagem
#operador de PREWITT que faz a estimativa de gradiente em uma imagem ou o SOBEL
#faz a combinação linear(somas e multiplicações)

#SUAVIZAÇÃO
#meio que um fator entre o eixo x ou y inbutido na direção contrária da variação observada
#explica um pouco da operação convulacional

#ARESTAS
#verticais ou horizontais
#para verificar os dois tipos de arestas, compomos o resultado entre os filtros como resultado -> vetor
#possui direção e sentido no vetor com magnetude e gradiente

#APLICANDO NO CÓDIGO
