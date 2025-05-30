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

#### Method 1: Using Poe (Recommended)

1. Clone the repository:
   ```
   git clone https://github.com/solmon/predictsolver.git
   cd predictsolver
   ```

2. Install poethepoet if you don't have it:
   ```
   uv pip install poethepoet
   ```

3. Setup the environment and install all dependencies in one step:
   ```
   poe setup-all
   ```

#### Method 2: Manual Setup

1. Clone the repository:
   ```
   git clone https://github.com/solmon/predictsolver.git
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
# Using Poe
poe run-sample

# Or directly with Python
python apps/sample_app.py
```

## Development

### Development Commands with Poe

You can use these Poe commands for your development workflow:

```
# Run tests
poe test           # Run all tests
poe test-core      # Run only core library tests

# Linting and formatting
poe lint           # Check code style with flake8
poe format         # Format code using black

# Complete quality check
poe check          # Run both linting and tests
```

### Adding a New App

1. Create a new directory in the `apps/` folder
2. Use the core libraries by importing from `predictsolver_core`

### Core Library Development

1. Make changes to the core library in `core/predictsolver_core/`
2. Run tests to ensure everything works correctly

## License

MIT
