# hello-tron

Hourly Bitcoin price email automation via GitHub Actions.

## What this does
- Runs every hour (`0 * * * *`) and can also be run manually.
- Fetches the current BTC price in USD from CoinGecko.
- Sends an email with the latest Bitcoin price via your SMTP provider.

## Files
- `.github/workflows/btc-hourly-email.yml` – Hourly automation workflow.
- `scripts/btc_price_email.py` – Script that fetches price and sends email.

## Required GitHub Secrets
Configure these repository secrets:
- `SMTP_HOST`
- `SMTP_PORT` (typically `587`)
- `SMTP_USER`
- `SMTP_PASSWORD`
- `EMAIL_FROM`
- `EMAIL_TO`

## Notes
- If your provider requires SSL on port `465`, update the script to use `smtplib.SMTP_SSL`.
- CoinGecko has API limits; this workflow calls it once per hour.
