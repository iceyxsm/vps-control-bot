# VPS Control Bot (GCP)

A minimal Telegram bot to start/stop a Google Cloud Compute Engine VM instance via chat commands.

## Setup

1. Clone the repo and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Set environment variables:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
   - `TELEGRAM_OWNER_ID`: Your Telegram user ID (for security)
   - `GCP_PROJECT`: GCP project ID
   - `GCP_ZONE`: GCP zone (e.g. `us-central1-a`)
   - `GCP_INSTANCE`: GCP instance name
   - `GOOGLE_APPLICATION_CREDENTIALS`: Path to your GCP service account JSON key

3. Run the bot:
   ```sh
   python bot.py
   ```

## Commands
- `/start_vps` — Start the VM
- `/stop_vps` — Stop the VM

## Security
Only the owner (set by `TELEGRAM_OWNER_ID`) can use the commands.
