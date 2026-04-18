#!/usr/bin/env python3
"""Fetch current Bitcoin price (USD) and email it."""

import json
import os
import smtplib
import ssl
import urllib.request
from datetime import datetime, timezone
from email.message import EmailMessage


def get_bitcoin_price_usd() -> float:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    with urllib.request.urlopen(url, timeout=15) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return float(payload["bitcoin"]["usd"])


def send_email(price_usd: float) -> None:
    smtp_host = os.environ["SMTP_HOST"]
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ["SMTP_USER"]
    smtp_password = os.environ["SMTP_PASSWORD"]
    email_from = os.environ["EMAIL_FROM"]
    email_to = os.environ["EMAIL_TO"]

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    subject = f"Bitcoin price update: ${price_usd:,.2f}"
    body = (
        "Hourly Bitcoin Price Alert\n\n"
        f"Current BTC price: ${price_usd:,.2f} USD\n"
        f"Checked at: {timestamp}\n"
    )

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = email_from
    message["To"] = email_to
    message.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls(context=context)
        server.login(smtp_user, smtp_password)
        server.send_message(message)


if __name__ == "__main__":
    btc_price = get_bitcoin_price_usd()
    send_email(btc_price)
