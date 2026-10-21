# Linux Sysadmin Toolkit

A collection of Python utilities for Linux system administration, security monitoring, network troubleshooting, and filesystem management.

These scripts were originally developed through hands-on systems administration work and are maintained as reusable tools for common Linux administrative and security tasks.

## Tools

### Attacker Report

Analyzes Linux authentication logs to identify repeated failed login attempts.

**Features:**
- Parses failed password events from system logs
- Extracts source IP addresses using regular expressions
- Counts failed login attempts by source
- Filters IP addresses that exceed a login-attempt threshold
- Uses GeoIP data to identify the originating country
- Generates a formatted attacker report

**File:** `attacker_report.py`

---

### System Report

Collects system and network information from a Linux host and generates a formatted system report.

**Information collected:**
- Hostname and domain
- IP address and subnet mask
- Default gateway
- DNS servers
- Operating system and version
- Kernel version
- Disk capacity and usage
- CPU model and processor information
- Total and available memory

The report is displayed in the terminal and automatically saved as a host-specific log file.

**File:** `system_report.py`

---

### Ping Test

Provides a menu-driven utility for performing basic Linux network troubleshooting.

**Features:**
- Detects and displays the system's default gateway
- Tests connectivity to the local gateway
- Tests connectivity to a remote IP address
- Tests connectivity using a domain name to help verify DNS resolution
- Displays success or failure for connectivity tests

**File:** `ping_test.py`

---

### Shortcut Manager

Provides an interactive utility for managing symbolic links on a Linux system.

**Features:**
- Searches the filesystem for a requested file
- Handles multiple matching files through user selection
- Creates symbolic links in the user's home directory
- Deletes existing symbolic links
- Generates a report of symbolic links
- Handles invalid input and common filesystem errors

**File:** `shortcut.py`

## Requirements

- Python 3
- Linux environment
- Standard Linux utilities used by the individual scripts
- GeoIP support for `attacker_report.py`

The attacker report uses the `geoip` package and GeoLite2 database for IP geolocation.

## Usage

Clone the repository:

```bash
git clone https://github.com/FalseMomo/linux-sysadmin-toolkit.git
cd linux-sysadmin-toolkit
