from mkdisk import MkDisk
from rmdisk import RmDisk
from rep import reporte
from fdisk import FDisk

def main():
    # disk = MkDisk()
    # disk.fit  = 'FF'
    # disk.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    # disk.size = 10
    # disk.unit = 'M'
    # disk.create()

    # rm = RmDisk()
    # rm.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    # rm.remove()

    repo = reporte()
    repo.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    repo.rep()

    # partition = FDisk()
    # # partition.delete = "FULL"
    # partition.size = 2
    # partition.type = 'P'
    # partition.unit = 'M'
    # partition.path = r'C:\Users\wwwed\OneDrive\Escritorio\Octavo_Semestre\LAB_Archivos\MIA_T2_202001144\T2\DISCOS\disco.dsk'
    # partition.name = 'primaria2megas'
    # partition.fit = 'wf'
    # # partition.add = '100'
    # partition.recibeData()

    # repo = reporte()
    # repo.path = r'\Users\JONATHAN ALVARADO\Desktop\disco.dk'
    # repo.rep()
    # pass

if __name__ == '__main__':
    main()