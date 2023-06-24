class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        visited = [False] * (n + 1)

        def combi(number, path):
            if len(path) == k:
                answer.append(path[:])
                print(path)
                return

            visited[number] = True

            for num in range(number, n + 1):
                if not visited[num]:
                    path.append(num)
                    combi(num, path)
                    path.pop()

            visited[number] = False

        for number in range(1, n + 1):
            combi(number, [number])

        return answer
