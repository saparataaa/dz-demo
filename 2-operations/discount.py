price = int(input("Введите цену товара:"))
discount_percent = int(input("Введите процент скидки:"))
discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount
print(f"цена со скидкой: {final_price}")