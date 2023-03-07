import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Takip edilecek hisse senedi sembolü
symbol = 'BTC'

# Veri aralığı
start_date = '2020-01-01'
end_date = '2023-02-27'

# Hisse senedi verilerini indirme
data = yf.download(symbol, start=start_date, end=end_date)

# Veri setini inceleme
print(data.head())

# Kapanış fiyatı grafiğini çizme
plt.plot(data['Close'])
plt.title(f"{symbol} Kapanış Fiyatı")
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.show()

# Basit Hareketli Ortalama hesaplama
sma20 = data['Close'].rolling(window=20).mean()
sma50 = data['Close'].rolling(window=50).mean()

# Basit Hareketli Ortalama grafiği çizme
plt.plot(data['Close'])
plt.plot(sma20, label='SMA20')
plt.plot(sma50, label='SMA50')
plt.title(f"{symbol} Kapanış Fiyatı ve Basit Hareketli Ortalama")
plt.xlabel('Tarih')
plt.ylabel('Fiyat')
plt.legend()
plt.show()

# Hisse senedi verilerini CSV dosyasına kaydetme
data.to_csv(f'{symbol}.csv', index=False)

