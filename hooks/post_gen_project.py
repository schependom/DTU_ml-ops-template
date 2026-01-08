from keyword import iskeyword
from operator import ge, le
import shutil
from pathlib import Path

try:
    from loguru import logger
except ImportError:
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)

project_name = "{{cookiecutter.project_name}}"
python_version = "{{cookiecutter.python_version}}"
project_structure = "{{cookiecutter.project_structure}}"

logger.info(f"Project name: {project_name}")
logger.info(f"Python version: {python_version}")
logger.info(f"Project structure: {project_structure}")

if not project_name.isidentifier() or not project_name.islower():
    raise ValueError(
        "\n"
        "Project name must be a valid project name, meaning that it must be a valid Python name and also be lowercase."
        " This means that it must not contain spaces or special characters, and must not start with a number."
        " In general it is best to use only lowercase letters and underscores."
        " You can read more about Python naming conventions for packages here:"
        " https://peps.python.org/pep-0008/#package-and-module-names"
        "\n",
    )
if iskeyword(project_name):
    raise ValueError(
        "Project name must not be a built-in keyword, as it will cause syntax errors.",
    )

min_version = "3.10"
max_version = "3.13"
if not (ge(python_version, min_version) and le(python_version, max_version)):
    raise ValueError(
        f"Python version must be between {min_version} and {max_version}."
        " These are the versions that still receive support."
        " You can read more about Python versioning here: https://devguide.python.org/versions/",
    )

# Remove unnecessary files and folders for the simple template
if project_structure == "simple":
    logger.info("Removing unnecessary files and folders for the simple template.")
    folder_and_files_to_remove = [
        ".github",
        ".devcontainer",
        "dockerfiles",
        "docs",
    ]
    for f in folder_and_files_to_remove:
        if Path(f).exists():
            shutil.rmtree(f)
