class CLASSS:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.deleted = False

def solution(n, k, cmd):

    rows = [CLASSS(i) for i in range(n)]
    for i in range(n - 1):
        rows[i].next = rows[i + 1]
        rows[i + 1].prev = rows[i]

    current = rows[k]
    stack = []

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                if current.prev:
                    current = current.prev
        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                if current.next:
                    current = current.next
        elif c[0] == 'C':
            stack.append(current)
            current.deleted = True

            # 현재 행이 마지막 행이면 이전 행을 선택
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            current = current.next if current.next else current.prev
        elif c[0] == 'Z':
            node = stack.pop()
            node.deleted = False

            if node.prev:
                node.prev.next = node
            if node.next:
                node.next.prev = node

    result = ['O' if not row.deleted else 'X' for row in rows]
    return ''.join(result)

# 예시 사용법
n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
print(solution(n, k, cmd))
