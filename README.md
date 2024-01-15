<div align="center">
  <br />
    <a href="">
      <img src="https://github.com/thebugged/drowsiness-detection/assets/74977495/c1b9b4e9-718d-4bda-804e-f984b9792da5" alt="Banner">
    </a>
  <br />

  <div>
    <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logoColor=white&logo=python&color=3776AB" alt="python" />
   <img src="https://img.shields.io/badge/-TensorFlow-black?style=for-the-badge&logoColor=white&logo=tensorflow&color=FF6F00" alt="tensorflow" />
   <img src="https://img.shields.io/badge/-OpenCV-black?style=for-the-badge&logoColor=white&logo=opencv&color=5C3EE8" alt="opencv" />
</div>


  <h3 align="center">Drowsiness Detector </h3>

   <div align="center">
Fatigue and drowsiness can impair a driver's ability to react quickly and make sound judgments, leading to accidents with severe consequences. The application utilizes the OpenCV library for real-time video capture and processing, detecting whether a driver is Alert or Drowsy.
    </div>
</div>
<br/>

🗃️ The dataset can be accessed here - [Training](https://www.kaggle.com/datasets/dheerajperumandla/drowsiness-dataset),[Testing](https://www.kaggle.com/datasets/adinishad/prediction-images)


## Setup & Installation
**Prerequisites**

Ensure the following are installed;
- [Python](https://www.python.org/downloads/)
- [Jupter Notebook](https://jupyter.org/install) (or install the Jupyter extension on Visual Studio Code).

To set up this project locally, follow these steps:

1. Clone the repository:
```shell
git clone https://github.com/thebugged/drowsiness-detection.git
```

2. Change into the project directory: 
```shell
cd drowsiness-detection
```

3. Install the required dependencies: 
```shell
pip install -r requirements.txt
```
<br/>

## Running the App
1. Run the `drowsy.ipynb` notebook to get the `drowsy.h5` & `drowsy.json` files to run the aplication.

2. Make sure the `drowsy.h5`, `drowsy.json` and `mainapp.py` are in the same directory then run the application using the command: 
```shell
   python mainapp.py
```
or
```shell
   python3 mainapp.py
```

