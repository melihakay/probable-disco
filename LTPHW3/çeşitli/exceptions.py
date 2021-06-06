x = input("x = ??\n >")
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except:
    print('Linux function was not executed')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')
