from forces_file import ForcesFile
from openfoam_case import OpenFoamCase

cases_folder = "subsonic_droptest_mesh"
cases = []

for i in range(1,13):
    cases.append(str(i))

for case in cases:
    case_path = cases_folder + '/' + case
    case = OpenFoamCase(case_path,'10')
    if cases_folder == "subsonic_droptest_mesh":
        case.get_forces_subsonic()
    else:
        case.get_forces_supersonic()
    case.save_forces()

   # case.get_base_pressure()
   # case.save_pressures()



