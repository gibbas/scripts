#!/usr/bin/python
#
# Prints out a matching password from your default keyring in
# Seahorse/Gnome Keyring in plaintext to stdout. Useful for stuff
# such as sudo -A 
#
# a = gibbas
# Code by Tommy Karlsson <$a@$a.com>

import gnomekeyring as gk

# use the password whose description starts with..
starts = 'VPN'

keyring = gk.get_default_keyring_sync()
keys = gk.list_item_ids_sync(keyring)

for key in keys:
	try:
		pw = gk.item_get_info_sync(keyring, key)
		if pw.get_display_name().startswith(starts):
			print pw.get_secret() 
	except:
		print "Didn't work"
