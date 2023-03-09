import os
import os.path as op

# Add the path here
PATH = "Model_Monitoring/"

START_PATH = op.dirname(op.abspath(__file__))

python_scripts = []  # list of python scripts

with os.scandir(PATH) as entries:
    for entry in entries:
        file_name = entry.name
        if file_name[len(file_name) - 3 :] == ".py":
            python_scripts.append(file_name)

for py_file in python_scripts:
    print(60 * "-")
    print("Running ", py_file)
    print(60 * "-")
    os.system("cd " + PATH + "&" + "python " + PATH + py_file)
    input("Press Enter to run the next file (if exists..)")
