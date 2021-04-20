#include "FusionEKF.h"
#include <iostream>
#include "Eigen/Dense"
#include "tools.h"

using Eigen::MatrixXd;
using Eigen::VectorXd;
using std::cout;
using std::endl;
using std::vector;

/**
 * Constructor.
 */
FusionEKF::FusionEKF() {
  is_initialized_ = false;

  previous_timestamp_ = 0;

  // Initializing matrices
  R_laser_ = MatrixXd(2, 2);
  R_radar_ = MatrixXd(3, 3);
  H_laser_ = MatrixXd(2, 4);
  Hj_ = MatrixXd(3, 4);

  // Measurement covariance matrix - laser
  R_laser_ << 0.0225, 0,
              0, 0.0225;

  // Measurement covariance matrix - radar
  R_radar_ << 0.09, 0, 0,
              0, 0.0009, 0,
              0, 0, 0.09;

  /**
   * DONE: Finish initializing the FusionEKF. 
   * DONE: Set the process and measurement noises. 
   */

  // Observation matrix H of laser
  H_laser_ << 1, 0, 0, 0, 
              0, 1, 0, 0;

  // Initializing state transition matrix
  ekf_.F_ = MatrixXd(4, 4);
  ekf_.F_ << 1, 0, 1, 0, 
             0, 1, 0, 1,
             0, 0, 1, 0,
             0, 0, 0, 1;

  // Initializing state estimation covariance matrix P
  ekf_.P_ = MatrixXd(4, 4);
  ekf_.P_ << 1, 0, 0, 0, 
             0, 1, 0, 0,
             0, 0, 1000, 0, 
             0, 0, 0, 1000;
  
  // Process noise variances
  noise_ax = 9;
  noise_ay = 9; 
  
  // Success
  cout << "[F-0] - Initializing FEKF done!\n";
}

/**
 * Destructor.
 */
FusionEKF::~FusionEKF() {}

void FusionEKF::ProcessMeasurement(const MeasurementPackage &measurement_pack) {
  /**
   * Initialization
   */
  if (!is_initialized_) {
    /**
     * DONE: Initialize the state ekf_.x_ with the first measurement.
     * DONE: Create the covariance matrix.
     */

    // First measurement
    cout << "EKF: " << endl;
    ekf_.x_ = VectorXd(4);
    ekf_.x_ << 1, 1, 1, 1;

    if (measurement_pack.sensor_type_ == MeasurementPackage::RADAR) {

      // DONE: Convert radar data from polar to cartesian coordinates and initialize state.
      float rho = measurement_pack.raw_measurements_[0];
      float theta = measurement_pack.raw_measurements_[1];
      float rho_dot = measurement_pack.raw_measurements_[2];
      
      ekf_.x_(0) = rho * cos(theta);
      ekf_.x_(1) = rho * sin(theta);
    }

    else if (measurement_pack.sensor_type_ == MeasurementPackage::LASER) {
      // TODO: Initialize laser state.
      float px = measurement_pack.raw_measurements_[0];
      float py = measurement_pack.raw_measurements_[1];

      ekf_.x_(0) = px;
      ekf_.x_(1) = py;
    }

    // Get first timestamp
    previous_timestamp_ = measurement_pack.timestamp_;

    // Done initializing, no need to predict or update
    is_initialized_ = true;

    // Success
    cout << "[F-1] Init 1st measurement done!\n";
    return;
  }

  /**
   * Prediction
   */

  /**
   * DONE: Update the state transition matrix F according to the new elapsed time. Time is measured in seconds (/10^6).
   * DONE: Update the process noise covariance matrix.
   */

  // Compute dt and update previous timestamp
  float dt = (measurement_pack.timestamp_ - previous_timestamp_) / 1000000.0;
  previous_timestamp_ = measurement_pack.timestamp_;

  // Compute for later use
  float dt_2 = dt * dt;
  float dt_3 = dt_2 * dt;
  float dt_4 = dt_3 * dt; 

  // Update state-transition matrix F (dp < constant velocity > dt)
  ekf_.F_(0, 2) = dt;
  ekf_.F_(1, 3) = dt;

  // Process covariance matrix Q
  ekf_.Q_ = MatrixXd(4, 4);
  ekf_.Q_ << dt_4/4*noise_ax, 0, dt_3/2*noise_ax, 0, 
             0, dt_4/4*noise_ay, 0, dt_3/2*noise_ay, 
             dt_3/2*noise_ax, 0, dt_2*noise_ax, 0, 
             0, dt_3/2*noise_ay, 0, dt_2*noise_ay;

  // Prediction
  ekf_.Predict();

  // Success
  cout << "[F-2] Prediction done!\n";

  /**
   * Update
   */

  /**
   * DONE:
   * - Use the sensor type to perform the update step.
   * - Update the state and covariance matrices.
   */

  if (measurement_pack.sensor_type_ == MeasurementPackage::RADAR) {

    // Calculate Jacobian 
    Hj_ = tools.CalculateJacobian(ekf_.x_);

    // Radar update
    ekf_.H_ = Hj_;
    ekf_.R_ = R_radar_;
    ekf_.UpdateEKF(measurement_pack.raw_measurements_);

   // Success
    cout << "[F-3.1] RADAR update done!\n";
  } else {

    // Laser updates
    ekf_.H_ = H_laser_;
    ekf_.R_ = R_laser_;

    ekf_.Update(measurement_pack.raw_measurements_);
    
    // Success
    cout << "[F-3.2] LiDAR update done!\n";
  }

  // print the output
  cout << "x_ = " << ekf_.x_ << endl;
  cout << "P_ = " << ekf_.P_ << endl;
}
