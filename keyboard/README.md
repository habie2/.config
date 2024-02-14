# keyboard config
## Linux
### xmodmap
change to default:
```bash
setxkbmap
```
change to .Xmodmap config:
```bash
xmodmap ~/.Xmodmap
```
.Xmodmap config: 
```{.Xmodmap}
!
! Swap Caps_Lock and Control_L
!
remove Lock = Caps_Lock
remove Control = Control_L
keysym Control_L = Caps_Lock
keysym Caps_Lock = Control_L
add Lock = Caps_Lock
add Control = Control_L
```
### gnome-tweaks
Update: using gnome-tweaks is easier. Following post: https://opensource.com/article/18/11/how-swap-ctrl-and-caps-lock-your-keyboard

## Windows 
1. Press `Win + R` to open the Run dialog, type `regedit`, and enter.
   
2. Navigate to the following:
```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Keyboard Layout
```
3. Right-click on the Keyboard Layout key, select New, and then click on Binary Value.
Name the new binary value `Scancode Map` and press Enter.

5. Double-click on the Scancode Map entry to edit its value.
Enter the following hexadecimal value:
```
00 00 00 00 00 00 00 00 03 00 00 00 1D 00 3A 00 3A 00 1D 00 00 00 00 00
```
5. Save and restart the computer.
