# cheesechain

Discord bot to generate message based on a slack data export, using a markov chain

## Usage

1. Extract a Slack export to a directory called `dataset` in the root of the repo
2. Copy `.env.dist` to `.env` and populate the values in it
3. Create & activate a venv via your means of choice
4. `poetry install --no-root`
5. `python -m cheesechain`
