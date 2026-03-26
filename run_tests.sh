#!/bin/bash

set -e

echo "========================================"
echo "Running Kotlin Tasks..."
echo "========================================"
cd kotlin
chmod +x gradlew
./gradlew check
./gradlew build
cd ..

echo -e "\n========================================"
echo "Running Python Tasks..."
echo "========================================"
cd python
if command -v uv &> /dev/null; then
    echo "Running ruff check..."
    uv run --extra dev ruff check . || {
        echo "ruff check found errors. Attempting to fix..."
        uv run --extra dev ruff check . --fix
    }

    echo "Running ruff format check..."
    uv run --extra dev ruff format --check . || {
        echo "ruff format check failed. Formatting..."
        uv run --extra dev ruff format .
    }

    echo "Running mypy..."
    uv run --extra dev mypy src

    echo "Running pytest..."
    uv run --extra dev pytest
else
    echo "Running ruff check..."
    ruff check . || {
        echo "ruff check found errors. Attempting to fix..."
        ruff check . --fix
    }

    echo "Running ruff format check..."
    ruff format --check . || {
        echo "ruff format check failed. Formatting..."
        ruff format .
    }

    echo "Running mypy..."
    mypy src

    echo "Running pytest..."
    pytest
fi
cd ..

echo -e "\n========================================"
echo "Running TypeScript Tasks..."
echo "========================================"
cd typescript
echo "Running lint..."
npm run lint
echo "Running build..."
npm run build
echo "Running test..."
npm test
cd ..

echo -e "\n========================================"
echo "All tasks completed successfully!"
echo "========================================"
