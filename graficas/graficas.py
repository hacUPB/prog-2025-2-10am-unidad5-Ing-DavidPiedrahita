import matplotlib.pyplot as plt
import numpy as np
import math

# Datos
# x = np.linspace(0, 10, 100)
# y = np.sin(x)

x = []
for i in range():
    x.append(i)

y = []
for i in range(len(x)):
    y.append(math.cos(x[i]))    

# Crear la gráfica
plt.plot(x, y)

# Agregar título y etiquetas
plt.title('Gráfica de Seno')
plt.xlabel('X')
plt.ylabel('coseno(X)')

# Mostrar la gráfica
plt.show()