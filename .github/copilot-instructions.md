# GitHub Copilot Instructions for Strix

This document provides context and guidelines for GitHub Copilot when working with the Strix codebase.

## Project Overview

Strix is an autonomous AI-powered security testing framework that acts like real hackers - running code dynamically, finding vulnerabilities, and validating them through actual proof-of-concepts. It's built for developers and security teams who need fast, accurate security testing without the overhead of manual pentesting.

## Technology Stack

- **Language**: Python 3.12+
- **Dependency Management**: Poetry
- **AI/LLM**: LiteLLM (supports OpenAI, Anthropic, GitHub Copilot, and other providers)
- **Web Framework**: FastAPI
- **Browser Automation**: Playwright
- **Testing**: pytest with pytest-asyncio, pytest-cov
- **Type Checking**: mypy, pyright
- **Linting**: ruff, pylint, bandit
- **Formatting**: ruff (replaces black + isort)
- **Container Runtime**: Docker

## Code Style Guidelines

### General Python Style
- Follow PEP 8 with a **100-character line limit**
- Use **type hints** for all function signatures
- Write **docstrings** for all public methods (Google/NumPy style)
- Keep functions focused and small
- Use meaningful, descriptive variable names
- Prefer explicit over implicit

### Type Checking
- The project uses **strict type checking** with mypy and pyright
- All function parameters and return types must be annotated
- Use `typing` module generics: `List`, `Dict`, `Optional`, `Union`, etc.
- Avoid using `Any` unless absolutely necessary

### Imports
- Use absolute imports from the `strix` package
- Group imports in order: stdlib, third-party, local
- Use `from typing import` for type hints
- Organize imports automatically with ruff

### Async/Await
- The codebase uses asyncio extensively
- Use `async def` for I/O-bound operations
- Properly await all async functions
- Use `pytest-asyncio` for async tests

### Error Handling
- Use specific exception types, not bare `except:`
- Log errors with appropriate context
- Use `tenacity` for retry logic where appropriate
- Avoid swallowing exceptions silently

## Project Structure

```
strix/
├── agents/         # AI agent implementations
├── interface/      # CLI and UI components (Textual)
├── llm/           # LLM provider integrations
├── prompts/       # Jinja templates for agent prompts
├── runtime/       # Execution runtime and sandboxing
├── telemetry/     # Monitoring and metrics
└── tools/         # Security testing tools (proxy, browser, etc.)
```

## Key Concepts

### Agents
- Agents are autonomous AI entities that perform security testing
- Located in `strix/agents/`
- Each agent has specialized capabilities and tools
- Agents can collaborate in teams for complex tasks

### Prompts
- Stored as Jinja2 templates in `strix/prompts/`
- Categories: vulnerabilities, frameworks, technologies
- Provide structured knowledge for agents
- Include examples, validation methods, and payloads

### Tools
- Security testing capabilities provided to agents
- Examples: HTTP proxy, browser automation, terminal, Python runtime
- Located in `strix/tools/`
- Designed to be composable and reusable

### Runtime
- Sandbox environment for running untrusted code
- Docker-based isolation
- Manages agent execution and resources

## Testing

- Write tests using `pytest`
- Place tests in a `tests/` directory (create if needed)
- Use fixtures for common setup
- Mock external dependencies (LLM calls, network requests)
- Aim for 80%+ code coverage
- Test both success and failure cases

Example test structure:
```python
import pytest
from strix.module import function_to_test

@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_function_behavior(sample_data):
    result = function_to_test(sample_data)
    assert result is not None
    assert result["key"] == "expected_value"
```

## Common Patterns

### LLM Integration
```python
from litellm import acompletion

async def call_llm(prompt: str, model: str = "gpt-4") -> str:
    response = await acompletion(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

### Tool Implementation
```python
from typing import Any, Dict

class SecurityTool:
    """Base class for security testing tools."""
    
    async def execute(self, **kwargs: Any) -> Dict[str, Any]:
        """Execute the tool with given parameters."""
        raise NotImplementedError
```

### Configuration
- Use Pydantic for configuration models
- Environment variables for secrets and settings
- Use `pydantic-settings` for environment variable loading

## Security Considerations

- **Never hardcode secrets** - use environment variables
- **Validate all inputs** - especially user-provided data
- **Use parameterized queries** - prevent injection attacks
- **Sanitize output** - prevent XSS in web interfaces
- **Run untrusted code in sandboxes** - use Docker isolation
- **Review security findings** - bandit checks are mandatory

## Development Workflow

1. **Setup**: `make setup-dev` installs dependencies and pre-commit hooks
2. **Format**: `make format` formats code with ruff
3. **Lint**: `make lint` checks code quality
4. **Type Check**: `make type-check` runs mypy and pyright
5. **Test**: `make test` runs pytest
6. **All Checks**: `make check-all` runs all quality checks

## Common Commands

```bash
# Install dependencies
poetry install --with=dev

# Run Strix
poetry run strix --target ./app-directory

# Format code
poetry run ruff format .

# Lint code
poetry run ruff check . --fix

# Type check
poetry run mypy strix/
poetry run pyright strix/

# Run tests
poetry run pytest -v

# Security scan
poetry run bandit -r strix/
```

## Documentation

- Use Google-style docstrings
- Include type hints in docstrings when helpful
- Provide examples for complex functions
- Document exceptions that can be raised

Example:
```python
def analyze_vulnerability(target: str, vuln_type: str) -> Dict[str, Any]:
    """Analyze a specific vulnerability type in the target.
    
    Args:
        target: The URL or path to analyze
        vuln_type: Type of vulnerability (e.g., "sqli", "xss")
        
    Returns:
        Dictionary containing analysis results with keys:
            - found: bool indicating if vulnerability was found
            - severity: str severity level (low/medium/high/critical)
            - details: str description of the finding
            
    Raises:
        ValueError: If vuln_type is not recognized
        ConnectionError: If target is unreachable
    """
    pass
```

## When to Ask for Clarification

- **Security-sensitive code**: Double-check security implications
- **Complex agent logic**: Confirm expected behavior
- **Breaking changes**: Verify compatibility requirements
- **New dependencies**: Ensure they align with project goals
- **Unclear requirements**: Ask before implementing

## Helpful Context

- This is a security tool - correctness and safety are paramount
- Performance matters - agents may run many operations in parallel
- The project is open source - code quality reflects on the community
- Users may not be security experts - UX and documentation matter
- False positives erode trust - validation is critical

## Additional Resources

- Main docs: README.md
- Contributing guide: CONTRIBUTING.md
- Prompt guidelines: strix/prompts/README.md
- Package config: pyproject.toml
