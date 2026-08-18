#!/bin/bash
# Live wallpaper launcher using xwinwrap + mpv (X11 only)
# Waits a few seconds after login so the desktop/panel is fully up
# before xwinwrap grabs the root window — this is what fixes the
# "doesn't start after reboot, I have to press play manually" issue.
sleep 5

VIDEO="$HOME/Videos/wallpaper.mp4"   # <-- change this to your video file
SOCKET="/tmp/mpv-wallpaper-socket"

rm -f "$SOCKET"

xwinwrap -ni -b -nf -un -o 1.0 -fdt -ov -- \
  mpv -wid WID \
      --loop \
      --no-audio \
      --hwdec=auto \
      --panscan=1.0 \
      --input-ipc-server="$SOCKET" \
      --really-quiet \
      "$VIDEO"
