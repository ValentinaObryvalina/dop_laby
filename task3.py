import re
from functools import reduce


news = '5 Курс биткоина вырос до 1000 долларов.10 В новогоднюю ночь выйдет новая первая серия' \
       ' нового сезона "Шерлока".7 В Новосибирске из автобуса сбежала кондуктор.1 Самолет «Почты' \
       ' России» вылетел с опозданием в несколько месяцев.20 Козёл Тимур подружился с тигром Амуром.' \
       '10 Инженерам из Space X удалось посадить первую ступень ракеты на землю.'


def make_news():
    news_and_levels = dict()

    for item in news.split('.'):  # добавляе каждую новость в список отдельно
        if not re.findall(r'^\d*', item) == [''] and int(re.findall(r'^\d*', item)[0]) not in news_and_levels:
            news_and_levels[int(re.findall(r'^\d*', item)[0])] = re.sub(r'^\d*', '', item)  # добавляем в словарь ключ - показатель интереса новости, значение - новость без цифр

    return news_and_levels


if __name__ == "__main__":
    news_with_levels = make_news()
    # не знаю как через reduce
    max_mark = 0

    for mark, new in news_with_levels.items():
        if mark > max_mark:
            max_mark = mark
            print(new)