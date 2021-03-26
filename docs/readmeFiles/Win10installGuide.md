# Installation Guide For Win10

- [Installation Guide For Win10](#installation-guide-for-win10)
  * [Create parent directory](#create-parent-directory)
  * [Clone team 13 repository under danceGame directory](#clone-team-13-repository-under-dancegame-directory)
  * [Install OpenPose](#install-openpose)
    + [Clone openpose repository under danceGame directory](#clone-openpose-repository-under-dancegame-directory)
    + [Prerequisites](#prerequisites)
    + [Cmake Configuration](#cmake-configuration)
  * [Run Openpose](#run-openpose)
  * [Run the Game](#run-the-game)


##   Create parent directory
Create directory at desired location, name it "danceGame"

    mkdir danceGame
##   Clone team 13 repository under danceGame directory

    cd danceGame

    git clone https://github.com/UCLComputerScience/COMP0016_2020_21_Team13
##  Install OpenPose
[Official installation instructions:](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
Tools:

Python version 3.7

Visual Studio 2019 Community

CMake 3.20.0

###  Clone openpose repository under danceGame directory

    git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose

###  Prerequisites
[Openpose Official Prerequisites](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/1_prerequisites.md)

[Install CMake GUI 3.20.0](https://cmake.org/download/)

![Download All Models that are Circled](../imagesForREADME/Win10InstallImg/caffe.png)

Clone pybind11 in the openpose/3rdparty directory mentioned above.

    cd openpose/3rdparty
    git clone https://github.com/pybind/pybind11
###  Cmake Configuration

![Verify the location of installation.](../imagesForREADME/Win10InstallImg/cmakePath.png)

Press configure, use Visual Studio 16 2019 as generator.

![Correct Settings](../imagesForREADME/Win10InstallImg/VSsetting.png)

Click on build python and cpu only for cpu mode:

![BUILD_PYTHON](../imagesForREADME/Win10InstallImg/buildPython.png)

![GPU_MODE](../imagesForREADME/Win10InstallImg/CPU_MODE.png)

Press "Configure" and then "Generate"

##  Run Openpose

Check OpenPose was properly installed by running any demo example: 01_body_from_image.py.

Open terminal, navigate to the path tutorial_api_python and then run 01_body_from_image.py. (or run it through visual studio code)

![CMD commands](../imagesForREADME/Win10InstallImg/commandLineCommand.png)

If openpose is properly installed, the following picture will pop out.

![Openpose Results](../imagesForREADME/Win10InstallImg/output.png)

##  Run the Game

    cd danceGame/COMP0016_2020_21_Team13/
    
    python3 gameInterface/mainGUI.py
Expected Output:

![Graphical User Interface](../imagesForREADME/Win10InstallImg/output2.png)