# Dance Game Engine
[Arthur Murray Dance Studio](https://arthurmurray.com/)     ~~~~~~~~~~~~~~~~   [Our Blog](https://medium.com/ucl-comp0016-2020-team13) ~~~~~~~~~~~~~~ [Our Website](http://students.cs.ucl.ac.uk/2020/group13/)

![Logo](docs/imagesForREADME/coverImage/uclAndArthurMuray.png)

- [Dance Game Engine](#dance-game-engine)
  * [Abstract](#abstract)
  * [Key Features](#key-features)
    + [Graphical User Interface](#graphical-user-interface)
    + [Preprocessing Image](#preprocessing-image)
    + [Multi Platform](#multi-platform)
  * [Installation Guide](#installation-guide)
    + [Python Package Dependencies](#python-package-dependencies)
    + [For MacOS Users](#for-macos-users)
      - [Create parent directory](#create-parent-directory)
      - [Clone team 13 repository under danceGame directory](#clone-team-13-repository-under-dancegame-directory)
      - [Install openpose](#install-openpose)
      - [Clone openpose repository under danceGame directory](#clone-openpose-repository-under-dancegame-directory)
      - [Install prerequisites](#install-prerequisites)
      - [Build with Cmake](#build-with-cmake)
      - [Compilation](#compilation)
      - [Running openpose](#running-openpose)
      - [Running the game](#running-the-game)
    + [For Windows 10 Users](#for-windows-10-users)
      - [Create parent directory](#create-parent-directory-1)
      - [Clone team 13 repository under danceGame directory](#clone-team-13-repository-under-dancegame-directory-1)
      - [Install OpenPose](#install-openpose)
      - [Clone OpenPose repository below team 13 github repository](#clone-openpose-repository-below-team-13-github-repository)
      - [Prerequisites](#prerequisites)
      - [Cmake Configuration](#cmake-configuration)
      - [Run Openpose](#run-openpose)
      - [Run the Game](#run-the-game)
  * [User Manual For Both MacOS and Win10 Users](#user-manual-for-both-macos-and-win10-users)
    + [User Maunal](#user-maunal)
      - [Important Notice:](#important-notice-)
      - [gameInterface folder](#gameinterface-folder)
      - [Testing folder](#testing-folder)
      - [PreprocessSkeleton folder](#preprocessskeleton-folder)
  * [Legal Issue](#legal-issue)
    + [Legal Statement](#legal-statement)
    + [Data Privacy Consideration](#data-privacy-consideration)
    + [Software Licences](#software-licences)
    + [Credits](#credits)

## Abstract

Aimed at helping inexperienced dancers to learn basic dancing moves and gain interests in dancing, we worked with Arthur Murray Dance Studio to develop a video game engine. We provide a graphical frontend that prompts users to follow the example moves shown on screen, and it gives feedback by querying the set of APIs developed by our team, which extract skeletal information from images and evaluate the similarity between the example and that of the users. We performed pose estimation with the OpenPose system developed by CMU. The similarity score between two skeletons is calculated using a heuristically-determined one-variable function with the skeletons' cosine similarity as input. Both the graphical frontend and the set of APIs are designed to be modular and extendible, providing large potential for enhancement and extension of the game itself, and to other fields where it may fit.

## Key Features
### Graphical User Interface
We provide a graphical frontend that prompts users to imitate the example moves shown on the screen. The set of APIs are called under the hood of a gaming GUI, to evaluate the users' postures against the examples, giving a similarity score as output. Both the GUI and API layers serve as interfaces to users, which could be dancers or developers, depending on the context for which they like to use the system. The similarity score between two skeletons is calculated using a heuristically determined one-variable function with the skeletons' cosine similarity as input. We show the similarity of 10 sets of images. We also show the same evaluation routine embedded within the GUI.
![Look of GUI](docs/imagesForREADME/coverImage/key1.png)

### Preprocessing Image

We support a routine to preprocess images, save the skeletons locally, and set the basis to reconstruct example dance videos into cleaner, more polished, and more flexible stick-figure based forms.
![Rountine](docs/imagesForREADME/coverImage/key2.png)

### Multi Platform
The system is deployable across MacOS, Windows, and Linux. It only requires a PC equipped with webcams, as found in ordinary households; no other additional hardware is required.
![Routine](docs/imagesForREADME/coverImage/key3.png)

## Installation Guide
### Python Package Dependencies
Install packages for python:

Numpy, matplotlib, opencv
 
`pip install numpy`

`pip install matplotlib`

`pip install opencv-python`
### For MacOS Users

####   Create parent directory
Create directory at desired location, name it "danceGame"

    mkdir danceGame
####   Clone team 13 repository under danceGame directory

    cd danceGame

    git clone https://github.com/UCLComputerScience/COMP0016_2020_21_Team13
####  Install openpose
[Official installation instructions: ](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
####  Clone openpose repository under danceGame directory

    git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
####  Install prerequisites
cd into the openpose folder:

    cd openpose
![Mac Os Prerequisites](docs/imagesForREADME/MacInstallImg/macPre.png)
Note: As for now, cmake has to be installed using brew install --cask cmake
####  Build with Cmake

    cd {openpose_folder}
   (Note: this may be unnecessary if you are still under the same folder as from section 3.2)
   

    mkdir build/

    cd build/
    
    cmake-gui ..
   Verify the location of installation.

   ![Location of Installation](docs/imagesForREADME/MacInstallImg/installLoc.png)

   Press configure, use Xcode as generator.

   ![Use Xcode as generator](docs/imagesForREADME/MacInstallImg/generator.png)

   Enable BUILD_PYTHON and configure again.

   ![Choose BUILD_PYTHON](docs/imagesForREADME/MacInstallImg/build_python.png)




   Set GPU_MODE and configure again.

   ![Choose CPU_ONLY](docs/imagesForREADME/MacInstallImg/GPU_MODE.png)

   If Configuring done appears, then press Generate.

   ![Press Generate](docs/imagesForREADME/MacInstallImg/generate.png)

   Generating done will appear below, and you can close CMake.

   ![Generating Done](docs/imagesForREADME/MacInstallImg/generatingDone.png)

####  Compilation

    cd build/
   (Note: this may be unnecessary if you are still under the same folder as from section 3.3)
   

    make -j`sysctl -n hw.logicalcpu`
   Note: I faced the problem Could NOT find vecLib (missing: vecLib_INCLUDE_DIR), and I had to manually install Caffe.
   ![Manually Install Caffe](docs/imagesForREADME/MacInstallImg/caffe.png)
####  Running openpose
  Running the openpose executable:
  

      
    cd openpose/
    ./build/examples/openpose/openpose.bin --image_dir examples/media/
   

   [Running the python tutorials](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/03_python_api.md)

    cd openpose/build/examples/tutorial_api_python

    python3 01_body_from_image.py
Note: I notice that cmake has problem finding python that are installed by brew, and running python3 01_body_from_image.py will result in an error:

![Error When Running 01_body_from_image.py](docs/imagesForREADME/MacInstallImg/error.png)

Adding the following lines in CmakeLists.txt(directly under the openpose folder) will solve the problem:

    set(Python_ADDITIONAL_VERSIONS 3.9)
    
    find_package(PythonLibs 3 REQUIRED)
![Add the following lines to CmakeLists.txt](docs/imagesForREADME/MacInstallImg/lines.png)

The expected output:

![Expected Output](docs/imagesForREADME/MacInstallImg/output.png)
####  Running the game

    cd danceGame/COMP0016_2020_21_Team13/
(parent folder created in section 1)

    python3 gameInterface/mainGUI.py
   Note: make sure any program you run is from the COMP0016_2020_21_Team13 as the working directory.
   The expected output:
   ![The expected output](docs/imagesForREADME/MacInstallImg/output2.png)

### For Windows 10 Users


####   Create parent directory
Create directory at desired location, name it "danceGame"

    mkdir danceGame
####   Clone team 13 repository under danceGame directory

    cd danceGame

    git clone https://github.com/UCLComputerScience/COMP0016_2020_21_Team13

(parent directory path should not be too long as windows maximum path length is 256)
####  Install OpenPose
[Official installation instructions:](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
Tools:

Python version 3.7

Visual Studio 2019 Community

CMake 3.20.0
####   Clone OpenPose repository below team 13 github repository

    git clone [https://github.com/CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
![Clone Openpose Repository and team13 github repository](docs/imagesForREADME/Win10InstallImg/preReq.png)

####  Prerequisites
[Openpose Official Prerequisites](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/1_prerequisites.md)

[Install CMake GUI 3.20.0](https://cmake.org/download/)

![Download All Models that are Circled](docs/imagesForREADME/Win10InstallImg/caffe.png)

Clone pybind11 in the openpose/3rdparty directory mentioned above.

    cd openpose/3rdparty
    git clone https://github.com/pybind/pybind11
####  Cmake Configuration

![Verify the location of installation.](docs/imagesForREADME/Win10InstallImg/cmakePath.png)

Press configure, use Visual Studio 16 2019 as generator.

![Correct Settings](docs/imagesForREADME/Win10InstallImg/VSsetting.png)

Click on build python and cpu only for cpu mode:

![BUILD_PYTHON](docs/imagesForREADME/Win10InstallImg/buildPython.png)

![GPU_MODE](docs/imagesForREADME/Win10InstallImg/CPU_MODE.png)

Press "Configure" and then "Generate"

####  Run Openpose

Check OpenPose was properly installed by running any demo example: 01_body_from_image.py.

Open terminal, navigate to the path tutorial_api_python and then run 01_body_from_image.py. (or run it through visual studio code)

![CMD commands](docs/imagesForREADME/Win10InstallImg/commandLineCommand.png)

If openpose is properly installed, the following picture will pop out.

![Openpose Results](docs/imagesForREADME/Win10InstallImg/output.png)

####  Run the Game

    cd danceGame/COMP0016_2020_21_Team13/
    
    python3 gameInterface/mainGUI.py
Expected Output:

![Graphical User Interface](docs/imagesForREADME/Win10InstallImg/output2.png)

## User Manual For Both MacOS and Win10 Users
### User Maunal

#### Important Notice:
To correctly run any files that has imported team13api.py,

ALL FILES MUST RUN AT THE DIRECTORY OF COMP0016_2020_21_Team13 FOLDER:

![win10](docs/imagesForREADME/UserManual/win10Command.png)

Unless if you changed the location of openpose folder, REMEMBER to change the directory in the team13api.py AND that in opInfo.py, accordng to your platform
![Important Dir](docs/imagesForREADME/UserManual/changeDir.png)

#### gameInterface folder
Go to danceGame\COMP0016_2020_21_Team13\gameInterface, and run mainGUI.py under directory COMP0016_2020_21_Team13 see example above. Expected output:

![Graphical User Interface](docs/imagesForREADME/gameInterface/startingStage.png)

Start the game by running it under COMP0016_2020_21_Team13 as the working directory

![Game Interface and its Components](docs/imagesForREADME/gameInterface/guiDetail.png)

#### Testing folder

1. IntegrationTest\scoring. Code folder holds `imageScoringTest.py` which process a list of images and output all the images with their skeleton

2. UnitTest\skeletonRecognition. Code folder holds `skeletonRecognition.py` which processes a list of pairs of images stored in data folder and output all the skeleton in a window when the program finished.

3. UnitTest\webcamTest. Code folder holds `webcamTesting.py` which turns on the webcam and show real-time video shoot by the webcam on user's computer.
####  PreprocessSkeleton folder

1. Input folder is where images need to be preprocessed are placed, remember to delete preprocessOutput folder before running `preprocessSkeleton.py`

2. `preprocessSkeleton.py`, a program that preprocess images stored at input folder, save output preprocessed files as .npz flies, create a folder called preprocessOutput and all the .npz files are stored in the preprocessOutput folder.


## Legal Issue

### Legal Statement
The software is an early proof of concept for development purposes and should not be used as-is in a live environment without further redevelopment and/or testing. No warranty is given and no real data or personally identifiable data should be stored. Usage and its liabilities are your own.

Our software follows the [AGPLv3](https://www.gnu.org/licenses/agpl-3.0.en.html) license
### Data Privacy Consideration
The data we used in our system are all pictures. The pictures shown when you run the python files in openpose/examples/tutorial_api_python and stored in openpose/examples/media are downloaded when we cloned openpose github repository. Other pictures in COMP0016_2020_21_Team13/testing/integrationTesting/scoring/data are screenshoted from videos in Youtube. All of these data are used only to see if the skeleton finding and skeleton matching algorithms are working correctly. Our game runs a local copy and will not store any user data or images but only process them on runtime.

The pictures shown on our website are screenshoted from the following websites:

https://www.bilibili.com/video/BV1PK4y1Y7jt?t=56&p=2

https://www.youtube.com/watch?v=kbM5aK-M82g&list=RDkbM5aK-M82g&index=1

https://www.youtube.com/watch?v=MOwaUlXZxkI

https://github.com/CMU-Perceptual-Computing-Lab/openpose

https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/00_index.md

The other pictures of graphs on our website are drawn by ourselves.

If you have any problems with the pictures please contact us.

### Software Licences
This project incorporates material from the project(s) listed below.

1. CMU-Perceptual-Computing-Lab/openpose (https://github.com/CMU-Perceptual-Computing-Lab/openpose)

COPYRIGHT: The Software is owned by Licensor and is protected by United States copyright laws and applicable international treaties and/or conventions.

[licence type: SOFTWARE LICENSE AGREEMENT.](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/LICENSE)

2. Tkinter

[licence type: MIT](https://github.com/PacktPublishing/Python-GUI-Programming-with-Tkinter/blob/master/LICENSE).

3. Matplotlib

[licence type: PSF](https://matplotlib.org/stable/users/license.html).

4. Python 3.7.1

[licence type: PSF](https://docs.python.org/3.7/license.html#psf-license-agreement-for-python-release)

5. PIL

[licence type: HPND](https://github.com/python-pillow/Pillow/blob/master/LICENSE).

6. Numpy
   
[licence type: BSD 3-Clause "New" or "Revised" License](https://github.com/numpy/numpy/blob/main/LICENSE.txt).

7. Opencv

[license type: Apache License](https://github.com/opencv/opencv/blob/master/LICENSE).

### Credits
System developed by Zhichen Xu, Jianping Huang, Qianhui Zhang.
Clients and organisations Arthur Murray Dance Studio, Adrian Persad, Shaun Persad.
Supervisors and Teaching Assistants Dr Yun Fu, An Zhao.
University College London

