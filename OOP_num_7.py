def sum_numbers(*args):
    sum_num = 0
    for i in args:
        sum_num += i
    return sum_num

result = sum_numbers(1, 2, 3, 4)
print(result)

def print_user_info(**kwargs):
    i = []
    for key, value in kwargs.items():
        i.append(f"{key}: {value}")
    print(", ".join(i))

print_user_info(name="Dana", age=30, city="Tel Aviv")


def combine_values(*args, **kwargs):
    sum_num = 0
    for i in args:
        sum_num += i
    print(f"Sum: {sum_num}")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

combine_values(2, 4, 6, name="Tom", job="Dev")


def greet_user(**kwargs):
    name = kwargs.get("name", "guest")
    print(f"Hello {name}")

greet_user(name="Lior")
greet_user()