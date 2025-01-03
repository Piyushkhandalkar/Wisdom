# Wisdom - Discord Bot for Anime Quotes

Wisdom is a Discord bot that sends random anime quotes to a channel at specified intervals. The bot is built using Python and the `discord.py` library and fetches quotes from a Kaggle dataset called **Anime Quotes**.

## Features

- Sends a random anime quote to a Discord channel at a specified time interval.
- Allows the server admins to change the time interval for sending quotes.
- Generates a random quote on command using `!gquote`.
- Securely stores the bot's token using environment variables.

## Prerequisites

- Python 3.8+
- A Discord account and a Discord server where you can add the bot.
- A Kaggle account to download the **Anime Quotes** dataset (or you can use your own dataset).
- A GitHub account to store and manage the project.

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

git clone https://github.com/Piyushkhandalkar/Wisdom.git

### 2. Create and Activate Virtual Environment (Optional but Recommended)

To avoid conflicts with other Python projects, it's recommended to use a virtual environment. You can create and activate one with the following commands:

python3 -m venv venv source venv/bin/activate

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file:
pip install -r requirements.txt

This will install `discord.py`, `apscheduler`, and `python-dotenv` among other dependencies.

### 4. Set Up Your Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new bot application.
2. Copy the **Bot Token**.
3. Create a `.env` file in the root directory of the project and add your token like this:

DISCORD_TOKEN=your-discord-bot-token-here


### 5. Add the Dataset

1. Download the **Anime Quotes** dataset from Kaggle (or use your own CSV dataset).
2. Place the dataset file (e.g., `AnimeQuotes.csv`) in the project directory.

### 6. Run the Bot

After everything is set up, you can run the bot with the following command:

python name.py


The bot will log in to Discord and start sending quotes to the specified channel at intervals.

## Commands

- `!set_interval <time_in_minutes>` - Sets the interval (in minutes) at which the bot sends a quote to the channel. Only admins can use this command.
- `!gquote` - Sends a random quote immediately to the channel.

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests! If you encounter any bugs or issues, open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with 💙 by Piyush Khandalkar
