# pylsh — archived Python library

[![Status: archived](https://img.shields.io/badge/status-archived-6e7781.svg)](https://github.com/mattilyra/LSH) [![License: MIT](https://img.shields.io/badge/license-MIT-2da44e.svg)](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/LICENSE)

> **README Skills optimization demo.** This is not an upstream README. It preserves the original installation, dependency, attribution, and learning links while documenting [`mattilyra/LSH@a57069b`](https://github.com/mattilyra/LSH/tree/a57069bfb70f4b620d47931f81966b5a73c1b480).

`pylsh` is a Python implementation of locality-sensitive hashing with MinHash for detecting near-duplicate documents. It uses the MurmurHash3 library to create document fingerprints.

## Project status

This repository is archived. Modern Python, NumPy, compiler, and packaging compatibility are unverified.

Two inspected version sources conflict: [`setup.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/setup.py) declares `0.3.0`, while [`lsh/__init__.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/__init__.py) declares `0.1.1`. No version badge is shown because the repository does not establish a single authoritative value.

## Minimal source-level example

```python
from lsh.minhash import MinHasher

hasher = MinHasher(seeds=128, char_ngram=5, random_state=0)
score = hasher.jaccard("near duplicate text", "near-duplicate text")
print(score)
```

The names and parameters come from [`lsh/minhash.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/minhash.py). The example was not executed for this showcase.

## Historical installation

NumPy is required to run the code. Cython is required only when regenerating the hashing and shingling `.cpp` files; by default, `setup.py` uses the pre-generated C++ sources unless `USE_CYTHON` is enabled.

```bash
git clone https://github.com/mattilyra/LSH
cd LSH
python setup.py install
```

A working compiler toolchain may still be required. Prefer an isolated historical environment because no supported Python range is declared.

## Examples and tests

- The original [Introduction notebook](http://nbviewer.jupyter.org/github/mattilyra/LSH/blob/master/examples/Introduction.ipynb) explains locality-sensitive hashing and parameter selection; it is also present in the repository's `examples` directory.
- Unit tests are stored under [`lsh/test`](https://github.com/mattilyra/LSH/tree/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/test).
- `setup.py` declares pytest as a test dependency, but no test run was performed for this documentation example.

## Attribution and license

The implementation uses MurmurHash3. Its original attribution link remains available at [aappleby/smhasher](https://github.com/aappleby/smhasher).

The repository snapshot is distributed under the [MIT license](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/LICENSE). MurmurHash3 remains subject to its own attribution and terms.
