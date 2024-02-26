# LREC-Coling2024
This repository contains the training and testing files of the paper 'At the Crossroad of Cuneiform and NLP: Challenges for Fine-grained Part-of-speech Tagging' from the LREC-Coling conference in Turin May 2024. In order to refer to content from this repository, please cite the paper as attested here: DOI...
## Data
### Datasets
We provide three datasets that with some manipulation can be used to reproduce our results. They contain the transliterations, i.e. the textual data represented by latin letters, or Unicode cuneiform signs, i.e. a Unicode rendering of the textual data, in the first part of each data line and tab-separated are the Part-of-Speech (PoS) and morphological (Morph) information (for further explanation see paper §3.5, §5.1 and §5.3).
+ transliteration_PoS+Morph.txt
+ transliteration_PoS.txt
+ unicode_data_set.txt

### Prepatation
#### Separation
In order to faciliate proper data separation we have implemented two tags in between lines of text. Those are <EoL> and <EoT>, *end of line* and *end of text* respectively. You can split the data on one or the other to make line or text separated data files. The verb separated can be done by looking for the Part-of-Speech tag 'V', but the fine-grained verb separation cannot currently be executed because that data plays an important role in future results.
#### Division of data
You have to have made a choice on *Separation* before this step. This would mean that the data to this point should consist of lines with textual and grammatical information, where each part is separated by an empty line, as decided above (see also paper §5.2). For the next steps see 'fold_maker.py'. We chose to randomize the order of the data input based on the separation. From this we split the data in five-folds of 80/20% training/test data. Meaning we trained a FLAIR model under the same parameters 5 times, each with a different split of training and testing data. From the 100% of randomized data, fold one used the first 80% for training and the rest for testing, the second used the first 60 and last 20% for training and the range 60-80% for testing. The pattern was repeated for the last three folds.

## Training
As explained in the paper we used the FLAIR toolkit (Version 0.12.2) to train our model, see the 'train_flair.py'. We iterated the training over the folds.

## Rights
This repository is authored by Gustav Ryberg Smidt, Katrien De Graef and Els Lefever. Everything in the repository is under Creative Commons licenses (CC-BY-NC-4.0).
