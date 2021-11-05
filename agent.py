# coding: utf-8

import json

from lib.os_ import OSInfo
from lib.cpu import CPUInfo
from lib.net import NetInfo
from lib.ram import RAMInfo
from lib.solana import SolanaInfo
from lib.tuning import TuningInfo
from lib.storage import StorageInfo


def __main__():
    os_info = OSInfo()
    cpu_info = CPUInfo()
    net_info = NetInfo()
    ram_info = RAMInfo()
    solana_info = SolanaInfo()
    tuning_info = TuningInfo()
    storage_info = StorageInfo()

    data = {
        "os": {
            "swap_used": os_info.swap_used_human,
            "swap_total": os_info.swap_total_human,
            "ramdisk_size": os_info.ramdisk_size,

            "distribution": os_info.distribution,
            "kernel_version": os_info.kernel_version,
        },
        "cpu": {
            "name": cpu_info.cpu_name,
            "governors": cpu_info.governors,
            "cores_number": cpu_info.cores_number,
        },
        "net": {
            "adapters": net_info.adapters,
        },
        "ram": {
            "size": ram_info.size_human
        },
        "storage": {
            "size": storage_info.size_human,
            "raid_levels": storage_info.raid_levels
        },
        "tuning": {
            "sysctl_params": dict(
                sorted(tuning_info.sysctl_params.items(), key=lambda t: t[0]))
        },
        "solana": {
            "address": solana_info.address,
            "version": solana_info.version,
        }
    }
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    __main__()