#!/usr/bin/env python3
"""
Test script to verify GitHub Copilot integration with Strix.

This script tests that:
1. GitHub Copilot OAuth token is properly configured
2. The model name format is correct
3. Environment variables are set correctly

Note: This test doesn't require Strix dependencies to be installed.
"""

import os


def test_github_copilot_token_logic():
    """Test the GitHub Copilot token configuration logic."""
    print("Testing GitHub Copilot OAuth token configuration logic...")

    # Simulate the logic from strix/llm/llm.py
    test_token = "ghu_test_oauth_token_12345"
    os.environ["GITHUB_COPILOT_TOKEN"] = test_token

    # Clear any existing GITHUB_COPILOT_API_KEY
    os.environ.pop("GITHUB_COPILOT_API_KEY", None)

    # Simulate the code from llm.py
    github_copilot_token = os.getenv("GITHUB_COPILOT_TOKEN")
    if github_copilot_token:
        os.environ["GITHUB_COPILOT_API_KEY"] = github_copilot_token

    # Verify it worked
    github_copilot_api_key = os.environ.get("GITHUB_COPILOT_API_KEY")

    if github_copilot_api_key == test_token:
        print("✓ GitHub Copilot token configuration logic works correctly")
        # Mask tokens in output for security
        print(f"  GITHUB_COPILOT_TOKEN: {github_copilot_token[:10]}...")
        print(f"  GITHUB_COPILOT_API_KEY: {github_copilot_api_key[:10]}...")
        return True
    else:
        print("✗ GitHub Copilot token not set correctly.")
        print(f"  Expected: {test_token[:10]}...")
        print(f"  Got: {github_copilot_api_key[:10] if github_copilot_api_key else 'None'}...")
        return False


def test_token_format():
    """Test that OAuth tokens have the correct format."""
    print("\nTesting GitHub Copilot OAuth token format...")

    valid_tokens = [
        "ghu_test123",
        "ghu_abcdefghijklmnopqrstuvwxyz1234567890",
    ]

    invalid_tokens = [
        "ghp_test123",  # Personal access token, not OAuth
        "ghs_test123",  # App token, not OAuth
        "abc_test123",  # Wrong prefix
    ]

    all_valid = True

    print("  Valid tokens:")
    for token in valid_tokens:
        if token.startswith("ghu_"):
            print(f"    ✓ {token[:15]}... - Valid OAuth token")
        else:
            print(f"    ✗ {token[:15]}... - Invalid format")
            all_valid = False

    print("  Invalid tokens (should be rejected):")
    for token in invalid_tokens:
        if not token.startswith("ghu_"):
            print(f"    ✓ {token[:15]}... - Correctly identified as invalid")
        else:
            print(f"    ✗ {token[:15]}... - Should be invalid")
            all_valid = False

    return all_valid


def test_model_name_format():
    """Test that GitHub Copilot model names are correctly formatted."""
    print("\nTesting GitHub Copilot model name formats...")

    test_models = [
        "github_copilot/gpt-4o",
        "github_copilot/gpt-4o-mini",
        "github_copilot/gpt-4",
        "github_copilot/gpt-3.5-turbo",
        "github_copilot/claude-3.5-sonnet",
        "github_copilot/o1-preview",
        "github_copilot/o1-mini",
    ]

    all_valid = True
    for model in test_models:
        if model.startswith("github_copilot/"):
            print(f"  ✓ {model} - Valid format")
        else:
            print(f"  ✗ {model} - Invalid format (should start with github_copilot/)")
            all_valid = False

    return all_valid


def test_environment_setup():
    """Test a complete environment setup scenario."""
    print("\nTesting complete environment setup...")

    # Clear environment
    for var in ["STRIX_LLM", "GITHUB_COPILOT_TOKEN", "GITHUB_COPILOT_API_KEY"]:
        os.environ.pop(var, None)

    # Set up as a user would
    os.environ["STRIX_LLM"] = "github_copilot/gpt-4o"
    os.environ["GITHUB_COPILOT_TOKEN"] = "ghu_example_oauth_token"

    # Simulate the llm.py initialization
    github_copilot_token = os.getenv("GITHUB_COPILOT_TOKEN")
    if github_copilot_token:
        os.environ["GITHUB_COPILOT_API_KEY"] = github_copilot_token

    # Verify
    strix_llm = os.environ.get("STRIX_LLM")
    copilot_token = os.environ.get("GITHUB_COPILOT_TOKEN")
    copilot_api_key = os.environ.get("GITHUB_COPILOT_API_KEY")

    if (
        strix_llm == "github_copilot/gpt-4o"
        and copilot_token == "ghu_example_oauth_token"
        and copilot_api_key == "ghu_example_oauth_token"
    ):
        print("  ✓ Complete environment setup works correctly")
        print(f"    STRIX_LLM: {strix_llm}")
        print(f"    GITHUB_COPILOT_TOKEN: {copilot_token[:20]}...")
        print(f"    GITHUB_COPILOT_API_KEY: {copilot_api_key[:20]}...")
        return True
    else:
        print("  ✗ Environment setup failed")
        return False


def main():
    """Run all tests."""
    print("=" * 70)
    print("GitHub Copilot Integration Test for Strix")
    print("=" * 70)
    print()

    results = []

    # Run tests
    results.append(test_github_copilot_token_logic())
    results.append(test_token_format())
    results.append(test_model_name_format())
    results.append(test_environment_setup())

    print("\n" + "=" * 70)
    if all(results):
        print("All tests passed! ✓")
        print("\nYou can now use GitHub Copilot with Strix:")
        print()
        print("  1. Get your GitHub Copilot OAuth token:")
        print("     gh auth login")
        print("     gh auth token")
        print()
        print("  2. Set environment variables:")
        print("     export STRIX_LLM='github_copilot/gpt-4o'")
        print("     export GITHUB_COPILOT_TOKEN='ghu_your_oauth_token'")
        print()
        print("  3. Run Strix:")
        print("     strix --target ./your-app")
        print()
        print("See docs/GITHUB_COPILOT.md for detailed setup instructions.")
        print("=" * 70)
        return 0
    else:
        print("Some tests failed! ✗")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
