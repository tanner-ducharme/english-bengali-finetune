## Instructions for running our code

Install the requirements from our requirements.txt

### Python version: whatever is the google colab default

### Encoder-decoder models
The encoder-decoder notebook for our best experiment is 'ift6289-project-facebook_mbart-large-50-many-to-many-mmt-BNtoEN.ipynb'.
It's best run on Google Colab as a notebook, but the file has also been uploaded as a `*.py` file.

The notebooks from our other experiments can be found in '/other notebooks/', but these have not been fully cleaned and/or commented.
More detailed instructions on running the code can be found within the notebook.

### Gemma models
The Gemma notebook for our best experiment is 'gemma7b - best experiment.ipynb'.
It's best run on google colab as a notebook, but a python file version has been made available (although you might have to tweak to get it to work with your GPU).

The notebooks from our other experiments can be found in '/other notebooks/', but these have not been fully cleaned and/or commented.
More detailed instructions on running the code can be found within the notebook.

### BLEU score
The script we used to calculate BLEU score is multi-bleu-detok.pl.
We use it as follows: perl multi-bleu-detok.pl -lc <reference_file> < <hypothesis_file>.
The -lc flag is optional

If the data is provided as a csv file in the form: Source, target, prediction, 
Then we can calculate the BLEU score by running:
./docwise <csv_file> <name_for_reference_file> <name_for_hypothesis_file>

### Visualizations
All graphs were generated using tensorboard. The tensorboard files are automatically created in the `results/exp_name/runs/` folder
