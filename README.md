# Model-eos6oli: Soltrannet-Aqueous-Solubility-Model

## Overview:
This repository houses all codes and datasets employed in the tasks of checking for bias, validating and reproducing the aqueous solubility model, eso6oli, which is a regression model that predicts the Log of solubility(LogS). 

## Abstract:
- Ersilia eso6oli is the SolTransNet model of SolTranNet−A Machine Learning Tool for Fast Aqueous Solubility Prediction [paper](https://pubmed.ncbi.nlm.nih.gov/34038123/) by Francoeur et al.
- SolTranNet is a molecule attention transformer, MAT, that predicts aqueous solubility from a molecule's SMILES representation. It is a Regression model, that predicts LogS (log of the solubility) in order to help filter out insoluble compounds! The fine tuning of this mode is done with pertained model MAT, which applies self attention to a molecular graph representation of the molecule.
  

## Model Information:
- Eos Model ID: eos6oli
- Slug: soltrannet-aqueous-solubility
- Task: regression
- Input: Compound(canonicalsmiles)
- Output: Experimental value
- Interpretation: Predicted LogS (log of the solubility)

## Installation
- To deploy Ersilia to Google Colab; fetch, serve, and run predictions with a model, follow the steps listed [here](https://github.com/ersilia-os/ersilia/blob/master/notebooks/ersilia-on-colab.ipynb]).
- To install SolTranNet on Google Colab, test, and run predictions with it, follow the steps listed [here](https://github.com/gnina/SolTranNet/blob/main/README.md)

## Structural organisation:
This repository is organised by folders:
- **data**: Contains the raw data, processed data and Model predictions.
- **figures**: Contains a collection of visualizations presented in PNG format..
- **Notebooks**: Houses the jupyter notebook files where most of the developmen took place.
- **src**: Contains important functions I will re-use throughout the repository, to avoid typing them each time.


## Steps to Reproduce The Solutions to These Tasks:
### Task 1 (Model's(eos6oli) Bias Evaluation):
- From the list of the models provided in the [Ersilia Book](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024), I selected tthe model of my choice which is [Aqueous Solubility Model](https://github.com/ersilia-os/eos6oli), especially because the model's publication, aim, and methodology resonated with me.
- I then went on to create a repository that contained all the files and datasets needed for the project.
- For my task 1, I downloaded the [dataset](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/solubility-dataset.csv) from the public repository of [Harvard Dataverse](https://dataverse.harvard.edu/). With this [dataset](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/solubility-dataset.csv), I was able, through random sampling, to generate the [1000 molecules](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules.csv) after proper data cleaning and preprocessing steps.
- I then went on to deploy Ersilia Model Hub to Google Colab, fetched and served the model, eso6oli. After serving the model, I ran prediction on the model [1000 molecules](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules.csv) using the model to generate these [Predictions](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules_predictions.csv).
- With the [Predictions](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules_predictions.csv), I was able to look into the model bias through the insights gathered from these [visualisations](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/tree/main/figures/Task(1)%20figures).
- The notebook containing the solution to task 1 can be found [here](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/Notebooks/Week2_Task1.ipynb).

### Task 2(Model's Reproducibilty):
- I installed, and tested the functionality of SolTranNet on Google Colab.
- After confirming that the model was working properely, I went on to run prediction on the [1000 molecules](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules.csv) and thereafter, saved the [predictions](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/Soltranet_pred.csv).
- I went on to evaluate the [predictions](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/Soltranet_pred.csv); employing these [visualisations](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/tree/main/figures/Task(2)%20figures/Model%20Bias%20vis) to gather insights from the model's performance and suprisingly to me, it corresponded with what I got earlier when eos6oli from the Ersilia Model Hub acted on the same dataset, thus, confirming the reproducibility of the model, eos6oli.
- To further confirm this reproducibility, I compared directly the predictions from both SolTranNet and eos6oli from the Ersilia Model Hub by merging the both predictions into a single DataFrame. With the use of [scatter plot](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/figures/Task(2)%20figures/reproducibility%20viz/repro_scatter_plot.png), it was confirmed that the values from both predictions were identical, thus, solidifying the fact that the model(eos6oli) is reproducible.
- I equally captured the performance of both models in this [tabel](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/figures/Task(2)%20figures/Performance%20metrics%20viz/performance%20metrics.png) and all the metrics were the same as well. With this, it was confirmed that the model was indeed reproducible.
- The Notebook containing the detailed solutions to task 2 can be found [here](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/Notebooks/Week2_Task2.ipynb)

### Week 3(Model Validation With External Dataset):
- To validate the model's ability to generalise well, I employed a strange and a new dataset which was gotten from [SolTranNet's GitHub Repo](https://github.com/francoep/SolTranNet_paper/blob/main/README.md).
- I installed SolTranNet on Google Colab, then fetched and tested it before going ahead to run prediction on the [data](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/llinas2020/llinas2020_set1_test.csv).
- I evaluated the model's performance on the predictions with different [visualisations](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/tree/main/figures/Task(3)%20figures/Soltranet_figures) and [performance metrics](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/figures/Task(3)%20figures/Soltranet_figures/Soltranet's%20Validation%20Performance%20Metrics.png).
- I then went on to reproduce these results on Ersilia-eos6oli. Both the [visualisations](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/tree/main/figures/Task(3)%20figures/eos6oli_figures) and [performance metrics](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/figures/Task(3)%20figures/eos6oli_figures/eos6oli%20performance%20metrics.png) were exactly the same with what I got from SolTranNet.
- The Notebook with the detailed solution to this task can be found [here](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Tasks/blob/main/Notebooks/Week3_Task.ipynb).

## References:
- [SolTranNet's Publication](https://pubs.acs.org/doi/10.1021/acs.jcim.1c00331)
- [SolTranNet's GitHub Repo For Datasets](https://github.com/gnina/SolTranNet)
- [Ersilia Google Colab Guide](https://github.com/ersilia-os/ersilia/blob/master/notebooks/ersilia-on-colab.ipynb)
- [Harvard Dataverse](https://dataverse.harvard.edu/)




  
