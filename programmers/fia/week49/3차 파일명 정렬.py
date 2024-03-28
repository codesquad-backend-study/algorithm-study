def solution(files):
    def compare_key(file_name):

        head = ''
        for i, char in enumerate(file_name):
            if char.isdigit():
                break
            head += char.lower()

        number = ''
        for index in range(i, len(file_name)):
            if len(number) >= 5:
                break

            if file_name[index].isdigit():
                number += file_name[index]
            else:
                break

        return [head, int(number)]

    files.sort(key=compare_key)

    return files
