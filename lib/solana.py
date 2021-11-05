# coding: utf-8

import subprocess


class SolanaInfo(object):
    __slots__ = ("version", "address")

    def __init__(self):
        self.version = None
        self.address = None

        self.read_address()
        self.read_version()

    def read_address(self):
        """ Read solana address (identity) """
        data = subprocess.check_output(["solana", "address"])
        self.address = data.strip()

    def read_version(self):
        data = subprocess.check_output(["solana", "--version"])
        self.version = data.strip()
