import tensorflow as tf
import numpy as np
import warnings

warnings.filterwarnings('ignore')
from PIL import Image
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

IMAGE_SIZE = (12, 8)  # Output display size as you want
import matplotlib.pyplot as plt

PATH_TO_SAVED_MODEL = "saved_model_tf"
print('Loading model...', end='')

# Load saved model and build the detection function
detect_fn = tf.saved_model.load(PATH_TO_SAVED_MODEL)
print('Done!')

# Loading the label_map
category_index = label_map_util.create_category_index_from_labelmap("./label_map.pbtxt", use_display_name=True)


# category_index=label_map_util.create_category_index_from_labelmap([path_to_label_map],use_display_name=True)

def load_image_into_numpy_array(path):
    return np.array(Image.open(path))


def tensorflow_detect(path):
    image_path = path
    image_name = path.split("upload/")[1]
    # print('Running inference for {}... '.format(image_path), end='')

    image_np = load_image_into_numpy_array(image_path)

    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image_np)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis, ...]

    detections = detect_fn(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy()
                  for key, value in detections.items()}
    detections['num_detections'] = num_detections

    # detection_classes should be ints.
    detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

    image_np_with_detections = image_np.copy()

    viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=.4,  # Adjust this value to set the minimum probability boxes to be classified as True
        agnostic_mode=False)
    plt.figure(figsize=IMAGE_SIZE, dpi=200)
    plt.axis("off")
    plt.imshow(image_np_with_detections)
    plt.show()
    plt.savefig(f'static/outputs/tf/{image_name}', bbox_inches='tight', pad_inches=0)

    classes = [cls for cls in detections['detection_classes'][detections['detection_scores'] > .4]]
    classes = [category_index.get(cls)['name'] for cls in classes]
    data = []
    if len(classes) == 0:

        data.append({
            "class": "Undefined",
            "score": "--",
            "result_image": f'static/outputs/tf/{image_name}'
        })

    else:

        for i in range(len(classes)):
            score = "{:.2f}".format(detections['detection_scores'][i] * 100)
            data.append({
                "class": classes[i],
                "score": str(score) + "%",
                "result_image": f'static/outputs/tf/{image_name}'
            })

    print(data)
    return data[0]
