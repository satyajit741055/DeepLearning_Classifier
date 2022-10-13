import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')

package_name = "deepClassifier"

list_of_files = [
   ".github/workflows/.gitkeep", # gitkeep used so that github will not take empty folder
   f"src/{package_name}/__init__.py",  # package
   f"src/{package_name}/components/__init__.py", # Structure 
   f"src/{package_name}/utils/__init__.py", # Structure 
   f"src/{package_name}/config/__init__.py", # Structure 
   f"src/{package_name}/pipeline/__init__.py", # Structure 
   f"src/{package_name}/entity/__init__.py", # Structure 
   f"src/{package_name}/constants/__init__.py",# Structure 
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml", # congiguration
   "dvc.yaml", # DVC pipeline file 
   "params.yaml",# Training Parameters 
   "init_setup.sh",# shell script file for creating environment 
   "requirements.txt", # requirements.txt 
   "requirements_dev.txt", # development Requirement 
   "setup.py", #for package 
   "setup.cfg", # for package 
   "pyproject.toml", # for package 
   "tox.ini", # testing of project locally 
   "research/trials.ipynb", # trial purpose
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")