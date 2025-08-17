# Day 2 - Filtering Vulnerability Data for Security Priorities
# File: scripts/step2_filter_data.py

"""
Day 2: Learning Data Filtering for Cybersecurity
===============================================

What this script does:
- Filters vulnerability data by severity levels
- Finds critical security issues that need immediate attention
- Identifies assets with the most vulnerabilities
- Creates focused reports for security teams

Learning Goals for Day 2:
- Master pandas filtering with conditions
- Understand boolean indexing
- Learn to prioritize security issues
- Create actionable security insights

Building on Day 1:
- Yesterday: Read data and explore structure
- Today: Filter and prioritize for action

Author: [Your Name]
Date: [Today's Date]  
Learning Day: 2 of 30
"""

import pandas as pd
import os
from datetime import datetime

def main():
    """Main function for Day 2 vulnerability filtering analysis"""
    
    print("=== Day 2: Security Priority Analysis ===")
    print("Building on Day 1: Now filtering for action!\n")
    
    # Load the data (using what we learned Day 1)
    data_file = 'data/vulnerabilities.csv'
    
    if not os.path.exists(data_file):
        print(f"❌ Data file not found: {data_file}")
        print("Make sure you completed Day 1 setup first!")
        return
    
    try:
        # Step 1: Load vulnerability data
        print("📖 Loading vulnerability data...")
        df = pd.read_csv(data_file)
        print(f"✅ Loaded {len(df)} total vulnerability records\n")
        
        # Step 2: Filter for CRITICAL vulnerabilities (most urgent)
        print("🚨 CRITICAL VULNERABILITIES (Fix Immediately!):")
        print("-" * 50)
        critical_vulns = df[df['Severity'] == 'Critical']
        
        if len(critical_vulns) > 0:
            for idx, vuln in critical_vulns.iterrows():
                print(f"• {vuln['Asset_Name']}: {vuln['Vulnerability_Name']}")
                print(f"  CVE: {vuln['CVE_ID']} | Status: {vuln['Status']}")
                print()
        else:
            print("✅ No critical vulnerabilities found!")
        
        print(f"Total Critical: {len(critical_vulns)} vulnerabilities\n")
        
        # Step 3: Filter for HIGH vulnerabilities (next priority)
        print("⚠️  HIGH SEVERITY VULNERABILITIES (Fix This Week):")
        print("-" * 50)
        high_vulns = df[df['Severity'] == 'High']
        
        for idx, vuln in high_vulns.iterrows():
            print(f"• {vuln['Asset_Name']}: {vuln['Vulnerability_Name'][:50]}...")
        
        print(f"Total High: {len(high_vulns)} vulnerabilities\n")
        
        # Step 4: Find assets with multiple vulnerabilities (risk hotspots)
        print("🎯 RISK HOTSPOTS (Assets with Most Vulnerabilities):")
        print("-" * 50)
        asset_counts = df['Asset_Name'].value_counts()
        
        for asset, count in asset_counts.head(5).items():
            print(f"• {asset}: {count} vulnerabilities")
            # Show what types of issues this asset has
            asset_vulns = df[df['Asset_Name'] == asset]
            severities = asset_vulns['Severity'].value_counts()
            severity_summary = []
            for severity, cnt in severities.items():
                severity_summary.append(f"{cnt} {severity}")
            print(f"  └─ {', '.join(severity_summary)}")
        print()
        
        # Step 5: Filter for OPEN (unpatched) vulnerabilities
        print("🔓 OPEN VULNERABILITIES (Still Vulnerable):")
        print("-" * 50)
        open_vulns = df[df['Status'] == 'Open']
        severity_breakdown = open_vulns['Severity'].value_counts()
        
        for severity, count in severity_breakdown.items():
            print(f"• {severity}: {count} open vulnerabilities")
        
        print(f"Total Open: {len(open_vulns)} out of {len(df)} total\n")
        
        # Step 6: Filter by date - recent discoveries (last 7 days simulation)
        print("📅 RECENTLY DISCOVERED (Newest Threats):")
        print("-" * 50)
        # Convert date strings to datetime for comparison
        df['Found_Date'] = pd.to_datetime(df['Found_Date'])
        df_sorted = df.sort_values('Found_Date', ascending=False)
        
        print("Most recent 3 vulnerabilities:")
        recent_vulns = df_sorted.head(3)
        for idx, vuln in recent_vulns.iterrows():
            print(f"• {vuln['Found_Date'].strftime('%Y-%m-%d')}: {vuln['Asset_Name']}")
            print(f"  {vuln['Vulnerability_Name']} ({vuln['Severity']})")
        print()
        
        # Step 7: Create a security action plan
        create_action_plan(df, critical_vulns, high_vulns, open_vulns)
        
        # Step 8: Save today's analysis
        save_filtered_results(critical_vulns, high_vulns, asset_counts)
        save_learning_summary(df, critical_vulns, high_vulns, open_vulns)
        
        print("🎉 Day 2 Complete! You've learned data filtering and security prioritization!")
        print("Next: Tomorrow we'll count and group data for trend analysis")
        
    except Exception as error:
        print(f"❌ Error occurred: {error}")
        print("This is part of learning! Let's debug this together.")

