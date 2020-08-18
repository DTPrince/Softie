# Softie

### Functionality Required
* Import csv (google forms results) soft reserves
    * Cleanse duplicates
* Import roster (exorsus I imagine)
    * flag players who don't have a soft reserve set
    * cleanse duplicates
* +1 support? (in new raid menu probs)
    * reset
* saving configuration
* manual entry for SRs
* handling 2 SR raids (in new raid menu probs)

### Main Views
3 tabbed views
1. Soft reserve explorer
    * Shows a list of all people and their reserves
    * should be searchable by player and by item
    * flags people without a soft reserve
2. Boss-view
    * Drop-down menu of bosses in raid
    * Shows items of boss and people who have them SR-ed
3. I don't remember but it was great, I'm sure


### Tool bar
* File
    * about
    * create new raid
    * import SR
        * SR
        * roster
        * raid
    * save
    * help
* Save icon

### Create new raid window
* Type
    * Raid (AQ20/ZG/MC/BWL/AQ40, etc)
    * No. soft reserves used (0-n)
    * +1?
        * reset at... (no reset/boss name)

### Hot-keys
* ctrl-s        -> Save
* ctrl-i        -> import SR
* ctrl-shift-i  -> import roster
* ctrl-l        -> load raid
* ctrl-n        -> new raid
* 1             -> tab 1
* 2             -> tab 2
* 3             -> tab 3

### Feature impl order
1. Boss-loot database
2. Toolbar (basics)
3. Tabs (basics)
3. New raid window
4. Import SRs
5. Save
6. ...

### Pipe dream
* Open old raid on startup (crashes, etc.)
* curl google forms or something (live would be primo)
* export configuration/package for others (master looter) to load. Might be the same as load old raid
* pictures with all the doods/items
* raid options menu
    * allows checking +1, etc
* Set background icon to be <IB> spinning wheel
