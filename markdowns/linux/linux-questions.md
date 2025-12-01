<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/linux-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Linux Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

## Table of Contents

1. [How do you check disk space usage?](#q1) <span class="beginner">Beginner</span>
2. [How do you manage file permissions (chmod)?](#q2) <span class="beginner">Beginner</span>
3. [How do you find a file by name or content?](#q3) <span class="intermediate">Intermediate</span>
4. [What is Grep and how do you use it?](#q4) <span class="beginner">Beginner</span>
5. [How do you check and kill running processes?](#q5) <span class="intermediate">Intermediate</span>
6. [What is the difference between Soft Link and Hard Link?](#q6) <span class="intermediate">Intermediate</span>
7. [How do you check listening ports?](#q7) <span class="intermediate">Intermediate</span>
8. [What is the difference between Cron and Crontab?](#q8) <span class="intermediate">Intermediate</span>
9. [Process vs Thread in Linux?](#q9) <span class="advanced">Advanced</span>
10. [How do you check memory usage?](#q10) <span class="beginner">Beginner</span>
11. [What is SSH and how does it work?](#q11) <span class="advanced">Advanced</span>
12. [Explain Standard Streams (Stdin, Stdout, Stderr)?](#q12) <span class="intermediate">Intermediate</span>
13. [How do you monitor log files in real-time?](#q13) <span class="beginner">Beginner</span>
14. [What is a Daemon?](#q14) <span class="intermediate">Intermediate</span>
15. [How do you change file ownership (chown)?](#q15) <span class="beginner">Beginner</span>
16. [What is the /proc filesystem?](#q16) <span class="advanced">Advanced</span>
17. [How do you archive and compress files (tar)?](#q17) <span class="beginner">Beginner</span>
18. [What is systemd?](#q18) <span class="advanced">Advanced</span>
19. [How do you check the Linux Kernel version?](#q19) <span class="beginner">Beginner</span>
20. [What is the difference between TCP and UDP?](#q20) <span class="intermediate">Intermediate</span>
21. [How do you set environment variables?](#q21) <span class="beginner">Beginner</span>
22. [What is the `top` vs `htop` command?](#q22) <span class="beginner">Beginner</span>
23. [How do you use `sed` for text replacement?](#q23) <span class="intermediate">Intermediate</span>
24. [What is `awk` used for?](#q24) <span class="advanced">Advanced</span>
25. [How do you check network connectivity (ping/curl)?](#q25) <span class="beginner">Beginner</span>

---

<a id="q1"></a>
### Q1: How do you check disk space usage?

**Difficulty**: Beginner

**Strategy**:
Disk space management is crucial for server health.
*   **`df` (Disk Free):** Displays the amount of available disk space for file systems. Use `-h` for human-readable format (GB, MB).
*   **`du` (Disk Usage):** Estimates file space usage. Useful for finding which directory is consuming space.

**Code Example**:
```bash
# Check free space on all mounted filesystems
df -h

# Check size of current directory
du -sh .

# Find top 5 largest directories
du -h --max-depth=1 | sort -hr | head -n 5
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q2"></a>
### Q2: How do you manage file permissions (chmod)?

**Difficulty**: Beginner

**Strategy**:
Linux permissions control who can Read (r=4), Write (w=2), and Execute (x=1) a file.
*   **Structure:** User (u), Group (g), Others (o).
*   **Numeric Mode:** Sum of values (e.g., 7 = 4+2+1 = rwx).
*   **Symbolic Mode:** `u+x` (add execute to user).

**Code Example**:
```bash
# Give User Read/Write/Exec (7), Group Read/Exec (5), Others Read/Exec (5)
chmod 755 script.sh

# Add execute permission for everyone
chmod +x script.sh

# Remove write permission for group and others
chmod go-w file.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q3"></a>
### Q3: How do you find a file by name or content?

**Difficulty**: Intermediate

**Strategy**:
*   **`find`:** Search for files in a directory hierarchy based on name, size, time, etc.
*   **`locate`:** Search a prebuilt database of files (faster but maybe outdated).
*   **`grep`:** Search *inside* files for specific text content.

**Code Example**:
```bash
# Find file by name (case insensitive)
find /var/log -iname "*.log"

# Find files larger than 100MB
find / -size +100M

# Find files modified in the last 24 hours
find . -mtime -1

# Search for string "error" inside all files in current dir
grep -r "error" .
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q4"></a>
### Q4: What is Grep and how do you use it?

**Difficulty**: Beginner

**Strategy**:
`grep` (Global Regular Expression Print) is a powerful command-line tool used for searching plain-text data sets for lines that match a regular expression. It is essential for log analysis.

**Code Example**:
```bash
# Search for "root" in /etc/passwd
grep "root" /etc/passwd

# Case insensitive search (-i) with line numbers (-n)
grep -in "error" app.log

# Recursive search in directory (-r)
grep -r "config" /etc/nginx/

# Invert match (show lines that DO NOT match)
grep -v "200 OK" access.log
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q5"></a>
### Q5: How do you check and kill running processes?

**Difficulty**: Intermediate

**Strategy**:
*   **`ps`:** Snapshot of current processes.
*   **`top` / `htop`:** Real-time view of processes.
*   **`kill`:** Send a signal to a process (default TERM 15, force KILL 9).
*   **`pkill`:** Kill by name.

**Code Example**:
```bash
# List all running processes
ps aux

# Find PID of a specific process (e.g., python)
ps aux | grep python

# Kill process with PID 1234 (Graceful)
kill 1234

# Force kill (if hung)
kill -9 1234

# Kill all processes named "node"
pkill node
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q6"></a>
### Q6: What is the difference between Soft Link and Hard Link?

**Difficulty**: Intermediate

**Strategy**:
*   **Soft Link (Symbolic Link):** A shortcut. It points to the *path* of the original file. If the original is deleted, the link breaks (dangling). Can link across filesystems.
*   **Hard Link:** A direct pointer to the *inode* (physical data) of the file. It is essentially a backup name for the file. If original is deleted, the content remains until all hard links are gone. Cannot link directories or across filesystems.

**Code Example**:
```bash
# Create Soft Link (ln -s target link_name)
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Create Hard Link
ln file.txt file_backup.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q7"></a>
### Q7: How do you check listening ports?

**Difficulty**: Intermediate

**Strategy**:
Identifying which application is using a port is common for debugging connectivity issues.
*   **`netstat`:** Legacy tool (but common).
*   **`ss`:** Modern replacement for netstat (faster).
*   **`lsof`:** List Open Files (and ports).

**Code Example**:
```bash
# Show all listening TCP/UDP ports with PID
sudo netstat -tulpn

# Modern equivalent
sudo ss -tulpn

# Check what is running on port 80
sudo lsof -i :80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q8"></a>
### Q8: What is the difference between Cron and Crontab?

**Difficulty**: Intermediate

**Strategy**:
*   **Cron:** The system daemon (service) that runs in the background and executes scheduled tasks.
*   **Crontab (Cron Table):** The text file that contains the list of commands to be executed and their schedule.

**Code Example**:
```bash
# Edit current user's crontab
crontab -e

# List current user's crontab
crontab -l

# Crontab Syntax: m h dom mon dow command
# Run backup.sh every day at 3:30 AM
30 03 * * * /home/user/backup.sh
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q9"></a>
### Q9: Process vs Thread in Linux?

**Difficulty**: Advanced

**Strategy**:
*   **Process:** An instance of a running program. Has its own isolated memory space, PID, and file descriptors. Heavyweight context switch.
*   **Thread:** A subset of a process (Lightweight Process). Threads within the same process share memory space and resources but have their own stack. Faster context switch.
*   In Linux, threads are treated as processes that share resources (`clone()` syscall).

**Code Example**:
```bash
# View threads of a specific PID
ps -T -p <PID>

# Count threads for a process
ls /proc/<PID>/task | wc -l
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q10"></a>
### Q10: How do you check memory usage?

**Difficulty**: Beginner

**Strategy**:
*   **`free`:** Displays total, used, and free memory/swap.
*   **`vmstat`:** Virtual memory statistics.
*   **`top`:** Real-time memory per process.

**Code Example**:
```bash
# Show memory in Human-readable format (MB/GB)
free -h

# Continuous monitoring every 2 seconds
vmstat 2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q11"></a>
### Q11: What is SSH and how does it work?

**Difficulty**: Advanced

**Strategy**:
**SSH (Secure Shell)** is a protocol for securely accessing network services over an unsecured network. It replaces insecure Telnet/FTP.
*   **Encryption:** Uses symmetric encryption for the session, asymmetric (Public/Private key) for authentication/key exchange, and hashing for integrity.
*   **Port:** Default 22.
*   **Key-Based Auth:** Safer than passwords. Public key on Server (`~/.ssh/authorized_keys`), Private key on Client.

**Code Example**:
```bash
# Connect to server
ssh user@192.168.1.10

# Generate SSH keys
ssh-keygen -t rsa -b 4096

# Copy public key to server
ssh-copy-id user@192.168.1.10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q12"></a>
### Q12: Explain Standard Streams (Stdin, Stdout, Stderr)?

**Difficulty**: Intermediate

**Strategy**:
In Linux, Everything is a file. Processes have 3 default file descriptors:
1.  **Stdin (0):** Standard Input (Keyboard).
2.  **Stdout (1):** Standard Output (Screen/Terminal).
3.  **Stderr (2):** Standard Error (Screen/Terminal).
You can redirect these streams using `>`, `>>`, `|`.

**Code Example**:
```bash
# Redirect Output to file (overwrite)
ls > list.txt

# Redirect Output to file (append)
echo "Log" >> app.log

# Redirect Error to file
python script.py 2> error.log

# Redirect Output AND Error to same file
command > output.log 2>&1

# Discard output (send to black hole)
command > /dev/null 2>&1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q13"></a>
### Q13: How do you monitor log files in real-time?

**Difficulty**: Beginner

**Strategy**:
*   **`tail -f`:** Follows the file as it grows.
*   **`less +F`:** Opens file and follows (allows scrolling back, unlike tail).
*   **`journalctl -f`:** Follow systemd logs.

**Code Example**:
```bash
# Watch syslog in real-time
tail -f /var/log/syslog

# Watch only lines containing "error"
tail -f app.log | grep "error"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q14"></a>
### Q14: What is a Daemon?

**Difficulty**: Intermediate

**Strategy**:
A **Daemon** is a background process that runs without direct user interaction. They usually handle system services (web server, database, printing).
*   Naming convention: often ends in `d` (e.g., `httpd`, `sshd`, `mysqld`).
*   Managed by init system (Systemd, SysVinit).

**Code Example**:
```bash
# Check status of ssh daemon
systemctl status sshd

# Restart a daemon
sudo systemctl restart nginx
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q15"></a>
### Q15: How do you change file ownership (chown)?

**Difficulty**: Beginner

**Strategy**:
`chown` changes the user and/or group ownership of a file.
*   Syntax: `chown user:group file`.
*   Root privileges usually required to change ownership to another user.

**Code Example**:
```bash
# Change owner to 'ubuntu'
sudo chown ubuntu file.txt

# Change owner and group to 'www-data' recursively
sudo chown -R www-data:www-data /var/www/html
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q16"></a>
### Q16: What is the /proc filesystem?

**Difficulty**: Advanced

**Strategy**:
`/proc` is a **pseudo-filesystem**. It doesn't exist on disk; it's created in memory by the kernel at boot.
*   It exposes kernel and process information as files.
*   Example: `/proc/cpuinfo` (CPU details), `/proc/meminfo` (Memory), `/proc/<PID>` (Process details).
*   Changing files here can alter kernel parameters at runtime (`sysctl`).

**Code Example**:
```bash
# Check CPU model
cat /proc/cpuinfo

# Enable IP forwarding (modify kernel param)
echo 1 > /proc/sys/net/ipv4/ip_forward
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q17"></a>
### Q17: How do you archive and compress files (tar)?

**Difficulty**: Beginner

**Strategy**:
`tar` (Tape Archive) is the standard tool. It bundles files. Compression (gzip) is usually added.
*   **c**: Create
*   **x**: Extract
*   **v**: Verbose
*   **f**: File
*   **z**: Gzip (compression)

**Code Example**:
```bash
# Create compressed archive
tar -czvf archive.tar.gz /path/to/folder

# Extract archive
tar -xzvf archive.tar.gz

# List contents without extracting
tar -tf archive.tar.gz
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q18"></a>
### Q18: What is systemd?

**Difficulty**: Advanced

**Strategy**:
**Systemd** is the modern init system (PID 1) for most Linux distributions (Ubuntu, CentOS, RHEL).
*   It bootstraps the user space and manages system processes/services.
*   Features: Parallel startup (faster boot), dependency management, on-demand activation, logging (journald).
*   Replaces older SysVinit scripts.

**Code Example**:
```bash
# List all active services
systemctl list-units --type=service

# View boot logs (errors)
journalctl -p 3 -xb
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q19"></a>
### Q19: How do you check the Linux Kernel version?

**Difficulty**: Beginner

**Strategy**:
Knowing the kernel version is important for compatibility and security patching.

**Code Example**:
```bash
# Print kernel release
uname -r

# Print all system info
uname -a

# Read from proc
cat /proc/version
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q20"></a>
### Q20: What is the difference between TCP and UDP?

**Difficulty**: Intermediate

**Strategy**:
*   **TCP (Transmission Control Protocol):** Connection-oriented, Reliable, Ordered, Error-checking. Heavyweight. Used for Web (HTTP), Email (SMTP), SSH.
*   **UDP (User Datagram Protocol):** Connectionless, Unreliable (fire and forget), Unordered. Lightweight/Fast. Used for Video Streaming, DNS, VoIP, Gaming.

**Code Example**:
```bash
# Check TCP connections
ss -t

# Check UDP connections
ss -u
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q21"></a>
### Q21: How do you set environment variables?

**Difficulty**: Beginner

**Strategy**:
Variables that affect the behavior of processes on the system (e.g., `PATH`, `EDITOR`).
*   **Temporary:** Valid only for current shell session.
*   **Permanent:** Added to `~/.bashrc` or `/etc/environment`.

**Code Example**:
```bash
# Set temporary variable
export APP_ENV=production

# View variable
echo $APP_ENV

# Make permanent (User)
echo 'export APP_ENV=production' >> ~/.bashrc
source ~/.bashrc
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q22"></a>
### Q22: What is the `top` vs `htop` command?

**Difficulty**: Beginner

**Strategy**:
Both monitor system resources (CPU/RAM) and processes.
*   **top:** Built-in, basic interface.
*   **htop:** Interactive, color-coded, scrollable, mouse support. Not installed by default.

**Code Example**:
```bash
# Install htop
sudo apt install htop
htop
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q23"></a>
### Q23: How do you use `sed` for text replacement?

**Difficulty**: Intermediate

**Strategy**:
`sed` (Stream Editor) allows filtering and transforming text. Most common use: Find and Replace.
*   Syntax: `s/search/replace/flags`.

**Code Example**:
```bash
# Replace first occurrence of "foo" with "bar" (print to stdout)
echo "foo bar foo" | sed 's/foo/bar/'

# Replace ALL occurrences (global flag 'g')
echo "foo bar foo" | sed 's/foo/bar/g'

# Edit file in-place (-i)
sed -i 's/localhost/127.0.0.1/g' config.conf
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q24"></a>
### Q24: What is `awk` used for?

**Difficulty**: Advanced

**Strategy**:
`awk` is a complete programming language designed for text processing and data extraction. It processes data row by row and splits it into columns (fields).
*   Default delimiter: Whitespace.
*   `$1` = First column, `$2` = Second, `$NF` = Last.

**Code Example**:
```bash
# Print only the 1st and 3rd column of a file
awk '{print $1, $3}' data.txt

# Print rows where the 2nd column is greater than 50
awk '$2 > 50 {print $0}' data.txt

# Sum values in the first column
awk '{sum += $1} END {print sum}' numbers.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

<a id="q25"></a>
### Q25: How do you check network connectivity (ping/curl)?

**Difficulty**: Beginner

**Strategy**:
*   **`ping`:** Check reachability (ICMP).
*   **`curl`:** Transfer data (HTTP/FTP). Check web server status.
*   **`telnet` / `nc`:** Check specific port connectivity.

**Code Example**:
```bash
# Check if google.com is reachable
ping -c 4 google.com

# Check headers of a website (is it 200 OK?)
curl -I https://google.com

# Download file
curl -O https://example.com/file.zip
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>
