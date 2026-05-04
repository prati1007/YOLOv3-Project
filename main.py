from models.common import DetectMultiBackend

model = DetectMultiBackend("yolov3.pt")
results = model("image.jpg")

print(results)
