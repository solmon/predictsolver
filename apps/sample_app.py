import argparse
import sys
import os
import numpy as np
import pandas as pd

# Add parent directory to path to import core package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../core"))

from predictsolver_core.models.base import BaseModel
from predictsolver_core.utils.preprocessing import preprocess_data, evaluate_model

def main():
    parser = argparse.ArgumentParser(description='PredictSolver Sample App')
    parser.add_argument('--data', type=str, help='Path to input data')
    parser.add_argument('--output', type=str, help='Path to output predictions')
    
    args = parser.parse_args()
    
    print("PredictSolver Sample App")
    print("========================")
    
    # Generate some dummy data if no input is provided
    if args.data:
        try:
            data = pd.read_csv(args.data)
            print(f"Loaded data from {args.data}")
        except Exception as e:
            print(f"Error loading data: {e}")
            data = pd.DataFrame(np.random.randn(100, 5), columns=['feature1', 'feature2', 'feature3', 'feature4', 'target'])
    else:
        print("No data provided, using random data")
        data = pd.DataFrame(np.random.randn(100, 5), columns=['feature1', 'feature2', 'feature3', 'feature4', 'target'])
    
    # Preprocess data
    X = data[['feature1', 'feature2', 'feature3', 'feature4']]
    y = data['target']
    
    X_processed = preprocess_data(X)
    
    # Create a dummy model for demonstration
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X_processed, y)
    
    # Make predictions
    y_pred = model.predict(X_processed)
    
    # Evaluate
    metrics = evaluate_model(y.values, y_pred)
    for metric, value in metrics.items():
        print(f"{metric.upper()}: {value:.4f}")
    
    # Save predictions if output path provided
    if args.output:
        output_df = pd.DataFrame({'true': y, 'predicted': y_pred})
        output_df.to_csv(args.output, index=False)
        print(f"Predictions saved to {args.output}")

if __name__ == "__main__":
    main()
