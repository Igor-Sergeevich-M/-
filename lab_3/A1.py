x1=int(input("Введите координату x1:"))
y1=int(input("Введите координату y1:"))
x2=int(input("Введите координату x2:"))
y2=int(input("Введите координату y2:"))
if x1>0 and y1>0 and x2>0 and y2>0: #L1 четверть
    print ("Yes,4")
elif x1<0 and y1>0 and x2<0 and y2>0: #L2 четверть
    print ("Yes,2")
elif x1<0 and y1<0 and x2<0 and y2<0: #L3 чертверть
    print ("Yes,3")
elif x1<0 and y1<0 and x2<0 and y2<0: #4 четверть
    print ("Yes,1")
else:
    print("No")
