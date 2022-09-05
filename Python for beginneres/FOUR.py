#list القوائم
section = ['CS', 'IT','IS']
marks = [69 , 65 , 64 , 66]

#print(section)
#print(marks)
#print(section[:2])# طباعة قبل العنصر
#print(section[2:])#طياعة بعد
#print(section[0:2])

#Funcion
section.append('PL')# اضافة في اخر القائمة
add= section.insert(1,'ID')#اضافة في موقع معين داخل القائمة
section.extend(marks)#الحاق بالقائمة
section.remove('ID')#حذف عنص محدد في القاتمة
section.pop()
ser = section.count(2)
print(ser)
print(section)




