# Resource directory

This folder is for the team's main deliverable: one row per local service, matched to the ECHO service category it helps with. Put the data in `resource-directory.csv` using these columns:

| Column | What goes in it |
| --- | --- |
| `echo_category` | One of the dashboard labels: Unhoused Resident, Behavioral Health, Senior Services, Housing, Youth/Family Services, Financial Support, Domestic Violence, Medical Support, Food Services |
| `provider` | Organization name |
| `program` | The specific program or service |
| `what_they_offer` | One plain-language sentence |
| `who_is_eligible` | Age, residency, income, or other limits |
| `hours` | As published |
| `how_to_reach` | Phone, walk-in address, or website |
| `cost` | Free, sliding scale, insurance, etc. |
| `source_url` | The page you took the details from |
| `checked_on` | Date you checked it (YYYY-MM-DD) |
| `notes` | Waitlists, handoff quality, anything a resident should know |

Take contact details from the source pages, not from memory. The main starting points are listed under "Community resources" in [../docs/project-card.md](../docs/project-card.md):

- The Township's May 2026 Behavioral Health Resource Guide (PDF)
- The library's Social Services page

The library page blocks automated tools, so open it in a browser.

## How the directory shows up on the trends page

The trends page (`site/index.html`) reads this file and lists each service under its category's panel, so a few details matter:

- **File name:** exactly `resource-directory.csv`, in this folder.
- **Category names:** copy them exactly from the table above, including capitals and the slash in Youth/Family Services. A row with a typo won't appear. If a service helps with two categories, give it two rows.
- **Commas:** if a field has a comma in it, like `Rental help, utilities`, wrap the whole field in double quotes. Spreadsheet apps do this for you when you export as CSV.
- **What's displayed:** provider, program, what they offer, how to reach, hours, and cost, with the name linked to the source page. Eligibility, checked-on date, and notes are saved but not shown yet.
- **To preview:** from the repo folder, run `python3 -m http.server` and open http://localhost:8000/site/.

Open questions, source conflicts, unpublished details and ideas for building on the directory are logged in [directory-backlog.md](directory-backlog.md).
