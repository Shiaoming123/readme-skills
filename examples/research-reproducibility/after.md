# Adaptive Federated Learning — reproducibility snapshot

> **README Skills showcase rewrite.** This is not an IBM publication. It documents [`IBM/adaptive-federated-learning@b6bc482`](https://github.com/IBM/adaptive-federated-learning/tree/b6bc482bf2aac15c28b50125ecc6f3e0096c5149).

Source accompanying the 2019 IEEE JSAC paper “Adaptive federated learning in resource constrained edge computing systems.”

## Reproducibility status

This repository is archived. The code and experiment instructions exist, but this showcase did **not** execute the legacy TensorFlow environment or reproduce the paper's numerical results.

The original README says the produced plot should look similar to selected Figure 4 subfigures, with higher fluctuation. Treat that as an author expectation—not a verification tolerance.

## Environment recorded by the snapshot

[`requirements.txt`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/requirements.txt) declares:

- Python 3, without a narrower supported range;
- TensorFlow `>=1.13,<2`;
- Matplotlib `>=3.0.3`;
- NumPy `>=1.16.2`.

Operating system, hardware, and exact dependency lock versions are not specified.

## Historical experiment flow

1. Download MNIST or CIFAR-10 manually into the paths described by the [source README](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md).
2. Review [`config.py`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/config.py). The fixed default selects MNIST even/odd, a smooth SVM, five clients, and two simulation seeds.
3. Start `server.py` and wait for its incoming-connection message.
4. Start five `client.py` processes on the same machine.
5. Run `plot_multi_run.py` after all processes finish.

The configuration writes `results/SingleRun.csv` or `results/MultipleRuns.csv`. Existing CSV data is appended, so isolate or remove previous results only after preserving anything needed.

## Supported experiment branches

The fixed configuration contains paths for MNIST with SVM, MNIST with CNN, and CIFAR-10 with CNN. Only one configuration is active at a time. Extending the code to other datasets or models is possible in source, but is not a supported-result claim.

## Citation and license

Use the complete citation provided in the [fixed source README](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/README.md). The repository snapshot includes an [MIT license](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/LICENSE); downloaded datasets retain their own terms.
