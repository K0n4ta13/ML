# Roommate Compatibility Finder

This project is an interactive application developed in Python using Streamlit. Its goal is to find the most compatible roommates based on current tenants.

## Installation

To run the project, follow these steps:

1. **Install dependencies**

   ```bash
   uv sync
   ```

2. **Activate the virtual environment**

   ```bash
   source .venv/bin/activate
   ```

## Running the Project

To start the application, run the following command:

```bash
streamlit run app.py
```

This will open the application in your default browser.

## Usage

1. Enter the id (between 1 and 12,000) of up to three current tenants in the sidebar.
2. Specify how many roommates you want to search for.
3. Click the "Search housemates" button.
4. The application will display a chart with compatibility levels and a table comparing possible roommates.
