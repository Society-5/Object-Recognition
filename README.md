# Object-Recognition

Real-time object detection from a webcam for the Robosapien project, built on the **TensorFlow Object Detection API** and a COCO-pretrained **SSD MobileNet v1** model (90 classes).

## Project-specific files

| File | Purpose |
|---|---|
| `object_detection_robot.py`, `object_detection_robot_new.py` | Downloads `ssd_mobilenet_v1_coco_11_06_2017`, loads the frozen graph, runs detection on each `cv2.VideoCapture(0)` frame, and draws labelled boxes. Press `q` to quit |
| `testcam.py` | Camera smoke test (work in progress) |

## Vendored code

Everything else (`anchor_generators/`, `box_coders/`, `builders/`, `core/`, `meta_architectures/`, `protos/`, `utils/`, `object_detection_tutorial.ipynb`, ...) is a copy of the [TensorFlow Object Detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) from TensorFlow Models, licensed under Apache 2.0.

## Run

Requires TensorFlow 1.x (uses `tf.GraphDef` and `tf.Session`), OpenCV, Pillow, and compiled protobufs (`protoc protos/*.proto --python_out=.`).

```bash
python object_detection_robot_new.py
```

---

Part of **[Society-5](https://github.com/Society-5)**: a WowWee Robosapien X that explores a floor on its own, using a phone camera and QR codes as markers, with a mixed-reality (VR) interface for remote control. See [Introduction](https://github.com/Society-5/Introduction) for the project overview.
