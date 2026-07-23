# ClimateApp Automation

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC?logo=pytest&logoColor=white)](https://pytest.org/)
[![Appium](https://img.shields.io/badge/mobile-Appium-662D91?logo=appium&logoColor=white)](https://appium.io/)
[![BrowserStack](https://img.shields.io/badge/cloud-BrowserStack-FF6C37?logo=browserstack&logoColor=white)](https://www.browserstack.com/)

Python automation framework for validating ClimateApp mobile journeys, web workflows, analytics events, and cross-device execution.

The project combines Appium, Selenium, pytest, BrowserStack, Mixpanel verification, CSV reporting, and optional Zephyr Scale result publishing.

> **Repository status:** This repository contains reusable page objects and project-specific execution scripts. Some workflows require organization-specific services and application builds before they can run from a clean clone.

## Contents

- [Coverage](#coverage)
- [Technology](#technology)
- [Repository layout](#repository-layout)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running tests](#running-tests)
- [Reports and artifacts](#reports-and-artifacts)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Contributing](#contributing)

## Coverage

### Mobile workflows

- Sign in and account creation
- Onboarding and notification permissions
- Track actions and onboarding tooltips
- Compost decision tree
- E-waste workflow, including map and camera actions
- App refresh and relaunch scenarios

### Web and analytics workflows

- Mixpanel event export and event-name verification
- CSV comparison against predefined event data
- Customer.io/CIO browser workflows
- Optional Zephyr Scale execution reporting

### Execution targets

- Local Android execution through an Appium server
- Remote Android execution through BrowserStack
- Remote iOS execution through BrowserStack
- Chrome-based web validation

## Technology

| Area | Tools |
| --- | --- |
| Language | Python 3.8+ |
| Test runner | pytest |
| Mobile automation | Appium Python Client, Selenium WebDriver |
| Cloud devices | BrowserStack App Automate |
| Web automation | Selenium, Chrome, webdriver-manager |
| Analytics | Mixpanel export and CSV comparison workflows |
| Reporting | CSV, XML, and optional Zephyr Scale publishing |

## Repository layout

```text
.
├── Pages/              # Mobile page objects and web integrations
│   ├── Mobile_pages/   # Login, onboarding, compost, e-waste, and tracking
│   └── Web_pages/      # Mixpanel and Customer.io workflows
├── Tests/              # Mobile flow implementations
├── TestSuite/          # Smoke orchestration and BrowserStack examples
├── Utility/            # Drivers, caching, logging, and result helpers
├── Results/            # Generated mobile test results
├── Mixpanel_Results/   # Exported events and comparison results
├── Resources/          # Local application assets; keep private builds out of Git
├── conftest.py         # Shared pytest and BrowserStack fixtures
├── browserstack.yml    # Android BrowserStack configuration
└── TestExecutionManager.py # Zephyr result orchestration
```

## Prerequisites

- Python 3.8 or newer
- Android SDK, emulator, or connected Android device for local Android runs
- Appium 2 and the required Android driver (`uiautomator2`)
- Xcode and WebDriverAgent for local iOS execution, if applicable
- Chrome for web workflows
- BrowserStack account and uploaded Android APK or iOS IPA for cloud runs
- Access to the relevant Mixpanel workspace and test account
- Access to the project’s Zephyr Scale integration when publishing results

## Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the project dependencies:

```bash
python -m pip install pytest appium-python-client selenium webdriver-manager requests
```

Start Appium for local Android execution:

```bash
appium
```

> **Dependency note:** A dependency lock file is not currently included. Pin the versions used by your team before adding CI or sharing a reproducible test environment.

## Configuration

Configure environment-specific values in your shell or a local `.env` file.

| Variable or file | Used by | Description |
| --- | --- | --- |
| `BROWSERSTACK_USERNAME` | BrowserStack | BrowserStack account username |
| `BROWSERSTACK_ACCESS_KEY` | BrowserStack | BrowserStack access key |
| `BROWSERSTACK_APP` | BrowserStack | Uploaded BrowserStack app identifier, such as `bs://...` |
| `APP_PATH` | Local Appium | Absolute path to the local APK or IPA |
| `TEST_EMAIL` | Mobile login flows | Dedicated non-production test account |
| `TEST_PASSWORD` | Mobile login flows | Password for the dedicated test account |
| `MIXPANEL_EMAIL` | Mixpanel workflows | Account or filter email used during event verification |
The BrowserStack YAML files are templates. Replace their app value with the identifier for your build and configure the account values in your local environment. BrowserStack Local must also be running when `browserstackLocal: true` is enabled.

Local Appium capabilities and result paths currently contain machine-specific defaults. Update them to use repository-relative paths or environment variables before running on another machine.

## Running tests

### Pytest collection

Run the tests that are discoverable by pytest:

```bash
pytest
```

Run an individual mobile flow:

```bash
pytest Tests/Mobile_Tests/Login_with_email.py -v
```

Use markers where supported:

```bash
pytest -m csv -v
```

### Smoke orchestration

The smoke suite combines multiple mobile and analytics workflows and writes results to the output directories:

```bash
python TestSuite/Test_Suite_Smoke.py
```

This is a project-specific orchestration script rather than a guaranteed clean-clone entry point. Confirm that the required application build and service access are available first.

### BrowserStack

Run the BrowserStack sample from the relevant platform directory after configuring credentials and the app identifier:

```bash
python TestSuite/android/bstack_sample.py
python TestSuite/ios/bstack_sample.py
```

For BrowserStack Local, install and start the BrowserStack Local binary before execution. Review the platform-specific `browserstack.yml` file for the selected device and OS version.

### Analytics verification

Analytics workflows are implemented under `Pages/Web_pages/Mixpanel_pages/`. They require access to the relevant analytics project data. Exported and comparison CSV files are written under `Mixpanel_Results/`.

## Reports and artifacts

| Location | Contents |
| --- | --- |
| `Results/` | Mobile flow CSV files and XML output |
| `Mixpanel_Results/` | Mixpanel exports, predefined events, and comparison results |
| BrowserStack dashboard | Remote session videos, logs, screenshots, and network logs when enabled |
| Zephyr Scale | Optional test-case and step results published by the internal integration |

Generated results should be reviewed before committing.

## Troubleshooting

### Appium cannot create a session

Check that the Appium server is running, the device is connected, the required driver is installed, and the configured app path exists. For BrowserStack, verify the app identifier and account credentials.

### Tests are not collected

Some existing flow classes use project-specific names instead of pytest’s conventional `Test...` class naming. Run the intended flow directly, or update the class and test naming conventions before relying on whole-repository collection.

### Web analytics checks fail at login

Confirm that the configured analytics account, event filter, and browser session are valid.

### Result reporting fails during import

Confirm that the reporting integration is available in the execution environment, or disable result publishing for local development.

## Contributing

1. Create a feature branch.
2. Keep secrets and private application artifacts local.
3. Use repository-relative paths and environment variables instead of machine-specific paths.
4. Add or update tests for behavior changes.
5. Run the relevant pytest command and review generated reports before opening a pull request.

## License

No license file is currently included. Add a license before distributing this project publicly.
