# Devices

The **Devices** view is the fleet: every ReachingBot in the loaded config, its
connection state, and the actions you run against it.

Open a config with **Load config** in the toolbar, or click **Open in Devices**
after saving one in the [Configuration builder](configuration-builder.md).

## Fleet toolbar

Across the top: counts of **running**, **idle** and **offline** devices, a
filter box, and the fleet-wide actions.

| Action | What it does |
| --- | --- |
| **Scan network** | Probes every device in the config for SSH connectivity and updates its state |
| **Start API server** / **Stop API server** | Serves the [motor API](../reference/motor-api.md) on every connected device |
| **Download videos** | Pulls this session's videos off each connected device that has an animal assigned |
| **Update firmware** | Installs a firmware archive on every connected device |
| **Trash icon** | Deletes all videos and logs on every connected device |
| **Load config** | Opens a different experiment YAML |

## Device states

| State | Meaning |
| --- | --- |
| **unknown** | Not probed yet — use **Connect** on the card, or **Scan network** |
| **idle** | Connected and ready to run a session |
| **running** | A session is in progress |
| **api** | Serving the motor API. Stop it before running sessions on this device |
| **offline** | The device didn't respond. Check it's powered and on the network, then **Retry connection** |

Each card also shows the device's IP address (or `no IP set`) and its firmware
version once probed (`FW 1.0.0`, or `no firmware`).

## Session parameters

A collapsible panel above the fleet holds the parameters applied to **every**
session started from this page, and to the camera feed. They are **not** part of
the saved config, and a session already running keeps the values it started
with.

| Parameter | Default | Notes |
| --- | --- | --- |
| **Trials** | `10` | Maximum trials before the session ends |
| **Time (seconds)** | `60` | Maximum session length |
| **Detection area** | `300` to `500` pixels² | Smallest and largest pellet blob area. Presets are available for common 20 mg and 45 mg pellets |
| **Through-beam sensor** | off | Enables the through-beam sensor on the device |

Whichever limit is reached first — trials or time — ends the session.

The pellet-detection ROI is **not** here: it is per-device and lives in the
config, because it depends on where each device's pellet sits in frame. See
[Pellet detection](../reference/pellet-detection.md).

## Running a session

1. Make sure the device reads **idle**. If it reads **unknown**, click
   **Connect**.
2. Enter the animal in **Scan or enter animal ID**. Animals from the config are
   offered as suggestions. **Start session** stays disabled until an animal is
   set.
3. Click **Start session**.

While it runs, the card shows the animal, elapsed time against the time limit,
and trial progress (`Trial 3/10`) as the device reports it, plus the most recent
line of device output.

**Stop session** ends it gracefully — the device is interrupted rather than
killed, so the session closes down and its videos are written out.

Sessions run per-device, so you can start several devices with different animals
and watch them side by side.

## Camera feed

**Feed** on an idle device opens the live camera preview, served by the device
itself. Use it to confirm pellet detection before a session: a good result is a
white circle tracking the pellet inside the white ROI rectangle, without
flickering.

The feed uses the **Detection area** from the session parameters and the
device's ROI from the config, so it previews what a session would actually do.
Only one preview can be open at a time, and closing it stops the camera on the
device.

## Download videos

**Download videos** copies each connected device's session folder to your PC:

```
remote  /home/{username}/ReachingBotVideos/{animal}_{date}
local   {VideoDirectory}/{date}/{animal}_{date}
```

Every file is prefixed with the device name, so several devices can write into
the same session folder without colliding. The device log is pulled first, then
the videos, with per-file progress. If the config sets `DownloadCSV: true`, the
CSVs come too.

The date is today's unless you are downloading an earlier session, and is
written the way the firmware names its session folders — an ISO date with the
month's leading zero stripped, e.g. `2026-6-08`. `VideoDirectory` comes from the
config — by default the `ReachingBotVideos` folder created next
to it.

Downloaded results can be read in the [Inspect](inspect.md) view, and the
videos scored in [Device Manager](../rbdm/outcome-classification.md).

## Firmware

Each card shows the firmware version once the device has been probed.

**Update firmware** asks for a firmware archive (`.zip`, `.gz` or `.tar`), then
confirms before installing it on **every connected device**. The old firmware is
removed first, the archive is uploaded, and it is extracted on the device. Once
removal has begun the update runs to completion rather than leaving a device
with no firmware on it, so an update can only be cancelled before it starts.

The new version is probed and shown on the card when it finishes.

## Deleting device data

The trash button deletes **all videos and logs** on every connected device.
It asks for confirmation first, and **cannot be undone**.

Use it when a device runs out of space. Videos are copied to your PC by
**Download videos**, not by the session itself, so download before deleting.
