# PredictSolver

A monorepo for machine learning applications and tools focused on predictive modeling and solving complex problems.

## Project Structure

```
predictsolver/
├── core/               # Core ML libraries and utilities
├── apps/               # Applications built with the core libraries
│   ├── sample_app.py   # Sample Python application
│   └── dataapi/        # NestJS-based data API service
├── tools/              # Development and utility tools
└── docs/               # Documentation
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- uv (Python package manager)
- pnpm (Node.js package manager for NestJS applications)
- Node.js 18.0.0 or higher (for NestJS applications)

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
# Run Python sample applications
poe run-sample          # Run classic ML demo
poe run-sample-api      # Run API integration demo

# Run NestJS Data API
poe run-dataapi         # Production mode
poe run-dataapi-dev     # Development mode with hot-reload
```

## Development

### Development Commands with Poe

You can use these Poe commands for your development workflow:

```
# Run tests
poe test                # Run all Python tests
poe test-core           # Run only core library tests
poe test-dataapi        # Run NestJS Data API tests
poe test-dataapi-e2e    # Run NestJS Data API end-to-end tests

# Linting and formatting
poe lint                # Check Python code style with flake8
poe format              # Format Python code using black

# Build
poe build-dataapi       # Build NestJS Data API for production

# Complete quality check
poe check               # Run Python linting and tests
poe check-all           # Run all tests (Python and NestJS)
```

### Data API (NestJS)

The Data API is built using NestJS and provides RESTful endpoints for accessing and manipulating data.

#### Development

```
# Install dependencies
cd apps/dataapi
pnpm install

# Run in development mode with hot-reload
pnpm run start:dev

# Or use Poe from the root directory
poe run-dataapi-dev
```

#### API Endpoints

The API includes the following endpoints (expand as your implementation grows):

- `GET /` - Health check endpoint
- More endpoints will be added as the API is developed

### Adding a New App

1. Create a new directory in the `apps/` folder
2. Use the core libraries by importing from `predictsolver_core`

### Core Library Development

1. Make changes to the core library in `core/predictsolver_core/`
2. Run tests to ensure everything works correctly

## License

MIT
