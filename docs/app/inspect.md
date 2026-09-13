# Inspect

The **Inspect** view reads the results of sessions you have already
[downloaded](devices.md#download-videos). It only reads local files — it does
not touch the devices, and it does not score anything.

<figure markdown>
![The Inspect view showing hits, misses, success rate and the trial table](../assets/app/inspect-results.png)
<figcaption>A scored session: totals across the top, then the results CSV as it appears on disk, with its path underneath.</figcaption>
</figure>

## Picking a session

| Field | Notes |
| --- | --- |
| **Video directory** | Filled in from the loaded config, or type a path in |
| **Session date** | Defaults to today |
| **Session** | The session folders found under that date. A folder with nothing to show is listed as `(no results)` |

Session folders follow the layout **Download videos** creates:
`{video directory}/{date}/{animal}_{date}`.

## What it shows

For a session with a results CSV:

- **Hits**, **Misses** and **Success rate** across the session
- The full CSV as a table, with the columns as they appear in the file
- The path of the CSV the numbers came from

Hits and misses are counted from the CSV's **Predicted** column, and the
success rate is hits ÷ (hits + misses), as a percentage.

## Where results come from

The ReachingBot app does **not** produce the `Predicted` column — that is the ML
outcome classifier, which is part of the legacy
[Device Manager](../rbdm/outcome-classification.md), not this app. Inspect reads
the CSV whoever produced it.

So a session downloaded by this app shows **This session has no results CSV yet**
until the videos have been scored. Score them in Device Manager, which writes
its results CSV into the same session folder, then reopen the session here.

See [Outcome classification](../rbdm/outcome-classification.md) for what the
outcomes mean.
