# excel-to-mysql-importer

Python script for importing data from an Excel file into a MySQL database with progress tracking.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This script utilizes pandas to read data from an Excel file and mysql.connector to interact with a MySQL database. It creates a table in the specified database and inserts the data from the Excel file into the table.

## Features

- Reads data from an Excel file.
- Handles NaN values, replacing them with 'None'.
- Creates a table in a MySQL database based on specified schema.
- Inserts data into the MySQL database table with a progress bar.

## Prerequisites

- Python 3.x
- pandas
- mysql-connector-python
- tqdm

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/muamal2/excel-to-mysql-importer.git
    ```

2. Install the required dependencies:

    ```bash
    pip install pandas mysql-connector-python tqdm
    ```

## Usage

1. Place your Excel file (`example.xls`) in the same directory as the script.
2. Modify the `db_config` dictionary in the script with your MySQL database connection details.
3. Run the script:

    ```bash
    python excel-to-mysql-importer.py
    ```

4. Monitor the progress bar as data is inserted into the database.

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
