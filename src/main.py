def multiplicacion(a, b):
    return a * b

def calculate(operacion: str) -> float:
    operadores = {'+': suma, '-': resta, '*': multiplicacion, '/': division}
    
    for simbolo, funcion in operadores.items():
        if simbolo in operacion:
            partes = operacion.split(simbolo)
            if len(partes) == 2:
                try:
                    a = float(partes[0].strip())
                    b = float(partes[1].strip())
                    return funcion(a, b)
                except ValueError:
                    return "Error: Números inválidos"
    return "Error: Operación no válida"