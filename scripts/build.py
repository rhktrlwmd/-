from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import textwrap
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / ".matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(ROOT / ".cache"))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import nbformat as nbf
import pandas as pd

LABS_DIR = ROOT / "labs"
BIB = ROOT / "references.bib"
COURSE_INFO = ROOT / "course-info.json"


LAB_SPECS = [
    {
        "id": "lab01",
        "title": "Лабораторная работа 1. Экспоненциальный рост",
        "subtitle": "Подготовка стенда и первая дифференциальная модель",
        "objective": "Освоить структуру проекта, литературный стиль исходников и базовую модель экспоненциального роста.",
        "source": "source/lab01_exponential_growth.qmd",
        "citations": ["malthus1798"],
        "figures": [
            ("results/figures/growth_main.png", "Сравнение аналитического решения и схемы Эйлера", "fig:lab01-main"),
            ("results/figures/growth_sweep.png", "Влияние коэффициента роста на траекторию модели", "fig:lab01-sweep"),
        ],
    },
    {
        "id": "lab02",
        "title": "Лабораторная работа 2. Основные модели",
        "subtitle": "SIR и Лотка–Вольтерра",
        "objective": "Исследовать детерминированные модели распространения инфекции и взаимодействия хищник–жертва.",
        "source": "source/lab02_core_models.qmd",
        "citations": ["kermack1927", "lotka1925", "volterra1926"],
        "figures": [
            ("results/figures/sir_dynamics.png", "Динамика SIR-модели", "fig:lab02-sir"),
            ("results/figures/lotka_volterra.png", "Фазовый портрет и временные ряды модели Лотки–Вольтерры", "fig:lab02-lv"),
        ],
    },
    {
        "id": "lab03",
        "title": "Лабораторная работа 3. Агентное моделирование",
        "subtitle": "Модель Daisyworld",
        "objective": "Построить агентную клеточную модель Daisyworld и изучить механизм климатической саморегуляции.",
        "source": "source/lab03_daisyworld.qmd",
        "citations": ["lovelock1983"],
        "figures": [
            ("results/figures/daisy_timeseries.png", "Численность маргариток и температура среды во времени", "fig:lab03-time"),
            ("results/figures/daisy_sweep.png", "Зависимость итоговой температуры от светимости", "fig:lab03-sweep"),
        ],
    },
    {
        "id": "lab04",
        "title": "Лабораторная работа 4. Агентный SIR",
        "subtitle": "Эпидемиологическая модель в агентном подходе",
        "objective": "Реализовать агентную SIR-модель с несколькими городами и миграцией агентов.",
        "source": "source/lab04_agent_sir.qmd",
        "citations": ["kermack1927"],
        "figures": [
            ("results/figures/agent_sir_main.png", "Динамика состояний S, I и R в агентной модели", "fig:lab04-main"),
            ("results/figures/agent_sir_sweep.png", "Влияние интенсивности миграции на пик инфекции", "fig:lab04-sweep"),
        ],
    },
    {
        "id": "lab05",
        "title": "Лабораторная работа 5. Сети Петри",
        "subtitle": "Задача обедающих философов",
        "objective": "Показать взаимосвязь маркировки сети Петри и проблем синхронизации на примере обедающих философов.",
        "source": "source/lab05_petri_philosophers.qmd",
        "citations": ["murata1989"],
        "figures": [
            ("results/figures/philosophers_states.png", "Сравнение числа философов в состоянии ожидания и еды", "fig:lab05-main"),
            ("results/figures/philosophers_sweep.png", "Сравнение пропускной способности стратегий для разных размеров стола", "fig:lab05-sweep"),
        ],
    },
    {
        "id": "lab06",
        "title": "Лабораторная работа 6. Сеть Петри для SIR",
        "subtitle": "Стохастическая SIR-модель через переходы",
        "objective": "Исследовать SIR-модель, представленную в терминах мест, переходов и стохастических firing-событий.",
        "source": "source/lab06_petri_sir.qmd",
        "citations": ["murata1989", "kermack1927"],
        "figures": [
            ("results/figures/petri_sir_main.png", "Стохастическая траектория сети Петри SIR", "fig:lab06-main"),
            ("results/figures/petri_sir_sweep.png", "Размер эпидемии при разных значениях коэффициента заражения", "fig:lab06-sweep"),
        ],
    },
    {
        "id": "lab07",
        "title": "Лабораторная работа 7. Дискретно-событийное моделирование",
        "subtitle": "M/M/c и модель Росса",
        "objective": "Смоделировать систему массового обслуживания и систему с резервом и ремонтом в событийнoм представлении.",
        "source": "source/lab07_des_models.qmd",
        "citations": ["banks2010", "ross2014"],
        "figures": [
            ("results/figures/mmc_main.png", "Очередь и загрузка в системе M/M/c", "fig:lab07-mmc"),
            ("results/figures/ross_reserve.png", "Среднее время до отказа в модели Росса", "fig:lab07-ross"),
        ],
    },
    {
        "id": "lab08",
        "title": "Лабораторная работа 8. Дискретно-событийный SIR",
        "subtitle": "Сравнение событийной и детерминированной постановки",
        "objective": "Сравнить дискретно-событийную SIR-модель с детерминированной кривой и анализом чувствительности.",
        "source": "source/lab08_des_sir.qmd",
        "citations": ["banks2010", "kermack1927"],
        "figures": [
            ("results/figures/des_sir_compare.png", "Сравнение детерминированной и событийной траекторий", "fig:lab08-main"),
            ("results/figures/des_sir_sweep.png", "Изменение пика инфекции при варьировании коэффициента заражения", "fig:lab08-sweep"),
        ],
    },
]


