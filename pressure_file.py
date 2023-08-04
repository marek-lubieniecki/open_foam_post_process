
class PressureFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None

        self.iterations = []
        self.pressures = []

        self.pressure_final = 0

        self.load_file()

    def load_file(self):
        self.file = open(self.filepath, "r")

        for line_no, line in enumerate(self.file.readlines()):
            split_line = line.split()
            if line_no == 1:
                pass
            if line_no >= 5:
                self.iterations.append(split_line[0])
                self.pressures.append(split_line[1])

        self.pressure_final = self.pressures[-1]
