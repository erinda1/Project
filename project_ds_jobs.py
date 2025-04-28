# Data Science Salaries Visualization Project

# Import necessary libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the visual style
sns.set(style="whitegrid")

# Load the dataset
file_path = 'ds_salaries.csv'  # Make sure the CSV is in the same folder or update the path
df = pd.read_csv(file_path)

# -------------------------------
# 1. Salary Trend Over Years (Line Chart)
# -------------------------------
plt.figure(figsize=(8,5))
avg_salary_per_year = df.groupby('work_year')['salary_in_usd'].mean().reset_index()
sns.lineplot(data=avg_salary_per_year, x='work_year', y='salary_in_usd', marker='o')
plt.title('Average Salary Over Years')
plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')
plt.grid(True)
plt.show()

# -------------------------------
# 2. Top 5 Job Titles by Average Salary (Bar Chart)
# -------------------------------
plt.figure(figsize=(10,6))
top_jobs = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette='viridis')
plt.title('Top 5 Job Titles by Average Salary')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Job Title')
plt.show()

# -------------------------------
# 3. Salary Distribution by Company Size (Box Plot)
# -------------------------------
plt.figure(figsize=(8,5))
sns.boxplot(data=df, x='company_size', y='salary_in_usd', palette='Set2')
plt.title('Salary Distribution by Company Size')
plt.xlabel('Company Size (S=Small, M=Medium, L=Large)')
plt.ylabel('Salary (USD)')
plt.grid(True)
plt.show()

# -------------------------------
# 4. Countries Offering Most Jobs (Bar Chart)
# -------------------------------
plt.figure(figsize=(10,6))
jobs_by_country = df['company_location'].value_counts().head(10)
sns.barplot(x=jobs_by_country.values, y=jobs_by_country.index, palette='mako')
plt.title('Top 10 Countries Offering Most Data Science Jobs')
plt.xlabel('Number of Jobs')
plt.ylabel('Country')
plt.show()

# -------------------------------
# 5. Most Popular Job Titles in the US (Bar Chart)
# -------------------------------
plt.figure(figsize=(10,6))
us_jobs = df[df['company_location'] == 'US']
us_job_counts = us_jobs['job_title'].value_counts().head(10)
sns.barplot(x=us_job_counts.values, y=us_job_counts.index, palette='coolwarm')
plt.title('Most Popular Data Science Job Titles in the US')
plt.xlabel('Number of Jobs')
plt.ylabel('Job Title')
plt.show()
