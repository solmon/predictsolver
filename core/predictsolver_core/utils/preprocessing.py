import numpy as np
import pandas as pd
from typing import Union, List, Dict, Any, Optional

def preprocess_data(data: Union[np.ndarray, pd.DataFrame],
                    normalize: bool = True,
                    fill_na: bool = True) -> Union[np.ndarray, pd.DataFrame]:
    """
    Preprocesses input data for model training or inference.
    
    Args:
        data: Input data as numpy array or pandas DataFrame
        normalize: Whether to normalize the data
        fill_na: Whether to fill NA values
        
    Returns:
        Preprocessed data
    """
    if isinstance(data, pd.DataFrame):
        # Handle DataFrame
        if fill_na:
            data = data.fillna(data.mean())
        
        if normalize:
            for col in data.select_dtypes(include=[np.number]).columns:
                data[col] = (data[col] - data[col].mean()) / data[col].std()
    else:
        # Handle numpy array
        if fill_na:
            # Replace NaN with column means
            col_means = np.nanmean(data, axis=0)
            inds = np.where(np.isnan(data))
            data[inds] = np.take(col_means, inds[1])
        
        if normalize:
            # Normalize each column
            means = np.mean(data, axis=0)
            stds = np.std(data, axis=0)
            data = (data - means) / stds
            
    return data

def evaluate_model(y_true: np.ndarray, 
                  y_pred: np.ndarray, 
                  metrics: Optional[List[str]] = None) -> Dict[str, float]:
    """
    Evaluate model predictions against ground truth.
    
    Args:
        y_true: Ground truth labels
        y_pred: Model predictions
        metrics: List of metrics to compute
        
    Returns:
        Dictionary of metric names and values
    """
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    
    if metrics is None:
        metrics = ["mse", "mae", "r2"]
    
    results = {}
    
    for metric in metrics:
        if metric.lower() == "mse":
            results["mse"] = mean_squared_error(y_true, y_pred)
        elif metric.lower() == "mae":
            results["mae"] = mean_absolute_error(y_true, y_pred)
        elif metric.lower() == "r2":
            results["r2"] = r2_score(y_true, y_pred)
    
    return results
