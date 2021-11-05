# coding: utf-8

import mdstat
import psutil
from .utils import humanize_size


class StorageInfo(object):
    __slots__ = ("size", "raid_levels")

    @property
    def size_human(self):
        return humanize_size(self.size)

    def __init__(self):
        self.size = 0
        self.raid_levels = []
        self.read_size_info()
        self.read_raid_info()

    def read_size_info(self):
        """ Read total disks size
        """
        for part in psutil.disk_partitions():
            disk = psutil.disk_usage(part.mountpoint)
            self.size += disk.total

    def read_raid_info(self):
        """ Read RAID info
        """
        stat = mdstat.parse()
        for device, device_info in stat["devices"].items():
            self.raid_levels.append(device_info["personality"])

