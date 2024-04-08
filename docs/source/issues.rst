.. include:: global.rst
.. issues:

Common Issues
=============

.. _fleaissue:

My Flea Market Doesn't Have New Offers or Trades
================================================

Problem
-------

Your flea market might not be displaying new offers or trades.

Cause
-----

This issue can often arise due to a misconfigured ``coopConfig.json`` file, which prevents flea market requests from being processed correctly, thereby stopping new offers and trades from appearing.

Solution
--------

Follow these steps to correct the issue:

1. **Stop the AKI Server**.

2. Navigate to the ``coopConfig.json`` file located in ``SIT\Server\user\mods\SITCoop\config\``.

3. Modify the ``messageWSUrlOverride`` field to include your local IP with the port ``:6969`` appended at the end (e.g., ``192.168.X.X:6969``).

4. Change ``useMessageWSUrlOverride`` to ``true``. Ensure the value ``true`` is in lowercase.

5. Save the changes to the ``coopConfig.json`` file.

6. Reboot the server and verify that it is functioning correctly.

.. note::
   If you're running the AKI Server on Docker or a Virtual Private Server (VPS), you'll need to set the ``messageWSUrlOverride`` to your VPS's external IP address.

For Docker Users
----------------

If you're using Docker, follow these commands to update your IP configuration:

1. Stop the SITCoop container:

   .. code-block:: bash

      docker stop sitcoop

2. Retrieve your external IP address:

   .. code-block:: bash

      curl -4 icanhazip.com

3. Edit the ``coopConfig.json`` file:

   .. code-block:: bash

      nano server/user/mods/SITCoop/config/coopConfig.json

   Update the file with the following configuration, replacing ``IP YOU GET FROM icanhazip.com`` with the IP address you obtained from the previous step:

   .. code-block:: json

      {
          "webSocketPort": 6970,
          "natHelperPort": 6971,
          "useUPNP": false,
          "useMessageWSUrlOverride": true, <--- SET THIS TO TRUE
          "messageWSUrlOverride": "IP you get from icanhazip.com:6969"
      }

4. Start the SITCoop container:

   .. code-block:: bash

      docker start sitcoop

By following these steps, you should be able to resolve the issue with the flea market not displaying new offers or trades in your AKI Server environment.


I'm getting an ``ERROR: listen EADDRNOTAVAIL: address not avalible`` error.
---------------------------------------------------------------------------

.. note:: 
   This happens because there is already a process running that is taking up the target port, and multiple apps can't access the same port
   below is a quick command line method to find what is currently holding the port and close it

#. Press ``Win + R`` and enter "cmd"
#. Press ``CTRL + Shift + Enter`` to open cmd as an admin, click "Yes" to allow
#. Type ``netstat -ano | findstr : 6969``
#. There should be a set of numbers at the end of the process, like ``17720``
#. Type ``taskkill /PID (NUMBER) /F``, replace (NUMBER) with the number you got from above and hit enter
#. Try booting your server again

Infinite loading screen
-----------------------

.. note:: 
   If you are getting an infinite loading screen, this is usually caused by mods that aren't compatible with the current version of |SIT|, try remvoing all your mods
   and launching the game and server again.

SIT Manager "A task was cancelled"
----------------------------------

.. note:: 
   This is most often caused by a firewall issue, however it can also be caused by an incorrect IP address

   Make sure you have entered the hosts IPv4 address correctly, and if using a VPN that there isn't any connection issues between you and the host.

Aki.Server.exe Has Deleted itself
---------------------------------

.. note:: 
   For some reason windows defender is dectecting the Aki server as malware, this is a false postive, Aki have requested it not be flagged as malware, however this
   process can take more than a month to resolve, so in the meantime, add the server directory as an exeption to Windows Defender, like below:

   (You will read Click 10 times, and you **WILL** enjoy it)

#. Open windows settings
#. Click "Update and Security"
#. Click "Windows Security"
#. Click "Open Windows Security"
#. Click "Virus and Threat Protection"
#. Under "Virus & Threat protection settings" click "Manage Settings"
#. Scroll down to "Exclusions" and click "Add or Remove exclusions"
#. Click "Add an Exclusion" and click "Folder"
#. Navigate to your |SDIR| and click "Select Folder"

.. raw:: html

   <details>
      <summary>Firewall Exclusion</summary>

.. video:: _static/videos/WindowsFirewall.webm
   :width: 700
   :loop:

.. raw:: html

   </details>

|brs|
