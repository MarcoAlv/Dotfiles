# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from colors import gruvbox, nord_fox
from unicode import lower_left_triangle, right_arrow, left_arrow

colors = [
    ["#97D59B", "#141417"],  # ACTIVE WORKSPACES 0
    ["#6A6A6A", "#6A6A6A"],  # INACTIVE WORKSPACES 1
    ["#384149", "#384149"],  # background lighter 2
    ["#FF8080", "#FF8080"],  # red 3
    ["#97D59B", "#97D59B"],  # green 4
    ["#FFFE80", "#FFFE80"],  # yellow 5
    ["#80D1FF", "#80D1FF"],  # blue 6
    ["#C780FF", "#C780FF"],  # magenta 7
    ["#80FFE4", "#80FFE4"],  # cyan 8
    ["#D5D5D5", "#D5D5D5"],  # white 9
    ["#4c566a", "#4c566a"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#8fbcbb", "#8fbcbb"],  # super cyan12
    ["#181E23", "#0E131A"],  # super blue 13
    ["#181e23", "#181e23"],  # super dark background 14
]



# add separator..

widget.Sep(
    linewidth = 3,
    padding = 10,
    foreground = colors[11],
    background = colors[14]
                        ),


# change style to widget.GroupBox look for these lines and replaces


widget.GroupBox(font='TerminessTTF Nerd Font',
                        fontsize = 13,
                        margin_y = 3,
                        margin_x = 2,
                        padding_y = 5,
                        padding_x = 4,
                        borderwidth = 5,
                        disable_drag = True,
                        active = colors[0],
                        inactive = colors[1],
                        rounded = True,
                        highlight_method = "block",
                        highlight_color = colors[1],
                        this_screen_border = colors[1],
                        this_current_screen_border = colors[2],
                        foreground = colors[1],
                        background = colors[14]
                        ),

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], 
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Comandos personalizados

    Key([mod], "f", lazy.spawn("firefox"), desc="Open firefox"),

    # Multimedia Key
    ## I need to program the functions to use in here

    Key([],"XF86MonBrightnessUp", lazy.spawn("brightnessctl set 10%+"), desc=""),
    Key([],"XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-"), desc=""),

    # audio

    Key([],"XF86AudioMute", lazy.spawn("firefox"), desc=""),

    # Key([],"XF86AudioRaiseVolume", lazy.spawn("amixer -q -D pulse set Master 10%+"), desc=""),
    # Key([],"XF86AudioLowerVolume", lazy.spawn("amixer -q -D pulse sset Master 10%-"), desc=""),

    Key([],"XF86AudioNext", lazy.spawn("firefox"), desc=""),
    Key([],"XF86AudioPrev", lazy.spawn("firefox"), desc=""),


]

# "" "" "" "" "阮"

"""

__groups = {
    1: Group(" "),
    2: Group(""),
    3: Group(""),
    4: Group(""),
    5: Group(""),
    6: Group("阮"),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],str(get_group_key(i.name)),
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],str(get_group_key(i.name)),
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

"""

groups = [Group(i) for i in [
    "  ", "   ", "   ", "   ", "  ", "   ", "   ", "   ", " 阮  ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name, switch_group=True))
    ])


layouts = [
    #
    layout.MonadTall(
    border_normal="#232323",
    border_focus="#0000ff",
    border_width=3,
    single_border_width=0,
    margin=5,
    single_margin=0,
    ),
    layout.Max(),
    layout.Columns(
    border_normal="#232323",
    border_focus="#0000ff",
    border_width=3,
    single_border_width=0,
    margin=4,
    single_margin=0,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=3),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=14,
    padding=2,
    background=colors[14],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(format="{state}"),
                # widget.WindowTabs()),
                widget.Chord(
                    chords_colors={
                        "launch": ("#8fbcbb", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # widget.TextBox("MarcoGAB", name="default"),
                # widget.TextBox("ArchLinux", foreground="#d75f5f"),
                widget.Systray(),

                widget.Battery(format='{hour:d}h:{min:02d}m | {percent:2.0%} |' , update_interval=60),

                left_arrow("#181e23", nord_fox['black']),
                widget.Memory(
                    foreground=nord_fox["pink"],
                    padding=10,
                    measure_mem="G",
                    format=" {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
                    background=nord_fox['black']
                ),
                left_arrow(nord_fox['black'], nord_fox['cyan']),
                widget.CPU(
                    foreground=nord_fox["black"],
                    padding=5,
                    format=" {freq_current}GHz {load_percent}%",
                    background=nord_fox['cyan']
                ),
                left_arrow(nord_fox['cyan'], nord_fox['green']),
                widget.Net(
                    foreground=nord_fox["black"],
                    interface="wlp2s0",
                    format="{down} ↓↑ {up}",
                    background=nord_fox['green']
                ),
                left_arrow(nord_fox['green'], nord_fox['yellow']),
                widget.Clock(
                    foreground=nord_fox["black"],
                    format=" %Y-%m-%d %a %I:%M %p",
                    padding=10,
                    background=nord_fox['yellow']
                ),
                left_arrow(nord_fox["yellow"], nord_fox["bg"]),
                widget.QuickExit(
                    background=nord_fox["bg"],
                    foreground=nord_fox["white"],
                    fontsize=18,
                    default_text="  ",
                ),
            ],
            26,  # Borders are magenta
        ),
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
