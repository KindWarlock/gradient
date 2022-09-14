import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1


size = 100
image = np.zeros((size, size, 3), dtype="uint8")
_image = image
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

# была идея сделать это через fill_diagonal, но я не придумала, как добиться нужного
# результата с 3 измерениями
    
# но сейчас собираемся закрашивать диагоналями
for i, v in enumerate(np.linspace(0, 1, size * 2 - 1)):
    # 1 - v, поскольку будем менять порядок
    r = lerp(color1[0], color2[0], 1 - v)
    g = lerp(color1[1], color2[1], 1 - v)
    b = lerp(color1[2], color2[2], 1 - v) 
    
    # как блинчик, переворачиваем изображение, когда закрасили половину
    if i >= size:
        _image = np.flip(image, (0, 1))

    row = (size - 1) - np.absolute((size - 1) - i) # y = -|x| + m - размер диагонали
    color = [r,g,b]
    for k in range(row + 1):
        _image[row - k, k, :] = color

plt.figure(1)
plt.imshow(image)
plt.show()
