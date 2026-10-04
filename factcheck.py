import pathlib
import sys

source = pathlib.Path(sys.argv[1])
if not source.exists():
    raise SystemExit(f"Файл не найден: {source}")
text = source.read_text(encoding="utf-8")
lines = text.splitlines()
links = [line.strip() for line in lines if "http://" in line or "https://" in line]
warnings = []
if not links:
    warnings.append("Не найдены ссылки на источники.")
if len(text) < 300:
    warnings.append("Текст короче 300 символов: вывод может быть неполным.")
if any(word in text.lower() for word in ("гарантированно", "точно разбогатеете", "100%")):
    warnings.append("Найдены категоричные или рекламные обещания.")
report = pathlib.Path("factcheck-report.md")
report.write_text("# Отчёт Protokol Factcheck\n\n" + f"Источник: {source}\n\n" + f"- Символов: {len(text)}\n- Строк: {len(lines)}\n- Ссылок: {len(links)}\n\n" + "## Предупреждения\n" + ("\n".join(f"- {item}" for item in warnings) if warnings else "Нарушений базовой структуры не найдено.") + "\n", encoding="utf-8")
print(f"Отчёт создан: {report}")
