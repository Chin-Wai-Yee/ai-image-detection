# AI-Image-Detection

<b> Universiti Tunku Abdul Rahman (UTAR) - Bachelor of Computer Science (Honours) - UCCD3074 DEEP LEARNING FOR DATA SCIENCE </b>

<b> Authors: </b> <br>
1\. Brandon Ting En Junn (21ACB01751) </b> <br>
2\. Chin Wai Yee (21ACB03370) <br>
3\. Loh Kin Ming (21ACB02961)

<b> Project Title: </b> [Classification of AI-Generated and Real Images using Deep Learning Techniques](/Assignment2_group2_BrandonTingEnJunn.pdf)

This is an application-based project for a course assignment. It uses deep learning techniques to classify an image whether it is AI-generated or real.

## Setup & Installation
### Source Code
- `Assignment2_group2_BrandonTingEnJunn.ipynb`
    - Contains the main source code.
        1. Upload to Kaggle.
        2. Make sure GPU is enabled for the session.
        3. Start the session.
        4. Run the code.

<i>

<u> Note: </u>

1. [Dataset](https://www.kaggle.com/datasets/tristanzhang32/ai-generated-images-vs-real-images) and Model used are included by default only through Kaggle.

2. If Model is empty, please download `model.pth` and upload it manually to Kaggle (Input -> New Model -> model.pth -> (Model Name) model -> (Framework) PyTorch -> (License) Apache 2.0 -> Create).

3. "Run all" will train a new model, but "4.1 Load Model" will always load and evaluate our previously trained model.

4. Skip "4.1 Load Model" if you want to evaluate the newly trained model.

5. `model_frozen.pth` is the model used in our ablation studies.

</i>

<hr>

### Application
- `demo.py`
    - Contains the demo of the application.
    - Requires Python.
    - Requires `model.pth` in the same directory.

<i>

<u> Note: </u>

1. It requires the installation of Python.

2. The application may not run if `model.pth` is not found or not in the same directory as `demo.py`.

3. The application may run into some Python dependencies missing errors. Please install the required dependencies if prompted.

4. The application may not run properly if GPU is not found on your device.

</i>
