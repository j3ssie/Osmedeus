import sys
import time
from pprint import pprint

from Osmedeus.core import utils
from Osmedeus.modules import initials
from Osmedeus.modules import subdomain
from Osmedeus.modules import recon
from Osmedeus.modules import assetfinding
from Osmedeus.modules import takeover
from Osmedeus.modules import screenshot
from Osmedeus.modules import portscan
from Osmedeus.modules import gitscan
from Osmedeus.modules import burpstate
from Osmedeus.modules import brutethings
from Osmedeus.modules import dirbrute
from Osmedeus.modules import vulnscan
from Osmedeus.modules import ipspace
from Osmedeus.modules import sslscan
from Osmedeus.modules import headers
from Osmedeus.modules import conclusion

# runnning normal routine if none of module specific
def normal(options):
    if options.get('RESET') == 'True':
        utils.print_good("Initials configurations")
        return
    utils.print_good("Running with {0} speed".format(options['SPEED']))

    # Create skeleton json
    initials.Initials(options)

    # Finding subdomain
    subdomain.SubdomainScanning(options)

    # Scanning for subdomain take over
    takeover.TakeOverScanning(options)

    # Screen shot the target on common service
    screenshot.ScreenShot(options)

    # Recon
    recon.Recon(options)

    # Recon
    assetfinding.AssetFinding(options)

    # Scanning for CorsScan
    cors.CorsScan(options)

    # Discovery IP space
    ipspace.IPSpace(options)

    # SSL Scan
    sslscan.SSLScan(options)

    # Headers Scan
    headers.HeadersScan(options)

    # Note: From here the module gonna take really long time
    # for scanning service and stuff like that
    utils.print_info('This gonna take a while')

    # Scanning all port using result from subdomain scanning
    # and also checking vulnerable service based on version
    portscan.PortScan(options)

    # Directory scan
    dirbrute.DirBrute(options)

    # Starting vulnerable scan
    vulnscan.VulnScan(options)

    # brutethings.BruteThings(options)

    conclusion.Conclusion(options)


def specific(options, module):
    module = module.lower()

    initials.Initials(options)

    if 'sub' in module or 'subdomain' in module:
        subdomain.SubdomainScanning(options)
        takeover.TakeOverScanning(options)
        screenshot.ScreenShot(options)
        cors.CorsScan(options)
        recon.Recon(options)
        assetfinding.AssetFinding(options)

    if 'ip' in module:
        # Discovery IP space
        ipspace.IPSpace(options)

    if 'screen' in module:
        # Discovery IP space
        screenshot.ScreenShot(options)

    if 'portscan' in module:
        # scanning port, service and vuln with masscan and nmap
        portscan.PortScan(options)

    if 'headers' in module:
        headers.HeadersScan(options)

    if 'asset' in module:
        assetfinding.AssetFinding(options)

    if 'vuln' in module:
        # scanning vulnerable service based on version
        vulnscan.VulnScan(options)

    if 'dir' in module:
        # run blind directory brute force directly
        dirbrute.DirBrute(options)

    if 'brute' in module or 'force' in module:
        # running brute force things based on scanning result
        brutethings.BruteThings(options)

    if 'git' in module:
        gitscan.GitScan(options)

    # if 'burp' in module:
    #     burpstate.BurpState(options)

    conclusion.Conclusion(options)


# just for debug purpose
def debug(options):
    utils.print_good("Debug routine")
    utils.print_good("Running with {0} speed".format(options['SPEED']))
    # Create skeleton json
    pprint(options)

    initials.Initials(options)

    # ##Finding subdomain
    subdomain.SubdomainScanning(options)

    # ####waiting for previous module
    # utils.just_waiting(options, 'SubdomainScanning')
    # recon.Recon(options)

    # ###Screen shot the target on common service
    screenshot.ScreenShot(options)


    # ###Scanning for subdomain take over
    # takeover.TakeOverScanning(options)

    # ##Discovery IP space

    # ipspace.IPSpace(options)


    # # # ##Scanning for CorsScan
    # cors.CorsScan(options)


    # ### SSL Scan
    # sslscan.SSLScan(options)

    # ##Headers Scan
    # headers.HeadersScan(options)

    # ##### Note: From here the module gonna take really long time for scanning service and stuff like that
    # utils.print_info('This gonna take a while')

    # dirbrute.DirBrute(options)

    # #Scanning all port using result from subdomain scanning and also checking vulnerable service based on version
    # portscan.PortScan(options)

    # # #Starting vulnerable scan
    # vulnscan.VulnScan(options)

    # # #Brute force service from port scan result
    # # brutethings.BruteThings(options)

    # conclusion.Conclusion(options)
