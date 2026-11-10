# Capstone project: activation-function research

This project compares nine activation functions on two deep-learning architectures:

- **ResNet-34** on **CIFAR-10** for computer vision.
- **Transformer Encoder** on **AG News** for natural-language processing.

## Requirements

```bash
pip install -r requirements.txt
```

## Project structure

| Path | Purpose |
|---|---|
| `activations.py` | Custom activations, including Mish and Swish, and their registry |
| `models/` | ResNet and Transformer definitions in `resnet.py` and `transformer.py` |
| `data.py` | Dataset loading and preprocessing |
| `train_utils.py` | Training loop and memory/accuracy metrics |
| `main.py` | Entry point for all 18 experiments |
| `analyze_results.py` | Summary tables and accuracy/time trade-off plots |
| `plot_learning_curves.py` | Per-epoch learning curves |

## Run experiments

```bash
python main.py
```

The run downloads CIFAR-10 and AG News, uses a fixed split of 90% training and 10% validation from each official training set plus its official test set, and trains each experiment for 30 epochs. Checkpoints are saved to `checkpoints/` and detailed outputs to `results/`. The configured random seed is 42.

## Analysis and visualization

After training, or when `results/final_experiment_results.csv` is available:

```bash
python analyze_results.py
```

This produces tables sorted by validation accuracy and a plot of best validation accuracy versus time per epoch.

```bash
python plot_learning_curves.py
```

This plots accuracy and loss over epochs for every activation. All plots are saved in `results/`.

## Metrics

Accuracy, validation loss, training time, gradient norm and peak GPU memory usage.

## Compared activations

ReLU, LeakyReLU, ELU, SELU, GELU, Swish, Mish, Hardswish and Softplus.

## Notes

CUDA accelerates training when available. Reduce `batch_size` in `main.py` if GPU memory is insufficient. Seeds are set to 42 in `main.py` and `train_utils.py`; hardware and execution settings can still affect reproducibility.
