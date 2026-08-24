# 6-Month Python Roadmap

> **Status update:** Month 1 content is complete as of Day 9, covering the original plan plus significant extra depth pulled in from work material (inheritance/MRO, dunder methods, operator overloading, decorators, deque performance, real-world assessment debugging, git conflict resolution). "Months" here are content phases, not literal calendar months — Month 1 took roughly 9 working sessions across about three weeks. Currently doing a spaced review week across all of Month 1 before starting Month 2.

**Starting point:** Comfortable with core syntax, control flow (`if`/`while`/`for`), functions (including `*args`/`**kwargs`), string handling, and scope (LEGB). Debugging instinct is a real strength — self-correction has been consistently fast. Currently enrolled in an employer-run Python program that starts from basics but ramps up quickly.

**Direction:** Data Analysis foundation first — this overlaps with the current work program and keeps AI/ML or backend development open as a later branch, once more is known about what's genuinely interesting.

**Cadence:** ~1 hour/day. Short mini-lessons + practice, roughly one small project per month, one capstone at the end. Where the work program moves faster than this plan on a given topic, we compress or skip ahead here rather than duplicate.

---

## Month 1 — Close the Gaps, Build the Real Foundation
Goal: nothing in core Python left shaky before data-specific tools get layered on.

- `for` loops in depth: list/dict/set comprehensions, nested iteration, `zip()`
- Object-Oriented Programming: classes, `__init__`, methods, attributes, basic inheritance
- File I/O: reading/writing `.txt`, `.csv`, `.json`
- Error handling in depth: multiple `except` blocks, `finally`, custom exceptions
- Modules & packages: importing your own files, `pip install`, virtual environments (`venv`)
- Git & GitHub basics (this week — see setup steps)

**Mini-project:** Command-line contact book (add/search/delete, saved to a file) — combines OOP, file I/O, and error handling.

## Month 2 — Intermediate Python & Good Habits
Goal: write code like someone who ships things, not just someone who's learned syntax.

- Data structures deeper dive: list vs tuple vs set vs dict — when and why
- Decorators and generators (conceptual + practical use)
- Working with dates/times (`datetime`)
- Intro to testing: `assert`, basic `pytest`
- Debugging tools: VS Code debugger, breakpoints — beyond print statements
- Virtual environments and `requirements.txt`, done properly

**Mini-project:** CLI expense tracker with saved history, basic reporting (totals/categories), and at least 3 unit tests.

## Month 3 — Data Analysis Foundations
Goal: start doing work that actually resembles the job.

- NumPy fundamentals: arrays, vectorized operations
- pandas fundamentals: Series, DataFrames, reading CSV/Excel, filtering, grouping, merging
- Data cleaning: missing values, duplicates, type conversion
- Jupyter Notebooks as a workflow
- Data visualization: Matplotlib, Seaborn
- SQL basics: `SELECT`, `WHERE`, `JOIN`, `GROUP BY` (practice on SQLite)

**Mini-project:** Clean and analyze a real public dataset end-to-end — ideally something tied to your actual work domain (network/telecom data, given the LTE work) — and produce 3–5 visual insights.

## Month 4 — Applied Data Work
Goal: build things that look like real analyst/engineer output.

- Working with APIs (`requests`), basic web scraping (`BeautifulSoup`)
- Intermediate SQL: subqueries, window functions
- Intro statistics for data work: distributions, correlation, basic hypothesis testing
- Proper Git workflows: branches, pull requests, resolving conflicts

**Mini-project:** Pull live data from a public API, store it, analyze it, publish a small dashboard or report.

## Month 5 — Specialize (Decision Point)
By now there'll be a much clearer read on what's actually enjoyable. Pick one lane:

- **Data Science/ML lean:** scikit-learn basics, simple regression/classification models
- **Data Analyst/BI lean:** deeper SQL, dashboarding tools (Power BI/Tableau basics), advanced pandas
- **Backend/software lean:** Flask or FastAPI basics, REST API design, PostgreSQL

We decide together based on what Months 3–4 reveal.

## Month 6 — Capstone & Portfolio Polish
- One larger capstone combining everything (scope depends on the Month 5 lane)
- Clean up and document every repo project properly (READMEs, comments, structure)
- Resume / LinkedIn / GitHub profile polish
- Mock technical interview practice, if job-hunting is the near-term goal

---

## Portfolio Ideas (ongoing — not just Month 6)
- Data cleaning + analysis project on a public dataset
- Automation script solving a real annoyance (file organizer, report generator)
- Small interactive dashboard
- API-based data pipeline project
- A project tied to your actual work domain — this tends to be the strongest portfolio piece, since it shows applied, relevant skill rather than a generic tutorial clone

---

## Notes
This is a living document — update it as pace and interests shift. Revisit monthly.
