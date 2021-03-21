# Dance Game Engine
## Installation Guide
### For Mac Users
#####  1. Create parent directory
Create directory at desired location, name it "danceGame"

    mkdir danceGame
####  2. Clone team 13 repository under danceGame directory

    cd danceGame

    git clone https://github.com/UCLComputerScience/COMP0016_2020_21_Team13
#### Install openpose
[Official installation instructions: ](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
##### Clone openpose repository under danceGame directory

    git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
##### Install prerequisites
cd into the openpose folder:

    cd openpose
![Mac Os Prerequisites](docs/imagesForREADME/MacInstallImg/macPre.png)
Note: As for now, cmake has to be installed using brew install --cask cmake
##### Build with Cmake

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

#### 4.Compilation

    cd build/
   (Note: this may be unnecessary if you are still under the same folder as from section 3.3)
   

    make -j`sysctl -n hw.logicalcpu`
   Note: I faced the problem Could NOT find vecLib (missing: vecLib_INCLUDE_DIR), and I had to manually install Caffe.
   ![Manually Install Caffe](docs/imagesForREADME/MacInstallImg/caffe.png)
  #### 5.Running openpose
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
#### Running the game

    cd danceGame/COMP0016_2020_21_Team13/
(parent folder created in section 1)

    python3 gameInterface/mainGUI.py
   Note: make sure any program you run is from the COMP0016_2020_21_Team13 as the working directory.
   The expected output:
   ![The expected output](docs/imagesForREADME/MacInstallImg/output2.png)

### For Windows 10 Users
#### 1. Clone team 13 repositories

    git clone [https://github.com/UCLComputerScience/COMP0016_2020_21_Team13](https://github.com/UCLComputerScience/COMP0016_2020_21_Team13)

(parent directory path should not be too long as windows maximum path length is 256)
#### 2. Install OpenPose
[Official installation instructions:](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
Tools:

Python version 3.7

Visual Studio 2019 Community

CMake 3.20.0
#####  1) Clone OpenPose repository below team 13 github repository

    git clone [https://github.com/CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
![Clone Openpose Repository and team13 github repository](docs/imagesForREADME/Win10InstallImg/preReq.png)

##### 2) Prerequisites
[Openpose Official Prerequisites](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/1_prerequisites.md)

[Install CMake GUI 3.20.0](https://cmake.org/download/)

![Download All Models that are Circled](docs/imagesForREADME/Win10InstallImg/caffe.png)

Clone pybind11 in the openpose/3rdparty directory mentioned above.

    cd openpose/3rdparty
    git clone https://github.com/pybind/pybind11
##### 3) Cmake Configuration

![Verify the location of installation.](docs/imagesForREADME/Win10InstallImg/cmakePath.png)

Press configure, use Visual Studio 16 2019 as generator.

![Correct Settings](docs/imagesForREADME/Win10InstallImg/VSsetting.png)

Click on build python and cpu only for cpu mode:

![BUILD_PYTHON](docs/imagesForREADME/Win10InstallImg/buildPython.png)

![GPU_MODE](docs/imagesForREADME/Win10InstallImg/CPU_MODE.png)

Press "Configure" and then "Generate"

#### 3. Run Openpose

Check OpenPose was properly installed by running any demo example: 01_body_from_image.py.

Open terminal, navigate to the path tutorial_api_python and then run 01_body_from_image.py. (or run it through visual studio code)

![CMD commands](docs/imagesForREADME/Win10InstallImg/commandLineCommand.png)

If openpose is properly installed, the following picture will pop out.

![Openpose Results](docs/imagesForREADME/Win10InstallImg/output.png)

#### 4. Run the Game

    cd danceGame/COMP0016_2020_21_Team13/
    
    python3 gameInterface/mainGUI.py
Expected Output:

![Graphical User Interface](docs/imagesForREADME/Win10InstallImg/output2.png)

## User Maunal
### gameInterface folder
Go to danceGame\COMP0016_2020_21_Team13\gameInterface, users can run the game by double-click the file `mainGUI.py`. Expected output:

![Graphical User Interface](docs/imagesForREADME/gameInterface/startingStage.png)

Start the game by clicking the button "click to start"

![Game Interface and its Components](docs/imagesForREADME/gameInterface/guiDetail.png)

### Testing folder

1. IntegrationTest\scoring. Code folder holds `imageScoringTest.py` which process a list of images and output all the images with their skeleton

2. UnitTest\skeletonRecognition. Code folder holds `skeletonRecognition.py` which processes a list of pairs of images stored in data folder and output all the skeleton in a window when the program finished.

3. UnitTest\webcamTest. Code folder holds `webcamTesting.py` which turns on the webcam and show real-time video shoot by the webcam on user's computer.
###  PreprocessSkeleton folder

1. Input folder is where images need to be preprocessed are placed, remember to delete preprocessOutput folder before running `preprocessSkeleton.py`

2. `preprocessSkeleton.py`, a program that preprocess images stored at input folder, save output preprocessed files as .npz flies, create a folder called preprocessOutput and all the .npz files are stored in the preprocessOutput folder.


