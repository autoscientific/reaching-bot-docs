# Moving from Device Manager

The ReachingBot app now covers the whole workflow — configure, run, score,
inspect — so Device Manager is no longer needed for a normal study. Both remain
supported and read the same files, so you can move between them.

## Your config files still work

Both apps read and write the same experiment YAML, so a config made in one opens
in the other and neither will reject the other's files. You do not need to
rebuild your studies. See [Experiment config file](../reference/config-file.md).

The app adds an `ip_address` key per device, which Device Manager ignores.

## Where things moved

| In Device Manager | In the ReachingBot app |
| --- | --- |
| **Setup** tab | [Configuration builder](configuration-builder.md) |
| **Devices** tab | [Devices](devices.md) |
| **Inspect** tab | [Inspect](inspect.md) |
| **Videos → Delete Videos On Connected Devices** | Trash button in the Devices toolbar |
| **Display Feed** | **Feed** on a device card |
| **Start API Server** | **Start API server** in the Devices toolbar |
| **Scoring** tab | [Scoring](scoring.md) |

## What is better

- **Scoring without the machine-learning stack.** [Scoring](scoring.md) gives
  identical predictions to Device Manager — same labels, keypoints and
  confidences on the reference set — with a fraction of the install size, and
  verified to match across macOS, Linux and Windows.
- **Per-device settings are editable.** Motor type, shooting mode, camera FPS,
  camera view and the pellet-detection ROI are editable from each device's row
  in the Configuration builder, at any time. Device Manager hardcoded most of
  these, or required hand-editing the YAML.
- **Live session output.** Device output is streamed to the app as it happens,
  with trial progress and elapsed time on the card.
- **Stoppable long operations.** Network scans, sessions, downloads and the API
  server can all be stopped from the UI.
- **Per-file download progress**, rather than a single wait.
- **Linux builds**, alongside macOS and Windows.

## What is not there

Scoring came across, but four of its options deliberately did not — the p-value
setting (fixed at 0.95), per-video trajectory CSVs, the labelled-video export,
and custom pose models from the config. [Scoring](scoring.md#differences-from-device-managers-scoring)
covers each. Device Manager is still the way to reach them.

Two platform changes are worth knowing before you move:

- **Intel Macs are not supported.** The app is Apple silicon only.
- **macOS 13 or later** is required.

Also still outstanding: **published installers** — see [Install](install.md).

## The workflow, end to end

1. Build or open the experiment config in the [Configuration builder](configuration-builder.md).
2. Run sessions from [Devices](devices.md).
3. **Download videos** — they land in `{VideoDirectory}/{date}/{animal}_{date}`.
4. [Score](scoring.md) those sessions; predictions go into each one's results CSV.
5. Read the totals in [Inspect](inspect.md).

Device Manager is not needed at any step. If you do use it — for one of the
scoring options above, or because a study started there — it reads and writes
the same config and the same session folders, so nothing has to be copied or
converted.
