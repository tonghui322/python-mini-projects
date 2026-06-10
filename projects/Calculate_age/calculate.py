#输入姓名和年龄 三种不同形式输出你的年龄 周岁 总月数 总天数

if __name__ == "__main__":
    name = input("请输入姓名:")
    age = input("请输入年龄:")
    try:
        #验证年龄是否为数字
        age_year = int(age)
        full_year = age_year + 1
        age_month = age_year * 12
        age_day = age_year * 365
        print(f"{name},你{full_year}周岁，{age_month}个月，{age_day}天。")
    except ValueError:
        print("输入年龄有误！")


