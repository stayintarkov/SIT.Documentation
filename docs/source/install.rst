Installation
============

.. _install:

This section is dedicated for a new installation of Stay In Tarkov. If you're looking to update SIT, click here.

Getting started
---------------
Escape From Tarkov requirements
~~~~~~~~~~~~~~~~~~

* You need a legally purchased copy of Escape From Tarkov, `obtainable here <https://www.escapefromtarkov.com/preorder-page>`_.
* You need to install the game using the official game launcher.
* You need to run the game at least once using the official game launcher.

.. warning::
   * **DON'T** move your original EFT game folder following the installation.
   * **DON'T** change any of the files in your original EFT game folder.
   * **DON'T** install SIT in your original EFT game folder. **YOU HAVE BEEN WARNED!**
   * **ALWAYS** make sure you are able to run the game using the official game launcher before using SIT.

Preparing the folder structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create the following folder structure on the drive of your choice, as long as it has enough space for Escape From Tarkov.

.. code-block:: none
   
   SIT/
   ├── Game/
   ├── Server/
   └── Launcher/

.. note::
   It is recommended to use this folder structure for a SIT installation. Note that the rest of the documentation will refer to 
   that structure.

Preparing Escape From Tarkov files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Copy your Escape From Tarkov game files to the "/SIT/Game" folder.

.. warning::
   * Do not create a subfolder in /SIT/Game (ex: /SIT/Game/EFT).
   * Do not change any of the files in /SIT/Game folder.

Installing SIT.Manager
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Download the latest `SIT.Manager release <https://github.com/stayintarkov/SIT.Manager.Avalonia/releases/latest>`_.
* Extract the SIT.Manager zip to the "/SIT/Launcher" folder. 

.. warning::
   * Do not create a subfolder in /SIT/Launcher (ex: /SIT/Launcher/SIT.Manager).

.. note::
   The SIT.Manager allows you to install and play SIT. It also provides additional tools such as mods management, downgrade patchers, 
   server management and much more.

Installing Stay In Tarkov
-------------------------

.. warning:: 
   Before proceeding with the steps below, make sure you have followed every steps in the "Getting started" section "here". We receive
   a lot of support requests about SIT not working but most of the time, steps are not followed correctly.

   **Make sure to follow every single steps properly and don't try to take shortcuts.**

Installing using SIT.Manager
----------------------------

* Start the manager from ``/SIT/Launcher/SIT.Manager.exe.``
* Go to "Settings" page.

Client
~~~~~~

#. Locate the "EFT Path" setting and click the "Change" button.

   * Browse to your "/SIT/Game" folder and click "Select Folder".

#. Go to the "Install" page.
#. Click "Install SIT".
#. Choose the latest version of Stay In Tarkov. It will be the first one in the list.
#. Wait for the manager to say "Install Completed"

Server
~~~~~~

#. Locate the "SPT-AKI Path" setting and click the "Change" button.

   * Browse to your "/SIT/Server" folder and click "Select Folder".

#. Go to the "Install" page.
#. Click "Install Server + SIT Mod".
#. Choose the latest version of SPT-AKI. It will be the first one in the list
#. Wait for the manager to say "Install Completed"

Installing manually
~~~~~~~~~~~~~~~~~~~

It is recommended to use SIT.Manager to install Stay In Tarkov. However, if you wish to do it manually, please follow the steps below.

WIP - Come back later.