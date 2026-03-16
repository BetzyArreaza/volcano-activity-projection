from goes2go import GOES
import matplotlib.pyplot as plt
import numpy as np

print("Descargando datos GOES...")

g = GOES(satellite=18, product="ABI-L2-FDCF")
ds = g.latest()

print("Variables disponibles:")
print(list(ds.variables))

# usar potencia térmica
rad = ds["Power"].values

cx = rad.shape[0] // 2
cy = rad.shape[1] // 2

region = rad[cx-50:cx+50, cy-50:cy+50]

prom = np.nanmean(region)

print("Potencia térmica promedio:", prom)

plt.imshow(region, cmap="hot")
plt.colorbar(label="Potencia térmica")

plt.title("Actividad térmica - Volcán de Fuego")

plt.show()