def create_action_plan(df, critical_vulns, high_vulns, open_vulns):
    """Create a prioritized action plan for security team"""
    
    print("📋 SECURITY ACTION PLAN:")
    print("=" * 50)
    
    # Priority 1: Critical and Open
    critical_open = critical_vulns[critical_vulns['Status'] == 'Open']
    if len(critical_open) > 0:
        print(f"🚨 PRIORITY 1: Fix {len(critical_open)} critical open vulnerabilities IMMEDIATELY")
        print("   Estimated time: 1-2 days")
    
    # Priority 2: High severity and Open  
    high_open = high_vulns[high_vulns['Status'] == 'Open']
    if len(high_open) > 0:
        print(f"⚠️  PRIORITY 2: Address {len(high_open)} high severity open vulnerabilities")
        print("   Estimated time: 1 week")
    
    # Priority 3: Medium severity
    medium_vulns = df[(df['Severity'] == 'Medium') & (df['Status'] == 'Open')]
    if len(medium_vulns) > 0:
        print(f"📝 PRIORITY 3: Plan remediation for {len(medium_vulns)} medium severity issues")
        print("   Estimated time: 2-4 weeks")
    
    print()

def save_filtered_results(critical_vulns, high_vulns, asset_counts):
    """Save filtered results to files for security team"""
    
    # Create reports directory
    if not os.path.exists('reports'):
        os.makedirs('reports')
    
    # Save critical vulnerabilities report
    if len(critical_vulns) > 0:
        critical_vulns.to_csv('reports/critical_vulnerabilities.csv', index=False)
        print("📊 Saved critical vulnerabilities to reports/critical_vulnerabilities.csv")
    
    # Save high severity report
    if len(high_vulns) > 0:
        high_vulns.to_csv('reports/high_severity_vulnerabilities.csv', index=False)
        print("📊 Saved high severity vulnerabilities to reports/high_severity_vulnerabilities.csv")
    
    # Save asset risk summary
    asset_summary = pd.DataFrame({
        'Asset_Name': asset_counts.index,
        'Total_Vulnerabilities': asset_counts.values
    })
    asset_summary.to_csv('reports/asset_risk_summary.csv', index=False)
    print("📊 Saved asset risk summary to reports/asset_risk_summary.csv")

def save_learning_summary(df, critical_vulns, high_vulns, open_vulns):
    """Document what we learned today"""
    
    summary = f"""
# Day 2 Learning Summary
Date: {datetime.now().strftime('%Y-%m-%d')}
Script: step2_filter_data.py

## What I Accomplished Today:
✅ Learned pandas data filtering with boolean conditions
✅ Filtered vulnerabilities by severity levels (Critical, High, Medium, Low)
✅ Identified risk hotspots (assets with most vulnerabilities)
✅ Filtered by status (Open vs Patched vulnerabilities) 
✅ Sorted by date to find recent discoveries
✅ Created actionable security priority reports

## Data Analysis Results:
- Total vulnerabilities processed: {len(df)}
- Critical vulnerabilities found: {len(critical_vulns)}
- High severity vulnerabilities: {len(high_vulns)}
- Open (unpatched) vulnerabilities: {len(open_vulns)}
- Assets analyzed: {df['Asset_Name'].nunique()}

## Key Technical Skills Learned:
- **Boolean filtering**: `df[df['Severity'] == 'Critical']`
- **Multiple conditions**: `df[(condition1) & (condition2)]`
- **Value counting**: `df['column'].value_counts()`
- **Date handling**: `pd.to_datetime()` and sorting
- **Data export**: `df.to_csv()` for reports

## Cybersecurity Insights Gained:
- How to prioritize vulnerability remediation by severity
- Identifying asset risk hotspots for focused attention  
- Importance of tracking open vs patched status
- Creating actionable reports for security teams

## Code Patterns Mastered:
```python
# Basic filtering
critical = df[df['Severity'] == 'Critical']

# Multiple conditions with AND
critical_open = df[(df['Severity'] == 'Critical') & (df['Status'] == 'Open')]

# Counting and ranking
asset_counts = df['Asset_Name'].value_counts()

# Date sorting
df_sorted = df.sort_values('Found_Date', ascending=False)
```

## Business Value Created:
- Automated identification of critical security risks
- Priority-based action plans for security teams
- Asset-focused risk assessment capabilities
- Exportable reports for management and compliance

## Tomorrow's Goals:
- Learn data grouping and aggregation
- Calculate vulnerability trends over time
- Create summary statistics by asset type
- Build automated dashboard-style reports

## Challenges Overcome:
- Understanding boolean indexing syntax with parentheses
- Working with date data types in pandas
- Creating multiple filtered views of the same dataset
- Organizing output for maximum clarity

## Real-World Applications:
This type of analysis is exactly what cybersecurity teams need daily:
- SOC analysts prioritizing incident response
- Vulnerability management teams planning patches
- Risk assessment for compliance reporting
- Asset owners understanding their security posture
"""
    
    with open('learning/day02_summary.md', 'w') as f:
        f.write(summary)
    
    print("📝 Learning summary saved to learning/day02_summary.md")

if __name__ == "__main__":
    main()