import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class ForcesFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = None
        self.new_file = None

        self.torque_reference_point = 0
        self.iterations = []
        self.force_x = []
        self.force_y = []
        self.force_z = []
        self.torque_x = []
        self.torque_y = []
        self.torque_z = []
        self.centre_of_pressure = []
        self.forces_summary = []

        self.force_x_average = 0
        self.force_y_average = 0
        self.force_z_average = 0

        self.torque_x_average = 0
        self.torque_y_average = 0
        self.torque_z_average = 0

        self.force_x_final = 0
        self.force_y_final = 0
        self.force_z_final = 0

        self.torque_x_final = 0
        self.torque_y_final = 0
        self.torque_z_final = 0

        self.centre_of_pressure_average = 0

        self.load_file()

    def load_file(self):
        self.file = open(self.filepath, "r")

        for line_no, line in enumerate(self.file.readlines()):
            new_line = line.replace('(','').replace(')','')
            split_line = new_line.split()
            if line_no == 1:
                pass
            if line_no >= 3:
                self.iterations.append(split_line[0])
                self.force_x.append(float(split_line[1]) + float(split_line[4]))
                self.force_y.append(float(split_line[2]) + float(split_line[5]))
                self.force_z.append(float(split_line[3]) + float(split_line[6]))
                self.torque_x.append(float(split_line[7]) + float(split_line[10]))
                self.torque_y.append(float(split_line[8]) + float(split_line[11]))
                self.torque_z.append(float(split_line[9]) + float(split_line[12]))
                self.centre_of_pressure.append(self.torque_z[-1]/self.force_y[-1])

        self.force_x_average = get_end_average(self.force_x, 100)
        self.force_y_average = get_end_average(self.force_y, 100)
        self.force_z_average = get_end_average(self.force_z, 100)

        self.torque_x_average = get_end_average(self.torque_x, 100)
        self.torque_y_average = get_end_average(self.torque_y, 100)
        self.torque_z_average = get_end_average(self.torque_z, 100)

        self.centre_of_pressure_average = get_end_average(self.centre_of_pressure, 100)

        self.forces_summary.append(self.force_x[-1])
        self.forces_summary.append(self.force_y[-1])
        self.forces_summary.append(self.force_z[-1])
        self.forces_summary.append(self.torque_x[-1])
        self.forces_summary.append(self.torque_y[-1])
        self.forces_summary.append(self.torque_z[-1])



    def plot_forces(self):
        fig, axs = plt.subplots(3, 3, sharex='col')
        fig.set_size_inches(15, 8)
        axs[0, 0].xaxis.set_major_locator(ticker.MultipleLocator(200))
        axs[0, 1].xaxis.set_major_locator(ticker.MultipleLocator(200))
        axs[0, 2].xaxis.set_major_locator(ticker.MultipleLocator(200))

        axs[0, 0].title.set_text('Force x')
        axs[1, 0].title.set_text('Force y')
        axs[2, 0].title.set_text('Force z')

        axs[0, 1].title.set_text('Torque x')
        axs[1, 1].title.set_text('Torque y')
        axs[2, 1].title.set_text('Torque z')

        axs[0, 2].title.set_text('COP')

        axs[0, 0].plot(self.iterations, self.force_x)
        axs[1, 0].plot(self.iterations, self.force_y)
        axs[2, 0].plot(self.iterations, self.force_z)

        axs[0, 1].plot(self.iterations, self.torque_x)
        axs[1, 1].plot(self.iterations, self.torque_y)
        axs[2, 1].plot(self.iterations, self.torque_z)

        axs[0, 2].plot(self.iterations, self.centre_of_pressure)

        plt.show()

    def print_forces(self):
        print("Force x: ", self.force_x[-1], " ", "Last 100 iter average: ", self.force_x_average)
        print("Force y: ", self.force_y[-1], " ", "Last 100 iter average: ", self.force_y_average)
        print("Force z: ", self.force_z[-1], " ", "Last 100 iter average: ", self.force_z_average)
        print("Torque x: ", self.torque_x[-1], " ", "Last 100 iter average: ", self.torque_x_average)
        print("Torque y: ", self.torque_y[-1], " ", "Last 100 iter average: ", self.torque_y_average)
        print("Torque z: ", self.torque_z[-1], " ", "Last 100 iter average: ", self.torque_z_average)
        print("COP :", self.centre_of_pressure[-1], " ", "Last 100 iter average: ", self.centre_of_pressure_average)


def get_end_average(force_list, number_of_iterations):
    return sum(force_list[-number_of_iterations:])/number_of_iterations


class ForcesFilesSupersonic:
    def __init__(self, files_directory):
        self.files_directory = files_directory
        self.force_filepath = files_directory + '/force.dat'
        self.torque_filepath = files_directory + '/moment.dat'
        self.force_file = None
        self.torque_file = None
        self.new_file = None

        self.torque_reference_point = 0
        self.iterations = []
        self.force_x = []
        self.force_y = []
        self.force_z = []
        self.torque_x = []
        self.torque_y = []
        self.torque_z = []
        self.centre_of_pressure = []
        self.forces_summary = []

        self.force_x_average = 0
        self.force_y_average = 0
        self.force_z_average = 0

        self.torque_x_average = 0
        self.torque_y_average = 0
        self.torque_z_average = 0

        self.force_x_final = 0
        self.force_y_final = 0
        self.force_z_final = 0

        self.torque_x_final = 0
        self.torque_y_final = 0
        self.torque_z_final = 0

        self.centre_of_pressure_average = 0

        self.load_files()

    def load_files(self):

        self.force_file = open(self.force_filepath, "r")
        self.torque_file = open(self.torque_filepath, "r")

        for line_no, line in enumerate(self.force_file.readlines()):
            split_line = line.split()
            if line_no == 1:
                pass
            if line_no >= 5:
                self.iterations.append(split_line[0])
                self.force_x.append(float(split_line[1]))
                self.force_y.append(float(split_line[2]))
                self.force_z.append(float(split_line[3]))

        for line_no, line in enumerate(self.torque_file.readlines()):
            split_line = line.split()
            if line_no == 1:
                 pass
            if line_no >= 5:
                self.torque_x.append(float(split_line[1]))
                self.torque_y.append(float(split_line[2]))
                self.torque_z.append(float(split_line[3]))
                self.centre_of_pressure.append(self.torque_z[-1]/self.force_y[-1])

        self.force_x_average = get_end_average(self.force_x, 100)
        self.force_y_average = get_end_average(self.force_y, 100)
        self.force_z_average = get_end_average(self.force_z, 100)

        self.torque_x_average = get_end_average(self.torque_x, 100)
        self.torque_y_average = get_end_average(self.torque_y, 100)
        self.torque_z_average = get_end_average(self.torque_z, 100)

        self.centre_of_pressure_average = get_end_average(self.centre_of_pressure, 100)

        self.forces_summary.append(self.force_x[-1])
        self.forces_summary.append(self.force_y[-1])
        self.forces_summary.append(self.force_z[-1])
        self.forces_summary.append(self.torque_x[-1])
        self.forces_summary.append(self.torque_y[-1])
        self.forces_summary.append(self.torque_z[-1])

