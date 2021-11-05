# coding: utf-8

import os
import psutil
import platform
from .utils import humanize_size

# Fix for Python2+
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class OSInfo(object):
    __slots__ = (
        "swap_used",
        "swap_total",
        "ramdisk_size",

        "distribution",
        "kernel_version",
    )

    @property
    def swap_used_human(self):
        return humanize_size(self.swap_used)

    @property
    def swap_total_human(self):
        return humanize_size(self.swap_total)

    def __init__(self):
        self.swap_used = 0
        self.swap_total = 0
        self.distribution = None
        self.ramdisk_size = None
        self.kernel_version = None

        self.read_os_info()
        self.read_swap_info()
        self.read_ramdisk_info()

    def read_os_info(self):
        self.distribution = self.read_distribution().lower()
        self.kernel_version = platform.release()

    def read_swap_info(self):
        swap = psutil.swap_memory()
        self.swap_used = swap.used
        self.swap_total = swap.total

    def read_ramdisk_info(self):
        """ Read ramdisk info from /etc/fstab
        """
        with open("/etc/fstab") as f:
            for line in f:
                if not line.startswith("tmpfs"):
                    continue
                self.ramdisk_size = line.split("size=")[1].split(" ")[0] + "B"

    def read_distribution(self):
        """ Read /etc/lsb_release if possible
        """
        try:
            return "%s" % "-".join(platform.linux_distribution())
        except AttributeError:
            # Deprecated since Python 3.7
            pass

        try:
            _data = dict()
            with open("/etc/lsb-release") as f:
                for line in f:
                    if line.startswith("DISTRIB_"):
                        key, value = line.strip().split("=")
                        _data[key] = value
            return "%s-%s-%s" % (_data["DISTRIB_ID"], _data["DISTRIB_RELEASE"],
                                 _data["DISTRIB_CODENAME"])
        except FileNotFoundError:
            pass

        return ""
