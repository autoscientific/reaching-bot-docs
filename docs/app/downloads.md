# ReachingBot app downloads

Installers for the current ReachingBot app. For the legacy Device Manager, see
its own [Downloads page](../rbdm/downloads.md).

Before installing, read [Install](install.md) — it covers the macOS and Windows
first-launch prompts, which you will hit, and the platform requirements
(**Apple silicon and macOS 13 or later**; there is no Intel Mac build).

<!-- app-releases -->

## Which file

| Platform | File |
| --- | --- |
| macOS, Apple silicon | `.dmg` |
| Windows | `.msi`, or the `.exe` installer |
| Linux | `.deb`, or the `.AppImage` |

Nothing else needs installing alongside the app — Python and the scoring models
ship inside it, which is why the downloads are large.

!!! note "Match the firmware"
    As with Device Manager, changing software versions in the middle of a study
    is not advisable without first testing. Session and camera behaviour depend
    on the firmware installed on each device, which you can check and update
    from the [Devices](devices.md#firmware) view.
