import json
from qafacteval import QAFactEval

kwargs = {
    "cuda_device": 0,
    "use_lerc_quip": True,
    "verbose": True,
    "generation_batch_size": 32,
    "answering_batch_size": 32,
    "lerc_batch_size": 8
}

model_folder = "/home/mb5018/long-doc-summ/QAFactEval/models"
metric = QAFactEval(
    lerc_quip_path=f"{model_folder}/quip-512-mocha",
    generation_model_path=f"{model_folder}/generation/model.tar.gz",
    answering_model_dir=f"{model_folder}/answering",
    lerc_model_path=f"{model_folder}/lerc/model.tar.gz",
    lerc_pretrained_model_path=f"{model_folder}/lerc/pretraining.tar.gz",
    **kwargs
)

# Score the batch
results = metric.score_batch_qafacteval(["This is a source document"], [["This is a summary."]], return_qa_pairs=True)
score = results[0][0]['qa-eval']['lerc_quip']

# Save results to a JSON file
with open("/home/mb5018/long-doc-summ/QAFactEval/results.json", "w") as f:
    json.dump(results, f, indent=4)

# Save the score to a text file
with open("/home/mb5018/long-doc-summ/QAFactEval/score.txt", "w") as f:
    f.write("LERC_QUIP Score: " + str(score))
