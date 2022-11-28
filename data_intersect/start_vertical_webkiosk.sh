DISPLAY=:0 xrandr --output HDMI-1 --rotate right
xinput set-prop 'USBest Technology SiS HID Touch Controller' --type=float "Coordinate Transformation Matrix" 0 1 0 -1 0 1 0 0 1
xset s noblank
snap run firefox -kiosk localhost:8000

