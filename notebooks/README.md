# SRNN PFC Notebooks

| Notebook                    | Colab Link |
|-----------------------------| -----------|
| 00_nengo_test               | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/00_nengo_test.ipynb)|
| 01_srnn_go_nogo             | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/01_srnn_go_nogo.ipynb)|
| 02_srnn_ctx_integrator      | TODO |
| 03_simplest_srnn_dms        | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/03_simplest_rnn_dms.ipynb)|
| 04_lmu_dms        | [Link](https://colab.research.google.com/github/neuromorphs/grill-srnn-pfc/blob/master/notebooks/04_lmu_dms.ipynb)|

## Usage Hints

### Running in Colab

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

### Generating Library from Notebooks

Some of these notebooks use [nbdev](https://nbdev.fast.ai/). This means that code defined in notebook cells can be exported directly to the srnn_pfc library. The cell should have `%nbdev_export` as its first line. Then, either call `nbdev_build_lib` from the command line or call `from nbdev import *; notebook2script()` in a notebook. Exports can be further organized using `#default_exp module_name` at the top of a notebook ([more info](https://nbdev.fast.ai/export.html)).

For these libraries to be useful immediately after calling `nbdev_build_lib`, the srfnn_pfc package should have been installed in developer mode with `pip install -e .` from within the grill-srnn-pfc folder.

### Running the NNI tests

From outside the grill-srnn-pfc directory, so as not to confuse python's import statements:
> `nnictl create --config grill-srnn-pfc\srnn_pfc\tune\lmu_dms_nni_cfg.yml`