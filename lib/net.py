# coding: utf-8
import subprocess


class NetInfo(object):
    __slots__ = (
        "adapters",
    )

    def __init__(self):
        self.adapters = []
        self.read_adapters()

    def read_adapters(self):
        data = subprocess.check_output(["lspci"])

        for line in data.split("\n"):
            line = line.strip()
            try:
                _, adapter = line.split("Ethernet controller: ")
                self.adapters.append(adapter)
            except ValueError:
                continue
