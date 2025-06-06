import os
from pathlib import Path

# Define the root project folder name
project_name = "src"

# List of all files (and nested folders) you want to create as part of your project scaffold
list_of_files = [

    f"{project_name}/__init__.py",  # Root __init__.py
    f"{project_name}/components/__init__.py",  # components folder with __init__.py
    f"{project_name}/components/data_ingestion.py",  
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",

    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/mongo_db_connection.py",
    f"{project_name}/configuration/aws_connection.py",

    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",

    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/proj1_data.py",

    f"{project_name}/constants/__init__.py",

    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/estimator.py",
    f"{project_name}/entity/s3_estimator.py",

    f"{project_name}/exception/__init__.py",

    f"{project_name}/logger/__init__.py",

    f"{project_name}/pipline/__init__.py",
    f"{project_name}/pipline/training_pipeline.py",
    f"{project_name}/pipline/prediction_pipeline.py",

    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",

    # Project-level files
    "app.py",                # main app entry file (optional for deployment)
    "requirements.txt",      # project dependencies
    "Dockerfile",            # Docker container config
    ".dockerignore",         # ignore rules for docker context
    "demo.py",               # optional demo/testing script
    "setup.py",              # for packaging
    "pyproject.toml",        # modern Python packaging support
    "config/model.yaml",     # model config (e.g., hyperparams)
    "config/schema.yaml",    # schema or validation rules for data
]

# Iterate through each path in the list
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert string to Path object
    filedir, filename = os.path.split(filepath)  # Separate directory and file name

    # If there's a directory in the path, create it (including parent directories if needed)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Don't raise an error if directory already exists

    # If the file does not exist or is empty, create it
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Empty file for now – to be filled in later
    else:
        # Optional: Print info if file already exists and is not empty
        print(f"file is already present at: {filepath}")
