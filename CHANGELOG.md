## [0.1.8](https://github.com/rilesdun/python_explorer_api/compare/v0.1.7...v0.1.8) (2023-09-25)


### Bug Fixes

* artifacts and tagging variables ([a7b14ac](https://github.com/rilesdun/python_explorer_api/commit/a7b14ac4d504e9f834ddfed06ea5f503198fd5ef))

## [0.1.7](https://github.com/rilesdun/python_explorer_api/compare/v0.1.6...v0.1.7) (2023-09-24)


### Bug Fixes

* fix job tagging ([0dac58b](https://github.com/rilesdun/python_explorer_api/commit/0dac58b3575d320d0f7f9fe88d64b0835b36a9a4))

## [0.1.6](https://github.com/rilesdun/python_explorer_api/compare/v0.1.5...v0.1.6) (2023-09-24)


### Bug Fixes

* fix artifact uploading ([ee605c7](https://github.com/rilesdun/python_explorer_api/commit/ee605c712a3853d3408fe2b1299c9a90c7f03f62))
* fix artifact uploading ([3a7dfd6](https://github.com/rilesdun/python_explorer_api/commit/3a7dfd69c213a52c221ac8781c41ce8d30d4e838))

## [0.1.5](https://github.com/rilesdun/python_explorer_api/compare/v0.1.4...v0.1.5) (2023-09-24)


### Bug Fixes

* rebase from main, start adding changes on dev ([#2](https://github.com/rilesdun/python_explorer_api/issues/2)) ([a0f575d](https://github.com/rilesdun/python_explorer_api/commit/a0f575d20fe0b7c7fb853263d8a5d8a36a1a13f8))

## [0.1.4](https://github.com/rilesdun/python_explorer_api/compare/v0.1.3...v0.1.4) (2023-09-21)


### Bug Fixes

* deployment step to public server ([8b0ca07](https://github.com/rilesdun/python_explorer_api/commit/8b0ca07630c1840f67ba4827cc51a23fee1b27d0))

## [0.1.3](https://github.com/rilesdun/python_explorer_api/compare/v0.1.2...v0.1.3) (2023-09-19)


### Bug Fixes

* publishing docker builds after releases ([d7a21d7](https://github.com/rilesdun/python_explorer_api/commit/d7a21d7879f65bd810d1ba01156668f22038afba))

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
