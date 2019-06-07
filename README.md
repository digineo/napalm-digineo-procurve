# Napalm Aruba

[![CircleCI](https://circleci.com/gh/digineo/napalm-digineo-procurve.svg?style=svg)](https://circleci.com/gh/digineo/napalm-digineo-procurve)

Napalm driver for aruba procurve switches. Written to be used in combination with netbox.


## Tested devices

| Switch Model Name               	| Tested Firmware Version 	|
|---------------------------------	|-------------------------	|
| **Aruba 2530 8G PoE+-Switch**     | YA.16.05.0008             |


## Motivation and Acknowledgement

There are already [a few](https://github.com/mwallraf/napalm-hp-procurve/) [python packages](https://github.com/ixs/napalm-procurve) that try to provide support for the procurve switches series to [napalm](https://napalm-automation.net/).  These packages come in different levels of quality and supported features though.

The main motivation point for this package is to write a napalm driver for procurve switches that also work well together with [netbox](https://github.com/digitalocean/netbox).  Thus the goal of this package is to provide all functionality of a napalm driver that is used by netbox.


## Is it any good?

[Yes.](https://news.ycombinator.com/item?id=3067434)
