# Using GitHub Copilot Models with Strix

This guide explains how to configure Strix to use GitHub Copilot's LLM models as your AI provider.

## Overview

GitHub Copilot provides access to powerful language models through OAuth authentication. Unlike traditional API key-based access, GitHub Copilot uses OAuth tokens for authentication, making it easy to use the same models that power GitHub Copilot in your IDE.

## Available Models

GitHub Copilot provides access to several models:

- `gpt-4o` - GPT-4 Optimized (recommended)
- `gpt-4o-mini` - GPT-4 Optimized Mini (faster, cost-effective)
- `gpt-4` - GPT-4
- `gpt-3.5-turbo` - GPT-3.5 Turbo
- `claude-3.5-sonnet` - Anthropic Claude 3.5 Sonnet
- `o1-preview` - OpenAI O1 Preview
- `o1-mini` - OpenAI O1 Mini

## Setup

### 1. Get GitHub Copilot OAuth Token

GitHub Copilot uses OAuth for authentication. You need to obtain an OAuth token:

**Method 1: Using GitHub CLI (Recommended)**

```bash
# Install GitHub CLI if you haven't already
# https://cli.github.com/

# Authenticate with GitHub
gh auth login

# Get your OAuth token
gh auth token
```

**Method 2: Using the GitHub Copilot Extension**

1. Install GitHub Copilot in VS Code or your IDE
2. Sign in to GitHub Copilot
3. Extract the OAuth token from the extension's authentication (this is stored in your IDE's secure storage)

**Method 3: Manual OAuth Flow**

You can also obtain a token through GitHub's OAuth flow. See the [GitHub OAuth documentation](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps) for details.

### 2. Configure Environment Variables

Set the following environment variables to use GitHub Copilot models:

```bash
# Set the model with github_copilot/ prefix
export STRIX_LLM="github_copilot/gpt-4o"

# Set your GitHub OAuth token
export GITHUB_COPILOT_TOKEN="ghu_your_oauth_token_here"

# Alternatively, use LLM_API_KEY
export LLM_API_KEY="ghu_your_oauth_token_here"
```

### 3. Run Strix

```bash
strix --target ./your-app-directory
```

## Model Selection Recommendations

For best results with Strix's security testing capabilities:

### Best Performance
- `github_copilot/gpt-4o` - Excellent reasoning and code analysis
- `github_copilot/claude-3.5-sonnet` - Strong at security analysis and code review
- `github_copilot/o1-preview` - Advanced reasoning capabilities

### Good Balance (Speed/Cost)
- `github_copilot/gpt-4o-mini` - Fast and cost-effective with good quality
- `github_copilot/gpt-4` - Proven performance, widely tested

### Legacy Options
- `github_copilot/gpt-3.5-turbo` - Basic tasks, fastest responses

## Configuration Examples

### Using GPT-4o (Recommended)
```bash
export STRIX_LLM="github_copilot/gpt-4o"
export GITHUB_COPILOT_TOKEN="ghu_your_token_here"
strix --target ./app-directory
```

### Using Claude 3.5 Sonnet
```bash
export STRIX_LLM="github_copilot/claude-3.5-sonnet"
export GITHUB_COPILOT_TOKEN="ghu_your_token_here"
strix --target ./app-directory
```

### Using O1 Preview
```bash
export STRIX_LLM="github_copilot/o1-preview"
export GITHUB_COPILOT_TOKEN="ghu_your_token_here"
strix --target ./app-directory
```

## Authentication

GitHub Copilot uses OAuth tokens that start with `ghu_`. These tokens are different from:
- GitHub Personal Access Tokens (start with `ghp_`)
- GitHub App tokens (start with `ghs_`)

Make sure you're using the correct token type.

## Rate Limits

GitHub Copilot has usage limits based on your subscription:
- **GitHub Copilot Individual**: Standard rate limits
- **GitHub Copilot Business**: Higher rate limits
- **GitHub Copilot Enterprise**: Highest rate limits with custom quotas

Rate limits are enforced per user and may vary based on model selection.

## Troubleshooting

### Authentication Error
```
LLM request failed: Invalid API key
```
**Solutions**:
- Ensure your `GITHUB_COPILOT_TOKEN` is a valid OAuth token (starts with `ghu_`)
- Verify your GitHub Copilot subscription is active
- Re-authenticate using `gh auth login` to get a fresh token

### Model Not Found
```
LLM request failed: Model not found
```
**Solutions**:
- Verify the model name is correct and uses the `github_copilot/` prefix
- Check that the model is available in your region
- Ensure your GitHub Copilot subscription includes access to the model

### Rate Limit Exceeded
```
LLM request failed: Rate limit exceeded
```
**Solutions**:
- Wait before making more requests
- Consider upgrading to GitHub Copilot Business or Enterprise
- Use a lighter model like `gpt-4o-mini` to reduce token usage

### Token Expired
```
LLM request failed: Unauthorized
```
**Solution**: Your OAuth token may have expired. Get a fresh token:
```bash
gh auth refresh
gh auth token
```

## Benefits of Using GitHub Copilot

1. **Unified Billing**: Use the same GitHub Copilot subscription for IDE and Strix
2. **OAuth Security**: More secure than traditional API keys
3. **Easy Setup**: No need to manage separate API keys for different providers
4. **Access to Multiple Models**: Switch between OpenAI and Anthropic models seamlessly

## Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [LiteLLM GitHub Copilot Provider](https://docs.litellm.ai/docs/providers/github_copilot)
- [GitHub CLI Documentation](https://cli.github.com/manual/)

## Notes

- GitHub Copilot tokens are OAuth tokens and should be treated as secrets
- Tokens may expire and need to be refreshed periodically
- Not all models may be available in all regions
- For production use, consider setting up automated token refresh
- GitHub Copilot is designed for individual developer use; for large-scale deployments, consider direct API access
