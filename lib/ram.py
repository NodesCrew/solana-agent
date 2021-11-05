# coding: utf-8
import psutil
from .utils import humanize_size


class RAMInfo(object):
    __slots__ = ("size", "freq")

    @property
    def size_human(self):
        return humanize_size(self.size)

    def __init__(self):
        self.size = 0
        self.read_ram_info()

    def read_ram_info(self):
        mem = psutil.virtual_memory()
        self.size = mem.total
