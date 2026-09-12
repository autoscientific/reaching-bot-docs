# Configuration builder

The **Configuration builder** writes the experiment YAML that the
[Devices](devices.md) view then runs from. It produces exactly the same file
format as the legacy Device Manager, so configs are interchangeable between the
two applications — see [Experiment config file](../reference/config-file.md).

The view is four numbered steps, in the order the work happens, beside a summary
rail on the right that shows the file being built, ticks each step off as it is
completed, and holds the **Save config** button.

To edit an existing study instead of starting fresh, put its path in the field
at the top of the page (or use the browse button) and the four steps are filled
in from it. Re-saving keeps any per-device settings that were already in the
file rather than resetting them to defaults.

## Step 1 — Name the experiment

| Field | Notes |
| --- | --- |
| **Experiment name** | Becomes the filename, e.g. `study-2026-04` → `study-2026-04.yaml` |
| **Project folder** | Where the YAML is written. A `ReachingBotVideos` folder is created alongside it and becomes the config's video directory |

## Step 2 — Device access

The SSH username and password for the ReachingBots themselves. These are
supplied to you by email; if you do not have them, contact
[info@autoscientific.co.uk](mailto:info@autoscientific.co.uk).

One login is stored per config and applied to every device in it.

!!! note
    The password is written into the YAML in plain text, as Device Manager did.
    Treat the config file as a credential and keep it out of shared drives and
    version control.

## Step 3 — Add your ReachingBots

### Scanning

**Scan for devices** looks for ReachingBots advertising themselves over mDNS. It
tries the standard hostnames — `ReachingBot`, then `ReachingBot1` through
`ReachingBot10` — and lists the ones that answer. A name that is not in use
takes a few seconds to time out, so a full scan is not instant; **Stop scan**
ends it between probes.

Clicking a found device fills in the form below it.

### Renaming a device

With a found device selected, pick a new hostname under **Rename … to** and
click **Rename**. This needs the device login from step 2.

The device is renamed and then **rebooted**, so it will drop off the network
until the reboot completes — expect it to disappear from a scan for a minute or
so.

### Adding a device by hand

| Field | Notes |
| --- | --- |
| **Name** | The device hostname, e.g. `ReachingBot1` |
| **IP address** | Optional. Leave blank to reach the device by hostname |
| **Camera position** | `Opposite motor` (default) or `Same side as motor` |

Added devices appear in a table showing **Device**, **Camera** and
**Motor · FPS**.

### Per-device settings

Each row has a settings button that opens the rest of that device's
configuration. **This is the main difference from Device Manager**, which
hardcoded these values — here each device can differ, and can be changed at any
point.

| Setting | Default | Notes |
| --- | --- | --- |
| **Motor type** | `MG996R` | Or `MG90S` for the legacy motors. Sets the servo pulse-width limits |
| **Shooting mode** | `segmented` | Or `continuous` — see [Video recording modes](../reference/video-recording-modes.md) |
| **Camera FPS** | `100` | Changing this with `continuous` mode is not recommended |
| **Camera view** | `Opposite motor` | Flips the frame when the camera is on the motor side |
| **`y1_offset`** | `0.61` | Pellet-detection ROI, top edge as a fraction of frame height |
| **`y2_offset`** | `0.98` | ROI bottom edge |
| **`x1_offset`** | `0.6` | ROI left edge as a fraction of frame width |
| **`x2_offset`** | `0.875` | ROI right edge |

See [Pellet detection](../reference/pellet-detection.md) for how to choose the
ROI, and the camera feed on the [Devices](devices.md#camera-feed) view for
checking it visually.

## Step 4 — Add the animals

| Field | Notes |
| --- | --- |
| **Animal ID** | Your identifier for the animal, e.g. `M-2271` |
| **Paw preference** | `To be determined` (default), `Left` or `Right` |

Animals are listed in a table and can be removed from it. Animal IDs added here
become the suggestions offered when starting a session on the
[Devices](devices.md) view.

## Saving

**Save config** writes `{project folder}/{experiment name}.yaml` and creates the
`ReachingBotVideos` directory next to it. The file is validated before it is
written, and the save is refused unless there is at least one device **and** at
least one animal.

Once saved, **Open in Devices** takes you straight to the fleet with that config
loaded.
