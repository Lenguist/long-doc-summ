# Long Document Summarization

This is a research project in long document summatization conducted in summer 2023

commands to run to get summaries:

used to collect an exhaustive set of summaries from that source.

cd booksum-main/scripts/data_collection/shmoop/
python get_summaries.py

cd ..
cd bookwolf
python get_summaries.py

cd ..
cd gradesaver
python get_summaries.py

NOW HERE
cd..
cd novelguide
python get_summaries.py

cd ..
cd pinkmonkey
python get_summaries.py

NOT DONE
cd..
cd shmoop
python get_summaries.py

NOT DONE
cd ..
cd sparknotes
python get_summaries.py

cd ..
cd thebestnotes
python get_summaries.py


python gather_data.py --matched_file chapter_summary_aligned_train_split.jsonl --split_paragraphs
python gather_data.py --matched_file chapter_summary_aligned_valid_split.jsonl --split_paragraphs
python gather_data.py --matched_file chapter_summary_aligned_test_split.jsonl --split_paragraphs

python gather_data.py --matched_file ../chapter-level-summary-alignments/chapter_summary_aligned_train_split.jsonl --split_paragraphs
python gather_data.py --matched_file ../chapter-level-summary-alignments/chapter_summary_aligned_test_split.jsonl --split_paragraphs
python gather_data.py --matched_file ../chapter-level-summary-alignments/chapter_summary_aligned_val_split.jsonl --split_paragraphs

cd ../../all_chapterized_books/27681-chapters