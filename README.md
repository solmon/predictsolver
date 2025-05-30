# PredictSolver

A monorepo for machine learning applications and tools focused on predictive modeling and solving complex problems.

## Project Structure

```
predictsolver/
├── core/               # Core ML libraries and utilities
├── apps/               # Applications built with the core libraries
├── tools/              # Development and utility tools
└── docs/               # Documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- uv (Python package manager)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/predictsolver.git
   cd predictsolver
   ```

2. Create and activate the virtual environment:
   ```
   uv venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```
   uv pip install -r requirements.txt
   ```

4. Install the core package in development mode:
   ```
   cd core
   uv pip install -e .
   cd ..
   ```

### Sample Application

Run the sample application:

```
python apps/sample_app.py
```

## Development

### Adding a New App

1. Create a new directory in the `apps/` folder
2. Use the core libraries by importing from `predictsolver_core`

### Core Library Development

1. Make changes to the core library in `core/predictsolver_core/`
2. Run tests to ensure everything works correctly

## License

MIT
