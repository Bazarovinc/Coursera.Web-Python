def calculate(data, findall):
    matches = findall(r'([abc]){1}([\+\-])?=([abc]?)([\+\-]?\d*)')  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        for a, sign, b, number in matches:
            right = data.get(b, 0) + int(number or 0)
            if sign == "-":
                data[a] -= right
            elif sign == "+":
                data[a] += right
            else:
                data[a] = right
        """
        Мое решение:
        if s == '':
            if v2 != '':
                data[v1] = data.get(v2, 0) + int(n or 0)
            else:
                data[v1] = int(n or 0)
        elif s in '+-':
            if v2 != '' and s == '+':
                data[v1] += data.get(v2, 0) + int(n or 0)
            elif s == '+':
                data[v1] += int(n or 0)
            if v2 != '' and s == '-':
                data[v1] -= data.get(v2, 0) + int(n or 0)
            elif s == '-':
                data[v1] -= int(n or 0)"""
    return data
