# coding: utf-8
import glob


class CPUInfo(object):
    __slots__ = ("cpu_name", "governors", "cores_number")

    def __init__(self):
        self.cpu_name = None
        self.governors = []
        self.cores_number = 0

        self.read_cpu_info()
        self.read_governors()

    def read_cpu_info(self):
        """ Read CPU info
        """
        with open("/proc/cpuinfo") as f:
            text_data = [x.strip() for x in f.read().split("\n\n") if x.strip()]
            self.cores_number = len(text_data)

        for line in text_data[0].split("\n"):
            if line.startswith("model name"):
                _, cpu_name = line.split(":")
                self.cpu_name = cpu_name.strip()

    def read_governors(self):
        pattern = "/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
        governors = set()
        for path in glob.glob(pattern):
            with open(path) as f:
                governors.add(f.read().strip())
        self.governors = list(governors)