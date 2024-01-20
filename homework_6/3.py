import seaborn as sns
import matplotlib.pyplot as plt

# Load Seaborn example dataset (replace 'tips' with your preferred dataset)
data = sns.load_dataset('tips')

# Scatter Plot
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
sns.scatterplot(x='total_bill', y='tip', data=data)
plt.title('Scatter Plot')

# Histogram
plt.subplot(1, 3, 2)
sns.histplot(data['total_bill'], bins=30)
plt.title('Histogram')

# Box Plot
plt.subplot(1, 3, 3)
sns.boxplot(x='day', y='total_bill', data=data)
plt.title('Box Plot')

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
