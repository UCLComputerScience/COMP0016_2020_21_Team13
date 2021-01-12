#important note: this is a modified version of the original getModels.sh, specifically to work with UCL CS COMP0016 Team13's project. 
#See https://github.com/CMU-Perceptual-Computing-Lab/openpose






# ------------------------- BODY, FOOT, FACE, AND HAND MODELS -------------------------
# Downloading body pose (COCO and MPI), face and hand models
OPENPOSE_URL="http://posefs1.perception.cs.cmu.edu/OpenPose/models/"
POSE_FOLDER="pose/"

# ------------------------- POSE (BODY+FOOT) MODELS -------------------------

# Body (MPI)
MPI_FOLDER=${POSE_FOLDER}"mpi/"
MPI_MODEL=${MPI_FOLDER}"pose_iter_160000.caffemodel"
wget -c ${OPENPOSE_URL}${MPI_MODEL} -P ${MPI_FOLDER}
