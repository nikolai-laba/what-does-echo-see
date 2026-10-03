# ECHO data key

The Village has not published formal definitions for the ECHO dashboard's categories. This key pieces them together from the Village's own Board presentations, program pages, and the dashboard's data model. Where a mapping is our inference, it says so. Compiled October 3, 2026.

## What ECHO is

E.C.H.O. (Engaging Community for Healthy Outcomes) is the Village's two-year Alternative Response to Calls for Service pilot, run by the Community Services division of Neighborhood Services and launched in February 2025.

- **Phase 1 (current) is care coordination.** A program manager and two care coordinators follow up after police, fire, or Village contact, take walk-ins and direct calls, and connect residents to services. Hours are Monday to Friday, 8:30 a.m. to 5 p.m. Contact: `echo@oak-park.us`, 708-358-5640.
- **ECHO does not respond to mental health crises.** Under the June 2026 Phase 2 plan, Thrive Counseling Center takes the crisis calls. ECHO handles follow-up, and might later co-respond on "Community Response" calls if the Board funds an expansion.
- **The data comes from ECHO's intake forms.** According to the dashboard's hidden "IT Notes" page, the source is a SharePoint list ("ECHO-LF Data Import") fed by Neighborhood Services ECHO forms. The data model has no field descriptions.

## Service categories

| Dashboard label | Earlier wording | What it covers |
| --- | --- | --- |
| Unhoused Resident | "Homelessness" (Jul 2025), "Unhoused Services" (Feb 2026) | Street outreach, care kits, emergency shelter navigation, and encampment work with Public Works. Probably also absorbed July 2025's "Panhandling/Soliciting" (inference). |
| Housing | "Housing", "Housing Support" | Housing instability for people who are still housed, such as rental and housing help. The Board lists it separately from homelessness. |
| Behavioral Health | "Mental Health" and "Substance Abuse" (Jul 2025) | Mental health connections and substance use treatment referrals. The two July 2025 categories appear to have been merged (inference). |
| Senior Services | Same | Wellness checks, "invalid assists and falls support", and dementia. Board example: a resident with dementia reported missing, connected to power of attorney help, a medical ID bracelet, and Township caregiver support. |
| Youth/Family Services | "Child/Family Services" | Truancy support, youth behavioral issues and family disputes, and the Township Youth Engagement Program. |
| Financial Support | Same | Financial, utility, and insurance help. |
| Domestic Violence | "Domestic Violence" plus a separate "Abuse" (Jul 2025) | Connection to domestic violence services. |
| Medical Support | "Medical" | Medical and dental help. |
| Food Services | "Food Insecurity" | Food assistance. |
| Other | Same | Not defined. |
| (blank) | Not in any presentation | Appears from July 2026. Likely a form or entry change; unconfirmed. |

## Referral sources

| Dashboard label | Wording in July 2025 | Meaning |
| --- | --- | --- |
| Police Department, Fire Department | Same | Follow-up after a 911 call. |
| Resident Contact | "Resident Referral" and "VOP Walk-In Referral" | Residents calling or walking into Village Hall, for themselves or someone else. |
| Community Engagement | Proactive outreach (Jul 2025 slide 11) | **ECHO's own outreach, not an outside referrer.** Includes business district support, a panhandling campaign, weekly district cleanings, and street outreach with unhoused residents. This is why 124 of its 160 services are Unhoused Resident. |
| Village of Oak Park Departments | "Village Staff Referral" | Other Village departments. |
| Community Partner | "Non-Profit Partner Referral" | Nonprofits; possibly also July 2025's "School Referral" (inference). |
| Business | Same | Businesses. |
| Emergency Housing | Not in July 2025 | Not defined. All 17 fall between July and October 2025. |

## Open questions for the ECHO team

1. **Services or referrals?** The dashboard counts 874 services for February to December 2025, while the Board was told "more than 700 referrals" (702 in the February 2026 deck). All 172 extra are Police, Fire, or Resident referrals; the other five sources match exactly. Can one referral produce more than one service row? Until this is answered, call the counts "services", not "referrals".
2. **September 2025.** The spike is real: the Board's own running total jumps by 162 that month. What caused it?
3. **2026 shifts.** One of ECHO's Year 2 goals is "tracking call data by address/referral type." Did intake categories change in 2026? That could explain the jump in "Other" in May 2026 and the blank category from July. Separately, did the January 2026 start of 911-to-988 transfers reduce Behavioral Health referrals?
4. **Timestamps.** About a quarter of services carry a 2 to 6 a.m. timestamp, which doesn't fit a business-hours team. What event and time zone does the timestamp record?

## Sources

- [E.C.H.O. program page](https://www.oak-park.us/Community/Community-Services/E.C.H.O-Engaging-Community-for-Healthy-Outcomes): services, hours, referral pathways
- [Launch announcement, March 2025](https://www.oak-park.us/News-articles/Engaging-Community-for-Healthy-Outcomes-E.C.H.O) and [Celebrating one year of E.C.H.O.](https://www.oak-park.us/News-articles/Celebrating-one-year-of-E.C.H.O)
- Village Board records:
  - [ECHO Phase 1 Update, July 2025](https://oak-park.legistar1.com/oak-park/attachments/b81639d5-5567-4d09-98cb-06b13d58035a.pdf) (ID 25-416): earlier category and referral names, case examples, Community Engagement activities
  - [E.C.H.O. Year 1 Implementation Overview, February 2026](https://oak-park.legistar1.com/oak-park/attachments/6231d073-37ec-4351-9ee5-4436c538741a.pptx) (ID 26-131): 2025 totals by category and referral source, Year 2 goals
  - [Phase 2 Recommendations, June 2026](https://oak-park.legistar1.com/oak-park/attachments/21db010a-41cb-410a-9828-9ce4a0ef9fc7.pptx) (MOT 26-176): 911 call-type volumes, Thrive partnership, proposed expansion
  - [CESSA Implementation memo, November 2025](https://www.oak-park.us/files/assets/oakpark/v/1/village-manager/memos-to-the-village-president/2025/io-2025-11-19-cessa.pdf): Phase 1 versus Phase 2, 988 transfers
- Wednesday Journal: [After one year, ECHO services grow](https://www.oakpark.com/2026/02/03/after-one-year-echo-services-grow-with-police-fire-resident-referrals/) (Feb 2026), [Trustees reviewing early ECHO data](https://www.oakpark.com/2025/07/15/oak-park-trustees-reviewing-early-data-on-echo-program/) (Jul 2025)
- ECHO Activity dashboard data model and "IT Notes" page, read through the public Power BI endpoints that `scripts/fetch_echo_activity.py` uses
