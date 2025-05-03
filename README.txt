UCCD3074 Deep Learning for Data Science Group Assignment
Trimester 2025 Feb

Title: Classification of AI-Generated and Real Images using Deep Learning Techniques

Application-based

Group 2:
1. Brandon Ting En Junn (Leader) CS 2101751
2. Chin Wai Yee CS 2103370
3. Loh Kin Ming CS 2102961

##########################################
Prepared By: Brandon Ting En Junn 2101751
##########################################
1. Assignment2_group2_BrandonTingEnJunn.pdf
- Final Report

2. Assignment2_group2_BrandonTingEnJunn.ipynb
- Source Code
- Setup:
	1. Upload Assignment2_group2_BrandonTingEnJunn.ipynb to Kaggle.
	2. Make sure GPU for the session is enabled.
	3. Start the session.
	* Important: Read Note:
	4. Run code.
- Note:
1. Dataset and Model are included only through Kaggle.
2. If Model is empty, please download model.pth from https://drive.google.com/file/d/1XUcsICq17c2XhKiJUqWo3H5LRQN5mKQR/view?usp=sharing. Then, upload it to Kaggle (Input -> New Model -> model.pth -> (Model Name) model -> (Framework) PyTorch -> (License) Apache 2.0 -> Create).
3. "Run all" will train a new model, but "4.1 Load Model" will always load and evaluate our previously trained model.
4. Skip "4.1 Load Model" if you want to evaluate the newly trained model.
5. If it is needed, model_frozen.pth from https://drive.google.com/file/d/1vh7_CsLL2DvkoxIe_RkrGAhhzSAjGSNe/view?usp=sharing is the model used in our ablation studies.

* Link to Dataset: https://www.kaggle.com/datasets/tristanzhang32/ai-generated-images-vs-real-images
* Link to Model (model.pth): https://drive.google.com/file/d/1XUcsICq17c2XhKiJUqWo3H5LRQN5mKQR/view?usp=sharing
* Link to Alblation Studies Model (model_frozen.pth): https://drive.google.com/file/d/1vh7_CsLL2DvkoxIe_RkrGAhhzSAjGSNe/view?usp=sharing
* Link to GitHub Repository: https://github.com/Chin-Wai-Yee/UCCD3074-Assignment-AI-image-detector

3. demo.py
- Demo Application
- Setup:
	1. Download model.pth from https://drive.google.com/file/d/1XUcsICq17c2XhKiJUqWo3H5LRQN5mKQR/view?usp=sharing.
	2. Move model.pth to the same directory as demo.py.
	3. Run the application, it may take awhile to load.
- Note:
1. It requires the installation of Python.
2. The application may not run if model.pth is not found or not in the same directory as demo.py.
3. The application may run into some Python dependencies missing errors. Please install the required dependencies if prompted.
4. The application may not run if GPU is not found on your device.
