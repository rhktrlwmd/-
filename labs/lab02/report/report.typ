#set page(margin: (left: 3cm, right: 1.8cm, top: 2cm, bottom: 2cm))
#set text(font: "Times New Roman", size: 14pt)
#set heading(numbering: none)
#show figure.caption: set text(size: 11pt, style: "italic")

#let course_name = "Имитационное моделирование"
#let student_name = "Исаева Зарина Исмайилбековна"
#let group_name = "НКНбд–01–23"
#let teacher_name = "Кулябов Дмитрий Сергеевич"
#let teacher_title = "преподаватель дисциплины"
#let lab_title = "Лабораторная работа 2. Основные модели"
#let lab_subtitle = "SIR и Лотка–Вольтерра"
#let objective = "Исследовать детерминированные модели распространения инфекции и взаимодействия хищник–жертва."
#let year = "2026"

#align(center)[
  МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ \
  РОССИЙСКОЙ ФЕДЕРАЦИИ \
  Федеральное государственное автономное образовательное учреждение высшего образования \
  «РОССИЙСКИЙ УНИВЕРСИТЕТ ДРУЖБЫ НАРОДОВ ИМЕНИ ПАТРИСА ЛУМУМБЫ» \
  Факультет физико-математических и естественных наук \
  Кафедра математического моделирования и искусственного интеллекта
]

#v(3.0cm)
#align(center)[#text(size: 18pt, weight: "bold")[ОТЧЁТ]]
#align(center)[по лабораторной работе №2]
#align(center)[#lab_title]
#align(center)[по дисциплине «#course_name»]

#v(3.5cm)
#align(right)[
  Выполнила: #student_name \
  Группа: #group_name \
  Преподаватель: #teacher_name, #teacher_title
]

#v(4.5cm)
#align(center)[Москва, #year]

#pagebreak()

= Цель работы
#objective

= Теоретические сведения
Работа основана на классических моделях имитационного моделирования и на воспроизводимой вычислительной схеме: литературный источник, исполняемый код, таблицы результатов и итоговые визуализации собираются автоматически в едином шаблоне.

= Ход выполнения
1. Подготовлен литературный источник в формате qmd.
2. Из источника автоматически сформирован исполняемый Julia-код.
3. Выполнен вычислительный эксперимент и сохранены результаты.
4. По полученным данным построены графики и сводные таблицы.

= Результаты моделирования

#figure(
  image("../results/figures/sir_dynamics.png", width: 86%),
  caption: [Динамика SIR-модели],
)

#figure(
  image("../results/figures/lotka_volterra.png", width: 86%),
  caption: [Фазовый портрет и временные ряды модели Лотки–Вольтерры],
)

#figure(
  table(columns: 2,
    stroke: rgb("#B8C2CC"),
    inset: 8pt,
    fill: (x, y) => if y == 0 { rgb("#EAF1F8") } else { white },
    [Показатель],
    [Значение],
    [Пик зараженных],
    [0.36],
    [Время пика],
    [16.4],
  ),
  caption: [Таблица основных результатов],
)

= Анализ результатов
Первый график показывает основную динамику модели, а второй отражает чувствительность результатов к изменению параметров. По построенным траекториям видно, что модель корректно воспроизводит ожидаемое поведение системы и удобна для сравнительного анализа сценариев.

= Выводы
В результате выполнения лабораторной работы подготовлен полный комплект воспроизводимых материалов: исходники, код, ноутбук, отчёт, презентация и архив исходных данных. Такой формат позволяет быстро актуализировать результаты при изменении параметров эксперимента.

= Список литературы
- William O. Kermack and Anderson G. McKendrick. A Contribution to the Mathematical Theory of Epidemics. Proceedings of the Royal Society A, 1927.
- Alfred J. Lotka. Elements of Physical Biology. Williams and Wilkins, 1925.
- Vito Volterra. Variazioni e fluttuazioni del numero d'individui in specie animali conviventi. Memorie della Reale Accademia Nazionale dei Lincei, 1926.
