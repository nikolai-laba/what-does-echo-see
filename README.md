# What does ECHO see?

Starter project 15 from [Day in Our Data](https://github.com/oak-park-cisc/Oak_Park_Day_in_our_Data), Oak Park's October 3, 2026 civic hackathon. Repo: https://github.com/nikolai-laba/what-does-echo-see

## The question

What community needs does the Village's E.C.H.O. (Engaging Community for Healthy Outcomes) care-coordination program run into, and where could service partnerships or resources be stronger? Goals and limits are in the [project card](docs/project-card.md). Category definitions and open questions are in the [data key](docs/echo-data-key.md).

## The data

| File | What it is | Used by the page |
| --- | --- | --- |
| `data/echo-activity-oak-park.csv` | ECHO dashboard counts, Feb 2025 to Sep 2026 (September partial): 1,598 services in five stacked tables | Yes |
| `data/crime-incidents-oak-park.csv` | Reported offenses, Jan 2022 to Sep 1, 2026, one row per offense | Only through the next file |
| `data/crime-monthly-oak-park.csv` | Monthly distinct incidents, built from the file above | Yes |
| `data/calls-for-service-totals.csv` | Yearly police and fire calls, 2022 to 2025, from the Board's June 2026 Phase 2 deck | Yes |
| `resources/resource-directory.csv` | 60 local services matched to ECHO categories, built by hand by the team | Yes |
| `data/police-calls-echo-relevant-2025.csv` | 2025 police calls by call type, with the team's own guess at the matching ECHO category | No (tests only) |

Sources and caveats for each file are in [data/README.md](data/README.md). The CSVs in `foia/templates/` are **synthetic** examples of what records requests might return. They are not data, and the page never loads them.

## How we got the numbers

Every step that changes a number:

1. **ECHO counts** (`scripts/fetch_echo_activity.py`): asks the public dashboard for grouped counts only, never individual records. In the weekday, time-block, and referral-by-service tables, counts under 5, and any cells that would reveal them, are replaced with `suppressed`.
2. **Crime counts** (`scripts/fetch_crime_incidents.py`, then `scripts/crime_monthly.py`): counts distinct incidents per month, in total and by crime against person, property, and society. An incident can fall in more than one of those three, so they add up to more than the total. The last month is dropped because it's partial.
3. **Calls for service and the resource directory** were typed in by hand from the cited sources.
4. **On the page** (`site/index.html`):
   - **By kind of need:** uses only the month-by-service table. Uncategorized services (`(blank)`) show as "Not categorized." A month with no row counts as 0. September 2026 is shown as partial. Totals and shares include it; the monthly average and the March–August year-over-year comparison use complete months only.
   - **By referral source:** uses the month-by-referral table for totals and trends, and the all-months referral-by-service table for what each source sent.
   - **By weekday:** percentages are shares of the cells that are shown.
   - **Community context:** groups crime into March–February 12-month windows and shows the change from the previous window.
   - **Everywhere:** the five ECHO tables are never added together, and hidden cells are never estimated.

`python3 -m unittest discover -s tests -v` checks the figures the page quotes, the privacy rules, and that no synthetic data reaches the page.

## How to use it

- **View it:** from the repo folder, run `python3 -m http.server` and open http://localhost:8000/site/.
- **Send it:** `python3 scripts/build_standalone.py` writes `dist/echo-trends.html`, one file with the data built in that opens with a double-click. Rebuild it after any data change.
- **Read the research:** [research/september-2025-spike.md](research/september-2025-spike.md) and [research/crime-and-echo.md](research/crime-and-echo.md).

Counts are logged services, not people or referrals.

## Status and next steps

**Status:** a draft prototype, not an official Village product. It goes to the Oak Park Board of Health and the ECHO team (echo@oak-park.us) for review before it's posted anywhere public.

**Next steps:**
- Ask the ECHO team the open questions in the [data key](docs/echo-data-key.md) and the [September 2025 note](research/september-2025-spike.md). For example: what caused September 2025, where our best guess is a one-time batch of police and fire follow-ups; and why the dashboard shows about 1.8 times the police and fire referrals reported to the Board for February–June 2025.
- Finish the open items in [resources/directory-backlog.md](resources/directory-backlog.md).
- Decide whether to send the draft records requests in [foia/](foia/README.md). None has been sent.

MIT license. The project card, the ECHO and crime data, and the extractors come from the CISC repo, © 2026 oak-park-cisc; see [LICENSE](LICENSE).
