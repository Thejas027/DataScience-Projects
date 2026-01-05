# Student Performance Analysis

A data analysis project that explores student performance metrics across multiple subjects and identifies key factors influencing academic success.

## 📋 Project Overview

This project analyzes student performance data to uncover patterns and insights related to academic achievement. It examines how various factors such as gender, parental education level, and test preparation courses affect student scores across math, reading, and writing.

## 📁 Project Structure

```
Student-Performance-Analysis/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── data/
│   └── StudentsPerformance.csv       # Student performance dataset
└── src/
    └── student_analysis.py            # Main analysis script
```

## 📊 Dataset

**File**: `data/StudentsPerformance.csv`

The dataset contains student performance information with the following features:
- **Gender**: Student gender
- **Math Score**: Mathematics performance score
- **Reading Score**: Reading comprehension score
- **Writing Score**: Writing ability score
- **Parental Level of Education**: Highest education level achieved by parents
- **Test Preparation Course**: Whether the student completed test preparation

## 🔧 Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn

## 📦 Installation

1. Clone or download this repository:
```bash
cd Student-Performance-Analysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the analysis script from the project root directory:

```bash
python src/student_analysis.py
```

The script will:
1. Load the student performance dataset
2. Clean and preprocess the data (remove duplicates, handle missing values)
3. Calculate aggregate metrics (total score, average score)
4. Generate descriptive statistics
5. Perform group-wise analysis (by gender, test prep, parental education)
6. Display visualization charts
7. Print key insights

## 📈 Analysis Components

### Data Cleaning
- Detection and removal of duplicate records
- Identification of missing values
- Column renaming for clarity

### Feature Engineering
- **Total Score**: Sum of math, reading, and writing scores
- **Average Score**: Mean of the three subject scores

### Statistical Analysis
- Descriptive statistics for all subjects
- Mean scores by demographic groups:
  - By gender
  - By test preparation completion
  - By parental education level

### Visualizations
- **Histogram**: Distribution of math scores
- **Bar Plot**: Average performance comparison by gender
- **Box Plot**: Impact of test preparation on overall performance

## 💡 Key Insights

1. **Test Preparation Impact**: Students who completed the test preparation course achieved higher average scores
2. **Subject Distribution**: Reading scores tend to be higher than math scores on average
3. **Parental Education Correlation**: Strong positive relationship between parental education level and student performance
4. **Gender Equity**: Performance differences between genders are relatively minimal

## 📝 Output

When executed, the script produces:
- Console output with statistical summaries
- Three visualization plots (histogram, bar plot, box plot)
- Insights about student performance patterns

## 🛠️ Technologies Used

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization

## 📄 Notes

- Plots are configured to display using the TkAgg backend for compatibility with VS Code
- All file paths are handled robustly to work from any working directory
- The dataset is expected to be in CSV format with specific column names

## 👨‍💻 Author

Created as part of a data science analysis project.

## 📝 License

This project is provided as-is for educational and analytical purposes.

---

**Last Updated**: January 2026
