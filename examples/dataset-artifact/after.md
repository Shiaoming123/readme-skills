# HICO-DET utilities — archived artifact card

> **README Skills showcase rewrite.** This is not an upstream README. It documents [`fredzzhang/hicodet@e4e2340`](https://github.com/fredzzhang/hicodet/tree/e4e234045e0a4128995a2e45e841b3ebe64eda0b).

Code for loading, exploring, visualizing, detecting, and evaluating human-object interactions with HICO-DET.

## Artifact status and rights

This GitHub repository is archived. The repository's MIT license covers its code snapshot; it does **not** establish permission to use the separately downloaded HICO-DET images or annotations. Verify the dataset's source terms before downloading or redistributing data.

The fixed `download.sh` retrieves an archive from Google Drive and extracts it without a checksum. Review the script and source before use; the download was not run for this showcase.

## Recorded schema

[`hicodet.py`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/hicodet.py) declares:

| Dimension | Count |
| --- | ---: |
| Object classes | 80 |
| Verb classes | 117 |
| Interaction classes | 600 |

Each indexed sample returns an image and annotations containing human boxes, object boxes, interaction indices, object indices, and verb indices. Images without bounding-box annotations are skipped during indexing.

## Source-level loader example

```python
from pocket.data import HICODet

dataset = HICODet(
    root="./hico_20160224_det/images/train2015",
    anno_file="./instances_train2015.json",
)
image, annotation = dataset[0]
```

This API is documented in [`DOC.md`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/DOC.md) and depends on the separately maintained Pocket library. No compatible Python, PyTorch, Pocket, CUDA, or hardware versions are pinned in the root README.

## Intended use and limitations

The repository provides research utilities and detector workflows, not a general-purpose people analytics product. Dataset coverage, labeling choices, model behavior, privacy, bias, and deployment suitability require evaluation beyond this code snapshot.

## Citation and license

The [source README](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/README.md) contains citations for related detection work. Repository code is under the [MIT license](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/LICENSE); dataset rights remain separate.
