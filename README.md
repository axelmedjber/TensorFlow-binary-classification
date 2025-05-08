
# Binary Classification AI Model

This project implements a binary classification model using TensorFlow/Keras with a simple neural network architecture. The model is trained on randomly generated data and visualizes the training progress.

## Code Overview

The code in `main.py` performs the following operations:

### Environment Setup
- Suppresses TensorFlow logging messages
- Configures matplotlib for a headless environment
- Imports necessary libraries (TensorFlow, NumPy, Matplotlib, Scikit-learn)

### Data Generation
- Creates synthetic data with 1000 samples and 30 features
- Generates binary labels (0 or 1)
- Splits data into training and testing sets
- Applies standard scaling to normalize the features

### Model Architecture
- Sequential model with three Dense layers:
  - Input layer: 64 neurons, ReLU activation
  - Hidden layer: 32 neurons, ReLU activation
  - Output layer: 1 neuron, Sigmoid activation
- Compiled with:
  - Binary crossentropy loss
  - Adam optimizer (learning rate: 0.001)
  - Accuracy metric

### Training
- Trains for 20 epochs
- Uses batch size of 32
- 10% validation split
- Training is done silently (verbose=0)

### Visualization
- Creates two subplots showing:
  1. Training and validation loss
  2. Training and validation accuracy
- Saves the plots as 'model_training_plots.png'

### Evaluation
- Evaluates model performance on the test set
- Prints the final test accuracy

## Output
The code generates:
- A trained neural network model
- Training visualization plots saved as 'model_training_plots.png'
- Final test accuracy measurement

## Dependencies
- TensorFlow
- NumPy
- Matplotlib
- Scikit-learn
