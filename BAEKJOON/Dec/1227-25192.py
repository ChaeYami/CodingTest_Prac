import sys
input = sys.stdin.readline

N = int(input())

new_chat = set()
cnt_gomgom = 0

for _ in range(N):
    chat = input().rstrip()
    if chat == 'ENTER': # 새로운 사람이 들어오면
        new_chat.clear() # 채팅 정보 초기화
            
    elif chat != 'ENTER':
        if chat not in new_chat: # 해당 사용자가 처음 채팅을 보냈다면
            new_chat.add(chat)
            cnt_gomgom+= 1
        
print(cnt_gomgom)