import streamlit as st
import os
import json
from PIL import Image

# Function to load the list of images
def load_images(image_folder):
    return [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Function to load the JSON file with results
def load_results(json_file):
    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            return json.load(f)
    return {}

# Function to save the results to a JSON file
def save_results(json_file, results):
    with open(json_file, 'w') as f:
        json.dump(results, f)

# Main function to run the app
def main():
    st.title("Image Reviewer")

    image_folder = "/home/mehdi/dalia-ml/crops"  # Folder containing images
    json_file = "results.json"  # JSON file to save results

    # Load images and results
    images = load_images(image_folder)
    results = load_results(json_file)

    # Initialize session state for image index
    if 'image_index' not in st.session_state:
        st.session_state.image_index = 0

    # Display progress
    labeled_images = len(results)
    total_images = len(images)
    st.write(f"Labeled {labeled_images} out of {total_images} images")

    # Display the current image
    if st.session_state.image_index < total_images:
        current_image = images[st.session_state.image_index]
        image_path = os.path.join(image_folder, current_image)
        image = Image.open(image_path)
        st.image(image, caption=current_image)

        # Buttons for Yes and No
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes"):
                results[current_image] = "Yes"
                st.session_state.image_index += 1
                save_results(json_file, results)
                st.experimental_rerun()
        with col2:
            if st.button("No"):
                results[current_image] = "No"
                st.session_state.image_index += 1
                save_results(json_file, results)
                st.experimental_rerun()
    else:
        st.write("No more images to review.")

if __name__ == "__main__":
    main()
