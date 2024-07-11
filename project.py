# region Load libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
# endregion

# region Load Bitcoin data
# ایجاد یک شیء Ticker برای دسترسی به داده‌های بیت کوین
btc = yf.Ticker("BTC-USD")
# دریافت داده‌های تاریخی بیت کوین برای 90 روز گذشته
data = btc.history(period="90d")
# endregion

# region Create DataFrame and calculate features
# ایجاد یک DataFrame جدید با استفاده از داده‌های مربوط به قیمت
df = data[['Open', 'High', 'Low', 'Close']].copy()
# محاسبه سود (Benefit) به عنوان تفاوت بین قیمت بسته شدن و قیمت باز شدن
df["Benefit"] = df["Close"] - df["Open"]
# محاسبه (Tolerance) به عنوان تفاوت بین بالاترین و پایین‌ترین قیمت
df["Tolerance"] = df["High"] - df["Low"]
# تعیین رنگ شمع (CandleColor) بر اساس سود یا زیان
df["CandleColor"] = df["Benefit"].apply(lambda price: "green" if price > 0 else "red")
# اضافه کردن حجم معاملات به DataFrame
df["Volume"] = data["Volume"]
# محاسبه اختلاف بالاترین و پایین‌ترین قیمت
df["High-Low"] = df["High"] - df["Low"]
# محاسبه اختلاف قیمت بسته شدن و باز شدن به صورت مطلق
df["Close-Open"] = abs(df["Close"] - df["Open"])
# محاسبه اندازه بدنه شمع (Body) به صورت مطلق
df["Body"] = df["Benefit"].apply(lambda x: abs(x))
# محاسبه دامنه نوسان (Range) به عنوان تفاوت بین High-Low و Close-Open
df["Range"] = df["High-Low"] - df["Close-Open"]
# محاسبه روند (Trend) به عنوان درصد تغییر قیمت بسته شدن
df["Trend"] = df["Close"].pct_change()
# endregion

# region Plot Candlestick Chart
# تنظیم اندازه نمودار
plt.figure(figsize=(14, 7))
# رسم نمودار شمعی با استفاده از میله‌هایی برای نشان دادن تحمل و سود
plt.bar(range(len(df)), df["Tolerance"], bottom=df["Low"], width=0.1, color=df["CandleColor"])
plt.bar(range(len(df)), df["Benefit"], bottom=df["Open"], width=0.8, color=df["CandleColor"])
# تنظیم برچسب‌های محورها و عنوان نمودار
plt.xlabel('Day')
plt.ylabel('Price (USD)')
plt.title('Bitcoin Candlestick Chart (Last 90 Candles)')
# نمایش نمودار
plt.show()
# endregion

# region Predict next candle
# انتخاب ویژگی‌ها و برچسب‌ها برای آموزش مدل
X = df[['Volume', 'High-Low', 'Body', 'Range', 'Trend']][-60:].values
y = df['Close'][-60:].values

# ایجاد و آموزش یک مدل رگرسیون خطی
model = LinearRegression()
model.fit(X, y)

# استخراج ویژگی‌های مربوط به شمع بعدی
next_volume = data['Volume'].iloc[-1]
next_high_low = df['High-Low'].iloc[-1]
next_body = df['Body'].iloc[-1]
next_range = df['Range'].iloc[-1]
next_trend = df['Trend'].iloc[-1]

# پیش‌بینی قیمت بسته شدن شمع بعدی
next_features = [[next_volume, next_high_low, next_body, next_range, next_trend]]
next_close = model.predict(next_features)[0]

# تعیین قیمت‌های باز شدن، بالاترین، و پایین‌ترین برای شمع بعدی
last_open = df['Open'].iloc[-1]
next_open = last_open
next_high = max(next_close, df['High'].iloc[-1])
next_low = min(next_close, df['Low'].iloc[-1])

# محاسبه سود و تعیین رنگ شمع برای شمع بعدی
next_benefit = next_close - next_open
next_candlecolor = "green" if next_benefit > 0 else "red"

# چاپ پیش‌بینی‌ها
#  تعریف توابع برای محاسبه درصد تغییر و تعیین رنگ کندل
def calculate_change_percent(next_open, next_close):
    return ((next_close - next_open) / next_open) * 100

def determine_candle_color(next_open, next_close):
    if next_close > next_open:
        return "Green"
    elif next_close < next_open:
        return "Red"
    else:
        return "Doji"
confidence = 100 - model.score(X, y) * 100  # سطح اطمینان بر اساس نمره مدل

# محاسبه درصد تغییر و رنگ کندل
change_percent = calculate_change_percent(next_open, next_close)
next_candlecolor = determine_candle_color(next_open, next_close)

# چاپ پیش‌بینی‌ها به همراه درصد احتمال
print(f"Predicted close price for the next candle: {next_close:.2f} USD with a confidence of {confidence:.2f}%")
print(f"Predicted open price for the next candle: {next_open:.2f} USD with a confidence of {confidence:.2f}%")
print(f"Predicted high price for the next candle: {next_high:.2f} USD with a confidence of {confidence:.2f}%")
print(f"Predicted low price for the next candle: {next_low:.2f} USD with a confidence of {confidence:.2f}%")
print(f"Predicted percentage change: {change_percent:.2f}%")
print(f"Predicted candle color for the next candle: {next_candlecolor}")

# endregion
