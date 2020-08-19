# SRNN PFC Notebooks

| Notebook                    | Colab Link |
|-----------------------------| -----------|
| 00_nengo_test               | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/00_nengo_test.ipynb)|
| 01_simplest_srnn            | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/01_simplest_rnn.ipynb)|

## Usage Hints

To make things easier for the development process, each notebook should have the `autoreload` magic code near the top:
```jupyterpython
%load_ext autoreload
%autoreload 2
```

To equalize the experience across Google Colab / local environments, each notebook should have a block to check if is running in Colab and if yes then install Nengo and this repository's package. You can probably lump the autoreload code in here too. This will look something like the following:
```jupyterpython
#@title Environment Setup
try:
    # See if we are running on google.colab
    from google.colab import files
    IN_COLAB = True
    !pip install nengo git+https://github.com/neuromorphs/grill-srnn-pfc.git 
    # TODO: kaggle creds for downloading data 
    
except ModuleNotFoundError:
    IN_COLAB = False

%load_ext autoreload
%autoreload 2
```