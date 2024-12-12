# Clase para representar una canción
class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion})"

# Clase para representar un nodo de la lista enlazada
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None

# Clase principal para la lista enlazada de canciones
class PlaylistManager:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cabeza = None
        self.total_canciones = 0

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        self.total_canciones += 1
        
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            return
        
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo_nodo

    def eliminar_cancion(self, titulo):
        if not self.cabeza:
            return False

        if self.cabeza.cancion.titulo == titulo:
            self.cabeza = self.cabeza.siguiente
            self.total_canciones -= 1
            return True

        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.cancion.titulo == titulo:
                actual.siguiente = actual.siguiente.siguiente
                self.total_canciones -= 1
                return True
            actual = actual.siguiente
        return False

    def buscar_cancion(self, titulo):
        actual = self.cabeza
        while actual:
            if actual.cancion.titulo == titulo:
                return actual.cancion
            actual = actual.siguiente
        return None

    def mostrar_playlist(self):
        if not self.cabeza:
            print("\nLa playlist está vacía.")
            return

        print(f"\nPlaylist: {self.nombre}")
        print(f"Total de canciones: {self.total_canciones}")
        print("-" * 50)
        
        actual = self.cabeza
        posicion = 1
        while actual:
            print(f"{posicion}. {actual.cancion}")
            actual = actual.siguiente
            posicion += 1

# Interfaz de línea de comandos
def menu():
    print("\n=== GESTOR DE PLAYLIST ===")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Buscar canción")
    print("4. Mostrar playlist")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    playlist = PlaylistManager("Mi Playlist Favorita")
    
    while True:
        opcion = menu()
        
        if opcion == "1":
            titulo = input("Título de la canción: ")
            artista = input("Artista: ")
            duracion = input("Duración (mm:ss): ")
            cancion = Cancion(titulo, artista, duracion)
            playlist.agregar_cancion(cancion)
            print("\n¡Canción agregada exitosamente!")
            
        elif opcion == "2":
            titulo = input("Título de la canción a eliminar: ")
            if playlist.eliminar_cancion(titulo):
                print("\n¡Canción eliminada exitosamente!")
            else:
                print("\nCanción no encontrada.")
                
        elif opcion == "3":
            titulo = input("Título de la canción a buscar: ")
            cancion = playlist.buscar_cancion(titulo)
            if cancion:
                print(f"\nCanción encontrada: {cancion}")
            else:
                print("\nCanción no encontrada.")
                
        elif opcion == "4":
            playlist.mostrar_playlist()
            
        elif opcion == "5":
            print("\n¡Gracias por usar el Gestor de Playlist!")
            break
            
        else:
            print("\nOpción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()