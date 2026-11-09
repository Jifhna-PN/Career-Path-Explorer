
# Career Path Explorer

A skill-based career exploration application built using Python and Streamlit. It helps users explore different career paths by comparing their existing technical skills with the skills required for various careers.

The application identifies matching skills, highlights skills that need improvement, calculates career match percentages, and generates a structured learning roadmap based on skill levels.

## Project Overview

Career Path Explorer allows users to understand how their current technical skills align with different career opportunities.

Users can select the skills they already know and explore suitable career paths based on the available dataset. The application also identifies missing skills and organizes them into a learning roadmap.

## Features

- **Skill Selection:** Select existing technical skills through an interactive sidebar.
- **Career Match Analysis:** Compare existing skills against the requirements of different career paths.
- **Skill Match Percentage:** Calculate the percentage of matching skills for each career.
- **Career Comparison:** View career match percentages and skill details in a comparison table.
- **Visual Analysis:** Explore career matches through a bar chart.
- **Skill Gap Identification:** Identify skills already known and skills that need to be learned.
- **Learning Roadmap:** Generate an ordered learning roadmap based on Beginner, Intermediate, and Advanced skill levels.
- **Summary Metrics:** View total selected skills, available career paths, average match, and highest career match.

## Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib

## Project Structure

```text
Career-Path-Explorer/
│
├── src/
│   └── app.py
├── data/
│   └── career_skills.csv
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Career-Path-Explorer.git
```

### 2. Navigate to the Project Directory

```bash
cd Career-Path-Explorer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser.

## How It Works

1. Select the technical skills you already know from the sidebar.
2. The application compares your selected skills with the skills associated with each career.
3. View the career match percentages and compare different career paths.
4. Select a career to explore its required skills.
5. Identify your matching skills and the skills you need to learn.
6. Follow the generated learning roadmap, organized according to skill levels.

## Dataset

The application uses a CSV dataset named `career_skills.csv`, stored inside the `data` directory.

The dataset contains the following fields:

- **Career:** Career path or job role.
- **Skill:** Technical skill associated with the career.
- **Category:** Skill category.
- **Level:** Required skill level (Beginner, Intermediate, or Advanced).

## Career Match Calculation

The career match percentage is calculated based on the number of selected skills that match the required skills for a career.

**Formula:**

Career Match (%) = (Matched Skills / Total Required Skills) × 100

The learning roadmap is generated using the missing skills and their corresponding skill levels.

## Future Enhancements

- Add more career paths and technical skills.
- Include learning resources for individual skills.
- Introduce personalized career recommendations.
- Add progress tracking for completed learning roadmap steps.

## Author

**Jifhna P N**

MCA Graduate | AI & Machine Learning Enthusiast

---

Built with Python, Streamlit, Pandas and Matplotlib.
