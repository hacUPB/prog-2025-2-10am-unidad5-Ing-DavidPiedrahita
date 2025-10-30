import matplotlib.pyplot as plt
import numpy as np

# Datos
data = ["a","e","a","i","u","o","e","a","i","u","o","a","e","e","i"]
# Crear el histograma
plt.hist(data, bins=15, edgecolor='black')

# Agregar título y etiquetas
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')

# Mostrar la gráfica
plt.show()
