import cv2
import numpy as np

def limiarizacao(img, l, c, limite):
    nova = np.zeros(img.shape, np.uint8)

    for i in range(0, int(l)):
        for j in range(0, int(c)):
            if img.item(i,j) < limite:
                nova.itemset((i,j), 0)
            else:
                nova.itemset((i,j), 255)

    return nova


def vizinho(img, l,c) -> int:
    # print("entrou")
    rotulo = 255
    for i in range(l-1, l+2):
        for j in range(c-1, c+2):
            if img.item(i,j) != 0 and img.item(i,j) < rotulo:
                rotulo = img.item(i,j)
    return rotulo

def rotular(img):
    alterou = True
    rotulo = 10
    l, c =img.shape
    lista_rotulos = []

    while alterou == True:
        alterou = False

        for i in range(1, l-1):
            for j in range(1, c-1):

                if img.item(i,j) != 0:
                    rv = vizinho(img,i,j)
                    if rv == 255:
                        # print (rv)
                        img.itemset((i,j), rotulo)
                        rotulo += 1
                        alterou = True

                    elif rv != img.item(i, j):
                        img.itemset((i, j), rv)
                        alterou = True

    # pega os rotulos atuais da imagem
    for i in range(1, l - 1):
        for j in range(1, c - 1):
            # adiciona o rotulo na lista para fazer a contagem posteriormente
            rotulo = img.item(i, j)
            if rotulo not in lista_rotulos:
                lista_rotulos.append(rotulo)

    return img, lista_rotulos

def main(imagem,mX,mY):
    img = cv2.imread(imagem,cv2.IMREAD_GRAYSCALE)
    novo = limiarizacao(img,img.shape[0],img.shape[1],127)
    kernel = np.ones((mX, mY), np.uint8)
    dilation = cv2.dilate(novo,kernel,iterations = 2)
    new = cv2.erode(dilation,kernel,iterations = 5)


    t1, t2 = rotular(new)
    cv2.imshow('new', t1)
    # imagem(new,new.shape[0],new.shape[1])
# imagem binariazada

# foi subtraido 2 da contagem da lista para descontar a borda branca da imagem e o rotulo preto.
    print('Total de moedas na figura A: {}'.format(len(t2)-2))

    tecla = cv2.waitKey(0)
    cv2.destroyAllWindows()

main('img01-a.png',3,3)
main('img01-b.png',5,5)
