import os

hz = ['iso']

for roots, dirs, files in os.walk('D:\专业'):
    for file in files:
        file_hz = file.split('.')[-1]
        # print(file_hz)
        file_path = os.path.join(roots, file)
        if file_hz in hz:
            print(file_path)
