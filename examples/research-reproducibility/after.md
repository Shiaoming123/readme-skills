# Adaptive Federated Learning in Resource-Constrained Edge Systems

[![Status: archived](https://img.shields.io/badge/status-archived-6e7781.svg)](https://github.com/IBM/adaptive-federated-learning) [![TensorFlow: 1.x](https://img.shields.io/badge/TensorFlow-1.x-ff6f00.svg)](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/requirements.txt) [![License: MIT](https://img.shields.io/badge/license-MIT-2da44e.svg)](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/LICENSE)

> **README Skills optimization demo.** This is not an IBM publication. It preserves the original paper, citation, dataset, experiment, configuration, output, and contributor information while documenting [`IBM/adaptive-federated-learning@b6bc482`](https://github.com/IBM/adaptive-federated-learning/tree/b6bc482bf2aac15c28b50125ecc6f3e0096c5149).

Source code accompanying the paper S. Wang, T. Tuor, T. Salonidis, K. K. Leung, C. Makaya, T. He, and K. Chan, “Adaptive federated learning in resource constrained edge computing systems,” *IEEE Journal on Selected Areas in Communications*, vol. 37, no. 6, pp. 1205–1221, Jun. 2019.

## Reproducibility status

The repository is archived. The code and experiment instructions exist, but this showcase did **not** execute the legacy TensorFlow environment or reproduce the paper's numerical results.

The original README says the plot should look similar to the SVM (SGD) subfigures in Figure 4, with higher fluctuation. Treat that as an author expectation, not a verified reproduction tolerance.

## Recorded environment

[`requirements.txt`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/requirements.txt) declares:

- Python 3, without a narrower supported range;
- TensorFlow `>=1.13,<2`;
- Matplotlib `>=3.0.3`;
- NumPy `>=1.16.2`.

Operating system, hardware, and exact lock versions are not specified.

## Getting started

Install the recorded dependencies in an isolated historical environment:

```bash
pip3 install -r requirements.txt
```

Download the datasets manually into `datasets`:

- For MNIST, download the standalone files from <http://yann.lecun.com/exdb/mnist/> into `datasets/mnist`.
- For CIFAR-10, download the binary version from <https://www.cs.toronto.edu/~kriz/cifar.html>, extract the standalone `*.bin` files, and place them in `datasets/cifar-10-batches-bin`.

## Historical experiment flow

1. Review [`config.py`](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/config.py). The fixed default selects MNIST even/odd, a smooth SVM, five clients, and two simulation seeds.
2. Run `server.py` and wait for `Waiting for incoming connections...`.
3. Run five parallel `client.py` instances on the same machine as the server.
4. Watch the server and clients for message-exchange output; the original README says the run takes a few minutes.
5. After all processes finish, run `plot_multi_run.py` to produce the plot.

## Code structure and outputs

All configuration options are in `config.py`, which also explains the available setups. The fixed configuration includes paths for MNIST with SVM, MNIST with CNN, and CIFAR-10 with CNN; only one setup is active at a time.

Results are saved as CSV files under `results`. New data is appended to an existing file. Preserve any needed output before deleting or isolating old CSV files for a new experiment.

The original README says the code can be extended to other datasets and models. That is an extensibility note, not evidence that other combinations reproduce supported results.

## Citation

When using this code for scientific publications, cite the accompanying paper:

```bibtex
@article{wang2019adaptive,
  title={Adaptive federated learning in resource constrained edge computing systems},
  author={Wang, Shiqiang and Tuor, Tiffany and Salonidis, Theodoros and Leung, Kin K and Makaya, Christian and He, Ting and Chan, Kevin},
  journal={IEEE Journal on Selected Areas in Communications},
  volume={37},
  number={6},
  pages={1205-1221},
  year={2019}
}
```

## Contributors

The original README credits Shiqiang Wang and Tiffany Tuor.

## License

The repository snapshot includes an [MIT license](https://github.com/IBM/adaptive-federated-learning/blob/b6bc482bf2aac15c28b50125ecc6f3e0096c5149/LICENSE). Downloaded datasets retain their own terms.
