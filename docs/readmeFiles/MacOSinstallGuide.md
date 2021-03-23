# Installation Guide For MacOS

- [Installation Guide For MacOS](#installation-guide-for-macos)
  * [Create parent directory](#create-parent-directory)
  * [Clone team 13 repository under danceGame directory](#clone-team-13-repository-under-dancegame-directory)
  * [Install openpose](#install-openpose)
    + [Clone openpose repository under danceGame directory](#clone-openpose-repository-under-dancegame-directory)
    + [Install prerequisites](#install-prerequisites)
    + [Build with Cmake](#build-with-cmake)
    + [Compilation](#compilation)
    + [Running openpose](#running-openpose)
- [Running the game](#running-the-game)

##   Create parent directory
Create directory at desired location, name it "danceGame"

    mkdir danceGame
##   Clone team 13 repository under danceGame directory

    cd danceGame

    git clone https://github.com/UCLComputerScience/COMP0016_2020_21_Team13
##  Install openpose
[Official installation instructions: ](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation/0_index.md)
###  Clone openpose repository under danceGame directory

    git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose
###  Install prerequisites
cd into the openpose folder:

    cd openpose
![Mac Os Prerequisites](../imagesForREADME/MacInstallImg/macPre.png)
Note: As for now, cmake has to be installed using brew install --cask cmake
###  Build with Cmake

    cd {openpose_folder}
   (Note: this may be unnecessary if you are still under the same folder as from section 3.2)
   

    mkdir build/

    cd build/
    
    cmake-gui ..
   Verify the location of installation.

   ![Location of Installation](../imagesForREADME/MacInstallImg/installLoc.png)

   Press configure, use Xcode as generator.

   ![Use Xcode as generator](../imagesForREADME/MacInstallImg/generator.png)

   Enable BUILD_PYTHON and configure again.

   ![Choose BUILD_PYTHON](../imagesForREADME/MacInstallImg/build_python.png)




   Set GPU_MODE and configure again.

   ![Choose CPU_ONLY](../imagesForREADME/MacInstallImg/GPU_MODE.png)

   If Configuring done appears, then press Generate.

   ![Press Generate](../imagesForREADME/MacInstallImg/generate.png)

   Generating done will appear below, and you can close CMake.

   ![Generating Done](../imagesForREADME/MacInstallImg/generatingDone.png)

###  Compilation

    cd build/
   (Note: this may be unnecessary if you are still under the same folder as from section 3.3)
   

    make -j`sysctl -n hw.logicalcpu`
   Note: I faced the problem Could NOT find vecLib (missing: vecLib_INCLUDE_DIR), and I had to manually install Caffe.
   ![Manually Install Caffe](../imagesForREADME/MacInstallImg/caffe.png)
###  Running openpose
  Running the openpose executable:
  

      
    cd openpose/
    ./build/examples/openpose/openpose.bin --image_dir examples/media/
   

   [Running the python tutorials](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/03_python_api.md)

    cd openpose/build/examples/tutorial_api_python

    python3 01_body_from_image.py
Note: I notice that cmake has problem finding python that are installed by brew, and running python3 01_body_from_image.py will result in an error:

![Error When Running 01_body_from_image.py](../imagesForREADME/MacInstallImg/error.png)

Adding the following lines in CmakeLists.txt(directly under the openpose folder) will solve the problem:

    set(Python_ADDITIONAL_VERSIONS 3.9)
    
    find_package(PythonLibs 3 REQUIRED)
![Add the following lines to CmakeLists.txt](../imagesForREADME/MacInstallImg/lines.png)

The expected output:

![Expected Output](../imagesForREADME/MacInstallImg/output.png)
# Running the game

    cd danceGame/COMP0016_2020_21_Team13/
(parent folder created in section 1)

    python3 gameInterface/mainGUI.py
   Note: make sure any program you run is from the COMP0016_2020_21_Team13 as the working directory.
   The expected output:
   ![The expected output](../imagesForREADME/MacInstallImg/output2.png)