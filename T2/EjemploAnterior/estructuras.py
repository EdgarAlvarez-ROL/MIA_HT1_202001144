class Partition:
    def __init__(self):
        self.part_status = ''
        self.part_type = ''
        self.part_fit = ''
        self.part_size = 0
        self.part_start = 0
        self.part_name = ''


class Mbr:
    def __init__(self):
        self.mbr_tamaño = 0
        self.mbr_fecha_creacion = 0
        self.mbr_disk_signature = 0
        self.dsk_fit = ''
        self.mbr_partition = [Partition() for _ in range(4)]