import numpy as np
from sklearn.cluster import KMeans


def k_means_quantize(data, n_clusters):

    data = np.array(data).reshape(-1, 1)

    kmeans = KMeans(n_clusters=n_clusters).fit(data)

    # Get the centroids
    centroids = kmeans.cluster_centers_

    # Quantise the data using the centroids
    quantized_data = kmeans.predict(data)

    # Convert the quantized data back to the original shape
    quantized_data = quantized_data.reshape(data.shape)

    return quantized_data, centroids
