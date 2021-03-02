import pixellib
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5") 
segment_image.segmentImage("/home/lilly/dancegame/Image0.png", output_image_name = "/home/lilly/dancegame/segmentation.png")
