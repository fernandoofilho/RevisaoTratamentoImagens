import cv2 
import numpy as np
# Filtros de suavização
def gaussianBlurFilter(image, kernel = (5,5)):
    return cv2.GaussianBlur(image, kernel, 0)

def medianBlurFilter(image, ksize = 5):
    return cv2.medianBlur(image, ksize)

def averageBlurFilter(image, ksize = 5):
    return cv2.blur(image, (ksize, ksize))

def bilateralBlurFilter(image, ksize = 5):
    return cv2.bilateralFilter(image, ksize, ksize, ksize)

# Filtros de detecção de bordas

def cannyFilter(image):
    return cv2.Canny(image, 100, 200)

def sobelFilter(image):
    return cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)

def prewittFilter(image):
    # Aplicar o filtro Prewitt horizontal
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    imagem_prewitt_x = cv2.filter2D(image, -1, kernel_x)

    # Aplicar o filtro Prewitt vertical
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    imagem_prewitt_y = cv2.filter2D(image, -1, kernel_y)
    return imagem_prewitt_x, imagem_prewitt_y

img = cv2.imread('./imagens/imagem_cidade.jpg')


################################################################ 
# Exibindo imagem

if img is not None:
    cv2.imshow('Imagem', img)  # Exibir a imagem em uma janela
    cv2.waitKey(0)  # Aguardar até que uma tecla seja pressionada
    cv2.destroyAllWindows()

# Imagem como matriz

print(img)



# Filtros de suavização
# kernel = 5
gaussianImage = gaussianBlurFilter(img)
medianBlurImage = medianBlurFilter(img)
averageBlurImage = averageBlurFilter(img)
bilateralBlurImage = bilateralBlurFilter(img)

# Exibindo as imagens
if medianBlurImage is not None and gaussianImage is not None:
    cv2.imshow('MedianBlurImage', medianBlurImage) 
    cv2.imshow('gaussianImage', gaussianImage) 
    cv2.imshow('averageBlurImage', averageBlurImage)
    cv2.imshow('bilateralBlurImage', bilateralBlurImage)


    cv2.waitKey(0)  # Aguardar até que uma tecla seja pressionada
    cv2.destroyAllWindows()

# Filtros de detecção de bordas
# kernel = 5

sobelImage = sobelFilter(img)
cannyImage = cannyFilter(img)
imagem_prewitt_x, imagem_prewitt_y = prewittFilter(img)

# Exibindo as imagens
if sobelImage is not None and cannyImage is not None:
    cv2.imshow('sobelImage', sobelImage) 
    cv2.imshow('cannyImage', cannyImage)
    cv2.imshow('imagem_prewitt_x', imagem_prewitt_x)
    cv2.imshow('imagem_prewitt_y', imagem_prewitt_y)
    cv2.waitKey(0)  # Aguardar até que uma tecla seja pressionada
    cv2.destroyAllWindows()
