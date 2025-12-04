import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Carica l'immagine
img = mpimg.imread("assets/IFAE_logo_SO.png")

fig, ax = plt.subplots()
ax.imshow(img)

def onclick(event):
    if event.xdata is not None and event.ydata is not None:
        x = int(event.xdata)
        y = int(event.ydata)
        # Nota: l'asse y in matplotlib parte da in alto in giù,
        # ma l'indice nell'array immagine è y dall'alto verso il basso,
        # quindi y coincide.
        color = img[y, x]  # ottieni il colore al pixel (x,y)
        # Se l'immagine ha canale alpha, color sarà un array con 4 elementi.
        print(f"Coordinate cliccate: x={x}, y={y}")
        print(f"Colore (RGBA): {color}")

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()
