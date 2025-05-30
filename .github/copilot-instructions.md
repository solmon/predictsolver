<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# PredictSolver Project Guide

This is a Python monorepo for machine learning applications organized as follows:

- `core/`: Contains the core ML libraries and utilities in the `predictsolver_core` package
- `apps/`: Contains applications built using the core libraries
- `tools/`: Contains development and utility tools
- `docs/`: Contains documentation

## Development Guidelines

### Code Style

- Follow PEP 8 style guidelines
- Use type hints for all function parameters and return types
- Document all public functions, classes, and methods with docstrings

### ML Code Patterns

- All models should inherit from the `BaseModel` class in `core/predictsolver_core/models/base.py`
- Use the preprocessing utilities in `core/predictsolver_core/utils/preprocessing.py` for data preparation
- Follow scikit-learn compatible API patterns (fit, predict, transform)

### Common Dependencies

- PyTorch for deep learning
- scikit-learn for machine learning algorithms
- pandas for data manipulation
- numpy for numerical computing
