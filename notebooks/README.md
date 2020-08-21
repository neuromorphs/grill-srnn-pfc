# SRNN PFC Notebooks

| Notebook                    | Colab Link |
|-----------------------------| -----------|
| 00_nengo_test               | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/00_nengo_test.ipynb)|
| 01_simplest_srnn            | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/01_simplest_rnn.ipynb)|

## Usage Hints

To equalize the experience across Google Colab / local environments, each notebook should have a block to check if is running in Colab and if yes then install Nengo and this repository's package. We also include the autoreload magic code in here too. This will look something like the following:
```jupyterpython
#@title Environment Setup
try:
    # See if we are running on google.colab
    from google.colab import files
    IN_COLAB = True
    !pip install --upgrade nengo nengo-gui nbdev git+https://github.com/neuromorphs/grill-srnn-pfc.git
    !jupyter serverextension enable nengo_gui.jupyter
    # TODO: kaggle creds for downloading data 
    
except ModuleNotFoundError:
    IN_COLAB = False

%load_ext autoreload
%autoreload 2
```