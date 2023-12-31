from FlashCards import Term
from FlashCards import Flashcard


def main():
    automation_scripting_terms = ['Continuous integration (CI)',
                                  'Code is constantly written and merged into a central repo frequently',
                                  'Security checks CI',
                                  'Documented sec baselines, large scale security analysis during testing',
                                  'Continuous Delivery (CD)',
                                  'the testing and release is automated for the application, manually deploy app',
                                  'Continuous Deployment (CD)', 'Entire testing and deployment process is automated']
    ob = Term()
    ob.add_terms(automation_scripting_terms)
    authentication_terms1 = ['Directory Services',
                             'Central database that stores all the usernames, psswds, computers, devices, '
                             'ect. All authentication requests reference this directory', 'Federation',
                             'Uses credentials stored with a third party to authenticate with your org, must est trust']
    ob.add_terms(authentication_terms1)
    authentication_terms2 = ['Attestation',
                             'Proves the hardware is really the user and is a sys you can trust. It is attesting '
                             'it is trust worthy', 'Remote Attestation', 'Device provides an operational report '
                                                                         'to verification server, Encrypted',
                             'IMEI', 'International Mobile Equipment Identity, is a numeric identifier, usually unique',
                             'SMS',
                             'Short message service/text, authenticates using a text, easy to reassign phone number '
                             'harder to'
                             'intercept', 'Push notification',
                             'Uses an authentication factor pushed to an app, sometimes push'
                             'is sent in the clear (bad)']
    ob.add_terms(authentication_terms2)
    authentication_terms3 = ['Pseudo random token generator', 'can be an app or device, many use TOTP', 'TOTP',
                             'Time based on time passwd algorithm, uses a secret key and time of day', 'HOTP',
                             'HMAC-based one time password algorithm, One-time psswd, never use it again, '
                             'hash is diff everytime', 'Phone call',
                             'call gives you a random number, same disadvs as text (interception, forwarded',
                             'Static code', 'authentication that does not change, like pin or psswrds', 'Smart card',
                             'integrated circuit card, credit cards or access control cards, something you have']
    ob.add_terms(authentication_terms3)
    biometrics_terms = ['Biometric Factors', 'Fingerprints, retinal structure, iris, voice, and facial features can be '
                                             'used as scanners for access', 'Gait analysis', 'type of biometric factor '
                                                                                             'that is rarely used '
                                                                                             'but very unique',
                        'False acceptance rate (FAR)', 'Likelihood that an unauthorized user will be accepted, scanner'
                                                       'is not sensitive enough', 'False rejection rate (FRR)',
                        'Likelihood that an authorized user will be rejected, the scanner is too sensitive',
                        'Crossover error rate (CER)', 'sweet spot Far = FRR, up to you to adjust settings to reach '
                                                      'point']
    ob.add_terms(biometrics_terms)
    AAA_framework_terms = ['AAA framework', 'stands for Authentication, Authorization, and Accounting',
                           'Authentication', 'Prove you are who you are with factors', 'Identification', 'Who you claim'
                                                                                                         ' to be '
                                                                                                         '(username)',
                           'Authorization', 'Access based on ID and authentication', 'Accounting',
                           'Tracking who is authenticating', 'Cloud based security', 'Centralized platform managed by '
                                                                                     '3rd party $$$, might have API '
                                                                                     'integration',
                           'On prem authentication', 'Internal, need expertise to monitor and configure',
                           'Mult-factor authentication', 'Factors: something you know (PW/PIN), have (smart card), '
                                                         'and are (Biometrics); Attributes: Somewhere or something you '
                                                         'are (location hard with IPv6), can do (signature), exhibit or'
                                                         ' exhibit (gait), someone you know (trust)']
    ob.add_terms(AAA_framework_terms)
    redundancy_terms = ['Redundancy', 'Duplicate parts of the system so the org can function in case of failure',
                        'Geographic dispersal', 'creating redundancy in a diff geo outside scope of disaster',
                        'Multipath Input/Output', 'Type of Disk Redundancy, creates diff routes to network, mult fiber '
                                                  'channel switches',
                        'RAID', 'Redundant Array of independent disks, all the data is available because its on '
                                'mult drives/disks', 'RAID 0', 'Striping without parity = no duplication of data, '
                                                               'losing one drive could be complete system failure',
                        'RAID 1', 'Bare minimum, mirrors, takes 1 physical drive and duplicate all data into another'
                                  'this requires twice the disk space', 'RAID 5', 'Striping with parity, and only needs'
                                                                                  '1 additional disk']
    ob.add_terms(redundancy_terms)
    network_redundancy_terms = ['Load balancing', 'Balances load between mult servers, servers can be active or on '
                                                  'standby, if active server fails passes it to standby and makes '
                                                  'it the new server', 'NIC teaming/LB Fail over (LBFO)', 'mult '
                                                                                                          'connections'
                                                                                                          'to servers, '
                                                                                                          'allowing '
                                                                                                          'redundant '
                                                                                                          'paths to '
                                                                                                          'make a '
                                                                                                          'single inter'
                                                                                                          'face',
                                'Port aggregation', 'allows you to group multiple physical ports into one unit. '
                                                    'Port aggregation is useful for implementing load balancing and '
                                                    'provides a redundant link backup.']
    ob.add_terms(network_redundancy_terms)
    power_redundancy = ['UPS', 'Uninterruptible power supply, used for short term backup', 'UPS examples', '3 kinds: '
                                                                                                           '$Offline/'
                                                                                                           'standby, $$'
                                                                                                           'Line-inter'
                                                                                                           'active, On'
                                                                                                           'line$$$',
                        'Long term power backup options', 'Generators, but you need fuel and it takes a bit to turn on',
                        'Dual power supplies', 'Redundancy within the power supply with external power circuits',
                        'PDU', 'power distribution unit, has mult power outlets and usually includes monitoring and '
                               'control features']
    ob.add_terms(power_redundancy)
    replication_terms = ['SAN replication', 'Share data between devices just in case of failure for fast recovery',
                         'SAN', 'Storage area network', 'SAN to SAN replication', 'duplicate data from one center to '
                                                                                  'another',
                         'SAN snapshot', 'Takes a snap shot at any interval of time and copies to other SAN',
                         'VM replication', 'Virtual machine redundancy, vm is really a big file, can act as backup',
                         'On prem vs cloud for redundancy', 'Cloud connection usually slower, local devices faster '
                                                            'connectivity, cloud is cheaper, locally stored data you '
                                                            'have more control']
    ob.add_terms(replication_terms)
    backup_types = ['file backups', 'archive attribute sets when file is modified, full backups and incremental',
                    'incremental backup', 'only does files that have changed since full backup', 'full back up', 'do '
                                                                                                                 'this'
                                                                                                                 'firs'
                                                                                                                 't',
                    'back up types', 'incremental backups, differential backup, and full', 'incremental backup',
                    'start with full and have a recovery day',
                    'differential backup', 'every day backup gets bigger instead of small parts, just need full and '
                                           'last differential', 'full backup',
                    ' all the selected data, high backup, low '
                    'restore time because single set of back'
                    'up tapes',
                    'incremental backup more info', 'new files and files modified since last backup'
                                                    'low backup, high restore time because its mult sets',
                    'Differential backup', 'all data modified since last backup, moderate backup and restore time',
                    'The archive attribute is cleared in', 'Full and incremental backups',
                    'Backup Media', 'Magnetic tape, disks, copy/image of system to duplicate',
                    'NAS', 'Network attached storage or file level access, connects to a shared a storage device across'
                           'the network, SAN is more efficient because it looks and feels like a separate storage device,'
                           'and does block-level access', 'other backups', 'Cloud and image', 'Backup locations',
                    'Offline (fast + secure, in disaster recovery site, Online backup (remote to third part, encrypted, '
                    'accessible from anywhere)']
    ob.add_terms(backup_types)
    resiliency_terms = ['Non persistence', 'Changes in cloud because usually cloud based environments are not static',
                        'High availability', 'Always on and availability when primary fails, may have mult components',
                        'Order of restoration', 'each application has a specific order certain components needs to be '
                                                'restored, depending on the type of the backup then the order is also'
                                                'specific', 'Incremental Order of restoration', 'Restores the full '
                                                                                                'backup, then all sub '
                                                                                                'incremental backups',
                        'Differential order of restoration',
                        'restores the full backup and the last differential backup',
                        'Diversity of technology', 'similar to biodiversity, using different types can be great if one '
                                                   'goes out or extra security from different types of attacks',
                        'Cryptography Diversity', 'We need this because all cryptography is temporary,'
                                                  'gives us more types of controls: admin, phys, technical']
    ob.add_terms(resiliency_terms)
    embedded_sys = ['Embedded system', 'hardware and software designed for specific tasks',
                    'example of embedded system', 'digital watch, traffic light controller',
                    'SoC', 'system on a chip, has mult components and functions on a single chip',
                    'Raspberry Pi', 'example of SoC', 'Issues with SoC',
                    'hardware my be difficult to upgrade or add to',
                    'FPGA',
                    'Field programmable gate array is an integrated circuit that be configured after it is made',
                    'SCADA/ICS', 'Supervisory control and data acquisition system also industrial control system, '
                                 'found in industrial facilities, very useful for monitoring from a '
                                 'computer using a central management console, segmented off network',
                    'IOT device issues', 'not made by security pros, better to put on separate network', 'Specialized'
                                                                                                         'devices',
                    'an example would be medical devices, these use embedded systems', 'VoIP',
                    'Voice over internet protocol, replaces POTS, is a complex embedded system', 'each '
                                                                                                 'computer is an example'
                                                                                                 'of a ', 'VoIP',
                    'HVAC', 'heating, ventilation, and air conditioning, not built with security in mind',
                    'Drones are an example of a', 'embedded system that is a flying vehicle',
                    'Examples of multifunction devices', 'Printers, scanners, and fax machines in one unit',
                    'RTOS', 'Real time operating system is designed to working with a specific schedule',
                    'example of RTOS', 'industrial equip, automobiles wheel slippage', 'Surveillance systems',
                    'Must secure so others cant see or hear, a type of embedded system is in this',
                    '5G', '5th generation of cellular communication, uses 10 gigabits per sec',
                    '5G significantly impacts', 'IoT devices because bandwidth is no longer an issue and you can send '
                                                'more data and cloud computing',
                    'SIM card', 'integrated circuit card, used to provide info to a cell network provider and'
                                'provides mobile details like IMSI', 'IMSI', 'internation mobile subscriber ID',
                    'Narrowband', 'type of connection that allows comms over narrow band of freq',
                    'Many Iot devices communicate over', 'narrowband', 'Baseband', 'single cable with digital'
                                                                                   'signal, on wired ethernet',
                    'Zigbee', 'IEEE 802.15.4 PAN, alt to wifi, not bluetooth, communicate with IoT over longer '
                              'distances and create a mesh network of devices',
                    'ISM band', 'freq that zigbee communicates on']
    ob.add_terms(embedded_sys)
    embedded_syscontraints = ['Constraint due to how embedded system is built',
                              'limited/missing features and power issues',
                              'Other constraints', 'has low CPU and type and speed of networks available, some cannot'
                                                   'be upgraded or doesnt even have authentication process']
    ob.add_terms(embedded_syscontraints)
    physical_securitycontrols = ['Purpose of physical barriers', 'safety, prevent access', 'Access control vestibules',
                                 'door opening mechanism, there is a set normal and action causes lock/unlock',
                                 'Signs',
                                 'physical security control that gives clear, specific instruction for EEs and '
                                 'visitors', 'alarms', 'physical control that is circuit based', 'CCTV', 'c'
                                                                                                         'losed '
                                                                                                         'circuit '
                                                                                                         'TV',
                                 'Industrial camouflage',
                                 'concealing an important facility in plain sight, like making '
                                 'it look like a warehouse or something with no visual clues or'
                                 ' signs', 'Guards and access lists', 'security using people'
                                                                      ' prevents guests from '
                                                                      'coming',
                                 'Two person integrity/control',
                                 'ensures no single person has access to assets, can use'
                                 'robot guards',
                                 'Door access controls', 'Conventional, deadbolt, electronic (pin) or token based (key '
                                                         'fob), or multi-factor',
                                 'Cable locks', 'temp locks and can work almost anywhere, actual cable with reinforced '
                                                'notch, def can cut this', 'USB data blocker', 'allow the voltage of a '
                                                                                               'USB but rejects the '
                                                                                               'data',
                                 'Proper lighting', 'type of security because attackers dont want to be seen',
                                 'Fencing',
                                 'physical security measure around the perimeter', 'Fire suppression',
                                 'remember these are electronics, water may not be best, Halon is bad, use Dupont FM',
                                 'Sensors', 'motion, noise, proximity, moisture, temp', 'Drone usage',
                                 'may be used for '
                                 'security for '
                                 'example site'
                                 'damage',
                                 'Faraday cage', 'blocks some types of signals, like the window of microwave oven',
                                 'Screened subnet or DMZ', 'a network with a controlled access through a firewall '
                                                           'and gives public access and keeps private items private',
                                 'PDS', 'protected distribution system, must keep cables in physically secure'
                                        'area. Prevents breakage, tapping, and DoS', 'Secure Areas',
                                 'Physical barrier to internal systems', 'air gap', 'physical separation between'
                                                                                    'networks so it would never be possible'
                                                                                    'for someone to get access through'
                                                                                    'shared network, like in stock market',
                                 'Vaults and safes', 'provides a secure room onsite', 'Hot and cold aisles',
                                 'these systems create heat, we need a cooling system that isnt too expensive so this '
                                 'helps by separating the air']
    ob.add_terms(physical_securitycontrols)
    secure_datadestruction = ['Why is proper data destruction and media sanitization important',
                              'Disposal can be a legal issue, critical info could end up in trash, you might want to resuse device',
                              'Garbage', 'can be used for malicious activity, shred it, burn, or pulp',
                              'Physical destruction', 'shredding drilling, pulverizing, electromag/degaussing',
                              '3rd party destruction will give', 'a certificate this was completed with'
                                                                 'the devices', 'Sanitizing media',
                              'purging data (some data) or wipe (unrecoverable, so we can reuse)']
    ob.add_terms(secure_datadestruction)
    crypt_concepts = ['cryptography uses', 'allows us to make things confidential, authenticate, non-repudiation, '
                                           'integrity', 'plaintext', 'unencrypted in the clear message', 'ciphertext',
                      'encrypted message', 'cipher', 'algorithm used to encrypt or decrypt', 'cryptographic keys',
                      'used to encrypt by adding to cipher, larger is better, mult can add more protection',
                      'key stretching', 'can use weak keys to make it stronger, hash pw and hash the hash', 'key '
                                                                                                            'stretching'
                                                                                                            'library',
                      'bcrypt, PBKDF2', 'Lightweight cryptography',
                      'a type of cryptography that does not need a high end CPU'
                      'or a ton of power, comes from IoT devices',
                      'Homomorphic encryption',
                      'HE, makes encrypted data easier to work with by allow you to make calc '
                      'with encrypted data, doesnt get decrypted at all, good with cloud',
                      'symmetric encryption', 'uses single shared key to encrypt and decrypt, bad if key gets out and '
                                              'scales poorly, like carrying the key in the locked case', 'asymmetric '
                                                                                                         'encryption',
                      'uses two or more keys, also known as public key cryptography, takes more overhead, you have a '
                      'public key (encrypt)  and private key (decrypt)', 'they key pair',
                      'large random number runs through key generation  number, one becomes public and the other is '
                      'private', '']
    ob.all_cards()
    card = Flashcard(ob)
    card.shuffle_cards()
    card.start_studying()



if __name__ == '__main__':
    main()
