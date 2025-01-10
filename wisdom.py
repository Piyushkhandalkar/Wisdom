import discord
import random
import csv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from discord.ext import commands


# Load quotes from CSV file
def load_quotes_from_csv():
    quotes = []
    try:
        with open("AnimeQuotes.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                quote = row[
                    "Quote"
                ].strip()  # Access the 'Quote' column and remove extra spaces
                if quote:  # Only add non-empty quotes
                    quotes.append(quote)
    except FileNotFoundError:
        print("Error: 'AnimeQuotes.csv' not found.")
    except Exception as e:
        print(f"Error loading CSV: {e}")

    return quotes


# Initialize bot and quotes
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
quotes = load_quotes_from_csv()
scheduler = AsyncIOScheduler()

# Global variable for interval time (in minutes)
interval_minutes = 5
server_channel_map = {}  # Dictionary to map server ID to channel ID

# Your Discord ID (for you to be able to use the command)
OWNER_ID = -----  # Replace with your actual Discord user ID


# Function to send a random quote
async def send_quote():
    for server_id, channel_id in server_channel_map.items():
        channel = bot.get_channel(channel_id)
        if channel:
            quote = random.choice(quotes)
            await channel.send(quote)


# Command to change the interval (only allowed for admins and the bot owner)
@bot.command()
async def set_interval(ctx, minutes: int):
    global interval_minutes, scheduler

    # Check if the user is an admin or the bot owner
    if ctx.author.id != OWNER_ID and not ctx.author.guild_permissions.administrator:
        await ctx.send("You do not have permission to change the interval.")
        return

    if minutes < 1:
        await ctx.send("Please provide a valid interval (greater than 0).")
        return

    # Update the interval and reschedule the job
    interval_minutes = minutes
    scheduler.remove_all_jobs()
    scheduler.add_job(
        send_quote, IntervalTrigger(minutes=interval_minutes)
    )  # Update interval
    await ctx.send(f"Quote interval has been set to {interval_minutes} minutes.")


# Command to generate a quote manually
@bot.command()
async def gquote(ctx):
    if ctx.guild.id in server_channel_map:
        channel_id = server_channel_map[ctx.guild.id]
        channel = bot.get_channel(channel_id)
        if channel:
            quote = random.choice(quotes)
            await channel.send(quote)
    else:
        await ctx.send("This server has not set up a channel for quotes.")


# Command to set the channel ID for the server (only admins can use this)
@bot.command()
async def set_channel(ctx, channel: discord.TextChannel):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("You do not have permission to set the channel.")
        return

    # Store the channel ID for this server
    server_channel_map[ctx.guild.id] = channel.id
    await ctx.send(f"Channel set to {channel.mention} for this server.")


# Event when the bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    # Start the scheduler to send quotes at the specified interval
    scheduler.add_job(send_quote, IntervalTrigger(minutes=interval_minutes))
    scheduler.start()

    # Send a welcome message (the bot needs a channel to send the message)
    # We won't automatically send a welcome message since the channel isn't set yet.


# Run the bot with your token
bot.run("token")

#this bot is made by piyush.

