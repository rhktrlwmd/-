#set page(width: 33.87cm, height: 19.05cm, margin: (left: 1.3cm, right: 1.3cm, top: 1.0cm, bottom: 1.0cm))
#set text(font: "Arial", size: 18pt, fill: rgb("#1F2933"))
#set heading(numbering: none)
#let accent = rgb("#0F4C81")
#let soft = rgb("#EAF1F8")

#let course_name = "Имитационное моделирование"
#let student_name = "Исаева Зарина Исмайилбековна"
#let group_name = "НКНбд–01–23"
#let teacher_name = "Кулябов Дмитрий Сергеевич"
#let lab_title = "Лабораторная работа 7. Дискретно-событийное моделирование"
#let objective = "Смоделировать систему массового обслуживания и систему с резервом и ремонтом в событийнoм представлении."

#let slide_title(title) = block(width: 100%, fill: accent, inset: 10pt, radius: 10pt)[#text(fill: white, size: 26pt, weight: "bold")[#title]]

#v(2.0cm)
#align(center)[#text(size: 28pt, weight: "bold", fill: accent)[#lab_title]]
#v(0.4cm)
#align(center)[#text(size: 18pt)[по дисциплине «#course_name»]]
#v(1.4cm)
#align(center)[Студент: #student_name]
#align(center)[Группа: #group_name]
#align(center)[Преподаватель: #teacher_name]

#pagebreak()
#slide_title([Цель и задачи])
#v(0.5cm)
- #objective
- Подготовить литературный источник, код, ноутбук, отчёт и презентацию.
- Выполнить вычислительный эксперимент и интерпретировать результаты.

#pagebreak()
#slide_title([Ход выполнения])
#v(0.5cm)
- Основной сценарий оформлен в формате qmd.
- Из источника автоматически собираются Julia-скрипт и ipynb.
- Результаты эксперимента сохраняются в csv и визуализируются графиками.

#pagebreak()
#slide_title([Основной результат])
#v(0.4cm)
#figure(
  image("../results/figures/mmc_main.png", height: 11.5cm),
  caption: [Очередь и загрузка в системе M/M/c],
)

#pagebreak()
#slide_title([Анализ чувствительности])
#v(0.4cm)
#figure(
  image("../results/figures/ross_reserve.png", height: 11.5cm),
  caption: [Среднее время до отказа в модели Росса],
)

#pagebreak()
#slide_title([Ключевые результаты])
#v(0.5cm)
- reserve = 1, mean_crash_time = 6
- reserve = 2, mean_crash_time = 10.035
- reserve = 3, mean_crash_time = 14.194
- reserve = 4, mean_crash_time = 19.216
#v(0.5cm)
#table(columns: 2,
  stroke: rgb("#B8C2CC"),
  inset: 8pt,
  fill: (x, y) => if y == 0 { soft } else { white },
    [reserve],
    [mean_crash_time],
    [1],
    [6],
    [2],
    [10.035],
    [3],
    [14.194],
    [4],
    [19.216],
)

#pagebreak()
#slide_title([Выводы])
#v(0.5cm)
- Лабораторная работа оформлена в едином академическом стиле.
- Подготовлены материалы для показа преподавателю и публикации в репозитории.
- Полученные результаты можно использовать для сравнения альтернативных сценариев.
