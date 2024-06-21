from ultralytics import YOLO  # type: ignore[import-untyped]

# Load a model
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="SKU-110K.yaml", epochs=100, imgsz=640, workers=0, batch=12)
model.save("sku110k_yolov8n.pt")  # save the model to disk
model.export(format="onnx")  # export to onnx (optional)
