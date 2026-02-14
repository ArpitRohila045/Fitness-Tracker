**Fitness-Tracker**

**Description:**
- Project for processing MetaMotion accelerometer and gyroscope CSV exports, exploring the signals, building features, and (eventually) training models to classify or analyze barbell exercise sets and count repetitions.

**Quick Overview:**
- Raw sensor CSVs are stored under [data/raw/MetaMotion](data/raw/MetaMotion). A preprocessing step resamples and combines accelerometer + gyroscope signals into an interim pickle under [data/interim](data/interim).
- Visualization notebooks and scripts live in [notebooks](notebooks) and [src/visualization](src/visualization).
- Feature engineering and modeling code is in [src/features](src/features) and [src/models](src/models). Some modules are scaffolds/empty and need implementation.

**Table of Contents**
- **Description**: this file
- **Setup**: install dependencies and create environment
- **Data**: where raw/interim/processed data live
- **Usage**: basic commands to run preprocessing, visualization, and notebooks
- **Project structure**: brief map of key files
- **Known issues & notes**: gotchas observed while inspecting the code

**Setup**

1) Recommended (Conda): create the provided environment:

```bash
conda env create -f environment.yml
conda activate tracking-barbell-exercises
```

2) Or using pip in a virtualenv:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

**Data**
- Place original CSV exports (.csv) under [data/raw/MetaMotion](data/raw/MetaMotion).
- The preprocessing script used in this repo creates a resampled pickle at [data/interim/01_data_processed.pkl](data/interim/01_data_processed.pkl).
- Processed datasets and model artifacts (not yet implemented) should go under [data/processed](data/processed) and [models](models).

**Usage — quick commands**

- Run the simple preprocessing/merge script (this script reads raw CSVs and writes a resampled pickle):

```bash
python src/visualization/visualize.py
```

- Start the Jupyter notebooks for exploration:

```bash
jupyter notebook notebooks/understandingData.ipynb
jupyter notebook notebooks/visulization.ipynb
```

- Feature-building and training scripts are placeholders and require implementation. See the Project structure below for locations.

**Project structure (key files)**
- [data/raw/MetaMotion](data/raw/MetaMotion): raw CSV exports from MetaMotion devices.
- [data/interim](data/interim): intermediate files (resampled pickle output).
- [src/visualization/visualize.py](src/visualization/visualize.py): small script that reads CSVs and produces a resampled pickle for analysis.
- [src/features/build_features.py](src/features/build_features.py): intended for feature engineering (currently empty).
- [src/data/make_dataset.py](src/data/make_dataset.py): (if present) dataset creation and resampling logic — inspect and merge with pipeline.
- [src/models/train_model.py](src/models/train_model.py): training script (currently empty).
- [src/models/predict_model.py](src/models/predict_model.py): prediction/inference script (currently empty).
- [notebooks](notebooks): exploratory analysis and visualization notebooks.

**Notes & Known Issues (observed during analysis)**
- `src/visualization/visualize.py` and other scripts contain hard-coded paths pointing at `c:\Users\hp\Desktop\Fitness-Tracker\...` — consider switching to relative paths or a configuration file for portability.
- The preprocessing pipeline in `src/visualization/visualize.py` writes to `../data/interme/01_data_processed.pkl` (note the directory name `interme` — this looks like a typo; expected `interim`). Verify and fix the output path in code to `data/interim` before running.
- Several important modules are scaffolds (empty): `src/features/build_features.py`, `src/models/train_model.py`, `src/models/predict_model.py`. They need implementation to complete the pipeline.

**How you can proceed (suggested next steps)**
1. Fix the hard-coded paths and the `interme` → `interim` typo in scripts.
2. Implement feature extraction in [src/features/build_features.py](src/features/build_features.py).
3. Implement model training in [src/models/train_model.py](src/models/train_model.py) and add a simple example (e.g., a small classifier using scikit-learn).
4. Add unit tests or small example scripts demonstrating end-to-end flow (raw CSV → interim pickle → features → train → predict).

**Contributing**
- Open an issue or PR for bugs, path fixes, and new features.

**License & Author**
- Author: Arpit Rohila (see `setup.py`)
