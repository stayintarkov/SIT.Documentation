.. include:: global.rst

.. _faqs:

Frequently Asked Questions (FAQ)
================================

This page contains common questions we get all the time, if their answer is simple enough it will appear here.

My |SIT| isn't working.
-----------------------

For support, you can join our :ref:`Discord <discord>` however, if your issue is because you haven't read this guide,
the **ENTIRE** support team will steal 47% of your Socks

How do I turn on Nametags.
--------------------------

See :ref:`Server Configuration <serverconf>` in the Configuration page for details on that.

.. _p2pr:

What is the Difference between Relay and a Peer-To-Peer connection?
-------------------------------------------------------------------

These are both connection options that the Host can pick, and each have some advantages and disadvantages

Relay
~~~~~

Relay is the system |SIT| swapped to using for connections since the change over from HTTP to WebSockets. It is a TCP based system that
has the User send data to the Aki Server, then the Server sends that to the other Users:

    User ------> Server ------> All Users

Using this method alows users with Restricted NAT types to still be able to connect to the server, since they are communicating with
the server instead of the clients, however, in some sitations this can lead to higher latency as the packets have to go to from the user, to the server,
back to the users.

Peer-To-Peer
~~~~~~~~~~~~

Peer-To-Peer is a new method added in the 0.14 update, it uses UDP and instead of communicating with the server, the clients all just cross
communicate instead, this does mean all clients will need to be able to connect directly to each other:

    User ------> Raid Host ------> User

This will allow for a theoretically lower latency if everyone has a NAT type that allows this, however if handled incorrectly it can cause
packets to "Go Missing" which will result in Latency Spikes and Massive De-sync. (So the True Live Tarkov Experience). But when handled
correctly, this method will allow for lower ping and faster responses from Clients to raid events.

So what should I use?
~~~~~~~~~~~~~~~~~~~~~

You can use either method outlined above, however if you have a Strict NAT type, you may need to use Relay, and if you have issues with one
method, give the other a shot.

How do I submit a Bug Report?
-----------------------------

.. note:: 
    Submiting a proper bug report is crutial to us helping you, if it is not submited properly it may cause :strike:`our souls to exit our bodies`
    us to not be able to properly help you.

    There are 2 kinds of bug report, a Standard Bug Report, which will be any issues while playing SIT.

    And a |SITM| Bug Report, for issues involving the |SIT| Manager Program.

.. _standbug:

Standard Bug Report
~~~~~~~~~~~~~~~~~~~

#. Go to the |SIT| :ref:`Discord<discord>`
#. Scroll to the bottom of the channels to find the "bug-reports" fourm, click on that
#. Click "New Post" and give it a Title related to your
#. Select the relevant tags for the post
#. The message should contain a description of your issue and steps we can use to replicate it **THIS IS VERY IMPORTANT**
#. Attach any relevant images that may help, or the ``diagnostics.zip`` if it's a manager issue, or if we request it, see :ref:`here<manbug>` for steps on how to obtain it
#. Create the post, and you're done

.. raw:: html

   <details>
      <summary>Creating Bug Report</summary>

.. image:: images/SubmitBugReport.apng
   :width: 800

.. raw:: html

   </details>

|brs|

.. _manbug:

|SITM| Bug Report
~~~~~~~~~~~~~~~~~

.. note:: 
    When creating an SIT Manager bug report, please follow these steps to get the ``diagnostics.zip`` file, and then do the steps outlines
    :ref:`here<standbug>` to submit the bug report on our Discord

#. Go to the "Tools" tab of the manager
#. Click Generate logs
#. Make sure everything is ticked, unless you've been told otherwise
#. Click "Generate Log Bundle"
#. Chose a location to save the ``diagnostics.zip``, somewhere you can access later
#. Follow the steps outlined :ref:`here<standbug>` to create a bug report on our discord. **MAKE SURE TO SELECT THE SIT MANAGER TAG AND INCLUDE YOUR** ``diagnostics.zip``

.. raw:: html

   <details>
      <summary>Creating Diagnostics.zip</summary>

.. image:: images/GenerateManLogs.apng
   :width: 800

.. raw:: html

   </details>

|brs|

.. _fleaissue:

My Flea market doesn't have new offeres or trades?
--------------------------------------------------

.. note:: 
   This issue can be caused by a misconfigured ``coopConfig.json`` file. It stops the flea market requests from coming through correctly
   which stops new offeres and trades from appearing. Here are the steps to fix it.

#. Stop the AKI Server
#. Open the ``coopConfig.json`` located in ``SIT/Server/user/mods/SITCoop/config/``
#. Change "messageWSUrlOverride:" to "0.0.0.0:6969" **ONLY CHANGE FROM 0.0.0.0 IF YOU KNOW WHAT YOU'RE DOING**
#. Change "useMessageWSUrlOverride:" to "true" **MAKE SURE TRUE IS LOWERCASE**
#. Save the file and reboot the server and make sure it's working