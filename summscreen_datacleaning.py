import os
import jsonlines
import json
from nltk.tokenize.treebank import TreebankWordDetokenizer
from tqdm import tqdm

dirs = ['ForeverDreaming', 'TVMegaSite']
for dirname in dirs:
    directory_path = f'summscreen/tokenized/{dirname}'
    out_path = f'summscreen/untokenized/{dirname}'

    file_names = os.listdir(directory_path)

    for fn in file_names:
        if "anonymize" in fn:
            newlines = []
            with open(os.path.join(out_path, fn), 'r') as json_file:
                for json_obj in tqdm(jsonlines.Reader(json_file), ncols=70):
                    json_obj['Recap'] = [x.replace(' . ', '. ') for x in json_obj['Recap']]
                    json_obj['Transcript'] = [x.replace(' . ', '. ') for x in json_obj['Transcript']]
                    newlines.append(json_obj)

            with open(os.path.join(out_path, fn), 'w') as json_file:
                writer = jsonlines.Writer(json_file)
                for dict_obj in newlines:
                    writer.write(dict_obj)

