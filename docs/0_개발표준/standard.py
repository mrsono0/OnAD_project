# 긴 함수 이름
def long_function_name(variable1,
    variable2, variable3, variable4,
    variable5):
    print(variable1)

# 긴 조건문의 경우 추가적인 들여쓰기를 사용하지 않음
if (this_is_one_thing and
    that_is_another_thing):
    do_something()

# 리스트등의 컨테이너 타입의 목록이 길 떄
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 

# 인덱싱과 슬라이싱의 경우
yes:
    a[:5]
    a[1:5]
    a[5][4][key]
no : 
    a[ :5 ]
    a[1: 5]
    a[ 5 ] [ 4 ] [ key ]

# 딕셔너리의 경우 : 이후에 한번의 띄어쓰기
yes_dic = {
    key: value,
    key1: value1
}
no_dic = {
    key:value,
    key1:value1
}

# 메소드끼리는 1줄, 함수끼리는 두줄
# 메소드의 경우
class ClassName():
    def __init__(self):
        return None
    
    def func1(self):
        return None

# 일반함수의 경우
def asdf():
    return None


def func2():
    return None

# 함수의 인자는 띄우지 않는다.
yes:
    create_new_dict(key=key1, value=value1)

no:
    create_new_dict(key = key2, value = value2)