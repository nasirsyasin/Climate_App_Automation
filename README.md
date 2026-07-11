# ClimateApp Automation

## Project Overview

`ClimateApp Automation` is a Python-based test automation repository for the ClimateApp mobile and web workflows. The project uses Appium for mobile UI automation, Selenium for web interactions, BrowserStack for cross-device execution, and Mixpanel verification for analytics workflows. It also includes integrations with Zephyr Scale for test execution reporting.

## Goals

- Validate core mobile user journeys: login, signup, notifications, compost, and e-waste flows
- Verify Mixpanel event exports and analytics data
- Record test outcomes via CSV logs and Zephyr Scale API reporting
- Support BrowserStack execution and local Appium execution paths

## Repository Structure

- `AuthenticatedRequester.py`
  - Sends authenticated Zephyr Scale test execution POST requests.

- `conftest.py`
  - Defines pytest fixtures and BrowserStack Appium driver setup.

- `TestExecutionManager.py`
  - Orchestrates Zephyr Scale test result payload creation and submission.

- `browserstack.yml`
  - BrowserStack capabilities and project settings for Android test execution.

- `Pages/`
  - Page object classes for mobile and web test flows.
  - `Pages/Mobile_pages/` contains Appium page objects for login, onboarding, notifications, track actions, compost, and e-waste.
  - `Pages/Web_pages/Mixpanel_pages/` contains Mixpanel export and verification logic.

- `Tests/`
  - Mobile test case classes that execute app flows and report results.

- `TestSuite/`
  - Higher-level smoke suite for grouped pytest execution.

- `Utility/`
  - Shared helpers for driver setup, caching, CSV logging, and browser automation.

- `Results/`
  - Output CSV files generated during test runs.

- `Mixpanel_Results/`
  - Exported Mixpanel CSV data and comparison files.

## Prerequisites

- Python 3.8+ installed
- `pip` package manager
- Appium server installed and running for local mobile test execution
- BrowserStack account and access keys for remote mobile execution
- Mixpanel and application-specific environment access as required by the tests

## Recommended Dependencies

The repository does not currently include a dependency manifest, but these packages are expected:

- `pytest`
- `appium-python-client`
- `selenium`
- `webdriver-manager`
- `requests`

## Configuration

1. Add your Zephyr Scale API token to a local `token.txt` file.
   - This file should be ignored by git and is already excluded via `.gitignore`.

2. Update any absolute file paths used by test scripts and helper classes.
   - Example hard-coded paths found in `AuthenticatedRequester.py` and various result logger functions.

3. Configure BrowserStack credentials and device settings in `browserstack.yml`.

4. Ensure the Appium server endpoint and mobile application path are valid when running local Appium tests.

## Running Tests

### Run all tests

```bash
pytest
```

### Run a single test module

```bash
pytest Tests/Mobile_Tests/Login_with_email.py
```

### Run the smoke suite

```bash
python TestSuite/Test_Suite_Smoke.py
```

## Output and Reporting

- Test execution results are written to CSV files under `Results/`.
- Mixpanel-related exports and verification output are stored under `Mixpanel_Results/`.
- Zephyr Scale execution reports are sent through the API endpoint configured in `AuthenticatedRequester.py`.

## Key Implementation Details

- `TestExecutionManager.py` uses `AuthenticatedRequester` to post test execution payloads.
- `conftest.py` provides a `setWebdriver` fixture for BrowserStack remote sessions.
- Mobile page objects are implemented using Appium and platform-specific locators for Android and iOS.
- `Utility/mobile_driver_setup.py` provides a singleton Appium driver instance.
- `Pages/Web_pages/Mixpanel_pages/MixpanelAnalyticsExecution.py` centralizes Mixpanel export and verification operations.

## Best Practices and Improvements

- Convert hard-coded paths to environment variables or a configuration file.
- Add a `requirements.txt` or `pyproject.toml` for dependency management.
- Add detailed environment setup documentation for BrowserStack, Appium, and Zephyr Scale.
- Refactor test logging to use a shared reporting utility rather than repeated CSV code.
- Add GitHub Actions or other CI configuration for automated test execution.

## Notes

- `token.txt` is excluded from version control to protect credentials.
- Review and sanitize any sensitive data before sharing or publishing this repository.
