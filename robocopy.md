# Robocopy

Be aware of versions, it's not uncommon to run into an installation which may lack needed features.

### Example usage

    robocopy "O:\IT" "\\<server_address>\e$\IT" /E /ZB /DCOPY:T /COPYALL /R:1 /W:1 /V /TEE /LOG:Robocopy.log

### Exclude older files on source (don't overwrite newer files)

    robocopy "O:\IT" "\\<server_address>\e$\IT" /E /ZB /DCOPY:T /COPYALL /R:1 /W:1 /V /TEE /XO /LOG:Robocopy.log
    
    # Broken down:
    /E Subdirectories, including empty ones
    /ZB restartable mode
    /DCOPY:T Copy timestamps
    /R:1 1 retry 
    /W:1 wait between retry in seconds
    /V Verbose output
    /TEE Output to console an dlog 
    /LOG:Robocopy.log
    /COPYALL Copy ALL file info
    /XO: Exclude older files on source

### File class categories

By default, Lonely files (and directories) are always copied, unless /XL switch is used. Changed, Newer and Older files will be considered to be candidates for copying (subject to further filtering described below), Same files will be skipped (not copied), and Extra and Mismatched files (and directories) will simply be reported in the output log.

    File        Exists In   Exists In        Source/Dest     Source/Dest   Source/Dest
    Class       Source      Destination      File Times      File Sizes    Attributes
    =========== =========== ================ =============== ============= ============
    Lonely      Yes         No               n/a             n/a           n/a
    Tweaked     Yes         Yes              Equal           Equal         Different
    Same        Yes         Yes              Equal           Equal         Equal
    Changed     Yes         Yes              Equal           Different     n/a
    Newer       Yes         Yes              Source > Dest   n/a           n/a
    Older       Yes         Yes              Source < Dest   n/a           n/a
    Extra       No          Yes              n/a             n/a           n/a
    Mismatched  Yes (file)  Yes (directory)  n/a             n/a           n/a
