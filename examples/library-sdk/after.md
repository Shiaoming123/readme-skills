# pylsh — archived Python library

> **README Skills showcase rewrite.** This is not an upstream README. It documents [`mattilyra/LSH@a57069b`](https://github.com/mattilyra/LSH/tree/a57069bfb70f4b620d47931f81966b5a73c1b480).

`pylsh` implements MinHash locality-sensitive hashing for finding near-duplicate text documents.

## Project status

This repository is archived. Modern Python, NumPy, compiler, and packaging compatibility are unverified.

Two inspected version sources conflict: [`setup.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/setup.py) declares `0.3.0`, while [`lsh/__init__.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/__init__.py) declares `0.1.1`. This rewrite does not select one as authoritative.

## Source-level example

```python
from lsh.minhash import MinHasher

hasher = MinHasher(seeds=128, char_ngram=5, random_state=0)
score = hasher.jaccard("near duplicate text", "near-duplicate text")
print(score)
```

The names and parameters come from [`lsh/minhash.py`](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/minhash.py). The example was not executed for this showcase.

## Historical installation

The fixed project uses `setup.py` and compiled extension sources:

```bash
python setup.py install
```

`setup.py` declares NumPy and Cython dependencies and defaults to pre-generated C++ sources. A working compiler toolchain may still be required. Prefer an isolated historical environment; no supported Python range is declared.

## Tests and learning material

- Unit tests are stored under [`lsh/test`](https://github.com/mattilyra/LSH/tree/a57069bfb70f4b620d47931f81966b5a73c1b480/lsh/test).
- The [introduction notebook](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/examples/Introduction.ipynb) explains parameter selection.

The repository declares pytest as a test dependency, but no test run was performed for this documentation example.

## License

The repository snapshot is distributed under the [MIT license](https://github.com/mattilyra/LSH/blob/a57069bfb70f4b620d47931f81966b5a73c1b480/LICENSE). MurmurHash3 attribution remains documented by the upstream project.
