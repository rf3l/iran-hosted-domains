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
the [release page](https://github.com/SamadiPour/iran-hosted-domains/releases).

### Qv2ray

In the release section, you'll find the qv2ray_schema file.

1. Download the file.
2. open `preferences` and click on `Advanced Route Settings`.
3. From the bottom of the screen, click on `import schema...`
4. choose the downloaded file (qv2ray_schema.json).
5. in the opened dialogue box, click on yes.
6. Click on OK.

![image](https://user-images.githubusercontent.com/24422125/115480663-397d3880-a260-11eb-88db-d3d7f8074767.png)

### .dat file

It can be used in all v2fly, v2ray and xray clients.

1. Download `iran.dat` file.
2. Copy/Import file in your client  
  for example:
    - v2ray macOS: `/usr/local/share/v2ray`
    ![image](https://user-images.githubusercontent.com/24422125/123522516-f2ce1380-d6d2-11eb-971f-0176f6e5b8ec.png)
    - SagerNet Android: import from `Route -> Three dots -> Manage Route Assets`   

<p align="center">
  <img alt="sagernet" src="https://user-images.githubusercontent.com/24422125/123522689-1cd40580-d6d4-11eb-90c1-a0341927e283.jpg">
</p>

3. Add proper rules
    - `ext:iran.dat:ir`
    - `ext:iran.dat:other`

4. Reconnect

## Files

- **iran.dat:** Contains both `ir_domains.txt` and `other_domains.txt`.
- **ir_domains:** Contains all websites that ends with `.ir`.
- **other_domains:** Contains all websites that ends with `.com` or other Top-level domains name.
- **qv2ray_schema:** Importable json schema that can be used in [Qv2ray](https://github.com/Qv2ray/Qv2ray).

## Source

Currently, there are only two main sources:

- [ITO GOV](https://g2b.ito.gov.ir/index.php/site/list_ip)
- [ADSL TCI](https://adsl.tci.ir/panel/sites)
- [Custom List](https://github.com/SamadiPour/iran-hosted-domains/blob/main/src/data/custom_domains.py)

If you know of any other source, or you found a website that isn't here, please open
an [issue](https://github.com/SamadiPour/iran-hosted-domains/issues) or add that specific site to `custom_domains.py`
file or contact me.

## How does it work?

I wrote a python script to get files from the above sources. This script runs in GitHub Action and generates domains
files.

Currently, I run GitHub Action manually, however, if I find out when these sources will update themselves, I will make
it run automatically.
