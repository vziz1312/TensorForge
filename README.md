# TensorForge

**From tensors to neural networks — learning deep learning from the ground up.**

TensorForge is a hands-on TensorFlow learning project focused on understanding the mathematics, implementation, and training of neural networks using Python.

The project documents my progress through practical experiments, starting with tensor operations and gradually advancing toward model training, evaluation, and deployment.

## Learning Philosophy

Rather than relying on high-level abstractions alone, TensorForge focuses on understanding how neural networks work internally — from individual neurons and activation functions to gradient-based optimization.

## Learning Roadmap

TensorForge follows a progressive, 12-day learning path:

| Day | Topic | Concepts |
|---|---|---|
| 01 | Tensor Basics | Constants, shapes, data types |
| 02 | Tensor Operations | Addition, multiplication, element-wise operations |
| 03 | Building a Neuron | Weights, biases, `tf.Variable` |
| 04 | Multiple Inputs | Weighted sums, `tf.reduce_sum` |
| 05 | Activation Functions | ReLU and non-linearity |
| 06 | Dense Layers | Keras Dense layers |
| 07 | Loss Functions | Mean Squared Error (MSE) |
| 08 | Gradients | Automatic differentiation, `GradientTape` |
| 09 | Optimization | Stochastic Gradient Descent (SGD) |
| 10 | Model Training | Sequential models, compilation, fitting |
| 11 | Model Evaluation | Training/testing, predictions, generalization |
| 12 | Saving & Loading | Model persistence using the `.keras` format |

Each lesson includes a Python implementation designed to reinforce the underlying concepts through practical experimentation.

## Project Structure

```text
TensorForge/
├── data/                   # Dataset storage
├── models/                 # Saved TensorFlow models
├── notebooks/              # Jupyter notebooks and experiments
├── src/                    # Daily Python implementations
│   ├── 01_tensors.py
│   ├── 02_tensors_operations.py
│   ├── 03_neuron.py
│   ├── 04_multiple_inputs.py
│   ├── 05_relu.py
│   ├── 06_dense_layer.py
│   ├── 07_loss.py
│   ├── 08_gradients.py
│   ├── 09_optimizer.py
│   ├── 10_training.py
│   ├── 11_evaluation.py
│   └── 12_save_load.py
├── .gitignore
├── README.md
└── requirements.txt
```

The `src/` directory contains the practical implementations, while `models/` stores trained models and `data/` is reserved for datasets.

## Installation

### Requirements

- Python 3.13
- TensorFlow 2.21.0
- pip

### 1. Clone the repository

```bash
git clone https://github.com/vziz1312/TensorForge.git
cd TensorForge
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows (CMD):**

```cmd
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify TensorFlow installation

```python
import tensorflow as tf

print(tf.__version__)
```

Expected version:

```text
2.21.0
```

## Running the Lessons

All practical implementations are located in the `src/` directory.

Activate your virtual environment, navigate to `src/`, and run the lesson you want:

```cmd
cd src
python 01_tensors.py
```

For example, to run the model saving and loading experiment:

```cmd
python 12_save_load.py
```

Each script is independent and focuses on a specific TensorFlow concept.

## Technologies

- **Python** — Main programming language
- **TensorFlow** — Deep learning framework
- **Keras** — Neural network API
- **NumPy** — Numerical computing

## Project Status

<badge color="success">12 lessons completed</badge>

The foundational learning phase is complete. The next stage will focus on more advanced neural network architectures, practical datasets, and football-related machine learning applications.