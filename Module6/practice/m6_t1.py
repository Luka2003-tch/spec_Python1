"""
Написать программу для подсчета размера всех .py файлов в текущей папке.
"""
impot os
import sys
import platform

#Применение среды для словаря
print(os.environ)
#Система на которой работаем + имя файла - 'Luka_File'
print (platform_system()) #out -> Windows
print (os.name) #out 'Luka_File'
print(sys.platform) ## out -> 'win32
#Папка в которой питон ищет файл 
print(sys.path)
path = input ('Write path -> ')    
os.chdir(path)                            
dir_work = os.listdir(path)        
i = 0
Luka_File = 0
for folder in dir_work:
  dir_work[i] = os.path.getsize(i)
Luka_File = Luka_File + folder_size[i]

print("Размер каталога = ", 'Luka_File')
main()

 
