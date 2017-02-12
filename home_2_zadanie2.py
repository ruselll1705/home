x=input('Введите слово для проверки программы: ',)
x1=x[:int(len(x)/2)+len(x)%2]
x2=x[(int(len(x)/2)+len(x)%2):]
print(x2+x1)
