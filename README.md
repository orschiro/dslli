# dslli
dslli stands for Disable Standby Laptop Lid Indicator. It provides an icon to the tray area that shows whether closing the laptop lid will trigger any action or none. You can toggle the action by assigning the provided script to a keyboard shortcut.

# Installation
From the [Release Page](https://github.com/orschiro/dslli/releases), download the latest version of `dslli.AppImage` and `dslli-indicator.AppImage`. Next, make both excecutable:

    $ chmod +x dslli.AppImage
    $ chmod +x dslli-indicator.AppImage

# Usage
To toggle between the two states, run the following command:

    $ ./dslli.AppImage

You can assign this command to a keyboard shortcut.

To display the status of the lid with in indicator icon in the tray area, run the following command:

    $ ./dslli-indicator.AppImage

You can add this command to your startup application preferences to start the indicator at system start.

# Screenshots

## Laptop goes to standby upon closing the lid
![](https://i.imgur.com/QjTzAXS.png)

## Laptop does not go to standby upon closing the lid
![](https://i.imgur.com/yyt6A0r.png)

# Attribution
I greatly appreciate the work of Jacob Vlijm who created dslli in response to my original question on [AskUbuntu](https://askubuntu.com/questions/815032/how-can-i-quickly-disable-standby-lid-off-in-ubuntu-unity-16-04). My mere intention with this repository is to structure his work and prepare it to provide a package that can be easily installed by new users. Moreover, I want to sincerely thank the user [probono](http://discourse.appimage.org/users/probono/summary) who helped me on the [AppImage Community Forum](http://discourse.appimage.org/t/hello-world-example/161/5) to create a universally installable AppImage package.
