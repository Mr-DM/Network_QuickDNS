
# QuickDNS

A DNS implementation project featuring a DNS client, server, and caching server.

## Components

### Dedicated Terminal

![alt text]({9A0E2E37-B86E-4CA6-8EE7-AF614B63FD88}.png)


### DNS_Client.py
CLI tool to send DNS queries to a DNS server.

**Usage:**
```bash
python DNS_Client.py <hostname> <server_ip> [port]
```

**VSC**
```bash
Run Python File in Dedicated Terminal
```

### DNS_Server.py
Authoritative DNS server that resolves domain names to IP addresses.

**Usage:**
```bash
python DNS_Server.py [--port 53]
```

**VSC**
```bash
Run Python File in Dedicated Terminal
```
### Caching_Server.py
DNS caching server that stores recent queries to improve response times.

**Usage:**
```bash
python Caching_Server.py [--port 53] [--upstream_server 8.8.8.8]
```

**VSC**
```bash
Run Python File in Dedicated Terminal
```
![alt text]({111EFB05-307D-483D-ACB2-88547428A925}.png)
## Installation

```bash
git clone <repository_url>
cd QuickDNS_stage1
```

## Requirements

- Python 3.7+
- No external dependencies

## Architecture

1. **Client** sends queries to the Caching Server
2. **Caching Server** checks its cache; if miss, forwards to DNS Server
3. **DNS Server** performs recursive lookups or returns authoritative answers

## License

MIT
