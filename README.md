# Can You Trust This Number?

A simple sensor-data regression example that generates synthetic sensor measurements, trains a linear regression model, and evaluates it on held-out test data.

## Project Structure

- `data/`
  - `data_generator.py` - generates synthetic sensor data and saves it to `data/raw/sensor_data.csv`
  - `raw/sensor_data.csv` - generated training dataset
  - `raw/sensor_testdata.csv` - test dataset used by `src/test.py`
- `models/`
  - `model1.pkl` - saved trained linear regression model
- `src/`
  - `train.py` - trains a linear regression model using the generated data and saves it to `models/model1.pkl`
  - `test.py` - evaluates the saved model on test data and prints MSE and R² score

## Dependencies

This project uses:

- Python 3.8+ (or compatible)
- pandas
- numpy
- scikit-learn
- joblib

Install dependencies with pip:

```bash
pip install pandas numpy scikit-learn joblib
```

## Usage

Generate training data:

```bash
python data/data_generator.py
```

Train the model:

```bash
python src/train.py
```

Evaluate the model:

```bash
python src/test.py
```

## Notes

- The synthetic dataset includes sensor readings and a target `True_Temperature` value.
- `src/train.py` trains a linear regression model on the generated data.
- `src/test.py` loads the saved model and evaluates it using mean squared error and R² score.
