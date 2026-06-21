#set page(width: 33.87cm, height: 19.05cm, margin: (left: 1.3cm, right: 1.3cm, top: 1.0cm, bottom: 1.0cm))
#set text(font: "Arial", size: 18pt, fill: rgb("#1F2933"))
#set heading(numbering: none)
#let accent = rgb("#0F4C81")
#let soft = rgb("#EAF1F8")

#let course_name = "Имитационное моделирование"
#let student_name = "Исаева Зарина Исмайилбековна"
#let group_name = "НКНбд–01–23"
#let teacher_name = "Кулябов Дмитрий Сергеевич"
#let lab_title = "Лабораторная работа 5. Сети Петри"
#let objective = "Показать взаимосвязь маркировки сети Петри и проблем синхронизации на примере обедающих философов."

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
  image("../results/figures/philosophers_states.png", height: 11.5cm),
  caption: [Сравнение числа философов в состоянии ожидания и еды],
)

#pagebreak()
#slide_title([Анализ чувствительности])
#v(0.4cm)
#figure(
  image("../results/figures/philosophers_sweep.png", height: 11.5cm),
  caption: [Сравнение пропускной способности стратегий для разных размеров стола],
)

#pagebreak()
#slide_title([Ключевые результаты])
#v(0.5cm)
- strategy = naive, philosophers = 4, throughput = 0.982
- strategy = naive, philosophers = 5, throughput = 1.246
- strategy = naive, philosophers = 6, throughput = 1.436
- strategy = naive, philosophers = 7, throughput = 1.704
- strategy = naive, philosophers = 8, throughput = 1.973
#v(0.5cm)
#table(columns: 3,
  stroke: rgb("#B8C2CC"),
  inset: 8pt,
  fill: (x, y) => if y == 0 { soft } else { white },
    [strategy],
    [philosophers],
    [throughput],
    [naive],
    [4],
    [0.982],
    [naive],
    [5],
    [1.246],
    [naive],
    [6],
    [1.436],
    [naive],
    [7],
    [1.704],
    [naive],
    [8],
    [1.973],
)

#pagebreak()
#slide_title([Выводы])
#v(0.5cm)
- Лабораторная работа оформлена в едином академическом стиле.
- Подготовлены материалы для показа преподавателю и публикации в репозитории.
- Полученные результаты можно использовать для сравнения альтернативных сценариев.
