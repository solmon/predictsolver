"""
API Connector module for exposing ML functionality to web services.
This module provides functions that can be called from the NestJS data API.
"""
import json
from typing import Dict, Any, List, Optional

from ..models.base import BaseModel


def get_model_info() -> Dict[str, Any]:
    """
    Return information about the available models.
    Used by the NestJS API to expose model metadata.
    
    Returns:
        Dict[str, Any]: Information about the available models
    """
    return {
        "models": [
            {
                "id": "linear_regression",
                "name": "Linear Regression",
                "type": "regression",
                "description": "Standard linear regression model"
            },
            {
                "id": "random_forest",
                "name": "Random Forest",
                "type": "classification",
                "description": "Random forest classifier for multiclass problems"
            }
        ],
        "version": "0.1.0"
    }


def predict_sample(model_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Make a prediction using the specified model.
    
    Args:
        model_id: The ID of the model to use
        data: The input data for prediction
        
    Returns:
        Dict[str, Any]: The prediction results
    """
    # This is a mock implementation
    if model_id == "linear_regression":
        return {
            "prediction": data.get("x", 0) * 2.5 + 10,
            "model_id": model_id
        }
    elif model_id == "random_forest":
        features = data.get("features", [])
        if not features:
            return {"error": "No features provided"}
        
        # Mock classification based on first feature
        if sum(features) > 10:
            class_id = 2
            class_name = "high"
        elif sum(features) > 5:
            class_id = 1
            class_name = "medium"
        else:
            class_id = 0
            class_name = "low"
            
        return {
            "prediction": class_id,
            "class_name": class_name,
            "model_id": model_id
        }
    else:
        return {"error": f"Model '{model_id}' not found"}


def to_json_file(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a JSON file, which can be read by the NestJS API.
    
    Args:
        data: The data to save
        file_path: The path to the output file
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def from_json_file(file_path: str) -> Dict[str, Any]:
    """
    Read data from a JSON file written by the NestJS API.
    
    Args:
        file_path: The path to the input file
        
    Returns:
        Dict[str, Any]: The parsed data
    """
    with open(file_path, 'r') as f:
        return json.load(f)
