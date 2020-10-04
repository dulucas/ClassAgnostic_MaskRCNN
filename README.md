# ObjSeg_MaskRCNN

## Installation

Check [INSTALL.md](INSTALL.md) for installation instructions.


## How it works
1. Download pre-trained model from https://drive.google.com/drive/folders/1ysQl5MtD3k4cLmk3AXCd34ELpxShmpMj?usp=sharing
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
