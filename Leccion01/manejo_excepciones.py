from NumerosIdenticosException import NumerosIdenticosException

resultado = None

try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        # raise se encarga de arrojar excepciones, ya sean personalizadas y predefinidas, seria como un throw
        raise NumerosIdenticosException('números idénticos')
    resultado = a/b
except ZeroDivisionError as e:
    print(f"Ocurrio un error ZeroDivisionError: {e}, {type(e)}")
except TypeError as e:
    print(f'Ocurrio un error TypeError: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error general: {e}, {type(e)}')
else:  # else en un bloque try funciona como su homologo en un if, si no es capturada ninguna excepcion, entra el bloque else
    print('No se arrojó ninguna excepción')
finally:
    print('Hola soy el bloque finally, entro por mis huevos haya excepcion o nó jeje')

print(f'Resultado: {resultado}')
print('Continuamos...')
