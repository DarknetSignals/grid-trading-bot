import ccxt
import time

# ✅ Connect to MEXC (No API Key Needed for Free Version)
exchange = ccxt.mexc()

print("\n📊 Welcome to the Free Grid Trading Bot!")
print("🔥 Upgrade to Pro for full automation: https://yourwebsite.com\n")

# ✅ User enters their price range
low_price = float(input("Enter lower price alert: "))
high_price = float(input("Enter upper price alert: "))

print("\n✅ Bot is running. It will notify you when BTC price hits your range.")

# ✅ Run continuous price tracking
while True:
    try:
        ticker = exchange.fetch_ticker('BTC/USDT')
        current_price = ticker['last']

        if current_price <= low_price:
            print(f"📉 BTC dropped to {current_price}! Consider buying.")
        elif current_price >= high_price:
            print(f"📈 BTC reached {current_price}! Consider selling.")

        time.sleep(30)  # Check price every 30 seconds
    except Exception as e:
        print(f"⚠️ Error fetching price data: {e}")
        time.sleep(60)  # Wait 1 minute before retrying
