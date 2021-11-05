# coding: utf-8


def humanize_size(bytes_count, suffix="B"):
    scale = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_count < scale:
            return "%.2f%s%s" % (bytes_count, unit, suffix)
        bytes_count /= scale
