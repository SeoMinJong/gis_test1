
def decorator(func):
    def decorated(input_text):
        print('func start!!!')
        func(input_text)
        print('func end...')

    return decorated

@decorator
def new_create(input_text):
    print(input_text)


def decorator_figure(func):
    def decorated(W, H):
        if W > 0 and H > 0:
            func(W, H)
        else:
            raise ValueError('계산할 수 있는 수인지 확인해주세요')

    return decorated

@decorator_figure
def triangle(W,H):
    result = (W*H)/2
    print(result)

    return result


@decorator_figure
def Square(W,H):
    result = W*H
    print(result)

    return result

# triangle(3,2)
# triangle(3,0)
Square(3,2)
Square(3,0)

