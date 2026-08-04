# Python EDA & Outlier Detection

This repository contains a Python script that performs **Exploratory Data Analysis (EDA)** on an Excel dataset. The script cleans the data, detects outliers using the **Interquartile Range (IQR)** method, and visualizes the results with a boxplot. 0

## Features

- Load data from an Excel file
- Handle missing values in the `CouponCode` column
- Detect outliers using the IQR method
- Display detected outliers
- Visualize the distribution of `TotalPrice` using a boxplot with highlighted outliers 1

## Requirements

Install the required Python libraries:

```bash
pip install pandas matplotlib seaborn openpyxl
```

## Usage

1. Place the dataset in the project directory.
2. Update the Excel file path if necessary.
3. Run the script:

```bash
python eda_script.py
```

## Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Output

The script:
- Cleans missing data
- Detects and prints outlier records
- Displays a boxplot highlighting outliers 2

## License

This project is available for educational and learning purposes.
