# An up-to-date `uv` Cookiecutter template for MLOps

Adapted from Nicki Skafte's [mlops_template](https://github.com/SkafteNicki/mlops_template), which
was in turn inspired by the popular
[cookiecutter-data-science](https://cookiecutter-data-science.drivendata.org/v1/) template.
This template is more opinionated than the latter regarding tools used. It has been updated to better fit machine learning-based
projects and is being used as the core template in the [DTU MLOps course](https://github.com/SkafteNicki/dtu_mlops).

## Requirements to use the template

You need the following to use this template:

-   `uv` and `uvx`, which can be installed with homebrew:

    ```bash
    brew install uv
    ```

-   Python 3.11 or higher
-   [Cookiecutter](https://github.com/cookiecutter/cookiecutter) version 2.4.0 or higher, which can be installed globally with `uvx`:

    ```bash
    uvx cookiecutter
    ```

-   Ruff VSCode extension (used in `.vscode/settings.json` for linting and formatting

## Start a new project

Start by creating a new repository on GitHub (`https://github.com/<username>/<repo_name>`).
Do **not** initialize the repository with a README, .gitignore or license. This will create conflicts later on.

### Option A

If you've already cloned this repository to your local machine, you must make sure the project is created in the
_current_ directory and not as a _subdirectory_.

To create the project in the current directory (and not as a directory inside of the current directory), like for example the cloned repository on your local machine, run

```bash
uvx cookiecutter https://github.com/schependom/DTU_ml-ops-template --output-dir ./ --overwrite-if-exists
```

### Option B

If you've **not** yet cloned this repository to your local machine, navigate
to the directory which houses all of your git repositories (e.g. `~/code` or `~/projects`) and run

```bash
uvx cookiecutter https://github.com/schependom/DTU_ml-ops-template
```

Follow the prompts to set up your new project. This will create a new directory with the name of your repository.
Afterwards, set this directory as the remote origin of your GitHub repository and push the initial commit:

```bash
# from the parent directory of the created repo (e.g. ~/projects)
cd <repo_name>
git init
git add .
git commit -m "init cookiecutter project"
git remote add origin https://github.com/<username>/<repo_name> # the repo created on GitHub
git push origin master
```

### Filling out the prompts

You will be prompted with the following questions in both Option A and Option B:

```txt
    [1/7] repo_name (repo_name):
    [2/7] project_name (project_name):
    [3/7] Select project_structure
        1 - advanced
        2 - simple
        Choose from [1/2] (1):
    [4/7] author_name (Your name (or your organization/company/team)):
    [5/7] description (A short description of the project.):
    [6/7] python_version (3.12):
    [7/7] Select open_source_license
        1 - No license file
        2 - MIT
        3 - BSD-3-Clause
        Choose from [1/2/3] (1):
```

A couple of notes regarding the different options:

1. When asked for the `repo_name` e.g. the repository name, this should be the same as when you created the Github
   repository in the beginning.

2. When asked for the `project_name` this should be a
   [valid Python package name](https://peps.python.org/pep-0008/#package-and-module-names). This means that the name
   should be all lowercase and only contain letters, numbers and underscores. The project name will be used as the name
   of the Python package. This will automatically be validated by the template.

3. When asked for the `project_structure` you can choose between `advanced` and `simple`. The `advanced` structure
   contains everything in the `simple` structure but also includes starting `dockerfiles`, `docs`, `github actions`,
   `dependabot` and more.

## Repository structure

Assuming you choose the `advanced` structure, the repository will look like
something like this:

```txt
├── configs
│   └── .gitkeep
├── .devcontainer
│   ├── devcontainer.json
│   └── postCreateCommand.sh
├── dockerfiles
│   ├── api.dockerfile
│   └── train.dockerfile
├── docs
│   ├── mkdocs.yaml
│   ├── README.md
│   └── source
│       └── index.md
├── .github
│   ├── dependabot.yaml
│   └── workflows
│       ├── linting.yaml
│       ├── pre-commit-update.yaml
│       └── tests.yaml
├── .gitignore
├── LICENSE
├── models
│   └── .gitkeep
├── notebooks
│   └── .gitkeep
├── .pre-commit-config.yaml
├── pyproject.toml
├── .python-version
├── README.md
├── reports
│   ├── figures
│   │   └── .gitkeep
│   └── .gitkeep
├── src
│   └── project_name
│       ├── api.py
│       ├── data.py
│       ├── evaluate.py
│       ├── __init__.py
│       ├── model.py
│       ├── train.py
│       └── visualize.py
├── tasks.py
├── tests
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_data.py
│   └── test_model.py
└── uv.lock
```

In particular lets explain the structure of the `src` folder as that is arguably the most important part of the
repository. The `src` folder is where the main code of the project is stored. The template divides the code into five
files, shown in the diagram below with their respective connections:

<img src="diagram.drawio.png" alt="diagram" width="1000"/>

-   `data.py`: this file is responsible for everything related to the data. This includes loading, cleaning, and splitting
    the data. If the data needs to be pre-processed then running this file should process raw data in the `data/raw`
    folder and save the processed data in the `data/processed` folder.
-   `model.py`: this file contains one or model definitions.
-   `train.py`: this file is responsible for training the model. It should import the training/validation data interface
    from `data.py` and the model definition from `model.py`.
-   `evaluate.py`: this file is responsible for evaluating the model. It should import the test data interface from
    `data.py` and load the trained model from the `models` folder. Output should be performance metrics of the trained
    model.
-   `api.py`: this file is responsible for serving the model. It should import the trained model from the `models` folder
    and provide an interface for making predictions.
-   `visualize.py`: this file is responsible for visualizing the data and model. It should import the training/validation/
    test data interface from `data.py` and the trained model from the `models` folder. Output should be visualizations
    of the data and model.

At some point one or more of the files may have grown too large and complicated. At this point it is recommended to
split the file into multiple files and move into a folder of the same name. As an example consider the `model.py`
containing many models. In this case it would be a good idea to refactor into

```txt
src/
└── project_name/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   ├── model1.py
    │   └── model2.py
    ├── ...
```

## The stack

Note that some of these tools need to be added to the dependencies in `pyproject.toml` by running `uvx add <package>`.
In case it is only used during development, add the `--dev` flag, or equivalently use `uvx add --group dev <package>`.

🐍 Python projects using `pyproject.toml`

🔥 Models in [Pytorch](https://pytorch.org/)

📦 Containerized using [Docker](https://www.docker.com/)

📄 Documentation with [Material Mkdocs](https://squidfunk.github.io/mkdocs-material/)

👕 Linting and formatting with [ruff](https://docs.astral.sh/ruff/)

🧐 Type checking with [ty](https://docs.astral.sh/ty/)

✅ Checking using [pre-commit](https://pre-commit.com/)

🛠️ CI with [GitHub Actions](https://github.com/features/actions)

🤖 Automated dependency updates with [Dependabot](https://github.com/dependabot)

📝 Project tasks using [Invoke](https://www.pyinvoke.org/)

and probably more that I have forgotten...