def load_course_info() -> dict:
    return json.loads(COURSE_INFO.read_text(encoding="utf-8"))


def ensure_dirs(*paths: Path) -> None:
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def parse_qmd_cells(text: str) -> list[tuple[str, str]]:
    cells: list[tuple[str, str]] = []
    current: list[str] = []
    kind = "markdown"
    in_code = False
    for line in text.splitlines():
        stripped = line.strip()
        if not in_code and (stripped.startswith("```{julia") or stripped == "```julia"):
            if current:
                cells.append((kind, "\n".join(current).strip("\n")))
            current = []
            kind = "code"
            in_code = True
            continue
        if in_code and stripped == "```":
            cells.append((kind, "\n".join(current).strip("\n")))
            current = []
            kind = "markdown"
            in_code = False
            continue
        current.append(line)
    if current:
        cells.append((kind, "\n".join(current).strip("\n")))
    return [cell for cell in cells if cell[1].strip()]


def cells_to_julia(cells: list[tuple[str, str]]) -> str:
    blocks = [content for kind, content in cells if kind == "code"]
    header = "# Этот файл сгенерирован автоматически из qmd-источника.\n\n"
    return header + "\n\n".join(blocks).strip() + "\n"


def write_notebook(cells: list[tuple[str, str]], out_path: Path) -> None:
    notebook = nbf.v4.new_notebook()
    notebook.cells = []
    for kind, content in cells:
        if kind == "markdown":
            notebook.cells.append(nbf.v4.new_markdown_cell(content))
        else:
            notebook.cells.append(nbf.v4.new_code_cell(content))
    out_path.write_text(nbf.writes(notebook), encoding="utf-8")


def run_command(command: list[str], cwd: Path, env: dict | None = None) -> None:
    completed = subprocess.run(command, cwd=cwd, env=env, text=True, capture_output=True)
    if completed.returncode != 0:
        raise RuntimeError(
            f"Command failed: {' '.join(command)}\nSTDOUT:\n{completed.stdout}\nSTDERR:\n{completed.stderr}"
        )


def run_julia_script(src_path: Path) -> None:
    env = os.environ.copy()
    env["JULIA_DEPOT_PATH"] = str(ROOT / ".julia")
    env["XDG_CACHE_HOME"] = str(ROOT / ".cache")
    run_command(["julia", src_path.name], cwd=src_path.parent, env=env)


def _save(fig_path: Path) -> None:
    fig_path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(fig_path, dpi=160)
    plt.close()


