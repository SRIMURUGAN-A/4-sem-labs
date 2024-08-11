import pandas as pd

# Load the dataset from the CSV file
file_path = 'example_data.csv'  # Replace with your actual CSV file path
data = pd.read_csv(file_path)

# Display the first few rows of the data
print(data.head())

# Import necessary libraries
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, adjusted_rand_score
import matplotlib.pyplot as plt
import seaborn as sns

# Extract features
X = data.values

# Apply k-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# Apply EM algorithm (Gaussian Mixture Models) clustering
gmm = GaussianMixture(n_components=3, random_state=42)
gmm_labels = gmm.fit_predict(X)

# Evaluate the clustering performance
kmeans_silhouette = silhouette_score(X, kmeans_labels)
gmm_silhouette = silhouette_score(X, gmm_labels)

kmeans_ari = adjusted_rand_score(kmeans_labels, gmm_labels)

print(f'k-Means Silhouette Score: {kmeans_silhouette:.2f}')
print(f'EM (GMM) Silhouette Score: {gmm_silhouette:.2f}')
print(f'Adjusted Rand Index between k-Means and EM (GMM): {kmeans_ari:.2f}')

# Visualize the clustering results
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=kmeans_labels, palette='viridis', legend=None)
plt.title('k-Means Clustering')

plt.subplot(1, 2, 2)
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=gmm_labels, palette='viridis', legend=None)
plt.title('EM (GMM) Clustering')

plt.show()
