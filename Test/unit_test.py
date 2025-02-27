import unittest
from unittest.mock import patch, MagicMock
import json
import tempfile
import os
from predictor import run_predictions, load_samples, send_batch_predictions, calculate_statistics

class TestPredictor(unittest.TestCase):

    def setUp(self):
        self.test_samples = [
            "Sample input 1",
            "Sample input 2",
            "Sample input 3"
        ]
        self.mock_response = {
            'predictions': [
                {'generated_text': 'Output 1'},
                {'generated_text': 'Output 2'},
                {'generated_text': 'Output 3'}
            ]
        }

    def test_load_samples(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write('\n'.join(self.test_samples))
            temp_file_name = temp_file.name

        loaded_samples = load_samples(temp_file_name)
        self.assertEqual(loaded_samples, self.test_samples)

        os.unlink(temp_file_name)

    @patch('predictor.boto3.client')
    def test_send_batch_predictions(self, mock_boto3_client):
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        mock_client.invoke_endpoint.return_value = {'Body': MagicMock(read=lambda: json.dumps(self.mock_response).encode())}

        model_name = 'TestModel'
        result = send_batch_predictions(model_name, self.test_samples)

        self.assertEqual(result, self.mock_response['predictions'])
        mock_client.invoke_endpoint.assert_called_once()

    def test_calculate_statistics(self):
        response_times = [0.5, 1.0, 1.5, 2.0, 2.5]
        stats = calculate_statistics(response_times)

        self.assertAlmostEqual(stats['min'], 0.5)
        self.assertAlmostEqual(stats['max'], 2.5)
        self.assertAlmostEqual(stats['mean'], 1.5)
        self.assertAlmostEqual(stats['median'], 1.5)
        self.assertAlmostEqual(stats['p95'], 2.5)

    @patch('predictor.send_batch_predictions')
    @patch('predictor.load_samples')
    def test_run_predictions(self, mock_load_samples, mock_send_batch_predictions):
        mock_load_samples.return_value = self.test_samples
        mock_send_batch_predictions.return_value = self.mock_response['predictions']

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_output_file:
            output_file_name = temp_output_file.name

        model_name = 'TestModel'
        input_file = 'dummy_input.txt'
        num_samples = 3

        run_predictions(model_name, input_file, num_samples, output_file_name)

        mock_load_samples.assert_called_once_with(input_file)
        mock_send_batch_predictions.assert_called_once_with(model_name, self.test_samples[:num_samples])

        with open(output_file_name, 'r') as f:
            output_data = json.load(f)

        self.assertEqual(len(output_data), num_samples)
        for item in output_data:
            self.assertIn('input', item)
            self.assertIn('output', item)
            self.assertIn('response_time', item)

        os.unlink(output_file_name)

    @patch('predictor.argparse.ArgumentParser.parse_args')
    @patch('predictor.run_predictions')
    def test_main(self, mock_run_predictions, mock_parse_args):
        mock_args = MagicMock()
        mock_args.model_name = 'TestModel'
        mock_args.input_file = 'input.txt'
        mock_args.num_samples = 10
        mock_args.output_file = 'output.json'
        mock_parse_args.return_value = mock_args

        import predictor
        predictor.main()

        mock_run_predictions.assert_called_once_with(
            'TestModel', 'input.txt', 10, 'output.json'
        )

if __name__ == '__main__':
    unittest.main()