# grill-srnn-pfc

A spiking recurrent neural network model to perform a stimulus match / non-match discrimination task <sup id="a-Qi-2011">[1, ](#f-Qi-2011)</sup><sup id="a-Meyer-2011">[2](#f-Meyer-2011)</sup>.
We use [Nengo](https://www.nengo.ai/) to build and parameterize our model.
Additionally, the model is constrained in various ways to better emulate real neural data recorded from monkey PFC while the monkeys performed this task <sup id="a-pfc3">[3](#f-pfc3)</sup>.

## Introduction

Some of the contributors to this project are interested in building invasive brain computer interfaces (iBCIs) that are robust to non-stationarity in neuron-sampling space across sessions and robust to non-relevant stimulus processing of naturalistic stimuli.
To build and test decoders with these properties of robustness, it is essential to have a model that can generate realistic neural data. In this project we aim to make such a model.

This work is inspired by the work of Kim, Li & Sejnowski<sup id="a-KS-2019">[ 4, ](#f-KS-2019)</sup><sup id="a-KS-2020">[5](#f-KS-2020)</sup> which also models this same task and is evaluated against these same data.

## Getting Started

### Python Environment

### Data

## Methods

### Model Description

### Constraints

### Evaluating the Model


## Footnotes and references

* <a id="f-Qi-2011" href="#a-Qi-2011"><sup>1</sup></a> [Changes in Prefrontal Neuronal Activity after Learning to Perform a Spatial Working Memory Task. Qi et al., Cerebral Cortex, 2011](https://academic.oup.com/cercor/article-abstract/21/12/2722/295413)
* <a id="f-Meyer-2011" href="#a-Meyer-2011"><sup>2</sup></a> [Stimulus selectivity in dorsal and ventral prefrontal cortex after training in working memory tasks. Meyer et al., J Neuroscience, 2011](https://www.jneurosci.org/content/31/17/6266.short)
* <a id="f-pfc3" href="#a-pfc3"><sup>3</sup></a> [Christos Constantinidis, Xue-Lian Qi, Travis Meyer (2016). Single-neuron spike train recordings from macaque prefrontal cortex during a visual working memory task before and after training. CRCNS.org. http://dx.doi.org/10.6080/K0ZW1HVD](http://dx.doi.org/10.6080/K0ZW1HVD)
* <a id="f-KS-2019" href="#a-KS-2019"><sup>4</sup></a> [Kim & Sejnowski, PNAS 2019](https://www.pnas.org/content/116/45/22811.short)
* <a id="f-KS-2020" href="#a-KS-2020"><sup>5</sup></a> [Kim & Sejnowski, bioRxiv 2020](https://www.biorxiv.org/content/10.1101/2020.02.11.944751v1.full.pdf)
* [Kim & Sejnowski code at https://github.com/rkim35/spikeRNN](https://github.com/rkim35/spikeRNN)
