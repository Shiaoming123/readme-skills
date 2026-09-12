# HICO-DET utilities — archived scientific artifact

[![Status: archived](https://img.shields.io/badge/status-archived-6e7781.svg)](https://github.com/fredzzhang/hicodet) [![Utilities: 9](https://img.shields.io/badge/utilities-9-0969da.svg)](#supported-utilities) [![Code license: MIT](https://img.shields.io/badge/code_license-MIT-2da44e.svg)](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/LICENSE)

> **README Skills optimization demo.** This is not an upstream README. It preserves all original utility, installation, dataset, Pocket, citation, documentation, and license links while adding an artifact card for [`fredzzhang/hicodet@e4e2340`](https://github.com/fredzzhang/hicodet/tree/e4e234045e0a4128995a2e45e841b3ebe64eda0b).

Utilities for loading, exploring, visualizing, detecting, and evaluating human-object interactions with the [HICO-DET dataset](http://www-personal.umich.edu/~ywchao/hico/).

## Artifact status and rights

This GitHub repository is archived. Its MIT license covers the code snapshot; it does **not** establish permission to use the separately downloaded HICO-DET images or annotations. Verify the dataset source terms before downloading or redistributing data.

The fixed `download.sh` retrieves an archive from Google Drive and extracts it without a checksum. Review the script and source before use; the download was not run for this showcase.

## Supported utilities

### Training and evaluation

- [Train and test advanced variants of DETR on HICO-DET](https://github.com/fredzzhang/hicodet/tree/main/detections#train-and-test-advanced-variants-of-detr-on-hico-det)
- [Train and test DETR on HICO-DET](https://github.com/fredzzhang/hicodet/tree/main/detections#train-and-test-detr-on-hico-det)
- [Fine-tune Faster R-CNN on HICO-DET](https://github.com/fredzzhang/hicodet/tree/main/detections#fine-tune-the-detector-on-hico-det)
- [Evaluate object detections](https://github.com/fredzzhang/hicodet/tree/main/detections#evaluate-detections)

### Exploration and visualization

- [Command-line dataset navigator](https://github.com/fredzzhang/hicodet/tree/main/utilities#dataset-navigator)
- [Large-scale visualization in a web page](https://github.com/fredzzhang/hicodet/tree/main/utilities#generate-and-visaulise-box-pairs-in-large-scales)
- [Visualize detected objects](https://github.com/fredzzhang/hicodet/tree/main/detections#visualise-detections)

### Detection generation

- [Generate object detections with Faster R-CNN](https://github.com/fredzzhang/hicodet/tree/main/detections#generate-detections-using-faster-r-cnn)
- [Generate ground-truth object detections](https://github.com/fredzzhang/hicodet/tree/main/detections#generate-ground-truth-detections)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/fredzzhang/hicodet.git
   cd hicodet
   ```

2. Prepare the [HICO-DET dataset](https://drive.google.com/open?id=1QZcJmGVlF9f4h-XLWe9Gkmnmj2z1gSnk). To use the historical helper:

   ```bash
   bash download.sh
   ```

   If the dataset already exists, create the original soft link instead:

   ```bash
   ln -s /path/to/hico_20160224_det ./hico_20160224_det
   ```

3. Install the lightweight deep-learning library [Pocket](https://github.com/fredzzhang/pocket).
4. Activate the environment created for Pocket.

No compatible Python, PyTorch, Pocket, CUDA, or hardware versions are pinned in the source README.

## Dataset class and recorded schema

[`hicodet.py`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/hicodet.py) declares:

| Dimension | Count |
| --- | ---: |
| Object classes | 80 |
| Verb classes | 117 |
| Interaction classes | 600 |

Each indexed sample returns an image plus human boxes, object boxes, interaction indices, object indices, and verb indices. Images without bounding-box annotations are skipped during indexing.

```python
from pocket.data import HICODet

dataset = HICODet(
    root="./hico_20160224_det/images/train2015",
    anno_file="./instances_train2015.json",
)
image, annotation = dataset[0]
```

The original dataset-class documentation is preserved in the fixed [`DOC.md`](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/DOC.md). The class is also available as `pocket.data.HICODet` in Pocket.

## Intended use and limitations

These are research utilities and detector workflows, not a general-purpose people-analytics product. Dataset coverage, labeling choices, model behavior, privacy, bias, and deployment suitability require evaluation beyond this code snapshot.

## Citation

If you find this work useful for research, preserve the original citations:

```bibtex
@inproceedings{zhang2023pvic,
  author    = {Zhang, Frederic Z. and Yuan, Yuhui and Campbell, Dylan and Zhong, Zhuoyao and Gould, Stephen},
  title     = {Exploring Predicate Visual Context in Detecting Human–Object Interactions},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  month     = {October},
  year      = {2023},
  pages     = {10411-10421},
}

@inproceedings{zhang2022upt,
  author    = {Zhang, Frederic Z. and Campbell, Dylan and Gould, Stephen},
  title     = {Efficient Two-Stage Detection of Human-Object Interactions with a Novel Unary-Pairwise Transformer},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
  month     = {June},
  year      = {2022},
  pages     = {20104-20112}
}

@inproceedings{zhang2021scg,
  author    = {Zhang, Frederic Z. and Campbell, Dylan and Gould, Stephen},
  title     = {Spatially Conditioned Graphs for Detecting Human–Object Interactions},
  booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
  month     = {October},
  year      = {2021},
  pages     = {13319-13327}
}
```

## License

Repository code is under the [MIT license](https://github.com/fredzzhang/hicodet/blob/e4e234045e0a4128995a2e45e841b3ebe64eda0b/LICENSE). Dataset rights remain separate.
