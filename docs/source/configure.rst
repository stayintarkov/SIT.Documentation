Configuration
=============

.. _configure:

This section is dedicated to the configuration of Stay In Tarkov. If you haven't installed Stay In Tarkov yet, click here.

Host configuration
------------------

Follow this section if you're planning to be the coop game host (server). At least one person in your group needs to follow
this process to be able to play coop together. The person with the best computer and network performance should be the
host for a better experience.

You must choose between port forwarding or virtual private network configuration. Port forwarding is the recommended choice.

**You do not need to do both.**

Port forwarding
~~~~~~~~~~~~~~~

.. note::
   Port forwarding is the process of opening a port on your external IP address and redirect the traffic to a specific 
   device. The process is different for all router models. Therefore, we cannot provide a step-by-step tutorial for 
   port forwarding.

   If you are unsure how to port forward, google "YOUR_ROUTER_MODEL port forward" or contact your Internet Service Provider.

.. warning::
   Not all Internet Service Provider allows port forwarding. Sometimes port forwarding is blocked at the provider level or
   at the router level. In any case, the person able to port forward should be the host, provided their computer and network 
   is capable.

   If you are unable to port forward, you can consider using a VPN such as Hamachi, RAdmin or ZeroTier. Click here to see
   how to configure a VPN with Stay In Tarkov.

* Open "SIT/Server/Aki_Data/Server/configs/http.json" with your preferred text text editor.
* Locate the "ip" parameter. You should see a default value of "127.0.0.1".
* Change "127.0.0.1" with your local IP address (ex: 192.168.0.23).
* Save your changes and close the text editor.

.. note::
   To find your local IP address:

   * Open the command prompt (press Win key + R and type cmd).
   * Type "ipconfig" (without quotes) and press enter.
   * If your computer is connected to your router using an ethernet cable, locate "Ethernet adapter".
   * If your computer is connected to your router using Wi-Fi, locate "Wireless LAN adapter Wi-Fi".
   * Locate the "IPv4 address" under the adapter you found: this is your local IP address.
   * Enter it in http.json.

Virtual Private Network
~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   Virtual private network such as Hamachi, Radmin or ZeroTier allows to create an internet-based "local" network. All traffic 
   will be transmitted through the internet and redirected to a virtual network adapter which acts as a local network. This is 
   useful for those which are unable to port forward. However, performance is not as good as port forwarding because 
   traffic must go through a third party service.

.. warning::
   We do not recommend using VPN to play Stay In Tarkov because they are known to have rate limitations and hinder network
   performance and stability. SIT is not well optimized and transmit a lot of data to synchronize information between players.
   
   **Use at your own risk.**

* Open "SIT/Server/Aki_Data/Server/configs/http.json" with your preferred text text editor.
* Locate the "ip" parameter. You should see a default value of "127.0.0.1".
* Change "127.0.0.1" with your VPN IP address (ex: 20.13.50.233).
* Save your changes and close the text editor.

.. note::
   To find your VPN IP address:

   * Open your VPN application (Hamachi, Radmin, ZeroTier, etc.)
   * Your VPN IP address is usually displayed in the main window.
   * If you cannot find it, google "VPN_NAME get my IP".

General configuration
---------------------