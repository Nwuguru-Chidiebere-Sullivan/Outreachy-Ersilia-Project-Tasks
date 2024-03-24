# Model-eos6oli: Soltrannet-Aqueous-Solubility-Model

## Overview:
This repository houses all codes and datasets employed in the tasks of checking for bias, validating and reproducing the aqueous solubility model, eso6oli, which is a regression model that predicts the Log of solubility(LogS). 

## Model Information:
- Eos Model ID: eos6oli
- Slug: soltrannet-aqueous-solubility
- Task: regression
- Input: Compound(canonicalsmiles)
- Output: Experimental value
- Interpretation: Predicted LogS (log of the solubility)

## Steps to Reproduce The Solutions to These Tasks:
### Task 1:
- From the list of the models provided in the [Ersilia Book](https://ersilia.gitbook.io/ersilia-book/contributors/internships/outreachy-summer-2024), I selected tthe model of my choice which is [Aqueous Solubility Model](https://github.com/ersilia-os/eos6oli), especially because the model's publication, aim, and methodology resonated with me.
- I then went on to create a repository that contained all the files and datasets needed for the project.
- For my task 1, I downloaded the [dataset](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/solubility-dataset.csv) from the public repository of [Harvard Dataverse](https://dataverse.harvard.edu/). With this [dataset](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/solubility-dataset.csv), I was able, through random sampling, to generate the [1000 molecules](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules.csv) after proper data cleaning and preprocessing steps.
- I then went on to deploy Ersilia Model Hub to Google Colab, fetched and served the model, eso6oli. After serving the model, I ran prediction on the model [1000 molecules](https://github.com/Nwuguru-Chidiebere-Sullivan/Outreachy-Ersilia-Project-Week2-Tasks/blob/main/data/1000_molecules.csv) using the model to generate [Predictions]()
  
