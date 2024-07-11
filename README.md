
## English Version

### Bitcoin Candlestick Analysis and Prediction

#### Overview
This project analyzes and predicts Bitcoin prices using historical data from the last 90 days. It utilizes various Python libraries for data analysis, visualization, and machine learning.

#### Features
- **Data Retrieval**: Fetches historical Bitcoin data using the `yfinance` library.
- **Data Processing**: Calculates various features such as benefit, tolerance, and trend from the retrieved data.
- **Visualization**: Plots candlestick charts using `matplotlib`.
- **Prediction**: Uses linear regression to predict the closing price of the next candlestick.

#### Libraries Used
- `yfinance`
- `pandas`
- `matplotlib`
- `sklearn`

#### How to Run
1. **Install the necessary libraries**:
    ```bash
    pip install yfinance pandas matplotlib scikit-learn
    ```
2. **Run the script**:
    ```bash
    python project.py
    ```

#### Project Structure
- **Data Loading**: Loads Bitcoin historical data for the past 90 days.
- **Feature Calculation**: Calculates features like Benefit, Tolerance, CandleColor, etc.
- **Visualization**: Creates a candlestick chart of Bitcoin prices.
- **Prediction**: Predicts the next candlestick’s closing price using linear regression.

#### Output
The script outputs the predicted open, high, low, and close prices of the next candlestick along with its color (green or red) and the confidence level of the prediction.

---

## نسخه فارسی

### تحلیل و پیش‌بینی شمع بیت‌کوین

#### مرور کلی
این پروژه به تحلیل و پیش‌بینی قیمت بیت‌کوین با استفاده از داده‌های تاریخی 90 روز گذشته می‌پردازد. از کتابخانه‌های مختلف پایتون برای تحلیل داده‌ها، تجسم‌سازی و یادگیری ماشین استفاده می‌کند.

#### ویژگی‌ها
- **بازیابی داده‌ها**: دریافت داده‌های تاریخی بیت‌کوین با استفاده از کتابخانه `yfinance`.
- **پردازش داده‌ها**: محاسبه ویژگی‌های مختلف مانند سود، تحمل، و روند از داده‌های بازیابی شده.
- **تجسم‌سازی**: رسم نمودار شمعی با استفاده از `matplotlib`.
- **پیش‌بینی**: استفاده از رگرسیون خطی برای پیش‌بینی قیمت بسته شدن شمع بعدی.

#### کتابخانه‌های استفاده شده
- `yfinance`
- `pandas`
- `matplotlib`
- `sklearn`

#### نحوه اجرا
1. **نصب کتابخانه‌های لازم**:
    ```bash
    pip install yfinance pandas matplotlib scikit-learn
    ```
2. **اجرای اسکریپت**:
    ```bash
    python project.py
    ```

#### ساختار پروژه
- **بارگیری داده‌ها**: بارگیری داده‌های تاریخی بیت‌کوین برای 90 روز گذشته.
- **محاسبه ویژگی‌ها**: محاسبه ویژگی‌هایی مانند سود، تحمل، رنگ شمع و غیره.
- **تجسم‌سازی**: ایجاد نمودار شمعی از قیمت‌های بیت‌کوین.
- **پیش‌بینی**: پیش‌بینی قیمت بسته شدن شمع بعدی با استفاده از رگرسیون خطی.

#### خروجی
اسکریپت قیمت‌های پیش‌بینی شده باز شدن، بالاترین، پایین‌ترین، و بسته شدن شمع بعدی را به همراه رنگ آن (سبز یا قرمز) و سطح اطمینان پیش‌بینی ارائه می‌دهد.

---