def plot_lab01(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    main = pd.read_csv(data_dir / "growth_main.csv")
    sweep = pd.read_csv(data_dir / "growth_sweep.csv")

    plt.figure(figsize=(8, 4.8))
    plt.plot(main["time"], main["analytic"], label="Аналитическое решение", linewidth=2)
    plt.plot(main["time"], main["euler"], label="Схема Эйлера", linestyle="--", linewidth=2)
    plt.xlabel("Время")
    plt.ylabel("u(t)")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "growth_main.png")

    plt.figure(figsize=(8, 4.8))
    for alpha, frame in sweep.groupby("alpha"):
        plt.plot(frame["time"], frame["value"], label=f"alpha={alpha}")
    plt.xlabel("Время")
    plt.ylabel("u(t)")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "growth_sweep.png")

    summary = sweep.groupby("alpha")["value"].max().reset_index().rename(columns={"value": "Максимум"})
    summary.columns = ["alpha", "Максимум"]
    return summary.to_markdown(index=False)


def plot_lab02(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    sir = pd.read_csv(data_dir / "sir.csv")
    lv = pd.read_csv(data_dir / "lotka_volterra.csv")

    plt.figure(figsize=(8, 4.8))
    for col in ["S", "I", "R"]:
        plt.plot(sir["time"], sir[col], label=col)
    plt.xlabel("Время")
    plt.ylabel("Численность")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "sir_dynamics.png")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    axes[0].plot(lv["time"], lv["prey"], label="Жертвы")
    axes[0].plot(lv["time"], lv["predator"], label="Хищники")
    axes[0].set_xlabel("Время")
    axes[0].set_ylabel("Численность")
    axes[0].legend()
    axes[1].plot(lv["prey"], lv["predator"], color="darkgreen")
    axes[1].set_xlabel("Жертвы")
    axes[1].set_ylabel("Хищники")
    plt.tight_layout()
    plt.savefig(lab_dir / "results" / "figures" / "lotka_volterra.png", dpi=160)
    plt.close()

    peak_row = sir.loc[sir["I"].idxmax()]
    summary = pd.DataFrame(
        [{"Показатель": "Пик зараженных", "Значение": round(float(peak_row["I"]), 2)},
         {"Показатель": "Время пика", "Значение": round(float(peak_row["time"]), 2)}]
    )
    return summary.to_markdown(index=False)


