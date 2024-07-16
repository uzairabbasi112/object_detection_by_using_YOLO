
import gradio as gr
from PIL import Image
import torch
import numpy as np
from ultralytics import YOLO
import numpy as np
# Load the YOLOv8 model from the .pth file
model = YOLO('best.pt')  # Ensure the correct path to your model

def predict(image):
    # Convert PIL image to numpy array
    img = np.array(image)

    # Predict using the model
    results = model(img)

    # Render the results on the image
    results_img = results[0].plot()

    # Convert the numpy array back to a PIL image
    results_img_pil = Image.fromarray(results_img)
    return results_img_pil

# Create a Gradio interface
gr_interface = gr.Interface(fn=predict, inputs=gr.Image(type='pil'), outputs=gr.Image(type='pil'))
gr_interface.launch()


