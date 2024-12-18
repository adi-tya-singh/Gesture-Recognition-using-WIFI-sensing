Here's a shorter version of the README file based on your provided details:

---

# Gesture Recognition using Wi-Fi Sensing

This project implements **Gesture Recognition** using **Wi-Fi CSI (Channel State Information)** data to recognize various hand gestures.

[GitHub Repository](https://github.com/adi-tya-singh/Gesture-Recognition-using-WIFI-sensing)

---

## Prerequisites

- Python 3.6+
- Required libraries: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `tensorflow`/`keras`

Install dependencies with:

```bash
pip install -r requirements.txt
```

---

## Dataset

The dataset contains **CSI data** captured from Wi-Fi routers for hand gestures. The repository includes:
- **Sample CSV files** with labeled gestures.
- **Preprocessed HTLTF amplitude and phase data**.

---

## Setup and Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/adi-tya-singh/Gesture-Recognition-using-WIFI-sensing
cd Gesture-Recognition-using-WIFI-sensing
```

2. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

3. **CSI Data**: Ensure your CSI data is in the correct format.

---

## Usage

Run the main script to start gesture recognition:

```bash
python main.py
```

This will load the CSI data, preprocess it, and train the model.

---

## Model Training and Evaluation

1. **Preprocess Data**: Use the `preprocess_data.py` script.
2. **Train Model**: Train the model using `train_model.py`.
3. **Evaluate Model**: Evaluate performance with `evaluate_model.py`.

---

## Visualization

The repository includes scripts for visualizing data and model results.

---


