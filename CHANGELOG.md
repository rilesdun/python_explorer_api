## [0.1.2](https://github.com/rilesdun/python_explorer_api/compare/v0.1.1...v0.1.2) (2023-09-19)

### Bug Fixes

* docker builds and pushes, condensed workflow ([d7e9741](https://github.com/rilesdun/python_explorer_api/commit/d7e97411bfca8dca595bfc48cc95e8a161840839))
* package-lock verification ([3ec2832](https://github.com/rilesdun/python_explorer_api/commit/3ec28322363e9e3fd5da4216d0a1cc0d001f0a89))
* version bumps on used actions ([f668b75](https://github.com/rilesdun/python_explorer_api/commit/f668b7533087ead33c401d711cc930a334203a48))
* workflow condensing ([0980310](https://github.com/rilesdun/python_explorer_api/commit/0980310fb8d103de32f22992196ab3cfe75c17fb))
* workflow condensing fixes ([c9fc542](https://github.com/rilesdun/python_explorer_api/commit/c9fc54215eafc93c450a1def985d7179a1a6269d))


## [0.1.0] - 09-18-2023

### Added

- Initial setup of the Flask application in `app.py`.
- Dockerfile for containerization of the application.
- Gunicorn configuration for running the application in production.
- Cache configuration for the application in `cache_config.py`.
- Functionality to fetch and display account information, account history, active witnesses, active sons, and witness count.
- Functionality to fetch and display block information and latest transactions.
- Functionality to fetch and display supply details, maximum supply, total supply, circulating supply, and rich list for various assets.
- Functionality to convert JSON file to HTML file in `json_to_html.py` for bandit security scans.
- Functionality to load environment variables from `.env` files in `config.py`.
- Requirements for the application in `requirements.txt`.
- README with instructions for installing dependencies and running the application in development and production modes.

### Changed

- N/A

### Deprecated

- N/A

### Removed

- N/A

### Fixed

- N/A

### Security

- N/A
