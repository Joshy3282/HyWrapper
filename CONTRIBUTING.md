# Contributing to HyWrapper

## How to Contribute

1.  **Fork the Repository**: Start by forking the [HyWrapper repository](https://github.com/Joshy3282/HyWrapper).
2.  **Create a Branch**: Create a new branch for your feature or bug fix.
3.  **Make Your Changes**: Implement your changes and ensure you follow the project's coding standards.
4.  **Run Tests**: Verify your changes by running the existing tests.
5.  **Submit a Pull Request**: Submit a pull request with a clear description of your changes.

## Development Setup

### Python

We use `uv` for dependency management and `ruff` for linting and formatting.

```bash
cd python
uv sync
uv run ruff check .
uv run pytest
```

### TypeScript

We use `npm` for dependency management and `eslint` for linting.

```bash
cd typescript
npm install
npm run lint
npm run test
```

### Kotlin

We use Gradle for building and testing the Kotlin SDK.

```bash
cd kotlin
./gradlew build
./gradlew test
```

## Community

Join our community for any questions or discussions related to HyWrapper.

- [Issues](https://github.com/Joshy3282/HyWrapper/issues)
- [Discussions](https://github.com/Joshy3282/HyWrapper/discussions)
- [Discord](https://discord.com/invite/serenity-843473054423318568)
