def say_hello(name):
    print("Hello, " + name)

say_hello("VS Code")


def say_day_of_week(date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return print("Today is " + days[date.weekday()])
