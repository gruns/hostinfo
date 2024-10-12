## HostInfo

#### Overview

`hostinfo` is a small Python 3 script that retrieves and displays quick, simple information about a provided URL, hostname, or IP address:
	* IPv4 address
	* Hostname
	* Location (city, region, country, postal code)
	* Owner (organization)

This information is fetched from ipinfo.io and cleaned up.

#### Get Started

First, install the dependencies:

```
pip3 install furl icecream
```

Then download [the script](/hostinfo), place it somewhere in your path, and run it with:

```
$n hostinfo <urlOrHostnameOrIpAddress>
```

Example:

```
$ hostinfo google.com
IPv4:      142.250.191.78
Hostname:  nuq04s43-in-f14.1e100.net
Location:  Sunnyvale, California, US, 94088
Owner:     AS15169 Google LLC
```

The first and only arguemnt, `<urlOrHostnameOrIpAddress>`, can be a URL, hostname, or IP address.

#### License

MIT