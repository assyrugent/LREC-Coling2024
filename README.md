# LREC-Coling2024
This repository contains the training and testing files of the paper 'At the Crossroad of Cuneiform and NLP: Challenges for Fine-grained Part-of-speech Tagging' from the LREC-Coling conference in Turin May 2024.
## Data
### Datasets
We provide three datasets that with some manipulation can be used to reproduce our results. They contain the transliterations, i.e. the textual data represented by latin letters, or Unicode cuneiform signs, i.e. a Unicode rendering of the textual data, in the first part of each data line and tab-separated are the Part-of-Speech (PoS) and morphological (Morph) information (for further explanation see paper §3.5, §5.1 and §5.3).
+ transliteration_PoS+Morph.txt
+ transliteration_PoS.txt
+ unicode_data_set.txt
In order to faciliate proper line separation of the data as experimented in the paper §5.2, we have implemented two tags in between lines of text. Those are <EoL> and <EoT>, *end of line* and *end of text* respectively. You can split the data on one or the other to make line or text separated data files. The verb separated can be done by looking for the Part-of-Speech tag 'V', but the fine-grained verb separation cannot currently be executed because that data plays an important role in future results.
