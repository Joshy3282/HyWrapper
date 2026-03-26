@echo off
setlocal

echo ========================================
echo Running Kotlin Tasks...
echo ========================================
cd kotlin
call gradlew.bat check
if %ERRORLEVEL% neq 0 (
    echo Kotlin check failed!
    exit /b %ERRORLEVEL%
)
call gradlew.bat build
if %ERRORLEVEL% neq 0 (
    echo Kotlin build failed!
    exit /b %ERRORLEVEL%
)
cd ..

echo.
echo ========================================
echo Running Python Tasks...
echo ========================================
cd python
where uv >nul 2>nul
if %ERRORLEVEL% equ 0 (
    echo Running ruff check...
    call uv run --extra dev ruff check .
    if %ERRORLEVEL% neq 0 (
        echo ruff check found errors. Attempting to fix...
        call uv run --extra dev ruff check . --fix
    )
    
    echo Running ruff format check...
    call uv run --extra dev ruff format --check .
    if %ERRORLEVEL% neq 0 (
        echo ruff format check failed. Formatting...
        call uv run --extra dev ruff format .
    )

    echo Running mypy...
    call uv run --extra dev mypy src
    if %ERRORLEVEL% neq 0 (
        echo mypy failed!
        exit /b %ERRORLEVEL%
    )

    echo Running pytest...
    call uv run --extra dev pytest
) else (
    echo Running ruff check...
    call ruff check .
    if %ERRORLEVEL% neq 0 (
        echo ruff check found errors. Attempting to fix...
        call ruff check . --fix
    )
    
    echo Running ruff format check...
    call ruff format --check .
    if %ERRORLEVEL% neq 0 (
        echo ruff format check failed. Formatting...
        call ruff format .
    )

    echo Running mypy...
    call mypy src
    if %ERRORLEVEL% neq 0 (
        echo mypy failed!
        exit /b %ERRORLEVEL%
    )

    echo Running pytest...
    call pytest
)
if %ERRORLEVEL% neq 0 (
    echo Python tests failed!
    exit /b %ERRORLEVEL%
)
cd ..

echo.
echo ========================================
echo Running TypeScript Tasks...
echo ========================================
cd typescript
echo Running lint...
call npm run lint
if %ERRORLEVEL% neq 0 (
    echo TypeScript lint failed!
    exit /b %ERRORLEVEL%
)
echo Running build...
call npm run build
if %ERRORLEVEL% neq 0 (
    echo TypeScript build failed!
    exit /b %ERRORLEVEL%
)
echo Running test...
call npm test
if %ERRORLEVEL% neq 0 (
    echo TypeScript tests failed!
    exit /b %ERRORLEVEL%
)
cd ..

echo.
echo ========================================
echo All tasks completed successfully!
echo ========================================
