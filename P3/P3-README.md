# **P3 - TRAFFIC SIGN RECOGNITION** 

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

![cover](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/COVER.png)

## I. The Pipline
[Video Output **HERE**](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/ALF_Output.mp4)
### 1. Camera Calibration
 
The camera calibration is done by traversing and finding corners in all the chessboard pictures in the folder */camera_cal*, then calculating the average correction matrix and distortion coefficients with the *cv2.calibrateCamera* function. **Figure 1** shows an example undistorted and warped chessboard image. **Figure 2** shows an example of distortion-corrected road image. 

![f1](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/warped_chessboard.jpg)
<p align="center">
  <b>Figure 1.</b> Example undistorted & warped chessboard. 
</p>

![f2](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/undistorted_straight_lines1.jpg)
<p align="center">
  <b>Figure 2.</b> Example undistorted & warped road image. 
</p>

### 2. Creating Binary Thresholded Image
Three thresholds were used in the *Binary_Threshold* function to generate the binary image for lane finding: a Sobel operator (x-gradient), an S-channel threshold (HLS color space) and a R-channel threshold (RGB color space). **Figure 3** shows an example binary-thresholded road image. The parameters for calibration were used for video processing later. 

![f3](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/binary_thresholded.png)
<p align="center">
  <b>Figure 3.</b> Example binary thresholded image. 
</p>

### 3. Perspective Transform
The images were then warped by *cv2.warpPerspective* function in the *P2_Main* function (video pipeline), with pre-defined src and dst point sets, which were used in *cv2.getPerspectiveTransform* to calculate the transform matrix. **Figure 4** shows an example warped road image. 

![f4](https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/binary_warped.jpg)
<p align="center">
  <b>Figure 4.</b> Example binary warped road image. 
</p>

### 4. Identifying Lane Pixels & Fitting Polynomial
In the *Lane_Processings* function two approaches were implemented for lane lines identification. If there is no prior detected fit then the sliding window method would be used to find lane pixels and fit the polynomial with the pixels found (functions: *Fit_Polynomial* and *Find_Lane_Pixels*, **Figure 5. a)**). If there exists a fit detected in previous frames, the *Search_Around_Prior* method will be used to find fit quicker (**Figure 5. b)**). 

<p align="center">
 <img src="https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/FL1.png"/)><img src="https://github.com/MatKal/SDND-PROJECTS/blob/main/P2/output/FL2.png"/>
</p>

<p align="center">
  <b>Figure 5. a)</b> Sliding window for finding lane pixels. <b>b) </b> Search around prior. 
</p>

### 5. Measure Curvature
In the function *Calculate_Curvature* the radiuses of left- and right-fit, as well as the distance between the car camera and lane center were calculated with the formula below, and the conversion parameters *x(y)m_per_pixel*. Then in the video pipeline the average radius is calculated and displayed with center_distance on the frame (up-left in the cover image). 

![l1](https://wikimedia.org/api/rest_v1/media/math/render/svg/020f434a4747b066c2ccc80bfb30f14b72e98976)

## II. Discussion
### 1. Robustness of Binary Thresholding
Although the thresholding worked well for the standard project video after tunning, it failed on the challenge videos, and vice-versa. Other color-spaces, e.g., LAB and YCrCb, could be explored to find a more robust threshold combination for the solution, in order to reduce the impact of the enviromental conditions such as lighting, contrast (different pavements and medians). 

### 2. The Curvature Radius
The curvature radius calculated during runtime is around 2000~5000 on the curve road, which is not close to the given number (about 1km). Possible cause could be in the camera calibration and perspective transformation process because different radiuses were given out when using different calibration image sets and different src-dst point sets. 

### 3. The Sanity Check
In the implementation a threshold for *Line.diffs* was used to do the sanity check to check if the new fit has a similar shape with the previous ones (if not, the latest valid lane would be returned). According to observation, the sanity check was sensitive to the result of binary thresholding. If there are too many frames that have failed in the sanity check, the accuracy of lane detection would be compromised until sufficient good frames have come. This also requires the accuracy and robustness of the binary thresholding. 
