import sys
import torch

sys.path.append("/home/shodh/evaluation")
from evaluate.evaluate import evaluate_models
from data_reader import Data


def main():
    data = Data()
    models = data.load_models()
    tasks = ",".join(data.load_datasets())

    for model in models:
        evaluate_models(model, tasks)


if __name__ == "__main__":
    main()
