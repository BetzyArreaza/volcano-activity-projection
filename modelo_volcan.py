import numpy as np
import matplotlib.pyplot as plt

print("----- MODELO AVANZADO DE ACTIVIDAD VOLCÁNICA -----")

# Datos históricos de ejemplo (explosiones por día)
dias = np.array([1,2,3,4,5,6,7,8,9,10])
explosiones = np.array([5,6,7,6,8,9,10,11,12,13])

# =============================
# MODELO DE TENDENCIA
# =============================

coeficientes = np.polyfit(dias, explosiones, 1)
modelo = np.poly1d(coeficientes)

pendiente = coeficientes[0]
intercepto = coeficientes[1]

print("\nTendencia de actividad:")
print("Pendiente:", round(pendiente,3))

# =============================
# PROYECCIÓN A 30 DÍAS
# =============================

dias_futuros = np.arange(11,41)
prediccion = modelo(dias_futuros)

print("\nProyección de actividad futura:")
for d,p in zip(dias_futuros[:10], prediccion[:10]):
    print("Día",d,"→",round(p,2),"explosiones")

# =============================
# MODELO DE POISSON
# =============================

lambda_eventos = np.mean(explosiones)

print("\nPromedio de explosiones por día:", round(lambda_eventos,2))

simulacion = np.random.poisson(lambda_eventos, 30)

print("\nSimulación probabilística (30 días):")
print(simulacion)

# =============================
# GRÁFICA
# =============================

plt.figure(figsize=(10,6))

plt.scatter(dias, explosiones, label="Datos reales")
plt.plot(dias, modelo(dias), label="Modelo de tendencia")

plt.scatter(dias_futuros, prediccion, label="Proyección 30 días")

plt.plot(np.arange(1,31), simulacion, label="Simulación Poisson")

plt.xlabel("Días")
plt.ylabel("Número de explosiones")
plt.title("Modelo avanzado de actividad del Volcán de Fuego")
plt.legend()

plt.savefig("modelo_volcan_avanzado.png")

plt.show()