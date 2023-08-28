import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = (
    'MKDISK',
    'FDISK',
    'SIZE',
    'UNIT',
    'PATH',
    'TYPE',
    'NAME',
    'NUM',
    'LETRA',
    'IGUAL',
    'MAYOR',
    'DIR',
    'LETRA_FKDISK',
    'CADENA',
)

# Expresiones regulares para tokens simples
t_MKDISK = r'mkdisk'
t_FDISK = r'fkdisk'
t_SIZE = r'size'
t_UNIT = r'unit'
t_PATH = r'path'
t_TYPE = r'type'
t_NAME = r'name'
t_MAYOR = r'>'
t_LETRA = r'[KM]'
t_LETRA_FKDISK = r'[BKM]'
t_NUM = r'\d+'
t_IGUAL = r'='

# Expresión regular para directorio
def t_DIR(t):
    r'\/[a-zA-Z0-9_\/\.]+'
    return t

# Expresión regular para directorio
def t_CADENA(t):
    # r'[a-zA-Z0-9]?[a-zA-Z0-9_]*'
    r'cadena'
    return t

# Ignorar caracteres en blanco y saltos de línea
t_ignore = ' \t\n'

# Manejo de errores
def t_error(t):
    print("Carácter ilegal:", t.value[0])
    t.lexer.skip(1)

# Construcción del analizador léxico
lexer = lex.lex()

# Variables para almacenar los valores de los comandos
command = ""
size = ""
unit = ""
path = ""
type = ""
name = ""
letra = ""
letra_fkdisk = ""


# Reglas de gramática
def p_comando_mkdisk(p):
    '''comando : MKDISK optional_unit
                | MKDISK'''
    global command, size, unit, path, letra
    command = "mkdisk"
    # size = p[5]
    if len(p) == 3:
        letra = p[2]
    # path = p[10]
    # print(len(p))
    print(f"Comando: {command}")
    print(f"Tamaño: {size}")
    if letra:
       print(f"Unit: {letra}")
    print(f"Path: {path}")
#  mkdisk >size=4 >unit=M >path=/home/user/Disco1.dsk


# Regla para la parte opcional UNIT IGUAL LETRA
def p_optional_unit(p):
    '''optional_unit : UNIT IGUAL LETRA
                     | '''
    if len(p) == 4:
        p[0] = p[3]
    else:
        p[0] = ""



def p_comando_fdisk(p):
    # fkdisk >size=4 >unit=M >path=/home/user/Disco1.dsk
    '''comando : FDISK atributos'''
    global command
    command = "fdisk"
    # type = p[4]
    # unit = p[7]
    # name = p[10]
    # size = p[12]
    # if len(p) == 15:
    #     path = p[2]
    print(f"Comando: {command}")
    # if path:
    #     print(f"Ruta: {path}")
    # print(f"Tipo: {type}")
    # print(f"Unidad: {unit}")
    # print(f"Nombre: {name}")
    # print(f"Tamaño: {size}")



def p_atributos(p):
    '''atributos : atributos atributo
                 | atributo'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_atributo(p):
    # UNIT OPCIONAL
    '''atributo : MAYOR TYPE IGUAL LETRA
                | MAYOR PATH IGUAL DIR
                | MAYOR UNIT IGUAL LETRA_FKDISK
                | MAYOR NAME IGUAL CADENA
                | MAYOR SIZE IGUAL NUM'''
    p[0] = (p[1], p[4])

    

# Manejo de errores sintácticos
def p_error(p):
    print("Error de sintaxis")

# Construcción del analizador sintáctico
parser = yacc.yacc()

# Lectura de comandos desde la entrada estándar
while True:
    try:
        entrada = input("Ingrese un comando: ")
        if entrada.lower() == "exit":
            break
        parser.parse(entrada)
    except EOFError:
        break