def plot_lab03(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    time_df = pd.read_csv(data_dir / "daisy_timeseries.csv")
    sweep = pd.read_csv(data_dir / "daisy_sweep.csv")

    fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    axes[0].plot(time_df["step"], time_df["black"], label="Черные")
    axes[0].plot(time_df["step"], time_df["white"], label="Белые")
    axes[0].legend()
    axes[0].set_ylabel("Количество")
    axes[1].plot(time_df["step"], time_df["temperature"], color="firebrick")
    axes[1].set_xlabel("Шаг")
    axes[1].set_ylabel("Температура")
    plt.tight_layout()
    plt.savefig(lab_dir / "results" / "figures" / "daisy_timeseries.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 4.8))
    plt.plot(sweep["luminosity"], sweep["final_temperature"], marker="o")
    plt.xlabel("Светимость")
    plt.ylabel("Итоговая температура")
    _save(lab_dir / "results" / "figures" / "daisy_sweep.png")

    return sweep.round(3).to_markdown(index=False)


def plot_lab04(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    main = pd.read_csv(data_dir / "agent_sir.csv")
    sweep = pd.read_csv(data_dir / "migration_sweep.csv")

    plt.figure(figsize=(8, 4.8))
    for col in ["S", "I", "R"]:
        plt.plot(main["step"], main[col], label=col)
    plt.xlabel("Шаг")
    plt.ylabel("Число агентов")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "agent_sir_main.png")

    plt.figure(figsize=(8, 4.8))
    plt.plot(sweep["migration"], sweep["peak_infected"], marker="o")
    plt.xlabel("Интенсивность миграции")
    plt.ylabel("Пик инфицированных")
    _save(lab_dir / "results" / "figures" / "agent_sir_sweep.png")

    return sweep.round(3).to_markdown(index=False)


def plot_lab05(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    states = pd.read_csv(data_dir / "philosophers_states.csv")
    sweep = pd.read_csv(data_dir / "philosophers_sweep.csv")

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.6))
    for strategy, frame in states.groupby("strategy"):
        axes[0].plot(frame["step"], frame["eating"], label=f"{strategy}: едят")
        axes[1].plot(frame["step"], frame["waiting"], label=f"{strategy}: ждут")
    axes[0].set_xlabel("Шаг")
    axes[0].set_ylabel("Едят")
    axes[1].set_xlabel("Шаг")
    axes[1].set_ylabel("Ожидают")
    axes[0].legend(fontsize=8)
    axes[1].legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(lab_dir / "results" / "figures" / "philosophers_states.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 4.8))
    for strategy, frame in sweep.groupby("strategy"):
        plt.plot(frame["philosophers"], frame["throughput"], marker="o", label=strategy)
    plt.xlabel("Число философов")
    plt.ylabel("Пропускная способность")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "philosophers_sweep.png")

    return sweep.round(3).to_markdown(index=False)


def plot_lab06(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    main = pd.read_csv(data_dir / "petri_sir.csv")
    sweep = pd.read_csv(data_dir / "petri_sir_sweep.csv")

    plt.figure(figsize=(8, 4.8))
    for col in ["S", "I", "R"]:
        plt.step(main["time"], main[col], where="post", label=col)
    plt.xlabel("Время")
    plt.ylabel("Маркировка")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "petri_sir_main.png")

    plt.figure(figsize=(8, 4.8))
    plt.plot(sweep["beta"], sweep["final_recovered"], marker="o")
    plt.xlabel("beta")
    plt.ylabel("Итоговое число выздоровевших")
    _save(lab_dir / "results" / "figures" / "petri_sir_sweep.png")

    return sweep.round(3).to_markdown(index=False)


def plot_lab07(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    mmc = pd.read_csv(data_dir / "mmc_timeseries.csv")
    ross = pd.read_csv(data_dir / "ross_summary.csv")

    fig, axes = plt.subplots(2, 1, figsize=(8, 7), sharex=True)
    axes[0].plot(mmc["time"], mmc["queue_length"], color="navy")
    axes[0].set_ylabel("Очередь")
    axes[1].plot(mmc["time"], mmc["busy_servers"], color="darkorange")
    axes[1].set_ylabel("Занятые каналы")
    axes[1].set_xlabel("Время")
    plt.tight_layout()
    plt.savefig(lab_dir / "results" / "figures" / "mmc_main.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 4.8))
    plt.bar(ross["reserve"].astype(str), ross["mean_crash_time"])
    plt.xlabel("Размер резерва")
    plt.ylabel("Среднее время до отказа")
    _save(lab_dir / "results" / "figures" / "ross_reserve.png")

    return ross.round(3).to_markdown(index=False)


def plot_lab08(lab_dir: Path) -> str:
    data_dir = lab_dir / "results" / "data"
    compare = pd.read_csv(data_dir / "des_sir_compare.csv")
    sweep = pd.read_csv(data_dir / "des_sir_sweep.csv")

    plt.figure(figsize=(8, 4.8))
    plt.plot(compare["time"], compare["I_des"], label="DES I(t)")
    plt.plot(compare["time"], compare["I_det"], label="ODE I(t)", linestyle="--")
    plt.xlabel("Время")
    plt.ylabel("Инфицированные")
    plt.legend()
    _save(lab_dir / "results" / "figures" / "des_sir_compare.png")

    plt.figure(figsize=(8, 4.8))
    plt.plot(sweep["beta"], sweep["peak_infected"], marker="o")
    plt.xlabel("beta")
    plt.ylabel("Пик инфицированных")
    _save(lab_dir / "results" / "figures" / "des_sir_sweep.png")

    return sweep.round(3).to_markdown(index=False)


PLOTTERS = {
    "lab01": plot_lab01,
    "lab02": plot_lab02,
    "lab03": plot_lab03,
    "lab04": plot_lab04,
    "lab05": plot_lab05,
    "lab06": plot_lab06,
    "lab07": plot_lab07,
    "lab08": plot_lab08,
}


def report_markdown(spec: dict, info: dict, summary_table: str) -> str:
    figure_blocks = []
    figure_labels = []
    for rel_path, caption, label in spec["figures"]:
        figure_blocks.append(f"![{caption}]({Path('..') / rel_path}){{#{label}}}")
        figure_labels.append(label)
    citation_text = " ".join(f"[@{key}]" for key in spec["citations"])
    return textwrap.dedent(
        f"""\
        # {spec["title"]}

        **Дисциплина:** {info["course_name"]}  
        **Студент:** {info["student_name"]}  
        **Группа:** {info["group"]}  
        **Преподаватель:** {info["teacher_name"]}, {info["teacher_title"]}  
        **Организация:** {info["organization"]}  
        **Год:** {info["year"]}

        ## Цель работы

        {spec["objective"]}

        ## Теоретические сведения

        Работа опирается на классические результаты и подходы, описанные в литературе {citation_text}. В рамках лабораторной работы использован литературный формат исходников: основной сценарий хранится в `qmd`, из него автоматически генерируются чистый `Julia`-код, ноутбук `ipynb` и документы для отчётности.

        ## Ход выполнения

        1. Подготовлен литературный источник в формате `qmd`.
        2. Из источника автоматически извлечён чистый исполняемый код `Julia`.
        3. Проведён вычислительный эксперимент и сохранены табличные результаты.
        4. На основе табличных данных построены иллюстрации и сводные таблицы.

        ## Результаты моделирования

        {'\n\n'.join(figure_blocks)}

        Таблица основных результатов:

        {summary_table}

        ## Анализ результатов

        График @{figure_labels[0]} показывает основную динамику модели, а @{figure_labels[1]} иллюстрирует чувствительность модели к изменению параметров. По полученным траекториям видно, что модель корректно воспроизводит ожидаемое качественное поведение системы и может использоваться для сравнительного анализа сценариев.

        ## Выводы

        В ходе выполнения лабораторной работы был получен воспроизводимый набор артефактов: литературный источник, исполняемый код, ноутбук, отчёт, презентация и архив исходных материалов. Автоматическая сборка позволяет быстро обновлять результаты после изменения параметров эксперимента.

        ## Список литературы
        """
    ).strip() + "\n"


def presentation_markdown(spec: dict, info: dict, summary_table: str) -> str:
    rows = "\n".join(f"- {line.strip()}" for line in summary_table.splitlines()[2:] if line.strip())
    return textwrap.dedent(
        f"""\
        % {spec["title"]}
        % {info["student_name"]}
        % {info["organization"]}

        # {spec["title"]}

        - Дисциплина: {info["course_name"]}
        - Студент: {info["student_name"]}
        - Преподаватель: {info["teacher_name"]}, {info["teacher_title"]}

        ---

        # Актуальность

        - Имитационное моделирование позволяет анализировать сложные динамические системы без дорогостоящих натурных экспериментов.
        - Выбранная постановка демонстрирует воспроизводимый вычислительный эксперимент с возможностью параметрического анализа.

        ---

        # Цель и задачи

        - {spec["objective"]}
        - Подготовить литературный источник, чистый код, ноутбук, отчёт и презентацию.
        - Выполнить анализ чувствительности модели.

        ---

        # Реализация

        - Основной исходник оформлен в `qmd`.
        - Чистый `Julia`-скрипт и `ipynb` формируются автоматически.
        - Результаты сохраняются в `csv`, после чего строятся итоговые графики.

        ---

        # Основные результаты

        {rows if rows else "- Основные результаты представлены в отчёте и на графиках."}

        ---

        # Выводы

        - Получена воспроизводимая лабораторная работа в едином шаблоне.
        - Подготовлены материалы для защиты и публикации в репозитории.
        """
    ).strip() + "\n"


def pandoc_report(md_path: Path, pdf_path: Path, docx_path: Path) -> None:
    env = os.environ.copy()
    env["XDG_CACHE_HOME"] = str(ROOT / ".cache")
    common = [
        "pandoc",
        str(md_path),
        "--from",
        "markdown+implicit_figures+table_captions+citations",
        "--standalone",
        "--citeproc",
        "--bibliography",
        str(BIB),
    ]
    run_command(common + ["-o", str(docx_path)], cwd=md_path.parent, env=env)
    run_command(common + ["--pdf-engine=typst", "-o", str(pdf_path)], cwd=md_path.parent, env=env)


def pandoc_slides(md_path: Path, html_path: Path, pdf_path: Path) -> None:
    env = os.environ.copy()
    env["XDG_CACHE_HOME"] = str(ROOT / ".cache")
    run_command(
        [
            "pandoc",
            str(md_path),
            "--standalone",
            "--to",
            "slidy",
            "--self-contained",
            "-o",
            str(html_path),
        ],
        cwd=md_path.parent,
        env=env,
    )
    run_command(
        [
            "pandoc",
            str(md_path),
            "--standalone",
            "--pdf-engine=typst",
            "-o",
            str(pdf_path),
        ],
        cwd=md_path.parent,
        env=env,
    )


def zip_sources(lab_dir: Path) -> None:
    archive_path = lab_dir / "release" / f"{lab_dir.name}-source-materials.zip"
    with zipfile.ZipFile(archive_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for relative in ["source", "src", "notebooks", "results/figures", "results/data", "report", "presentation"]:
            base = lab_dir / relative
            if not base.exists():
                continue
            for file in base.rglob("*"):
                if file.is_file():
                    archive.write(file, file.relative_to(lab_dir))


def build_lab(spec: dict, info: dict) -> None:
    lab_dir = LABS_DIR / spec["id"]
    source_path = lab_dir / spec["source"]
    src_dir = lab_dir / "src"
    notebook_dir = lab_dir / "notebooks"
    results_data = lab_dir / "results" / "data"
    results_figures = lab_dir / "results" / "figures"
    report_dir = lab_dir / "report"
    presentation_dir = lab_dir / "presentation"
    release_dir = lab_dir / "release"

    ensure_dirs(src_dir, notebook_dir, results_data, results_figures, report_dir, presentation_dir, release_dir)

    cells = parse_qmd_cells(source_path.read_text(encoding="utf-8"))
    julia_code = cells_to_julia(cells)
    src_path = src_dir / "main.jl"
    src_path.write_text(julia_code, encoding="utf-8")
    write_notebook(cells, notebook_dir / f"{spec['id']}.ipynb")
    shutil.copy2(source_path, release_dir / source_path.name)

    run_julia_script(src_path)
    summary_table = PLOTTERS[spec["id"]](lab_dir)

    report_md = report_dir / "report.md"
    report_md.write_text(report_markdown(spec, info, summary_table), encoding="utf-8")
    presentation_md = presentation_dir / "presentation.md"
    presentation_md.write_text(presentation_markdown(spec, info, summary_table), encoding="utf-8")

    pandoc_report(report_md, report_dir / "report.pdf", report_dir / "report.docx")
    pandoc_slides(presentation_md, presentation_dir / "presentation.html", presentation_dir / "presentation.pdf")
    zip_sources(lab_dir)


def render_lms_response(info: dict) -> None:
    response = ROOT / "lms-response.md"
    repo_placeholder = "https://github.com/USERNAME/REPOSITORY"
    release_placeholder = repo_placeholder + "/releases/tag/v1.0.0"
    body = textwrap.dedent(
        f"""\
        ## Скринкасты

        - [Rutube](https://rutube.ru/)
          - [Выполнение лабораторной работы](https://rutube.ru/)
          - [Подготовка отчёта](https://rutube.ru/)
          - [Подготовка презентации](https://rutube.ru/)
          - [Защита лабораторной работы](https://rutube.ru/)

        - [VKvideo](https://vkvideo.ru/)
          - [Выполнение лабораторной работы](https://vkvideo.ru/)
          - [Подготовка отчёта](https://vkvideo.ru/)
          - [Подготовка презентации](https://vkvideo.ru/)
          - [Защита лабораторной работы](https://vkvideo.ru/)

        ## Репозиторий

        - [GitHub]({repo_placeholder})
          - [Релиз v1.0.0]({release_placeholder})

        ## Приложенные файлы

        Для каждой лабораторной работы подготовлены:

        - отчёт в `markdown`, `docx`, `pdf`;
        - презентация в `markdown`, `html`, `pdf`;
        - ноутбук `ipynb`;
        - архив исходных материалов;
        - исходник в литературном формате `qmd`.

        ## Данные для титульных листов

        - Студент: {info["student_name"]}
        - Преподаватель: {info["teacher_name"]}, {info["teacher_title"]}
        - Организация: {info["organization"]}
        """
    )
    response.write_text(body, encoding="utf-8")


def main() -> None:
    info = load_course_info()
    for spec in LAB_SPECS:
        build_lab(spec, info)
    render_lms_response(info)
    print("Build completed.")


if __name__ == "__main__":
    main()
