# Installing the ReachingBot app

Installers are listed on the [Downloads](downloads.md) page, which the release
build updates itself.

Nothing else needs installing alongside the app. The Python backend is frozen
into the bundle, so an installed copy needs neither Python nor `uv` on the
machine.

Before installing, make sure the hardware is assembled and the
[device drivers](../hardware/drivers.md) are in place.

## Requirements

| Platform | File | Notes |
| --- | --- | --- |
| macOS, Apple silicon | `.dmg` | **macOS 13 or later.** Intel Macs are not supported |
| Windows | `.msi`, or the `.exe` installer | |
| Linux | `.deb`, or the `.AppImage` | Built on Ubuntu 22.04, which sets the oldest glibc — and so the oldest distribution — they will run on |

!!! warning "Apple silicon only"
    There is no Intel Mac build. Both the macOS 13 minimum and the dropped
    Intel support come from the scoring runtime the app now bundles. Check
    which you have under  → About This Mac.

The installers are large — roughly 50 MB on macOS, 95 MB on Windows and 200 MB
on Linux — because the scoring models and a video decoder ship inside them.

## First launch on macOS and Windows

Builds are **not** signed with an Apple Developer ID or an Authenticode
certificate, so both operating systems will warn you the first time. You only
need to do this once.

**macOS** — drag ReachingBot into Applications and open it. When macOS says it
cannot verify the developer:

1. Click **Done**.
2. Open **System Settings → Privacy & Security**.
3. Scroll down and click **Open Anyway** next to the ReachingBot message.

If macOS instead says the app is **damaged**, clear the quarantine flag once in
Terminal:

```sh
xattr -cr /Applications/ReachingBot.app
```

**Windows** — on the SmartScreen prompt, choose **More info → Run anyway**.

## Versions

The version shown in the app matches the release tag it was built from
(for example tag `v0.2.0` → version `0.2.0`).

Unlike Device Manager, the app does not have to match a particular firmware
version to start, but session and camera behaviour do depend on the firmware
installed on each device. You can check and update firmware from the
[Devices view](devices.md#firmware).

## Next

- [Build a configuration](configuration-builder.md)
- [Run a session](devices.md)
- [Score the videos](scoring.md)
