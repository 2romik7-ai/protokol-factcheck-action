# Protokol Factcheck Action

Бесплатная GitHub Action для базовой проверки Markdown-материалов перед публикацией.

## Использование

```yaml
name: Factcheck
on: [push, pull_request]
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: 2romik7-ai/protokol-factcheck-action@v1
        with:
          file: README.md
```

Action создаёт `factcheck-report.md`, считает ссылки и предупреждает о категоричных рекламных обещаниях. Это технический предварительный контроль, а не экспертное заключение.

Расширенный Pro-набор: https://boosty.to/protokol_research
