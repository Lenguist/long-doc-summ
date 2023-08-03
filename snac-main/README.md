# SNaC: Summary Narrative Coherence

This repository contains the data and models for the paper: SNAC: Coherence Error Detection for Narrative Summarization by Tanya Goyal, Junyi Jessy Li and Greg Durrett

```
@inproceedings{goyal2022snac,
  title={SNaC: Coherence Error Detection for Narrative Summarization},
  author={Goyal, Tanya and Li, Junyi Jessy and Durrett, Greg},
  booktitle={EMNLP},
  year={2022}
}
```


SNAC is a narrative coherence evaluation framework for fine-grained annotations of long summaries. It includes a taxonomy of coherence errors grounded in actual errors generated by summarization models. The SNaC taxonomy is shown below: 

<img width="1046" alt="Screen Shot 2022-11-29 at 2 10 03 AM" src="https://user-images.githubusercontent.com/22390810/204474063-2acc27ac-b5d6-4015-b705-c4ad7f0aa420.png">

We conduct human annotation to collect span-level annotations for 150 summaries across 3 model sizes (GPT3-175B, GPT3-6B, BART) and two domains (Books, movie screenplay). The resulting dataset contains 9.6K span-level error annotations. The dataset can be downloaded [here](https://drive.google.com/file/d/1ff-pV2sX9XNDMdaPxY7v22T2i0235tcE/view?usp=sharing").

You can browse through the dataset using this online tool: https://coherence-annotation-summaries.herokuapp.com/explore_dataset

## SNaC Trained Models

We train T5 models on the collected SNaC annotations to automatically detect errors in generated summaries. Given context, i.e. the generated summary uptil a certain point, the trained models predict whether the next sentence has coherence errors or not. 

We release two configurations of models:

1. T5 w/o span: Only predicts true/false to indicate if the next sentence is coherent or not. 

2. T5 w/ span: Preduct true/false to indicate if the next sentence is coherent or not. If false, additionally predicts the fine-grained error label and the error span. See example below:
<img width="676" alt="Screen Shot 2022-11-29 at 2 25 50 AM" src="https://user-images.githubusercontent.com/22390810/204477259-75032b52-95e6-47c0-a455-4fb4508604e7.png">

### Running trained models

Download the trained models here: https://drive.google.com/drive/folders/1iwkfMvtyP-6k3jTIsUDB8rW7f4sFLPiH?usp=sharing

The snac_evaluate.py file expects a validation file (.tsv) with 3 columns: id, context, sentence. Each row should contain the next sentence  to be evaluated (sentence column), the context until that point in the story, i.e. the (n-1) sentences leading up to the next sentence (context column). I've included a sample.tsv here. 

To run this code, preprocess your summaries to tokenize into sentences and convert to the format above. A summary with n sentences should correspond to n rows. 

``` 
python3 snac_evaluate.py --validation_file sample.tsv --model_name_or_path  [model_path]   --output_dir [output_dir]
python3 snac_evaluate.py --validation_file sample.tsv --model_name_or_path  /home/mb5018/long-doc-summ/snac-main/t5-span  --output_dir  /home/mb5018/long-doc-summ/snac-main
```

It will generate an output file with the predicted errors in each sentence with the following format:

  If it detects a coherence error: false <label1> [spans for label1] <label2> [spans for label2]
  
  If no coherence error is detected: true

The different label options are: character (CharE errors), event (RefE errors), scene (SceneE), inconsistent (InconE).