"""
My First Cybersecurity Data Analysis Script
==========================================

What this script does:
- Reads vulnerability data from a CSV file
- Shows basic information about the data
- Displays the first few records

Learning Goals for Day 1:
- Understand how to read CSV files with Python
- See what vulnerability data looks like
- Get comfortable with basic pandas operations

Author: Sugumar Srinivasan
Date: 16-August-2025
Learning Day: 1 of 30
"""

import pandas as pd
import os

def main():
    """Main function that runs our vulnerability analysis"""
    
    print("=== My First Vulnerability Data Analysis ===")
    print("Learning Day 1: Reading and Understanding Data\n")
    
    # Step 1: Check if our data file exists
    data_file = 'data/vulnerabilities.csv'
    
    if not os.path.exists(data_file):
        print(f"❌ Data file not found: {data_file}")
        print("Make sure you have created the data/vulnerabilities.csv file")
        return
    
    try:
        # Step 2: Read the vulnerability data
        print("📖 Reading vulnerability data...")
        vulnerabilities = pd.read_csv(data_file)
        
        # Step 3: Show basic information
        print(f"✅ Successfully loaded {len(vulnerabilities)} vulnerability records")
        print(f"📊 Data has {vulnerabilities.shape[1]} columns")
        
        # Step 4: Show what columns we have
        print(f"\n📋 Column names:")
        for i, column in enumerate(vulnerabilities.columns, 1):
            print(f"   {i}. {column}")
        
        # Step 5: Show first few records
        print(f"\n🔍 First 3 vulnerability records:")
        print("-" * 60)
        print(vulnerabilities.head(3).to_string(index=False))
        
        # Step 6: Basic analysis - count by severity
        if 'Severity' in vulnerabilities.columns:
            print(f"\n📈 Vulnerability Count by Severity:")
            severity_counts = vulnerabilities['Severity'].value_counts()
            for severity, count in severity_counts.items():
                print(f"   {severity}: {count} vulnerabilities")
        
        # Step 7: Save today's learning
        save_learning_summary(vulnerabilities)
        
        print(f"\n🎉 Day 1 Complete! You just analyzed {len(vulnerabilities)} vulnerabilities!")
        print("Next: Tomorrow we'll learn to filter and find specific issues")
        
    except Exception as error:
        print(f"❌ Something went wrong: {error}")
        print("Don't worry! This is normal when learning. Let's fix it together.")

def save_learning_summary(data):
    """Save what we learned today to a file"""
    
    summary = f"""
# Day 1 Learning Summary
Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}
Script: step1_read_data.py

## What I Accomplished Today:
✅ Successfully read vulnerability data from CSV file
✅ Learned basic pandas operations (read_csv, head, shape, columns)
✅ Understood vulnerability data structure
✅ Created my first data analysis script

## Data Summary:
- Total vulnerabilities analyzed: {len(data)}
- Number of columns: {data.shape[1]}
- Columns: {', '.join(data.columns)}

## Key Learning:
- pandas.read_csv() is used to load CSV files
- .shape tells us rows and columns (rows, columns)
- .head() shows first few records
- .columns gives us column names
- .value_counts() counts occurrences of each value

## Tomorrow's Goals:
- Learn to filter data for specific criteria
- Find only "High" and "Critical" vulnerabilities
- Count vulnerabilities per asset

## Challenges Faced:
[Write any problems you encountered and how you solved them]

## Code Skills Gained:
- File reading with pandas
- Basic data exploration
- Error handling with try/except
- Function creation
"""
    
    # Create learning directory if it doesn't exist
    if not os.path.exists('learning'):
        os.makedirs('learning')
    
    # Save the summary
    with open('learning/day01_summary.md', 'w') as f:
        f.write(summary)
    
    print("📝 Learning summary saved to learning/day01_summary.md")

if __name__ == "__main__":
    main()