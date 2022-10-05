# About Sensbio

Sensbio is a set of simple CLIs and Jupyter-Notebooks that allow users to identify possible transcription factors (TFs) inducible by small chemical compounds. A web-based application in development is available at [Sensbio-app](https://github.com/jonathan-tellechea/sensbio_app)

# Installation

For the main algorithms (sequence.py and molecular.py) to work, the installation of dependencies can be done through Anaconda environment manager.
1. Clone this repository in your computer.
2. Execute: `conda env create -f environment.yml`
3. Activate the sensbio environment: `conda activate sensbio`

# Usage
## Molecular tools.

Two tools are available to identify possible TFs triggered by your input molecule (in SMILES format):

- **molecular.ipynb** 
    - Simply change the **input_molecule** variable with your desired target SMILES and run the whole notebook.
- **molecular.py**
    - Run the script by calling it together with your target molecule withing quotation marks as argument:
    - `python molecular.py 'YOUR SMILES'`

## Protein sequence tools.

Similarly, two tools are available to find TFs in the database similar to your input protein sequence.

- **sequence.ipynb** 
    - Simply change the **sequence** variable with your query amino-acid sequence.
- **sequence.py**
    - Run the script by calling it together with your query protein sequence within quotation marks as argument:
    - `python sequence.py 'YOUR SEQUENCE'`

# License

This project is licensed under the terms of the MIT license.
