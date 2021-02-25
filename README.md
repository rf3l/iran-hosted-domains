# Iran Hosted Domains

## Motivation

Many Iranians are aware of the fact that a lot of websites are blocked or censored, so they use a VPN daily. The
following issues arise when using VPN for some Iran hosted websites:

- They may force you to have Iran IP to be able to access.
- They may offer 50% off bandwidth while having Iran IP.
- They may limit speed for non-Iran IPs or VPNs are slow.

Some of these issues also affect Iranians in other countries.

To fix these issues, I decided to list all Iran hosted domains here.

## Usage

This can differ depending on which tool you use. You can download the domains list from
the [release](https://github.com/SamadiPour/iran-hosted-domains/releases) section.

I will provide more detailed instructions for popular tools.

## Source

Currently, there are only two main sources:

- [ITO GOV](https://g2b.ito.gov.ir/index.php/site/list_ip)
- [ADSL TCI](https://adsl.tci.ir/panel/sites)

If you know of any other source, or you found a website that isn't here, please open
an [issue](https://github.com/SamadiPour/iran-hosted-domains/issues) or contact me.

## How does it work?

I wrote a python script to get files from the above sources. This script runs in GitHub Action and generates domains
files.

Currently, I run GitHub Action manually, however, if I find out when these sources will update themselves, I will make
it run automatically.