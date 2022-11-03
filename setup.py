from setuptools import find_packages, setup

import sys

cv_ver = ""
keras_ver = ">=2.0.0"
if sys.version_info.major < 3:
      cv_ver = "<=4.2.0.32" 
      keras_ver = "<=2.3.0"


setup(name="segmentation_test",
      description="Image Segmentation test",
      author="Mayank Yadav",
      author_email='mayank69123@gmail.com',
      platforms=["any"],
      license="GPLv3",
      url="https://github.com/bunbun205/segmentation_test",
      packages=find_packages(exclude=["test"]),
      entry_points={
            'console_scripts': [
                  'segmentation_test = .__main__:main'
            ]
      },
      install_requires=[
            "h5py<=2.10.0",
            "Keras"+keras_ver,
            "imageio==2.5.0",
            "imgaug>=0.4.0",
            "opencv-python"+cv_ver,
            "tqdm"],
      extras_require={
            # These requires provide different backends available with Keras
            "tensorflow": ["tensorflow"],
            "cntk": ["cntk"],
            "theano": ["theano"],
            # Default testing with tensorflow
            "tests-default": ["tensorflow", "pytest"]
      }
)