from FlashCards import Term, Flashcard
def main():
    automation_scripting_terms = ['Continuous integration (CI)',
                                  'Code is constantly written and merged into a central repo frequently',
                                  'Security checks CI',
                                  'Documented sec baselines, large scale security analysis during testing',
                                  'Continuous Delivery (CD)',
                                  'the testing and release is automated for the application, manually deploy app',
                                  'Continuous Deployment (CD)', 'Entire testing and deployment process is automated']
    ob = Term(automation_scripting_terms)
    ob.convert_list()
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
    card = Flashcard(ob)
    card.shuffle_cards()
    card.start_studying()


if __name__ == '__main__':
    main()
