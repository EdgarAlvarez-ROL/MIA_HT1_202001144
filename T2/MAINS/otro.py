import ply.lex as lex
import ply.yacc as yacc
from mkdisk import MkDisk
from rep import reporte


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
    'LETRA_MKDISK',
    'IGUAL',
    'MAYOR',
    'DIR',
    'LETRA_FDISK',
    'CADENA',
    'REP',
)

# Expresiones regulares para tokens simples
t_MKDISK = r'mkdisk'
t_FDISK = r'fdisk'
t_REP = r'rep'
t_SIZE = r'size'
t_UNIT = r'unit'
t_PATH = r'path'
t_TYPE = r'type'
t_NAME = r'name'
t_MAYOR = r'>'
t_LETRA_MKDISK = r'[MK]'
t_LETRA_FDISK = r'[BKM]'
t_NUM = r'\d+'
t_IGUAL = r'='

# Expresión regular para directorio
def t_DIR(t):
    # r'\/[a-zA-Z0-9_\/\.]+'
    r'C:\\[^\\]+(\\[^\\]+)*\\[^.]+\.[a-zA-Z0-9]+'
    # r'[^\\]+(\\[^\\]+)*\\[^.]+\.[a-zA-Z0-9]+'
    # r'\\[a-zA-Z0-9_\\\.]+'
    return t

# Expresión regular para cadena
def t_CADENA(t):
    r'"[^"]+"|\'[^\']+\''
    t.value = t.value[1:-1]  # Elimina las comillas alrededor de la cadena
    # r'[a-zA-Z][a-zA-Z0-9_]*'
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
unit_fkdisk = ""


# Reglas de gramática
def p_comando_mkdisk(p):
    '''comando : MKDISK atributosm'''
    global command, size, unit, path
    command = "mkdisk"
    print(f"Comando: {command}")
    for atributo in p[2]:
        # print(f"{atributo[0]}: {atributo[1]}")
        if atributo[0] == "size":
            size = atributo[1]
        elif atributo[0] == "unit":
            unit = atributo[1]
        elif atributo[0] == "path":
            path = atributo[1]
    # imprimir valores ingresados
    print("Size: "+str(size))
    print("Unit: "+str(unit))
    print("Path: "+str(path))
    
    # creacion del disco con los valores ingresados
    disk = MkDisk()
    disk.fit  = 'FF'
    disk.path = path
    disk.size = size
    disk.unit = unit
    disk.create()

    # reseteo de las variables para su uso futuro
    size = ""
    unit = ""
    path = ""
    

def p_atributosM(p):
    '''atributosm : atributosm atributom
                 | atributom'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_atributoM(p):
    '''atributom : MAYOR PATH IGUAL DIR
                 | MAYOR UNIT IGUAL LETRA_FDISK
                 | MAYOR SIZE IGUAL NUM'''
    p[0] = (p[2], p[4])



# Reglas para el comando fdisk
def p_comando_fdisk(p):
    '''comando : FDISK atributos'''
    global command, size, unit_fkdisk, path, name, type
    command = "fdisk"
    print(f"Comando: {command}")
    for atributo in p[2]:
        # print(f"{atributo[0]}: {atributo[1]}")
        if atributo[0] == "size":
            size = atributo[1]
        elif atributo[0] == "unit":
            unit_fkdisk = atributo[1]
        elif atributo[0] == "type":
            type = atributo[1]
        elif atributo[0] == "path":
            path = atributo[1]
        elif atributo[0] == "name":
            name = atributo[1]
    print("Size: "+str(size))
    print("Unit: "+str(unit_fkdisk))
    print("Path: "+str(path))
    print("Name: "+str(name))
    print("Type: "+str(type))
    size = ""
    unit_fkdisk = ""
    path = ""
    name = ""
    type = ""
    

def p_atributos(p):
    '''atributos : atributos atributo
                 | atributo'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_atributo(p):
    '''atributo : MAYOR PATH IGUAL DIR
                | MAYOR TYPE IGUAL LETRA_FDISK
                | MAYOR UNIT IGUAL LETRA_FDISK
                | MAYOR NAME IGUAL CADENA
                | MAYOR SIZE IGUAL NUM'''
    p[0] = (p[2], p[4])



# reglas comadno REP
def p_comando_rep(p):
    '''comando : REP'''
    global path
    repo = reporte()
    repo.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    repo.rep()

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
