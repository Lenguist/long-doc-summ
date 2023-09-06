# Long Document Summarization

This is a research project in long document summatization conducted in summer 2023

For QAFactEval:

run pip install qafacteval, fix issues as neccessary
test by running python test.py

For SNAC evaluation:

snac-main folder contains all the scripts. Snac preprocess takes in txt summary and generates tsv file, then snac_evaluate gives snac output, then snac-postprocess gets visualization from the snac output

Tasks:
- Prepare data
  - Booksum ✅ 100 books
  - SummScreen in progress
  - Real books! coming in future
- Eval
  - Automated
    - BERTScore ✅
    - R1, R2, R-L ✅
    - METEOR ✅
  - Coherence
    - Snac in progress
  - Faithfulness
    - QAFactEval
      - work on running it on compute cluster
      - swap out default question generator for gpt
  - Coverage
- Summary generation