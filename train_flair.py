from collections import defaultdict
import os
from sklearn.model_selection import train_test_split
from flair.data import Corpus
from flair.datasets import ColumnCorpus
from flair.embeddings import StackedEmbeddings, FlairEmbeddings
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from tqdm import tqdm


# IMPORTANT: COMMENT OUT THE TRAINING PROCESSES YOU DON'T NEED!
# If you don't do that, this will take a long time.

# Define where the training data folders are located
folder_location = os.path.dirname(__file__)
fold_prefix = 'fold0'
folds = [0,1,2,3,4]



# Chose language pre-trained embeddings
languages = ['ar','multi','es','ja'] # Limit to fit training needs
# Chose training data sentence seperator types
seperator = ['sep_EoL','sep_EoT','sep_V'] # Limit to fit training needs
# Chose the type of input data and labels
data_sets = ['transliteration_PoS','transliteration_PoS+Morph','unicode_transliteration_PoS'] # Limit to fit training needs

# Iterate through the pre-trained language embeddings model necessary
for lang in languages:
    # Initialize the pre-trained embeddings model
    # This is also where you can play around with other types of embeddings models than the FLAIR embeddings
    embedding = StackedEmbeddings(
    [
    FlairEmbeddings(f'{lang}-forward'),
    FlairEmbeddings(f'{lang}-backward'),
    ]
        )
    # The following loops will train all the models given seperator and data_sets with the lang pre-trained embeddings
    for sep in tqdm(seperator):
        for data_input in tqdm(data_sets):
            for fold in tqdm(folds):

                # Define parameters necessary for the training    
                dictionary = []
                tag_dict = defaultdict(int)
                tag_type = 'pos'
                columns = {0: 'text', 1: 'pos'}

                # The data_folder is where the data of the current training is found
                data_folder = f'{folder_location}/{sep}/{data_input}_{fold_prefix}{fold}'

                # We here define the training and testing files
                corpus: Corpus = ColumnCorpus(data_folder, columns,
                                              train_file='train.txt',
                                              test_file='test.txt')

                # Define the sequence tagger parameters
                tagger = SequenceTagger(hidden_size=256,
                                        embeddings=embedding,
                                        tag_dictionary=corpus.make_tag_dictionary('pos'),
                                        tag_type='pos',
                                        use_crf=True,
                                        )

                # Initiate the sequence tagger parameters and the corpus
                trainer = ModelTrainer(tagger, corpus)

                # Train the sequence tagger
                trainer.train(f'{folder_location}/{sep}/{data_input}_{fold_prefix}{fold}/{lang}/model', learning_rate=0.1, 
                    mini_batch_size=8, 
                    anneal_factor=0.5, 
                    patience=5, 
                    max_epochs=100,
                    )