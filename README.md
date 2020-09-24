# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._


#### [Project homepage](https://github.com/akail/cookiecutter-data-science/)


### Requirements to use the cookiecutter template:
-----------
 - Python 3.5+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter

or using pipx

pipx install cookiecutter
```


### To start a new project, run:
------------

    PYTHONPATH=<this directory> ccds https://github.com/akail/cookiecutter-data-science


[![asciicast](https://asciinema.org/a/244658.svg)](https://asciinema.org/a/244658)


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── .gitignore         <- Avoids uploading data, credentials, outputs, system files, etc
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│   │                     the creator's initials, and a short `-` delimited description, e.g.
│   │                     `1.0-jqp-initial-data-exploration`.
│   │
│   ├── README.md      <- README with specific information related to using notebooks
│   ├── eda            <- Exploratory Data Analysis.  For short term usage
│   ├── poc            <- Proof of concept
│   ├── modeling       <- Model building and training
│   └── evaluation     <- How good is the model
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── test_requirements.txt <- The requirements file for automated test running
│
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
│
├── scripts            <- Reusable but independent python and bash scripts
│
├── {{ cookiecutter.module_name }}                <- Source code for use in this project.
│   ├── __init__.py    <- Makes {{ cookiecutter.module_name }} a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── tests              <- Unit and functional tests using pytest
│
└── tox.ini            <- tox file with settings for running tox; see tox.testrun.org
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing development requirements
------------

    pip install -r requirements.txt

### Running the tests
------------

    pytest tests
