from PIL import Image
import random

# Constantes padrão
WIDTH = 800
HEIGHT = 600
X1, Y1, X2, Y2 = -2.0, -1.5, 1.0, 1.5
MAX_ITER = 100
ESCAPE = 2.0

def mandelbrot(c):
    # Cálculo do conjunto de Mandelbrot
    z = 0
    n = 0
    while abs(z) <= ESCAPE and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return (0, 0, 0)
    else:
        return (n % 256, (n * 2) % 256, (n * 5) % 256)

def julia(c):
    # Cálculo do conjunto de Julia
    z = complex(0.0, 0.0)
    n = 0
    while abs(z) <= ESCAPE and n < MAX_ITER:
        z = z*z + c
        n += 1
    if n == MAX_ITER:
        return (0, 0, 0)
    else:
        return (n % 256, (n * 2) % 256, (n * 5) % 256)

def generate_fractal(type="Mandelbrot", width=WIDTH, height=HEIGHT, x1=X1, y1=Y1, x2=X2, y2=Y2, max_iter=MAX_ITER, escape=ESCAPE):
    # Gera a imagem fractal com base nas configurações fornecidas pelo usuário
    image = Image.new("RGB", (width, height))
    pixels = image.load()
    for x in range(width):
        for y in range(height):
            cx = x1 + (x / width) * (x2 - x1)
            cy = y1 + (y / height) * (y2 - y1)
            c = complex(cx, cy)
            if type == "Mandelbrot":
                color = mandelbrot(c)
            elif type == "Julia":
                color = julia(c)
            pixels[x, y] = color
    return image

if __name__ == "__main__":
    # Exemplo de uso
    type = input("Digite o tipo de fractal que deseja gerar (Mandelbrot ou Julia): ")
    width = int(input("Digite a largura da imagem em pixels: "))
    height = int(input("Digite a altura da imagem em pixels: "))
    x1 = float(input("Digite o valor de x1: "))
    y1 = float(input("Digite o valor de y1: "))
    x2 = float(input("Digite o valor de x2: "))
    y2 = float(input("Digite o valor de y2: "))
    max_iter = int(input("Digite o número máximo de iterações: "))
    escape = float(input("Digite o valor de escape: "))
    image = generate_fractal(type, width, height, x1, y1, x2, y2, max_iter, escape)
    filename = type.lower() + "_" + str(random.randint(1, 1000)) + ".png"
    image.save(filename)