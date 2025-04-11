import os
from pathlib import Path

package_name = "StudentPerformance"

list_of_files = [
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/model_evaluation/__init__.py",
    f"src/{package_name}/split/__init__.py",
    f"src/{package_name}/split/spliting.py",
    f"src/{package_name}/train_test/__init__.py",
    f"src/{package_name}/train_test/train_model.py",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filename} already exists.")