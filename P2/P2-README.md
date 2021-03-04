# **P2 - ADVANCED LANE FINDING** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/COVER.png)

## I. The Pipline
### 1. Camera Calibration
 
The camera calibration is done by traversing and finding corners in all the chessboard pictures in the folder */camera_cal*, then calculating the average correction matrix and distortion coefficients with the *cv2.calibrateCamera* function. **Figure 1** shows an example undistorted and warped chessboard image. **Figure 2** shows an example of distortion-corrected road image. 

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/warped_chessboard.jpg)
<p align="center">
  <b>Figure 1.</b> Example undistorted & warped chessboard. 
</p>

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/undistorted_straight_lines1.jpg)
<p align="center">
  <b>Figure 2.</b> Example undistorted & warped road image. 
</p>

### 2. Creating Binary Thresholded Image
Three thresholds were used in the *Binary_Threshold* function to generate the binary image for lane finding: a Sobel operator (x-gradient), an S-channel threshold (HLS color space) and a R-channel threshold (RGB color space). **Figure 3** shows an example binary-thresholded road image.

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/binary_thresholded.png)
<p align="center">
  <b>Figure 3.</b> Example binary thresholded image. 
</p>

### 3. Perspective Transform
The images were then warped by *cv2.warpPerspective* function in the *P2_Main* function (video pipeline), with pre-defined src and dst point sets, which were used in *cv2.getPerspectiveTransform* to calculate the transform matrix. **Figure 4** shows an example warped road image. 

![alt text](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/binary_warped.jpg)
<p align="center">
  <b>Figure 4.</b> Example binary warped road image. 
</p>

### 4. Identifying Lane Pixels & Fitting Polynomial
In the *Lane_Processings* function

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/COVER.png">
    <source src="https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/ALF_Output.mp4" type="video/mp4">
  </video>
</figure>

## II. Discussion
