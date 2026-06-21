#set page(width: 33.87cm, height: 19.05cm, margin: (left: 1.3cm, right: 1.3cm, top: 1.0cm, bottom: 1.0cm))
#set text(font: "Arial", size: 18pt, fill: rgb("#1F2933"))
#set heading(numbering: none)
#let accent = rgb("#0F4C81")
#let soft = rgb("#EAF1F8")

#let course_name = "Имитационное моделирование"
#let student_name = "Исаева Зарина Исмайилбековна"
#let group_name = "НКНбд–01–23"
#let teacher_name = "Кулябов Дмитрий Сергеевич"
#let lab_title = "Лабораторная работа 1. Экспоненциальный рост"
#let objective = "Освоить структуру проекта, литературный стиль исходников и базовую модель экспоненциального роста."

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
  image("../results/figures/growth_main.png", height: 11.5cm),
  caption: [Сравнение аналитического решения и схемы Эйлера],
)

#pagebreak()
#slide_title([Анализ чувствительности])
#v(0.4cm)
#figure(
  image("../results/figures/growth_sweep.png", height: 11.5cm),
  caption: [Влияние коэффициента роста на траекторию модели],
)

#pagebreak()
#slide_title([Ключевые результаты])
#v(0.5cm)
- alpha = 0.15, Максимум = 60.4965
- alpha = 0.25, Максимум = 200.855
- alpha = 0.35, Максимум = 666.863
- alpha = 0.45, Максимум = 2214.06
#v(0.5cm)
#table(columns: 2,
  stroke: rgb("#B8C2CC"),
  inset: 8pt,
  fill: (x, y) => if y == 0 { soft } else { white },
    [alpha],
    [Максимум],
    [0.15],
    [60.4965],
    [0.25],
    [200.855],
    [0.35],
    [666.863],
    [0.45],
    [2214.06],
)

#pagebreak()
#slide_title([Выводы])
#v(0.5cm)
- Лабораторная работа оформлена в едином академическом стиле.
- Подготовлены материалы для показа преподавателю и публикации в репозитории.
- Полученные результаты можно использовать для сравнения альтернативных сценариев.
