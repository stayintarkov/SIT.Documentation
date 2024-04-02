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