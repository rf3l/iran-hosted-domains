# Iran Hosted Domains

Many Iranians are aware of the fact that a lot of websites are blocked or censored, so they use a VPN daily. There are
some issues when you use a VPN while visiting some Iranian websites. To exclude those websites from the VPN, I have
listed all Iranian hosted domains here.

## VPN Problems

The following issues arise when using VPN for some Iran hosted websites:

- They may force you to have Iran IP to be able to access.
- They may offer 50% off bandwidth while having Iran IP.
- They may limit speed for non-Iran IPs or VPNs are slow.

## Usage

This can differ depending on which tool you use. You can download the domains list from
the [release](https://github.com/SamadiPour/iran-hosted-domains/releases) section.

I will provide more detailed instructions for popular tools.

## Files

- **ir_domains:** Contains all websites that ends with `.ir`
- **other_domains:** Contains all websites that ends with `.com` or other Top-level domains name
- **qv2ray_schema:** Importable json schema that can be used in [Qv2ray](https://github.com/Qv2ray/Qv2ray)

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