import cv2
import numpy as np

# abri a imagem
# mascara
# if
#   ....
    # mascara = 255
# se mascara != 0
#     saida = img[i][j]
# else
#     saida = 0


def main():
    cap = cv2.VideoCapture(0)

    mascara_morfologia_a = np.ones((10, 10), np.uint8)
    mascara_morfologia_b = np.ones((8, 8), np.uint8)

    while(cap.isOpened()):
        ret, frame = cap.read()
        copia = frame
        l = frame.shape[0]
        c = frame.shape[1]
        d = frame.shape[2]
        mascara = np.ones((l,c), np.uint8)

        for i in range(1,l-1):
            for j in range(1,c-1):

                r = frame.item(i,j,2)
                g = frame.item(i,j,1)
                b = frame.item(i,j,0)
                # print(modulo)
                if r > 95 and g > 40 and b > 20 and (r - g) > 15 and r > g and r > b:
                    mascara.itemset((i,j), 255)
                    # print("fio")
                else:
                    mascara.itemset((i,j), 0)

        mascara = cv2.erode(mascara, mascara_morfologia_a, iterations=1)
        mascara = cv2.dilate(mascara, mascara_morfologia_b, iterations=5)
        mascara = cv2.erode(mascara, mascara_morfologia_a, iterations=1)


        for i in range(1, l-1):
            for j in range(1, c-1):
                for k in range(0, d):
                    if mascara.item(i, j) != 0:
                        copia.itemset((i, j, k), frame.item(i, j, k))
                    else:
                        copia.itemset((i, j, k), 0)

        cv2.imshow('new', copia)

# R > 95, G > 40, B > 20
# (max(R, G, B) − min(R, G, B)) < 15
# |R − G| > 15, R > G, R > B





        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


main()
