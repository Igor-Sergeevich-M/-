pre = int(input("Введите предыдущее: "))
cur = int(input("Введите текущее показание : "))
volume_used = cur - pre
if cur < pre:
    volume_used = 10000 - pre + cur
else:
    volume_used = cur - pre
if volume_used <= 300:
    total_cost = 21.00
elif volume_used <= 600:
    total_cost = 21.00 + (volume_used - 300) * 0.06
elif volume_used <= 800:
    total_cost = 21.00 + (300 * 0.06) + (volume_used - 600) * 0.04
else:
    total_cost = 21.00 + (300 * 0.06) + (200 * 0.04) + (volume_used - 800) * 0.025
total_cost = round(total_cost, 2)
average_cost = round(total_cost / volume_used, 2)

print("Предыдущее  Текущее   Использовано   К оплате   Средняя цена")
print("  {}       {}    {}   {:.2f}       {:.2f}".format(pre, cur, volume_used, total_cost, average_cost))
