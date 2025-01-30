# Standard Configuration

The project can be configured with `uv` or `pip`. Both ways will be explained.

<details><summary>Using pip</summary>

1. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
2. Activate the virtual environment:
    ```bash
    source .venv/bin/activate # Linux / Mac
    .venv\Scripts\activate # Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
</details>

<details><summary>Using uv</summary>

1. Install uv:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh   
    ```
2. Install the python version you want to use:
    ```bash
    uv python install <your_version>
    ```
3. Install the dependencies:
    ```bash
    uv sync --all-groups
    ```
</details>

# Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
uv run pytest kata_name/tests
```