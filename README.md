# CSV Data Analyzer

A command-line tool for analyzing CSV data using Python and Pandas.

## Features

* View dataset
* Show top student by average score
* Calculate subject statistics
* Filter students by math score
* Input validation with error handling

## Technologies

* Python
* Pandas

## Project Structure

```
csv-data-analyzer
│
├── csv_analyzer.py
├── students.csv
└── README.md
```
## Example Input

| name | gender | math | english | science |
|-----|-----|-----|-----|-----|
| Alice | F | 85 | 90 | 88 |
| Bob | M | 78 | 75 | 80 |
| Charlie | M | 92 | 85 | 87 |
| Diana | F | 88 | 91 | 90 |
| Evan | M | 70 | 65 | 72 |
| Fiona | F | 95 | 94 | 96 |

## Example Menu

```
=== CSV Data Analyzer ===

1: Show Data
2: Top Student
3: Subject Statistics
4: Filter Student
5: Exit
```

## How to Run

Install pandas

```
pip install pandas
```

Run program

```
python csv_analyzer.py
```
