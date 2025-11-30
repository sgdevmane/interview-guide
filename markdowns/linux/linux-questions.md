# Linux Interview Questions

## Table of Contents

1. [How do you check disk space and usage?](#q1-how-do-you-check-disk-space-and-usage) <span class="beginner">Beginner</span>
2. [Explain file permissions (chmod)?](#q2-explain-file-permissions-chmod) <span class="beginner">Beginner</span>
3. [How to find a file by name or content?](#q3-how-to-find-a-file-by-name-or-content) <span class="intermediate">Intermediate</span>
4. [What is `grep` and how do you use it?](#q4-what-is-grep-and-how-do-you-use-it) <span class="beginner">Beginner</span>
5. [How to check running processes and kill them?](#q5-how-to-check-running-processes-and-kill-them) <span class="intermediate">Intermediate</span>
6. [Difference between Soft Link and Hard Link?](#q6-difference-between-soft-link-and-hard-link) <span class="intermediate">Intermediate</span>
7. [How to check listening ports (netstat/ss)?](#q7-how-to-check-listening-ports-netstatss) <span class="intermediate">Intermediate</span>
8. [Explain `cron` and `crontab`?](#q8-explain-cron-and-crontab) <span class="intermediate">Intermediate</span>
9. [What is the difference between Process and Thread?](#q9-what-is-the-difference-between-process-and-thread) <span class="advanced">Advanced</span>
10. [How do you check memory usage (free/top)?](#q10-how-do-you-check-memory-usage-freetop) <span class="beginner">Beginner</span>
11. [What is SSH and how does it work?](#q11-what-is-ssh-and-how-does-it-work) <span class="advanced">Advanced</span>
12. [Explain standard streams (stdin, stdout, stderr)?](#q12-explain-standard-streams-stdin-stdout-stderr) <span class="intermediate">Intermediate</span>
13. [How to view the end of a log file in real-time?](#q13-how-to-view-the-end-of-a-log-file-in-real-time) <span class="beginner">Beginner</span>
14. [What is a Daemon?](#q14-what-is-a-daemon) <span class="intermediate">Intermediate</span>
15. [How to change the owner of a file (chown)?](#q15-how-to-change-the-owner-of-a-file-chown) <span class="beginner">Beginner</span>
16. [What is the `/proc` filesystem?](#q16-what-is-the-proc-filesystem) <span class="advanced">Advanced</span>
17. [How to compress and extract files (tar)?](#q17-how-to-compress-and-extract-files-tar) <span class="beginner">Beginner</span>
18. [What is `systemd`?](#q18-what-is-systemd) <span class="advanced">Advanced</span>
19. [How to check IP address and Network Interface info?](#q19-how-to-check-ip-address-and-network-interface-info) <span class="beginner">Beginner</span>
20. [Explain the Linux Boot Process?](#q20-explain-the-linux-boot-process) <span class="advanced">Advanced</span>

---

<div id="q1-how-do-you-check-disk-space-and-usage" class="question">
  1. How do you check disk space and usage?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><code>df -h</code>: Displays <strong>free disk space</strong> for all mounted filesystems in a human-readable format (GB/MB).</li>
    <li><code>du -sh <directory></code>: Displays <strong>disk usage</strong> of a specific directory (summary).</li>
  </ul>
</div>

<div id="q2-explain-file-permissions-chmod" class="question">
  2. Explain file permissions (chmod)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p>Linux permissions are Read (r=4), Write (w=2), Execute (x=1). They are set for Owner, Group, and Others.</p>
  <ul>
    <li><code>chmod 755 file</code>: Owner(rwx=7), Group(rx=5), Others(rx=5).</li>
    <li><code>chmod +x script.sh</code>: Adds execute permission for everyone.</li>
  </ul>
</div>

<div id="q3-how-to-find-a-file-by-name-or-content" class="question">
  3. How to find a file by name or content?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>By Name:</strong> <code>find /path -name "filename.txt"</code></li>
    <li><strong>By Content:</strong> <code>grep -r "search_string" /path/to/search</code></li>
  </ul>
</div>

<div id="q4-what-is-grep-and-how-do-you-use-it" class="question">
  4. What is `grep` and how do you use it?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <p><code>grep</code> searches for patterns in files.</p>
  <ul>
    <li><code>grep "error" log.txt</code>: Search for "error" in log.txt.</li>
    <li><code>grep -i "error" log.txt</code>: Case-insensitive search.</li>
    <li><code>grep -v "info" log.txt</code>: Invert match (show lines NOT containing "info").</li>
  </ul>
</div>

<div id="q5-how-to-check-running-processes-and-kill-them" class="question">
  5. How to check running processes and kill them?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><code>ps aux</code>: Lists all running processes.</li>
    <li><code>top</code> or <code>htop</code>: Real-time view of processes.</li>
    <li><code>kill <PID></code>: Sends SIGTERM to process ID.</li>
    <li><code>kill -9 <PID></code>: Forcefully kills the process (SIGKILL).</li>
  </ul>
</div>

<div id="q6-difference-between-soft-link-and-hard-link" class="question">
  6. Difference between Soft Link and Hard Link?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Soft Link (Symbolic Link):</strong> Points to the file path (like a shortcut). If original file is deleted, the link breaks. Can cross filesystems.
      <br><code>ln -s original linkname</code></li>
    <li><strong>Hard Link:</strong> Points to the inode (physical data). If original file is deleted, the content remains accessible via the link. Cannot cross filesystems.
      <br><code>ln original linkname</code></li>
  </ul>
</div>

<div id="q7-how-to-check-listening-ports-netstatss" class="question">
  7. How to check listening ports (netstat/ss)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>Modern systems use <code>ss</code>, older ones use <code>netstat</code>.</p>
  <ul>
    <li><code>ss -tulpn</code>:
      <ul>
        <li><code>-t</code>: TCP</li>
        <li><code>-u</code>: UDP</li>
        <li><code>-l</code>: Listening sockets</li>
        <li><code>-p</code>: Show process using the port</li>
        <li><code>-n</code>: Numeric (don't resolve hostnames)</li>
      </ul>
    </li>
    <li><code>netstat -tulpn</code>: Similar flags.</li>
  </ul>
</div>

<div id="q8-explain-cron-and-crontab" class="question">
  8. Explain `cron` and `crontab`?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>cron:</strong> The daemon that executes scheduled commands.</li>
    <li><strong>crontab:</strong> The file where users define schedules.</li>
    <li>Format: <code>* * * * * command_to_run</code>
      <br>(Minute, Hour, Day of Month, Month, Day of Week).</li>
    <li>Example: <code>0 2 * * * /backup.sh</code> runs every day at 2:00 AM.</li>
  </ul>
</div>

<div id="q9-what-is-the-difference-between-process-and-thread" class="question">
  9. What is the difference between Process and Thread?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Process:</strong> An instance of a program in execution. Has its own memory space (heap, stack, globals). Heavyweight context switching.</li>
    <li><strong>Thread:</strong> A segment of a process. Threads share the memory space of the parent process. Lightweight context switching.</li>
  </ul>
</div>

<div id="q10-how-do-you-check-memory-usage-freetop" class="question">
  10. How do you check memory usage (free/top)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><code>free -h</code>: Shows total, used, and free RAM/Swap in human-readable format.</li>
    <li><code>vmstat</code>: Reports virtual memory statistics.</li>
    <li><code>cat /proc/meminfo</code>: Detailed memory info.</li>
  </ul>
</div>

<div id="q11-what-is-ssh-and-how-does-it-work" class="question">
  11. What is SSH and how does it work?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><strong>SSH (Secure Shell)</strong> is a protocol for secure remote login.</p>
  <ul>
    <li>Uses <strong>Public Key Cryptography</strong> for authentication.</li>
    <li><strong>Handshake:</strong> Client and Server agree on encryption parameters.</li>
    <li><strong>Authentication:</strong> Client proves identity using private key (or password).</li>
    <li><strong>Session:</strong> All data transferred is encrypted.</li>
    <li>Default port: 22.</li>
  </ul>
</div>

<div id="q12-explain-standard-streams-stdin-stdout-stderr" class="question">
  12. Explain standard streams (stdin, stdout, stderr)?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <ul>
    <li><strong>stdin (0):</strong> Standard Input. Data fed into a program (keyboard or pipe).</li>
    <li><strong>stdout (1):</strong> Standard Output. Where the program prints normal data (terminal).</li>
    <li><strong>stderr (2):</strong> Standard Error. Where the program prints error messages.</li>
    <li><strong>Redirection:</strong>
      <ul>
        <li><code>> file</code>: Redirect stdout to file.</li>
        <li><code>2> file</code>: Redirect stderr to file.</li>
        <li><code>|</code> (Pipe): Pass stdout of one command to stdin of another.</li>
      </ul>
    </li>
  </ul>
</div>

<div id="q13-how-to-view-the-end-of-a-log-file-in-real-time" class="question">
  13. How to view the end of a log file in real-time?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <pre><code class="language-bash">tail -f /var/log/syslog</code></pre>
  <p>The <code>-f</code> (follow) flag keeps the stream open and prints new lines as they are added to the file.</p>
</div>

<div id="q14-what-is-a-daemon" class="question">
  14. What is a Daemon?
  <span class="difficulty intermediate">Intermediate</span>
</div>

<div class="answer">
  <p>A <strong>Daemon</strong> is a background process that runs without direct user interaction.</p>
  <ul>
    <li>Usually starts at boot time.</li>
    <li>Ends with the letter 'd' (e.g., <code>httpd</code>, <code>sshd</code>, <code>mysqld</code>).</li>
    <li>Managed by init systems like <code>systemd</code> or <code>System V</code>.</li>
  </ul>
</div>

<div id="q15-how-to-change-the-owner-of-a-file-chown" class="question">
  15. How to change the owner of a file (chown)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <pre><code class="language-bash">chown user:group filename</code></pre>
  <p>Example: <code>chown mctavish:developers project.js</code> changes owner to 'mctavish' and group to 'developers'.</p>
</div>

<div id="q16-what-is-the-proc-filesystem" class="question">
  16. What is the `/proc` filesystem?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><code>/proc</code> is a virtual filesystem (not on disk, but in memory) that contains information about running processes and the kernel.</p>
  <ul>
    <li><code>/proc/cpuinfo</code>: CPU details.</li>
    <li><code>/proc/meminfo</code>: Memory usage.</li>
    <li><code>/proc/[PID]/</code>: Info about a specific process (e.g., <code>/proc/1/cmdline</code>).</li>
  </ul>
</div>

<div id="q17-how-to-compress-and-extract-files-tar" class="question">
  17. How to compress and extract files (tar)?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><strong>Compress (Create Archive):</strong>
      <br><code>tar -czvf archive.tar.gz /path/to/directory</code>
      <br>(c: create, z: gzip, v: verbose, f: file)
    </li>
    <li><strong>Extract:</strong>
      <br><code>tar -xzvf archive.tar.gz</code>
      <br>(x: extract)
    </li>
  </ul>
</div>

<div id="q18-what-is-systemd" class="question">
  18. What is `systemd`?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <p><code>systemd</code> is the standard init system and service manager for most Linux distributions.</p>
  <ul>
    <li>It is the first process started (PID 1).</li>
    <li>It manages services (<code>systemctl start nginx</code>).</li>
    <li>It handles parallel startup of system components.</li>
    <li>It manages logs via <code>journald</code>.</li>
  </ul>
</div>

<div id="q19-how-to-check-ip-address-and-network-interface-info" class="question">
  19. How to check IP address and Network Interface info?
  <span class="difficulty beginner">Beginner</span>
</div>

<div class="answer">
  <ul>
    <li><code>ip addr show</code> (or just <code>ip a</code>): Modern command.</li>
    <li><code>ifconfig</code>: Deprecated but common legacy command.</li>
    <li><code>hostname -I</code>: Shows just the IP address.</li>
  </ul>
</div>

<div id="q20-explain-the-linux-boot-process" class="question">
  20. Explain the Linux Boot Process?
  <span class="difficulty advanced">Advanced</span>
</div>

<div class="answer">
  <ol>
    <li><strong>BIOS/UEFI:</strong> Performs POST (Power On Self Test) and loads the Bootloader.</li>
    <li><strong>Bootloader (GRUB):</strong> Loads the Kernel into memory.</li>
    <li><strong>Kernel:</strong> Initializes hardware and mounts the root filesystem.</li>
    <li><strong>Init System (systemd):</strong> Starts services and user space (PID 1).</li>
  </ol>
</div>
