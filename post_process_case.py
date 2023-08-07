from openfoam_case import OpenFoamCase
import os


cases_folder = "supersonic_test"  # define folder with results

print("Opening cases")

# Iterate over cases in the folder
for path in os.listdir(cases_folder):
    case_path = cases_folder + '/' + path
    print(case_path)
    if not os.path.isfile(case_path):
        case = OpenFoamCase(case_path,'10')
        if "subsonic" in cases_folder:
            case.get_forces_subsonic()
        else:
            case.get_forces_supersonic()
        case.save_forces()




