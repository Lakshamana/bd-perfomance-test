
import os
import random
import datetime
import csv
import threading
import time

random.seed(os.urandom(16))

pessoa = {"sexo": ["M","F"],
          "idade":[str(x) for x in range(128)],
          "renda":[str(x) for x in range(1024)],
          "escolaridade":["0","1","2","3"],
          "idioma":[str(x) for x in range(4096)],
          "pais":[str(x) for x in range(256)],
          "localizador":["-1.45502-48.5024","-23.5489-46.6388"]}

def generate_data():
        data = (pessoa["sexo"][random.randint(0,1)],random.randint(0,127),random.randint(0,1023),random.randint(0,3),
                random.randint(0,4095),random.randint(0,255),pessoa["localizador"][random.randint(0,1)])
        with open("test.csv",'a',newline='') as file:
            datawriter = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #datawriter.writerow(['Sexo','idade','renda','escolaridade','idioma','pais','localizador'])
            for x in range(10**7):
                datawriter.writerow([pessoa["sexo"][random.randint(0,1)],random.randint(0,127),random.randint(0,3),random.randint(0,1023),
                random.randint(0,4095),pessoa["localizador"][random.randint(0,1)],random.randint(0,255)])
print(datetime.datetime.now())
t1=threading.Thread(target=generate_data)
t2=threading.Thread(target=generate_data)
t3=threading.Thread(target=generate_data)
t4=threading.Thread(target=generate_data)
t5=threading.Thread(target=generate_data)
t6=threading.Thread(target=generate_data)
t7=threading.Thread(target=generate_data)
t8=threading.Thread(target=generate_data)
t9=threading.Thread(target=generate_data)
t10=threading.Thread(target=generate_data)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
while (t10.isAlive()):
    print("thread 10 is still alive")
    time.sleep(5)
print(datetime.datetime.now())