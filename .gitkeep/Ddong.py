# 스택과 최대치 정의
stack = 0
max_stack = 5

def A():
    global stack
    if stack + 1 <= max_stack:
        stack += 1
        print(f"현재 스택: {stack}")
    else:
        print(f"스택 오바했다 {stack}")
        stack = max_stack
    

def B():
    global stack
    if stack + 2 <= max_stack:  # 오타 수정: max_stackck -> max_stack
        stack += 2
        print(f"현재 스택: {stack}")
    else:
        print(f"스택 오바했다 {stack}")
        stack = max_stack

def C():
    global stack
    if stack + 3 <= max_stack:
        stack += 3
        print(f"현재 스택: {stack}")
    else:
        print(f"스택 오바했다 {stack}")
        stack = max_stack

# 예시 실행
stack = 3
A()  # 스택 3 -> 4
B()  # 스택 4 -> 5
A()  # 스택이 이미 최대치이므로 변화 없음
