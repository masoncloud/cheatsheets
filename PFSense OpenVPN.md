OpenVPN insallation
===================
### Written for PFSense platform (Works on Version 2.3-RELEASE)
Pulled from https://www.highlnk.com/2013/12/configuring-openvpn-on-pfsense/



Let’s get started by configuring a certificate authority in pfSense
Goto System–>Cert Manager

If you do not have one here than you should create a CA
Goto - Createan internal Certificate Authority
Settings I like:
```
Name - *****,
Method - Create an Internal Cert Auth.
Key Length - 4096 bits
Digest Algo - SHA512
```

Now Create a Cert:
Goto Certificate Manager tab
```
Method - Create Internal Cert
Descriptive name - ****
CA - pfSense Firewall
Key Length - 4096
Digest Algo - SHA512
Cert Type: Server Cert
Lifetime - ****
```

Fill in the geographic info you like for the cert.

Now that we have all the components in place we can configure OpenVPN.

Go To VPN–>OpenVPN

Select the Wizard.
```
Auth- Local User Access
CA - The one you created earlier.
Cert - The cert you created earlier.
```

You should select the WAN interface where OpenVPN will bind to if you want to be able to access your network
from the outside

The next sections deals with the cryptographic settings. In here we will specify to use TLS authentication and
have it generate a shared TLS authentication key which will give us another layer of security.

```
Interface - WAN
Protocol - UDP
Local Port - 1194
Description - ****

TLS Auth - Enabeled
Gen TLS Key - Enabled
TLS Shared Key - Null
DH Parameters - 2048
Enc Algo - AES-256-CBC+HMAC-SHA1(256)
```

Tunnel Settings

Moving onto the Tunnel settings we have the option of specifying the tunnel network which is the network that
our clients connecting to the VPN will be assigned an address from. You can specify whether all traffic should be
redirected through the tunnel and the local network that clients connecting from the outside can access. Near the
middle we can specify the maximum number of concurrent sessions and whether we want to use compression for the data
traversing the tunnel.

```
Tunnel Network - Local Net but with isolated subnet
Redirect Gateway - Enabled
Local Network - Local Subnet
Concurent Connections - 10
Compression - Enabled
Inter-Client Communication - Enabled
```

Client Settings

```
Dynamic IP - Enabeled
Address Pool - Enabled
```

Firewall
```
Add Firewall Rule - Enabled
OpenVPN add rule - Enabled
```

Once you are done you should see an entry under the server tab of OpenVPN.

The next step is to start creating user accounts that we will use during the authentication process. Creating user
accounts is done over at System–>User Manager under the users tab.

create a new user and fill out the form

Once the account has been created, we need to create a user certificate for the account. We will be going back to
System–>Cert Manager and under the certificates tab create a new certificate.

Hit the plus sign to start the creation process. Make sure to select “User Certificate” from the dropdown as you are
creating the certificate.

```
Method - Create an Internal Cert
Descriptive Name - ****
Cert Auth - CA created ealier
Key Length - 4096
Digest Alg - SHA512
Cert Type - User Cert
Lifetime - ***
Distinguished Name - ***
```

Once the certificate is created, we will go back to the user account that we made and modify it.
We will assign the certificate that we just created to the user account.
From the drop down list select the user certificate that we recently created.


```
System -> Cert Manager

Method - Choose Existing Cert
Existing Cert - One from ealier
```

Install the OpenVPN Client Export Utility from System–>Packages.
Then goto OpenVPN Client Export and save the client in the desired format.

Import in your client of choice and all is well.

