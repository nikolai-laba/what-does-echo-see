# What does ECHO see?

Team workspace for starter project 15 at [Day in Our Data](https://github.com/oak-park-cisc/Oak_Park_Day_in_our_Data), the October 3, 2026 civic hackathon run by Oak Park's Civic Information Systems Commission. It contains only what this project needs.

**The question:** what community needs is the Village's ECHO program running into, and where could service partnerships or resources be stronger?

## Where to start

1. Read the [project card](docs/project-card.md). It sets the demo, the stretch goals, the no-code roles, and the limits.
2. Read the [ECHO data key](docs/echo-data-key.md). It explains what each service category and referral source means, and lists open questions for the ECHO team.
3. Open the [data](data/README.md).

## What's here

| Folder | Contents |
| --- | --- |
| [data/](data/) | The ECHO snapshot, 2025 police call volumes by type, total calls for service, and the crime snapshot (stretch goal) |
| [docs/](docs/) | The project card and the data key |
| [resources/](resources/) | The resource directory, the team's main deliverable (see its README for the columns) |
| [scripts/](scripts/) | The extractors that built the ECHO and crime files. Kept for reference; we work from the cached snapshots. |
| [tests/](tests/) | Checks on the snapshot and the ECHO privacy rules: `python3 -m unittest discover -s tests -v` |

## Ground rules for this project

- **Aggregates only.** ECHO serves people in crisis, and the data holds counts, not people. Never estimate a `suppressed` cell or anything about an individual. Don't download the dashboard's row-level "Dataset" file.
- **Don't add the five ECHO tables together.** Each counts the same services a different way. Monthly charts use `breakdown = service_by_month`.
- **Use the cached data.** These are the event's reviewed snapshots. If we ever refresh, write to a scratch file and compare first (see [data/README.md](data/README.md)).
- **Review before publishing.** Anything we publish goes to the Board of Health and the ECHO team (`echo@oak-park.us`) before it's posted publicly. Label prototypes as unfinished. Nothing here is an official Village product or position.

## License

MIT. The project card, ECHO and crime data, and scripts come from the CISC repo, © 2026 oak-park-cisc; see [LICENSE](LICENSE).
