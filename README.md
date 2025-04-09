Leading_Food_Delivery_Time_Prediction
==============================

Build Ml-Project for predicting the delivery time of order

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

 conda create --name fiid_delivery_env_3_11 python=3.11
 source activate fiid_delivery_env_3_11 



Steps for dvc setup:

1.dvc init

It creates a .dvc/ folder, which contains DVC’s internal config and state files.

.dvc/config:
This is the configuration file for DVC. It stores default settings such as:
[core]
    remote = storage
You can configure remotes, cache location, and more here.

.dvc/.gitignore:
This file ensures Git ignores DVC's internal files that shouldn’t be committed (like cache or temp data).
It usually contains:
/cache/
===============================================
⚠️ Why are .dvc/ files being tracked by Git?
Even though DVC manages large data files separately, some DVC files are meant to be committed, especially:

.dvc/config → tracks DVC settings (required)

.dvc/.gitignore → tells Git to ignore large file caches

.dvcignore → tells DVC what to ignore (like temp files)

These files are text metadata and help others reproduce your DVC setup — that's why Git tracks them.

✅ They are supposed to be committed to Git. Only bulky files (like datasets, model binaries) are stored outside Git.


For tracking the data by dvc:
=============================
First remove the /data/ from git ignore - allow git to track .
we wil track data by dvc and will allow git to use the metadata to track:
dvc add data/raw/swiggy.csv
it will create two file inside the raw .gitignore and swiggy.csv.dvc - whom dvc will track


dvc.yaml - we will write steps for our pipeline

params.yaml - we will define the parameters

dvc dag --it will make the dag through dvc.yaml file - to see our flow we can see

dvc repro


=======

dvc init
git add .dvc .gitignore
git commit -m "Initialize DVC"

#setup local remote for dvc
mkdir -p dvc_storage
dvc remote add -d local_remote ./dvc_storage