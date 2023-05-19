import threading
import time

def say(msg): # 데이터 수집하는 함수
    while True:
        time.sleep(1)
        print(msg)
# thread 3개 생성, 시작
for msg in ['you','need','python']:
    t = threading.Thread(target=say, args=(msg,))
    t.daemon = True
    t.start()

for i in range(100):
    time.sleep(0.01)
    print(i)