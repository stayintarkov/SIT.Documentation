Usage
=====

.. _installation:

StayInTarkov Coop Mod Install Guide for Host
============================================

**Downloads**
-------------

- SPT AKI versions have been provided, but some may encounter a 404 error. If so, try the following troubleshooting steps:

  .. code-block:: none

     If you encounter a 404 error while trying to download:
     - Clear Cache/Cookies: Though it might not directly solve the issue, it's worth a try.
     - Use a Proxy: Try accessing the download through a free proxy server. 

  .. note::

     Clearing cache/cookies might not always help, but it's a simple step to attempt. Using a proxy can sometimes bypass download restrictions or errors encountered on specific networks.

- `SPT Aki 3.7.6 <https://pixeldrain.com/u/jCCfDEsi>`_
- `SIT.Aki-Server-Mod <https://github.com/stayintarkov/SIT.Aki-Server-Mod/releases>`_
- `SIT.Manager <https://github.com/stayintarkov/SIT.Manager/releases/latest/download/SIT.Manager.zip>`_ 
    - `Requires .Net8 <https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/runtime-desktop-8.0.0-windows-x64-installer>`_

**Installation Steps**
----------------------

1. Ensure Escape from Tarkov is up to date.

2. Download the three ZIP files listed in the Downloads section above.

3. Create three folders named `SIT-game`, `server`, `launcher`:

   .. code-block:: none

      SIT/
      ├── server/      # SPT-Aki Server Mod
      ├── SIT-game/    # EFT Client
      └── launcher/    # SIT Manager or Classic Launcher

4. Copy your live Escape from Tarkov files into the `SIT-game` folder. 

   - Downgrade EFT to a supported version using patchers available through a provided link.

5. Extract the contents of the chosen SPT AKI version into the `server` folder.

6. Extract the `SIT.Server-Aki-Mod` into `server/user/mods/SITCoop`. Ensure you run `Aki.Server.exe` once to generate configuration files.

7. Extract the `SIT.Manager` into the `launcher` folder.

8. **Configure IP Settings:**

   - Modify `server/Aki_Data/Server/configs/http.json` with your local or VPN (Hamachi/Radmin) IP address.
   - Adjust `server/user/mods/SITCoop/config/coopConfig.json` to match your external or VPN IP.

9. **Port Forwarding (If Not Using Hamachi/Radmin):**

   .. note::

      Port forward `6969` and `6970` if not using a VPN solution. This step might require additional router configuration.

10. Start `server/aki.server.exe`.

11. Launch `SIT.Manager`, specify the `SIT-game` folder path in the settings, and confirm the EFT version is correct.

12. Install `SIT` from the tools tab, selecting the most recent release.

13. Enter the server IP and connect to begin hosting.

.. warning::

   DO NOT CHANGE the port number in `http.json` or `coopConfig.json`. They DO NOT need to be the same.





.. _installation:

StayInTarkov Coop Mod Install Guide for Client
===========================================

.. note:: If you are running the server for your friends, follow the guide `HERE <https://discord.com/channels/1175114933713776690/1178076298803949588/1178076379171008632>`_. This guide is for clients only. When in doubt, start over or reach out for support `HERE <https://discord.com/channels/1175114933713776690/1175127842737094656>`_.


**NOTE:** After copying the Escape From Tarkov files, you should **NOT** touch the live version of EFT again.

Prerequisites
=============
Escape from Tarkov must be up to date and **RUN THE GAME AT LEAST ONCE**.

Install Steps
=============

1. Download the latest SIT Manager from the `SIT.Manager releases <https://github.com/stayintarkov/SIT.Manager/releases/latest/download/SIT.Manager.zip>`_.

2. Create a new folder named SIT to house your 'Game' and 'Launcher' folders.

3. Inside the SIT folder, create two more folders named 'Game' and 'Launcher'. Your folder structure should resemble the following:

.. code-block:: none

   SIT/
   ├── Game/
   └── Launcher/

4. Copy all files from your 'live' Escape From Tarkov folder to your 'Game' folder.

.. image:: https://i.imgur.com/QGBbogr.png
   :alt: Game folder after copying files

5. Download the latest downgrader from the provided link.

6. After downloading, extract the contents so that 'patcher.exe' and 'AKI_Patches' are in the 'Game' directory.

.. note:: Run 'patcher.exe' and **WAIT** for it to complete. It will prompt you when finished. It's normal for the 'Aki_Patches' folder to be deleted during the downgrade process.

7. Next, extract the 'SIT.Manager.zip' and copy its contents to the 'Launcher' folder.

8. Start the launcher by running the 'SIT.Manager.exe' file located in your 'Launcher' directory.

9. In the SIT.Manager, set the EFT Path to your copied and patched EFT files in the 'Game' folder.

.. note:: Select 'Settings', click 'Change' for 'EFT Path' setting, and select your 'SIT/Game' folder.

10. Select the 'Tools' menu and click 'Install SIT'. The launcher will download the latest release of SIT.

11. Make sure to select the version of SIT that matches your version of EFT. 

.. note:: Look at the 'Product version' in the 'Details' pane of 'EscapeFromTarkov.exe' properties to find your version.

12. After installation, obtain the server IP from your host and enter it in the 'Play' tab along with a username and password. Select 'Remember Me' and click 'Connect'.

