# Öklid Mesafesi Hesaplayıcı

Bu Python programı, 2D uzayda verilen noktalar arasındaki Öklid mesafesini hesaplar. Öklid mesafesi, iki nokta arasındaki düz çizgi mesafesidir ve aşağıdaki formülle hesaplanır:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

---

## Özellikler

### 1. `points` Listesi
- **Açıklama:**  
  2D uzaydaki noktalar, `(x, y)` formatında bir liste olarak tanımlanmıştır.
- **Örnek:**  
  ```python
  points = [(2, 3), (5, 7), (1, 8), (4, 2)]
