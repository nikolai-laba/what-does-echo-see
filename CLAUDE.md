# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A private team workspace for starter project 15, "What does ECHO see?", from the Day in Our Data civic hackathon (Oak Park, IL, October 3, 2026). It was split out of the CISC event repo (https://github.com/oak-park-cisc/Oak_Park_Day_in_our_Data) and holds only this project's data, docs, and extractors. There is no app or build step yet. The deliverables are charts of aggregate ECHO activity and a resource directory (`resources/`), most of which is built by hand by no-code teammates.

Read these first: `docs/project-card.md` (goals and limits), `docs/echo-data-key.md` (category and referral definitions, open questions), `data/README.md` (file-level sources and caveats).

## Commands

```text
python3 -m unittest discover -s tests -v                                   # all checks, stdlib only
python3 -m unittest discover -s tests -k test_call_volume_files_match_the_board_deck   # one check
python3 scripts/fetch_echo_activity.py -o /tmp/echo-live.csv                # refresh to a scratch path only
```

## Data

- `data/echo-activity-oak-park.csv`: five aggregate tables stacked in long format, chosen with the `breakdown` column; only the columns that apply to a breakdown are filled.
  - `service_by_month` and `referral_by_month`: exact counts, including counts of 1 to 4.
  - `service_by_weekday`, `service_by_time_block`, `referral_by_service`: small cells, plus complementary cells, are written as the string `suppressed`.
- `data/police-calls-echo-relevant-2025.csv`: 2025 police calls for service by dispatch call type, transcribed from the Village Board's June 2026 Phase 2 presentation. `suggested_echo_category` and `match_confidence` are the team's own crosswalk, not the Village's. The two biggest rows (Remove Unwanted, Welfare Check) are low confidence.
- `data/calls-for-service-totals.csv`: yearly police and fire calls for service, 2022 to 2025.
- `data/crime-incidents-oak-park.csv`: stretch goal only, used as monthly counts by NIBRS `incident_type`. It has one row per offense, so count distinct `incident_id` to get incidents. It counts reported crimes, which is a weak comparison for ECHO's non-criminal work; the call-volume files compare much more directly.
- `scripts/`: Power BI "publish to web" replay extractors, standard library only. `fetch_echo_activity.py` sends grouped COUNT queries only, applies `suppress()`, and exits if any table's total doesn't match the model total. Keep both of those behaviors.

## Rules any code or output must follow

- Work from the cached snapshots; refresh only when asked. A refreshed ECHO file changes the totals pinned in `tests/test_echo.py` (1,598 services, 73 suppressed cells), so update the test, `data/README.md` and the card together.
- Never add the five ECHO breakdowns together. Monthly trends use `service_by_month` only.
- Parse `count` as a number or missing. `suppressed` means unavailable: not 0, not "<5", and never estimated or back-solved from other tables.
- A service is one logged contact, not one person; describe counts as workload. The dashboard's 2025 total (874) is higher than the "702 referrals" reported to the Board, so don't call the counts referrals.
- Keep the partial current month visually separate from complete months.
- Don't interpret time of day; the timestamp's meaning is unconfirmed. Weekday counts reflect a Monday-to-Friday team.
- There is no geography or individual-level data, so nothing can be mapped. Never fetch the dashboard's row-level "Dataset" export.
- In the resource directory, take addresses, phone numbers and hours from the cited source pages, never from memory, and record `source_url` and `checked_on`.
- Outputs go to the Board of Health and the ECHO team (`echo@oak-park.us`) for review before anything is posted publicly.

## Source access notes

- `www.oak-park.us` returns 403 to curl but works through WebFetch.
- `www.oppl.org` sits behind a Cloudflare challenge and needs a real browser.
- Village Board documents can be found through the Legistar API: `https://webapi.legistar.com/v1/oak-park/matters?$filter=substringof('ECHO',MatterTitle)`, then `/matters/{id}/attachments`.
