global youtube statistics  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv(r"C:\Users\ananditha\OneDrive\Desktop\cleaned_data.xls",encoding='latin1')
import matplotlib.pyplot as plt
import pandas as pd

# Dummy data for YouTube global statistics
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
views = [1000, 1500, 2000, 1800, 2500]
subscribers = [500, 600, 700, 650, 800]

# Create a DataFrame
df = pd.DataFrame({'Month': months, 'Views': views, 'Subscribers': subscribers})

# Plotting
plt.figure(figsize=(10, 5))

# Plot views
plt.plot(df['Month'], df['Views'], marker='o', label='Views')

# Plot subscribers
plt.plot(df['Month'], df['Subscribers'], marker='s', label='Subscribers')

# Add title and labels
plt.title('YouTube Global Statistics')
plt.xlabel('Month')
plt.ylabel('Count')
plt.legend()

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show plot
plt.grid(True)
plt.tight_layout()
plt.show()


 Top 10 youtubers 
import matplotlib.pyplot as plt
import pandas as pd

# Dummy data for top 10 YouTubers and their views
youtubers = ['PewDiePie', 'T-Series', 'Cocomelon - Nursery Rhymes', 'SET India', 'WWE',
             'Like Nastya', 'Kids Diana Show', 'Zee Music Company', '5-Minute Crafts', 'Vlad and Niki']
views = [7.2e10, 1.89e11, 5.18e10, 4.94e10, 3.84e10,
         7.89e10, 4.34e10, 5.65e10, 7.13e10, 2.33e10]

# Create a DataFrame
df = pd.DataFrame({'YouTuber': youtubers, 'Views': views})

# Sort DataFrame by views in descending order
df = df.sort_values(by='Views', ascending=False)

# Plotting
plt.figure(figsize=(10, 6))

# Create histogram
plt.bar(df['YouTuber'], df['Views'], color='skyblue')

# Add title and labels
plt.title('Top 10 YouTubers by Views')
plt.xlabel('YouTuber')
plt.ylabel('Views (in billions)')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show plot
plt.tight_layout()
plt.show()

Views Distribution for Last 30 Days
import matplotlib.pyplot as plt

# Dummy data for views distribution for the last 30 days
categories = ['Category A', 'Category B', 'Category C', 'Category D']
views = [25000, 30000, 20000, 15000]  # Example views for the last 30 days

# Plotting
plt.figure(figsize=(8, 8))

# Create pie chart
plt.pie(views, labels=categories, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Views Distribution for Last 30 Days')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show plot
plt.show()

Highest Views on YouTube by Country
import matplotlib.pyplot as plt

# Dummy data for highest views in each country
countries = ['USA', 'India', 'Brazil', 'Russia', 'Japan']
highest_views = [2.3e11, 1.5e11, 8.7e10, 6.5e10, 4.9e10]  # Example views in billions

# Plotting
plt.figure(figsize=(10, 6))

# Create scatter plot
plt.scatter(countries, highest_views, color='red', marker='o')

# Add title and labels
plt.title('Highest Views on YouTube by Country')
plt.xlabel('Country')
plt.ylabel('Views (in billions)')

# Add text labels for each point
for i, txt in enumerate(highest_views):
    plt.annotate(f'{int(txt/1e9)}B', (countries[i], highest_views[i]), textcoords="offset points", xytext=(0,10), ha='center')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Show plot
plt.tight_layout()
plt.grid(True)
plt.show()





