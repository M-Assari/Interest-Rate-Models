
# Interest Rate Models (Vasicek & Ho-Lee)

## Overview
This project implements and calibrates the **Vasicek** and **Ho-Lee** interest rate models using real market data. It includes:
- **Monte Carlo Simulation** of interest rate paths.
- **Calibration** using historical interest rate data.
- **Unit Testing** to ensure model correctness.

## Project Structure
```
Interest-Rate-Models/
├── models.py          # Vasicek & Ho-Lee models
├── calibration.py     # Model calibration functions
├── notebook.ipynb     # Main Jupyter Notebook
├── tests.py           # Unit tests
├── data/              # Folder for storing market data
│   ├── spots-monthly.csv
├── README.md          # Documentation
├── requirements.txt   # Dependencies
```

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Interest-Rate-Models
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
### Running the Jupyter Notebook
```bash
jupyter notebook notebook.ipynb
```

### Running Unit Tests
```bash
python -m unittest tests.py
```

## Models Implemented
### Vasicek Model
$$
d r_t = a (b - r_t) dt + \sigma dW_t
$$
- Mean-reverting stochastic process.

### Ho-Lee Model
$$
d r_t = \theta dt + \sigma dW_t
$$
- No mean reversion, pure Brownian motion.

## License
MIT License
