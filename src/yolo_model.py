# roboflow API

# from roboflow import Roboflow
#
# rf = Roboflow(api_key="hkMbGodB7g2VkxKW4eJt")
# project = rf.workspace().project("beko")
# model = project.version(1).model

# def yolo_detect(path):
#     # infer on a local image
#     image_name = path.split("upload/")[1]
#     detections = model.predict(path, confidence=40, overlap=30).json()["predictions"]
#
#     if len(detections) == 0:
#         data = {
#             "class": "Undefined",
#             "score": "--",
#         }
#     else:
#         data = {
#             "class": detections[0]['class'],
#             "score": str("{:.2f}".format(detections[0]['confidence'] * 100)) + "%",
#         }
#
#     # save prediction
#     model.predict(path, confidence=40, overlap=30).save(f"./static/outputs/{image_name}")
#     data["result_image"] = f"static/outputs/{image_name}"
#     return data


# Local saved model
from ultralytics import YOLO

model_path = "saved_model_yolo/best.pt"

model = YOLO(model_path)
names = model.names


def yolo_detect(path):
    image_name = path.split("upload/")[1]
    results = model.predict(path, conf=0.4, save=True, project="static", name="outputs/yolo", exist_ok=True)

    data = []
    if len(results[0].boxes.cls) == 0:
        data.append({
            "class": "Undefined",
            "score": "--",
            "result_image": f"static/outputs/yolo/{image_name}"
        })
    else:
        for r in results:
            for c, t in zip(r.boxes.cls, r.boxes.conf):

                score = "{:.2f}".format(t * 100)
                data.append({
                    "class": names[int(c)],
                    'score': str(score + "%"),
                    "result_image": f"static/outputs/yolo/{image_name}"
                })

    print(data)
    # for first detection
    return data[0]
