# VSCode Configuration

This directory contains shared VSCode configuration for the Strix project.

## Files

- **settings.json**: Project-wide VSCode settings including Python, Copilot, and formatting configurations
- **extensions.json**: Recommended extensions for development

## Recommended Extensions

The extensions.json file recommends the following extensions:

- **GitHub Copilot** - AI pair programmer
- **Python** - Python language support
- **Ruff** - Fast Python linter and formatter
- **Jinja** - Template syntax highlighting for prompt files

## User-Specific Settings

If you need to customize settings for your own development environment, create a `.vscode/settings.json` file in your user settings directory, not in this repository. The `.gitignore` is configured to ignore most `.vscode` files except these shared configuration files.

## GitHub Copilot

GitHub Copilot is configured to work optimally with this Python project. For best results:

1. Install the GitHub Copilot extension
2. Review `.github/copilot-instructions.md` for project-specific context
3. Ensure Python extension and type checking are enabled
