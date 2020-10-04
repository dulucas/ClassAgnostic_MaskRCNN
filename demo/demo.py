from maskrcnn_benchmark.config import cfg
from predictor import COCODemo
import cv2

config_file = "../configs/e2e_mask_rcnn_R_50_FPN_1x_agnostic.yaml"

cfg.merge_from_file(config_file)
cfg.merge_from_list(["MODEL.DEVICE", "cuda"])

coco_demo = COCODemo(
    cfg,
    min_image_size=800,
    confidence_threshold=.3, # change confidence threshold to show the low quality of detections
)

image_path = './bear.jpg'
image = cv2.imread(image_path)
# box format: xyxy
#     first pair of (x,y) : left up corner of bbox
#     second pair of (x, y) : right bottom corner of bbox
results, boxes, masks = coco_demo.run_on_opencv_image(image)

cv2.imshow('img', results)
cv2.waitKey()

