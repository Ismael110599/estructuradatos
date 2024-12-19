class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class AnalizadorSintactico:
    def __init__(self):
        self.operadores = {'+', '-', '*', '/'}

    def es_balanceada(self, expresion):
        pila = []
        pares = {')': '(', '}': '{', ']': '['}
        for char in expresion:
            if char in '({[':
                pila.append(char)
            elif char in ')}]':
                if not pila or pila[-1] != pares[char]:
                    return False
                pila.pop()
        return not pila

    def es_valida(self, expresion):
        if not self.es_balanceada(expresion):
            return False, "Error: Expresión no balanceada."

        anterior = None
        for char in expresion.replace(' ', ''):
            if char.isalnum():
                if anterior and anterior.isalnum():
                    return False, "Error: Operandos consecutivos."
            elif char in self.operadores:
                if not anterior or anterior in self.operadores or anterior in '({[':
                    return False, "Error: Operador en posición inválida."
            anterior = char

        if anterior in self.operadores:
            return False, "Error: Expresión termina en operador."

        return True, "Expresión válida."

    def construir_arbol(self, expresion):
        def es_operador(c):
            return c in self.operadores

        pila_nodos = []
        for char in expresion.replace(' ', ''):
            if char.isalnum():
                pila_nodos.append(NodoArbol(char))
            elif es_operador(char):
                nodo = NodoArbol(char)
                nodo.derecho = pila_nodos.pop()
                nodo.izquierdo = pila_nodos.pop()
                pila_nodos.append(nodo)
        return pila_nodos[0] if pila_nodos else None

    def mostrar_arbol(self, nodo, nivel=0):
        if nodo:
            self.mostrar_arbol(nodo.derecho, nivel + 1)
            print(' ' * 4 * nivel + '->', nodo.valor)
            self.mostrar_arbol(nodo.izquierdo, nivel + 1)

# Ejemplo de uso
analizador = AnalizadorSintactico()
expresion = "(a + b) * c"
valida, mensaje = analizador.es_valida(expresion)
print(mensaje)

if valida:
    arbol = analizador.construir_arbol("ab+c*")  # Notación postfija
    print("Árbol de expresión:")
    analizador.mostrar_arbol(arbol)
