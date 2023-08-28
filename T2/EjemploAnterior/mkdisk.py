from estructuras import Mbr, Partition
import random
import time
import struct 
import os

class MkDisk:
    def __init__(self):
        self.size = 0
        self.fit = 0
        self.unit = ''
        self.path = ''
        self.name = ''

    def driver(self, disco):
        
        complete_path  = disco.path = disco.name
        mbr_partition = [Partition() for _ in range(4)]

        if not self.existsPath(disco.path):
            self.createPath(disco.path)

    def existsPath(self, path):
        return os.path.isdir(path)

    def createPath(self, path):
        try:
            os.makedirs(path, exist_ok=True)
            print("RUTA creada con exito")
        except OSError as e:
            print("Error al crear la ruta")


    def create(self, disco):
        try:
            with open(disco.path, "wb") as file:
                buffer = bytearray(1024)
                if disco.unit.lower == 'k':
                    for _ in range(disco.size):
                        file.write(buffer)
                else:
                    for _ in range(disco.size*1024):
                        file.write(buffer)

            size = disco.size*1024 if not disco.unit or disco.unit.lower == 'm'else disco.size*1024*1024

            mbr_disco = Mbr()
            mbr_disco.dsk_fit = 'F'
            mbr_disco.mbr_fecha_creacion = int(time.time())
            mbr_disco.mbr_disk_signature = random.randint(1, 999999)
            mbr_disco.mbr_tamaño = size

            part_vacia = Partition()
            part_vacia.part_status = '0'
            part_vacia.part_type = '-'
            part_vacia.part_fit = '-'
            part_vacia.part_start = -1
            part_vacia.part_size = -1
            part_vacia.part_name = b'0'*16

            mbr_disco.mbr_partition = [part_vacia]*4

            with open(disco.path, 'rb+') as file:
                file.write(struct.pack('', mbr_disco.mbr_tamaño, 
                                            mbr_disco.mbr_tamaño,
                                            mbr_disco.mbr_fecha_creacion,
                                            mbr_disco.dsk_fit.encode(),
                                            mbr_disco.mbr_partition[0],
                                            mbr_disco.mbr_partition[1],
                                            mbr_disco.mbr_partition[2],
                                            mbr_disco.mbr_partition[3],))

        
            print("DISCO creado exitosamente en la ruta: ", disco.path)
        except OSError as e:
            print("Error in mkdisk")


