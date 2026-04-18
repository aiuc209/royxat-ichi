mahsulotlar = [
    {"nomi": "Apple", "price": 10000},
    {"nomi": "Banana", "price": 5000},
    {"nomi": "Cherry", "price": 20000}
]

for mahsulot in mahsulotlar:
    soliq = mahsulot["price"] * 0.15
    mahsulot["price"] += soliq

print(mahsulotlar)
