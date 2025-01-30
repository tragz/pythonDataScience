import unittest

from Quantization.K_Quantization import k_means_quantize


class TestQuantization(unittest.TestCase):

    def test_k_means_quantization(self):
        data = [ 1,3,5, 7, 9]
        n_cluster = 2
        quantized_data, centroids = k_means_quantize(data, n_cluster)
        print("Test Case : 1")
        print("Data \n", data)
        print("Quantized data \n", quantized_data)
        print("Centroids \n", centroids)

        data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        n_clusters = 3
        quantized_data, centroids = k_means_quantize(data, n_cluster)
        print("Test Case : 2")
        print("Data \n", data)
        print("Quantized data \n", quantized_data)
        print("Centroids \n", centroids)

        data = [-10, -5, 0, 5, 10]
        n_clusters = 3
        quantized_data, centroids = k_means_quantize(data, n_cluster)
        print("Test Case : 3")
        print("Data \n", data)
        print("Quantized data \n", quantized_data)
        print("Centroids \n", centroids)
