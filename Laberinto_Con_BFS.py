from collections import deque

def encontrar_caminosBFS(laberinto, entrada, salida):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    cola = deque([[entrada]])
    
    caminos = []
    
    while cola:
        camino_actual = cola.popleft()
        x, y = camino_actual[-1]
        
        if (x, y) == salida:
            caminos.append(camino_actual)
        else:
            for dx, dy in direcciones:
                nx, ny = x + dx, y + dy
                if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0:
                
                    if (nx, ny) not in camino_actual:
                        nuevo_camino = list(camino_actual)
                        nuevo_camino.append((nx, ny))
                        cola.append(nuevo_camino)
    
    return caminos

# Ejemplo de uso
laberinto = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]
entrada = (0, 0)
salida = (4, 4)


caminos_encontrados = encontrar_caminosBFS(laberinto, entrada, salida)
for i, camino in enumerate(caminos_encontrados, start=1):
    print(f"Camino {i}: {camino}")