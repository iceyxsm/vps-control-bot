import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from googleapiclient.discovery import build
from google.oauth2 import service_account

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OWNER_ID = int(os.getenv("TELEGRAM_OWNER_ID"))
GCP_PROJECT = os.getenv("GCP_PROJECT")
GCP_ZONE = os.getenv("GCP_ZONE")
GCP_INSTANCE = os.getenv("GCP_INSTANCE")

SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
CREDENTIALS = service_account.Credentials.from_service_account_file(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), scopes=SCOPES
)

compute = build("compute", "v1", credentials=CREDENTIALS)

async def start_vps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    compute.instances().start(
        project=GCP_PROJECT, zone=GCP_ZONE, instance=GCP_INSTANCE
    ).execute()
    await update.message.reply_text("✅ VPS start command sent.")

async def stop_vps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    compute.instances().stop(
        project=GCP_PROJECT, zone=GCP_ZONE, instance=GCP_INSTANCE
    ).execute()
    await update.message.reply_text("🛑 VPS stop command sent.")

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(CommandHandler("start_vps", start_vps))
app.add_handler(CommandHandler("stop_vps", stop_vps))

if __name__ == "__main__":
    app.run_polling()
