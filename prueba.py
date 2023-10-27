from bluedot.btcomm import BluetoothServer
import board
import neopixel
import time

pixel_pin = board.D21

num_pixels = 210

pixels = neopixel.NeoPixel(pixel_pin, num_pixels)


# Mapeo de colores
color_dict = {
    '1': (255, 0, 0),
    '2': (0, 255, 0),
    '3': (0, 0, 255),
    '4': (244, 255, 82),
    '5': (250, 120, 5),
    '6': (153, 5, 250),
    '7': (253, 235, 208),
    '8': (133, 193, 233),
    '9': (255, 255, 255)
}

def leer(data):
    print('inicia proceso de pintado')
    data = data.split(',')
    indice = 0
 
    while indice < len(data):
            
        dataT = data[indice].strip()
        if dataT == '1':
            pixels[indice] = (255, 0, 0)
        elif dataT == '2':
            pixels[indice] = (0, 255, 0)
        elif dataT == '3':
            pixels[indice] = (0, 0, 255)
        elif dataT == '4':
            pixels[indice] = (244, 255, 82)
        elif dataT == '5':
            pixels[indice] = (250, 120, 5)
        elif dataT == '6':
            pixels[indice] = (153, 5, 250)
        elif dataT == '7':
            pixels[indice] = (253, 235, 208)
        elif dataT == '8':
            pixels[indice] = (253, 235, 208)
        elif dataT == '9':
            pixels[indice] = (255, 255, 255)
        else:
            pixels[indice] = (0,0,0)
        indice += 1

print("Inicia servicio")
s = BluetoothServer(leer)
