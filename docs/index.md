# ReachingBot Documentation

User documentation for ReachingBot, the ReachingBot app, and the ReachingBot
Device Manager.

## Which application do I use?

There are two desktop applications. They drive the same hardware, read and write
the same [config files](reference/config-file.md), and can be used together.

<div class="grid cards" markdown>

- ### [ReachingBot app](app/index.md)

    **The current app.** Run sessions, build configs, preview the camera,
    download videos, update firmware. Available for macOS, Windows and Linux.

    Does **not** do ML video scoring.

    [Get started →](app/index.md)

- ### [Device Manager (legacy)](rbdm/index.md)

    **The original app.** Still supported, and still the only way to score
    videos with the ML outcome classifier and DeepLabCut.

    Keep it installed for scoring, or if you are mid-study.

    [Get started →](rbdm/index.md)

</div>

Running sessions in the new app and scoring them in Device Manager is a
supported workflow — see
[Moving from Device Manager](app/migrating.md).

## Start here

Whichever application you use, set the hardware up first:

1. [Hardware setup and assembly](hardware/setup.md)
2. [Device drivers](hardware/drivers.md)

## Reference

Pages that apply to both applications:

- [Experiment config file](reference/config-file.md) — the YAML both apps read and write
- [Pellet detection](reference/pellet-detection.md) — configuring the camera-based pellet detector
- [Video recording modes](reference/video-recording-modes.md) — segmented vs continuous capture
- [Motor API](reference/motor-api.md) — drive the bot from your own scripts over HTTP

For additional help and support, email [info@autoscientific.co.uk](mailto:info@autoscientific.co.uk).
