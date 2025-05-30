import unittest
import numpy as np
import pandas as pd
import sys
import os

# Add parent directory to path to import core package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../core"))

from predictsolver_core.utils.preprocessing import preprocess_data, evaluate_model


class TestPreprocessing(unittest.TestCase):
    
    def test_preprocess_data_numpy(self):
        """Test preprocessing with numpy arrays"""
        # Create test data with NaN values
        data = np.array([[1.0, 2.0], [np.nan, 4.0], [5.0, 6.0]])
        result = preprocess_data(data)
        
        # Check if NaN values are filled
        self.assertFalse(np.isnan(result).any())
        
    def test_preprocess_data_pandas(self):
        """Test preprocessing with pandas DataFrames"""
        # Create test DataFrame with NaN values
        df = pd.DataFrame({
            'feature1': [1.0, np.nan, 3.0],
            'feature2': [4.0, 5.0, 6.0]
        })
        result = preprocess_data(df)
        
        # Check if NaN values are filled
        self.assertFalse(result.isna().any().any())
        
    def test_evaluate_model(self):
        """Test model evaluation metrics"""
        y_true = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
        y_pred = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
        
        metrics = evaluate_model(y_true, y_pred)
        
        # Check if all metrics are calculated
        self.assertIn('mse', metrics)
        self.assertIn('mae', metrics)
        self.assertIn('r2', metrics)
        
        # Check if metrics have reasonable values
        self.assertLess(metrics['mse'], 0.1)  # Should be small for good predictions
        self.assertLess(metrics['mae'], 0.2)  # Should be small for good predictions
        self.assertGreater(metrics['r2'], 0.9)  # Should be close to 1 for good predictions


if __name__ == '__main__':
    unittest.main()
