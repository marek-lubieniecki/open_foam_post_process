from forces_file import ForcesFile, ForcesFilesSupersonic
from pressure_file import PressureFile
import numpy as np


class OpenFoamCase:
    def __init__(self, directory, version):
        self.directory = directory
        self.version = version

        self.forces_folders = ["forcesRocket"]
        self.forces_files = []
        self.pressure_folders = ["averagePressure"]
        self.yplus_folder = ["yplus"]
        self.residual_folder = ["residuals"]
        self.force_array = np.zeros([6, len(self.forces_folders)])
        self.pressure_array = np.zeros([1, len(self.pressure_folders)])

    def get_forces_subsonic(self):

        for id, force_folder in enumerate(self.forces_folders):
            folderPath = self.directory + '/' + force_folder + '/0/' + 'forces.dat'
            forceFile = ForcesFile(folderPath)
            self.force_array[:, id] = forceFile.forces_summary
            self.forces_files.append(forceFile)
            if id == 0:
                forceFile.plot_forces()

    def get_forces_supersonic(self):
        for id, force_folder in enumerate(self.forces_folders):
            folderPath = self.directory + '/' + force_folder + '/0'
            forcesFile = ForcesFilesSupersonic(folderPath)
            self.force_array[:, id] = forcesFile.forces_summary
            self.forces_files.append(forcesFile)

    def get_base_pressure(self):
        filepath = self.directory + '/' + self.pressure_folders[0] + '/0/surfaceFieldValue.dat'
        pressureFile = PressureFile(filepath)
        self.pressure_array[0, 0] = pressureFile.pressure_final

    def save_forces(self):
        save_filename = self.directory + "_case_forces.txt"
        np.savetxt(save_filename, self.force_array)

    def save_pressures(self):
        save_filename = self.directory + "_case_pressures.txt"
        np.savetxt(save_filename, self.pressure_array)