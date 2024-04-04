.. include:: global.rst
.. issues:

Common Issues
=============

.. _fleaissue:

My Flea market doesn't have new offeres or trades?
--------------------------------------------------

.. note:: 
   This issue can be caused by a misconfigured ``coopConfig.json`` file. It stops the flea market requests from coming through correctly
   which stops new offeres and trades from appearing. Here are the steps to fix it.

#. Stop the AKI Server
#. Open the ``coopConfig.json`` located in ``SIT\Server\user\mods\SITCoop\config\``
#. Change "messageWSUrlOverride:" to "0.0.0.0:6969" **ONLY CHANGE FROM 0.0.0.0 IF YOU KNOW WHAT YOU'RE DOING**
#. Change "useMessageWSUrlOverride:" to "true" **MAKE SURE TRUE IS LOWERCASE**
#. Save the file and reboot the server and make sure it's working

I'm getting a ``ERROR: listen EADDRNOTAVAIL: address not avalible`` error.
--------------------------------------------------------------------------

.. note:: 
   This happens because there is already a process running that is taking up the target port, and multiple apps can't access the same port
   below is a quick command line method to find what is currently holding the port and close it

#. Press ``Win + R`` and enter "cmd"
#. Press ``CTRL + Shift + Enter`` to open cmd as an admin, click "Yes" to allow
#. Type ``netstat -ano | findstr : 6969``
#. There should be a set of numbers at the end of the process, like ``17720``
#. Type ``taskkill /PID (NUMBER) /F``, replace (NUMBER) with the number you got from above and hit enter
#. Try booting your server again