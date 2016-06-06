@echo off

rem parse xml file
java -jar D:\apktoolAndDex\apktool\apktoolV2.jar d resources %1.apk -f -o L:\APKDecompiled\%1\
rem parse code
"C:\Program Files (x86)\HaoZip"\HaoZipC e L:\APKDecompiled\%1.apk -oL:\APKDecompiled\%1 classes.dex *.arsc 
D:\apktoolAndDex\dex\dex2jar.bat L:\APKDecompiled\%1\classes.dex



