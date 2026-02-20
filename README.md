##  Guía de Uso

La ejecución se realiza a través del script principal `main.py` utilizando diversos flags para configurar el problema y el algoritmo.

### Estructura del Comando

```bash
python main.py -p PROBLEM -f FUNCTION -l LAYOUT_FILE [OPCIONES]

```

### Argumentos Principales

| Parámetro | Descripción | Ejemplo |
| --- | --- | --- |
| `-p` | Clase del problema (definido en `algorithms/problems.py`). | `SimpleSurvivorProblem` |
| `-f` | Algoritmo de búsqueda (BFS, DFS, A*, etc.). | `tinyHouseSearch` |
| `-l` | Archivo de mapa/entorno (sin extensión `.lay`). | `tinyHouse` |
| `-h` | Heurística obligatoria para búsquedas tipo **A***. | `manhattanHeuristic` |

---

## Opciones de Configuración

Puedes personalizar la simulación con los siguientes parámetros adicionales:

### Visualización e Interfaz

* **`-t` (Modo Texto):** Desactiva la interfaz gráfica. Ideal si trabajas desde una terminal sin servidor X o SSH.
* **`-q` (Modo Silencioso):** Salida mínima en consola, sin gráficos. Perfecto para pruebas de rendimiento.
* **`-z [valor]`:** Ajusta el zoom de la ventana (ej: `2.0` para duplicar, `0.5` para reducir).
* **`-x [segundos]`:** Tiempo de espera entre cada paso. Si usas un valor negativo, el agente avanzará de forma manual paso a paso.

### Utilidades y Depuración

* **`-r` (Registro):** Guarda el historial completo de las acciones del robot en un archivo de log.
* **`-c` (Manejo de Excepciones):** Evita que el programa se detenga si ocurre un error inesperado, intentando continuar la ejecución.
* **`--help`:** Muestra todas las opciones de ayuda directamente en la terminal.

---

##  Ejemplo de Ejecución

Para probar el sistema con el escenario de ejemplo `tinyHouse`, ejecuta el siguiente comando:

```bash
python main.py -p SimpleSurvivorProblem -f tinyHouseSearch -l tinyHouse -x 0.5 -z 2.0
