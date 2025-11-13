# # Ejercicios Listas y Tuplas

# 1. Rotación de Playlist Musical
# Tienes una lista con el orden de canciones de una playlist.
# Escribe un programa que pida al usuario un número n y rote la lista de canciones n posiciones a la
# derecha.
# # Ejemplo
# playlist = ["Canción A", "Canción B", "Canción C", "Canción D"]
# # Si n = 2 → ["Canción C", "Canción D", "Canción A", "Canción B"]

# 2. Filtrar Ingredientes Prohibidos
# Un chef tiene una lista de ingredientes para una receta.
# Escribe un programa que pida al usuario los ingredientes que no quiere (pueden ser varios, separados
# por coma) y genere una nueva lista eliminando los ingredientes prohibidos.
# python
# CopiarEditar
# # Ejemplo
# ingredientes = ["harina", "huevo", "leche", "azúcar", "chocolate"]
# # Prohibidos: huevo, leche → ["harina", "azúcar", "chocolate"]

# 3. Codificador por Saltos
# Crea un programa que reciba una lista de letras y un número salto.
# Debe generar una nueva lista con las letras saltando de acuerdo al valor dado.
# Ejemplo
# letras = ["a", "b", "c", "d", "e", "f", "g"]
# salto = 2 → ["a", "c", "e", "g"]

# 4. Eliminar Duplicados y Ordenar al Revés
# Dada una lista con números repetidos, crea un programa que elimine los duplicados y ordene los valores
# de mayor a menor.
# # Ejemplo
# numeros = [4, 2, 8, 4, 1, 8, 3] → [8, 4, 3, 2, 1]

# 5. Combinar Nombres y Apellidos
# Tienes dos listas: una de nombres y otra de apellidos.
# Escribe un programa que genere una nueva lista con el nombre completo de cada persona combinando
# ambas listas posición por posición.
# # Ejemplo
# nombres = ["Ana", "Luis", "Carla"]
# apellidos = ["Pérez", "Ramírez", "López"]
# # Resultado: ["Ana Pérez", "Luis Ramírez", "Carla López"]
# Intercambio de Variables sin Variables Temporales
# Usando tuplas, intercambia los valores de dos variables sin usar una variable auxiliar.

# python
# CopiarEditar
# a, b = 5, 10
# # Resultado esperado: a = 10, b = 5