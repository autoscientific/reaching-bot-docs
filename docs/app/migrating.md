# Moving from Device Manager

Both applications are supported, and they are designed to sit side by side: the
ReachingBot app runs your sessions, and Device Manager scores the videos.

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
| Scoring / DeepLabCut | Not present — stays in Device Manager |

## What is better

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

- **ML video scoring and DeepLabCut pose estimation.** These are the one real
  gap, and they are deliberate — see [Scoring](index.md#scoring). Keep Device
  Manager installed for them.
- **Published installers.** See [Install](install.md).

## A workflow that uses both

1. Build or open the experiment config in the ReachingBot app.
2. Run sessions from the app's Devices view.
3. **Download videos** from the app — they land in
   `{VideoDirectory}/{date}/{animal}_{date}`.
4. Score that folder in Device Manager, which writes its results CSV into it.
5. Read the scored results back in the app's [Inspect](inspect.md) view, or in
   Device Manager's Inspect tab.

Because both apps use the same directory layout and the same config, nothing has
to be copied or converted between steps.
