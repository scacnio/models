#copied from https://github.com/BenGreenfield825
import wget
model_link = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_1024x1024_coco17_tpu-8.tar.gz"
wget.download(model_link)
import tarfile
tar = tarfile.open('ssd_resnet50_v1_fpn_1024x1024_coco17_tpu-8.tar.gz')
tar.extractall('.')
tar.close()