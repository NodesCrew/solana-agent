# coding: utf-8

import subprocess

SYSCTL_PARAMS_MAP = {
    "net.core.rmem_max": int,
    "net.core.rmem_default": int,
    "net.core.wmem_max": int,
    "net.core.wmem_default": int,
    "vm.swappiness": int,
    "vm.max_map_count": int,
}


def iter_sysctl_params():
    data = subprocess.check_output(["sysctl", "-a"])
    for line in data.split("\n"):
        if line.strip():
            param, value = line.split("=")
            yield param.strip(), value.strip()


class TuningInfo(object):
    __slots__ = (
        "sysctl_params",
    )

    def __init__(self):
        self.sysctl_params = dict()
        self.read_sysctl_params()

    def read_sysctl_params(self):
        """ Read sysctl params
        """
        for param, value in iter_sysctl_params():
            if param in SYSCTL_PARAMS_MAP:
                self.sysctl_params[param] = SYSCTL_PARAMS_MAP[param](value)
