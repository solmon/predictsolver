import argparse
import sys
import os
import numpy as np
import pandas as pd
import json

# Add parent directory to path to import core package
sys.path.append(os.path.join(os.path.dirname(__file__), "../../core"))

from predictsolver_core.models.base import BaseModel
from predictsolver_core.utils.preprocessing import preprocess_data, evaluate_model
from predictsolver_core.api import get_model_info, predict_sample

def show_model_info():
    """Display available model information"""
    info = get_model_info()
    print("\nAvailable Models:")
    print("-" * 50)
    for model in info["models"]:
        print(f"Model: {model['name']} (ID: {model['id']})")
        print(f"Type: {model['type']}")
        print(f"Description: {model['description']}")
        print("-" * 50)
    print(f"API Version: {info['version']}\n")


def run_prediction_demo():
    """Run prediction demonstrations for available models"""
    # Regression model example
    print("\nRunning Linear Regression prediction:")
    result = predict_sample("linear_regression", {"x": 5})
    print(f"Input: x=5")
    print(f"Prediction: {result['prediction']}")
    
    # Classification model example
    print("\nRunning Random Forest classification:")
    result = predict_sample("random_forest", {"features": [2, 3, 5]})
    print(f"Input features: [2, 3, 5]")
    print(f"Predicted class: {result.get('class_name')} (class_id: {result['prediction']})")


def main():
    parser = argparse.ArgumentParser(description='PredictSolver Sample App')
    parser.add_argument('--data', type=str, help='Path to input data')
    parser.add_argument('--output', type=str, help='Path to output predictions')
    parser.add_argument('--mode', type=str, default='classic', choices=['classic', 'api'],
                        help='Run mode: classic (sklearn demo) or api (NestJS API demo)')
    
    args = parser.parse_args()
    
    print("\n" + "=" * 60)
    print("PredictSolver Sample App".center(60))
    print("=" * 60)
    
    if args.mode == 'api':
        # Run the API demo mode
        show_model_info()
        run_prediction_demo()
    else:
        # Run the classic sklearn demo mode
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
    
    print("\n" + "=" * 60)
    print("End of demonstration".center(60))
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
