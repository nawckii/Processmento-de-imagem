import cv2
import numpy as np


def Negativo(img, linhas, colunas):
    imgNeg = np.zeros(img.shape, np.uint8)
    for i in range(0, int(linhas)):
        for j in range(0, colunas):
            negativo0 = 255 - img.item(i, j,0)
            imgNeg.itemset((i, j,0), negativo0)
            negativo1 = 255 - img.item(i, j,1)
            imgNeg.itemset((i, j,1), negativo1)
            negativo2 = 255 - img.item(i, j,2)
            imgNeg.itemset((i, j,2), negativo2)
    return imgNeg

def limiarizacao(img, l, c, limite):
    nova = np.zeros(img.shape, np.uint8)

    for i in range(0, int(l)):
        for j in range(0, int(c)):
            if img.item(i,j) < limite:
                nova.itemset((i,j), 0)
            else:
                nova.itemset((i,j), 255)

    return nova

def inverte(img, l, c):
    nova = np.zeros(img.shape, np.uint8)
    nova1 = np.zeros(img.shape, np.uint8)
    ll = 1
    cc = 1
    for i in range(l-1, 0, -1):
        if ll >= l:
            ll = 1
        for j in range(c-1, 0, -1):
            if cc >= c:
                cc = 1
                aux = img[ll,cc]
                nova1.itemset((ll,cc), aux)
            nova.itemset((i,j), aux)
            cc += 1
        ll += 1
    return nova, nova1

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")

    return cv2.LUT(image, table)

def main():
    img = cv2.imread('widow.jpg')
    imgPB = cv2.imread('widow.jpg', cv2.IMREAD_GRAYSCALE)
    imgNeg = Negativo(img,img.shape[0],img.shape[1])
    imgLim = limiarizacao(imgPB,img.shape[0],img.shape[1],50)
    imgGam = adjust_gamma(img, 5)

    #coloridas
    cv2.imshow('imagem', img)
	# cv2.imshow('imagemNeg', imgNeg)
	# #preto e branco
	# cv2.imshow('imagemPb', imgPB)
	# cv2.imshow('imagemMed', imgMed)
    cv2.imshow('imagemGam', imgLim)


    tecla = cv2.waitKey(0)
    cv2.destroyAllWindows()
main()
