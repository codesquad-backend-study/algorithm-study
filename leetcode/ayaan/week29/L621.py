import collections


def leastInterval(tasks, n):
    task_counter = collections.Counter(tasks)
    result = 0
    print(task_counter)

    while True:
        sub_count = 0
        # most_common(n + 1) : 개수가 많은 task부터 n + 1개를 가져온다
        for task, _ in task_counter.most_common(n + 1):
            sub_count += 1
            result += 1

            task_counter.subtract(task)
            # 0인 task 제거
            task_counter += collections.Counter()

        if not task_counter:
            break

        # idle 개수 추가
        result += n - sub_count + 1

    print(result)


leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2)
