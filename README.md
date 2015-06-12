# sshcp
Moving big files around the network
Secure transfers often fail when the files are relatively big (>100GB). This can be frustrating when moving big files using scp or rsync. This simple utility does low level splitting of files, transfers the chunks over the network and reassembles the chunks on the other side.
