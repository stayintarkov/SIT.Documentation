.. include:: global.rst

.. _faqs:

Frequently Asked Questions (FAQ)
================================

This page contains common questions we get all the time, if their answer is simple enough it will appear here.

My |SIT| isn't working.
-----------------------

For support, you can join our `Discord <https://discord.gg/f4CN4n3nP2>`_ however, if your issue is because you haven't read this guide,
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