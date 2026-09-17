Personal portfolio built with Astro.

Run `npm run dev` for development, or `npm run build` followed by `npm run preview` to review the static production build.

After changing `src/content.config.ts`, restart the development server if entries are missing or stale. During the optional-date migration, the running server temporarily retained the old validation state; reloading the server restored agreement with the production build.

## Content dates and ordering

The legacy `publishDate` field controls chronological ordering within project categories and on the blog. It is not currently displayed to visitors. Project entries use the documented project/report period; blog entries use the original post's publication date when available. These dates are not the date a page was added to this repository.

When only a month, year, or season is known, its first day is a sorting anchor, not a claim about an exact publication or completion day. The frontmatter comment records that precision. Unknown dates are omitted and sort after dated entries. Equal dates sort by entry ID so development and production agree. The homepage's featured projects have a separate explicit order in `src/pages/index.astro`.

Date sources checked in September 2026:

| Entry | Date used | Evidence / precision |
| --- | --- | --- |
| ROS post (both copies) | June 27, 2025 | Original WordPress publication |
| Cycloidal proposal | April 25, 2025 | Original WordPress publication |
| Worlds presentation | April 25, 2025 | Original WordPress publication; event occurred earlier that month |
| Configurable bumpers | October 24, 2023 | Original Chief Delphi post, UTC date |
| Arctangent integral | May 23, 2024 | Date printed on the final report PDF |
| Faro shuffling | February 2024 | Existing page's report month; day unknown |
| Soil monitoring | January 2025 | Page identifies ETSD 2025 January term |
| Phone holder | 2024 | Page identifies TSA 2024; month/day unknown |
| Airbag concept | 2023–2024 season | Page identifies Conrad Challenge season; sorts under 2024 |
| Suspended rover | May 2026 | Resume lists September 2025–May 2026; uses latest project month |
| L'SPACE | August 2026 | Sid confirmed May–August 2026; uses final project month |

Original posts: [WordPress archive](https://technolowebblog.wordpress.com/) and [Chief Delphi bumper post](https://www.chiefdelphi.com/t/the-zebracorns-behind-the-stripes-design-code-and-build-blog-2023-2024/440094/11).

The CubeSat and differential-swerve-module dates still need confirmation. CubeSat is described as a senior-year project (2024–2025), which does not establish a particular calendar year. C4 and Artemis retain their existing 2025 and 2024 season dates.

## Legacy pages

`/education` and `/experience` redirect to the corresponding anchored sections on `/about/`. Update the About page rather than maintaining duplicate biographies.
