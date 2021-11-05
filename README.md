# ClassAgnostic_MaskRCNN

This is a repo for training class-agnostic Mask R-CNN. Code is based on [maskrcnn_benchmark](https://github.com/facebookresearch/maskrcnn-benchmark). We provide a class-agnostic Mask R-CNN pre-trained on COCO dataset. Details of training can be found [here](https://github.com/dulucas/ClassAgnostic_MaskRCNN/blob/main/configs/e2e_mask_rcnn_R_50_FPN_1x_agnostic.yaml).

## Installation

Check [INSTALL.md](INSTALL.md) for installation instructions.


## How it works
1. Download pre-trained model from https://1drv.ms/u/s!Ar4uxu1EELfHdIvVAVSbn_BXJcs?e=Jo4Jof
2. Put the pre-trained model anywhere you want
3. Modify the model path in the config file
```
cd configs
vim e2e_mask_rcnn_R_50_FPN_1x_agnostic.yaml
# Modify the model path in third line "WEIGHT: "/home/duy/phd/lucasdu/duy/maskrcnn_ensemble/maskrcnn_all_class_agnostic/model_0090000.pth""
```

4. Run the demo
```
cd demo
python demo.py
```

## Citations
```
@misc{massa2018mrcnn,
author = {Massa, Francisco and Girshick, Ross},
title = {{maskrcnn-benchmark: Fast, modular reference implementation of Instance Segmentation and Object Detection algorithms in PyTorch}},
year = {2018},
howpublished = {\url{https://github.com/facebookresearch/maskrcnn-benchmark}},
note = {Accessed: [Insert date here]}
}
```
