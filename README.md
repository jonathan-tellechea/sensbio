# About Sensbio

Sensbio is a set of simple CLIs and Jupyter-Notebooks that allow users to identify possible transcription factors (TFs) inducible by small chemical compounds. A web-based application in development is available at [Sensbio-app](https://github.com/jonathan-tellechea/sensbio_app)

# Installation

For the main algorithms (sequence.py and molecular.py) to work, the installation of dependencies can be done through Anaconda environment manager.
1. Clone this repository in your computer.
2. Execute: `conda env create -f environment.yml`
3. Activate the sensbio environment: `conda activate sensbio`

If the user wants to use the tools through the supplied notebooks, it is necessary the installation of the required dependencies separately. For instance, through the following command:
- `conda install -c conda-forge jupyterlab`

# Usage
## Molecular tools.

Two tools are available to identify possible TFs triggered by your input molecule (in SMILES format):

- **molecular.ipynb** 
    1. Simply change the **input_molecule** variable with your desired target SMILES and run the whole notebook.
- **molecular.py**
    1. Run the script by calling it together with your target molecule withing quotation marks as argument:
    2. `python molecular.py 'YOUR SMILES'`

## Protein sequence tools.

Similarly, two tools are available to find TFs in the database similar to your input protein sequence.

- **sequence.ipynb** 
    1. Simply change the **sequence** variable with your query amino-acid sequence.
- **sequence.py**
    1. Run the script by calling it together with your query protein sequence within quotation marks as argument:
    2. `python sequence.py 'YOUR SEQUENCE'`

# License

This project is licensed under the terms of the MIT license.
