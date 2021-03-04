# **P2 - Advanced Lane Finding** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/COVER.png)

### 1. Camera Calibration
 
The camera calibration is done by traversing and finding corners in all the chessboard pictures in the folder */camera_cal*, then calculating the average correction matrix and distortion coefficients with the *cv2.calibrateCamera* function. **Figure 1** shows an example undistorted and warped chessboard image. 

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/warped_chessboard.jpg)
<p align="center">
  <b>Figure 1.</b> Example undistorted & warped chessboard. 
</p>

### 2. 
