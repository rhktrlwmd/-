#set page(width: 33.87cm, height: 19.05cm, margin: (left: 1.3cm, right: 1.3cm, top: 1.0cm, bottom: 1.0cm))
#set text(font: "Arial", size: 18pt, fill: rgb("#1F2933"))
#set heading(numbering: none)
#let accent = rgb("#0F4C81")
#let soft = rgb("#EAF1F8")

#let course_name = "Имитационное моделирование"
#let student_name = "Исаева Зарина Исмайилбековна"
#let group_name = "НКНбд–01–23"
#let teacher_name = "Кулябов Дмитрий Сергеевич"
#let lab_title = "Лабораторная работа 3. Агентное моделирование"
#let objective = "Построить агентную клеточную модель Daisyworld и изучить механизм климатической саморегуляции."

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
  image("../results/figures/daisy_timeseries.png", height: 11.5cm),
  caption: [Численность маргариток и температура среды во времени],
)

#pagebreak()
#slide_title([Анализ чувствительности])
#v(0.4cm)
#figure(
  image("../results/figures/daisy_sweep.png", height: 11.5cm),
  caption: [Зависимость итоговой температуры от светимости],
)

#pagebreak()
#slide_title([Ключевые результаты])
#v(0.5cm)
- luminosity = 0.7, final_temperature = 21.212, final_black = 204, final_white = 228
- luminosity = 0.8, final_temperature = 24.53, final_black = 194, final_white = 203
- luminosity = 0.9, final_temperature = 27.855, final_black = 163, final_white = 156
- luminosity = 1, final_temperature = 30.953, final_black = 129, final_white = 135
- luminosity = 1.1, final_temperature = 34.208, final_black = 90, final_white = 89
#v(0.5cm)
#table(columns: 4,
  stroke: rgb("#B8C2CC"),
  inset: 8pt,
  fill: (x, y) => if y == 0 { soft } else { white },
    [luminosity],
    [final_temperature],
    [final_black],
    [final_white],
    [0.7],
    [21.212],
    [204],
    [228],
    [0.8],
    [24.53],
    [194],
    [203],
    [0.9],
    [27.855],
    [163],
    [156],
    [1],
    [30.953],
    [129],
    [135],
    [1.1],
    [34.208],
    [90],
    [89],
)

#pagebreak()
#slide_title([Выводы])
#v(0.5cm)
- Лабораторная работа оформлена в едином академическом стиле.
- Подготовлены материалы для показа преподавателю и публикации в репозитории.
- Полученные результаты можно использовать для сравнения альтернативных сценариев.
