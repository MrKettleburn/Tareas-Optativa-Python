def encontrar_caminos(laberinto, entrada, salida):
    def dfs(x, y, camino_actual):
        if (x, y) == salida:
            caminos.append(camino_actual)
            return
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(laberinto) and 0 <= ny < len(laberinto[0]) and laberinto[nx][ny] == 0:
                laberinto[x][y] = 1  # Marcar como visitado
                dfs(nx, ny, camino_actual + [(nx, ny)])
                laberinto[x][y] = 0  # Desmarcar para explorar otros caminos

    caminos = []
    dfs(entrada[0],entrada[1], [entrada])
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


caminos_encontrados = encontrar_caminos(laberinto, entrada, salida)
for i, camino in enumerate(caminos_encontrados, start=1):
    print(f"Camino {i}: {camino}")