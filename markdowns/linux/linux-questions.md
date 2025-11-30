# Linux Interview Questions

## Table of Contents

1. [Check disk space?](#q1) <span class="beginner">Beginner</span>
2. [File permissions (chmod)?](#q2) <span class="beginner">Beginner</span>
3. [Find file by name?](#q3) <span class="intermediate">Intermediate</span>
4. [Grep usage?](#q4) <span class="beginner">Beginner</span>
5. [Check/Kill processes?](#q5) <span class="intermediate">Intermediate</span>
6. [Soft vs Hard Link?](#q6) <span class="intermediate">Intermediate</span>
7. [Check listening ports?](#q7) <span class="intermediate">Intermediate</span>
8. [Cron vs Crontab?](#q8) <span class="intermediate">Intermediate</span>
9. [Process vs Thread?](#q9) <span class="advanced">Advanced</span>
10. [Check memory usage?](#q10) <span class="beginner">Beginner</span>
11. [What is SSH?](#q11) <span class="advanced">Advanced</span>
12. [Stdin, Stdout, Stderr?](#q12) <span class="intermediate">Intermediate</span>
13. [Tail log file?](#q13) <span class="beginner">Beginner</span>
14. [What is a Daemon?](#q14) <span class="intermediate">Intermediate</span>
15. [Change owner (chown)?](#q15) <span class="beginner">Beginner</span>
16. [What is /proc?](#q16) <span class="advanced">Advanced</span>
17. [Tar command?](#q17) <span class="beginner">Beginner</span>
18. [What is systemd?](#q18) <span class="advanced">Advanced</span>
19. [Check IP address?](#q19) <span class="beginner">Beginner</span>
20. [Linux Boot Process?](#q20) <span class="advanced">Advanced</span>
21. [What is an Inode?](#q21) <span class="advanced">Advanced</span>
22. [What is the Root User?](#q22) <span class="beginner">Beginner</span>
23. [What is Sudo?](#q23) <span class="beginner">Beginner</span>
24. [Explain `ls -l` output?](#q24) <span class="beginner">Beginner</span>
25. [Create a directory?](#q25) <span class="beginner">Beginner</span>
26. [Remove a directory?](#q26) <span class="beginner">Beginner</span>
27. [Move vs Rename file?](#q27) <span class="beginner">Beginner</span>
28. [Copy file vs directory?](#q28) <span class="beginner">Beginner</span>
29. [What is the PATH variable?](#q29) <span class="intermediate">Intermediate</span>
30. [How to set an Environment Variable?](#q30) <span class="intermediate">Intermediate</span>
31. [What is .bashrc?](#q31) <span class="intermediate">Intermediate</span>
32. [Difference between `>` and `>>`?](#q32) <span class="beginner">Beginner</span>
33. [What is a Pipe `|`?](#q33) <span class="beginner">Beginner</span>
34. [Head vs Tail?](#q34) <span class="beginner">Beginner</span>
35. [What is `sed`?](#q35) <span class="advanced">Advanced</span>
36. [What is `awk`?](#q36) <span class="advanced">Advanced</span>
37. [Count lines in a file?](#q37) <span class="beginner">Beginner</span>
38. [Sort contents of a file?](#q38) <span class="beginner">Beginner</span>
39. [Remove duplicate lines?](#q39) <span class="intermediate">Intermediate</span>
40. [Compare two files?](#q40) <span class="intermediate">Intermediate</span>
41. [What is `nohup`?](#q41) <span class="intermediate">Intermediate</span>
42. [Run process in background?](#q42) <span class="beginner">Beginner</span>
43. [Bring background to foreground?](#q43) <span class="intermediate">Intermediate</span>
44. [What are Signals (SIGINT, SIGKILL)?](#q44) <span class="advanced">Advanced</span>
45. [What is Load Average?](#q45) <span class="advanced">Advanced</span>
46. [Check CPU info?](#q46) <span class="beginner">Beginner</span>
47. [Check Kernel version?](#q47) <span class="beginner">Beginner</span>
48. [What is Swap Space?](#q48) <span class="intermediate">Intermediate</span>
49. [Mount vs Unmount?](#q49) <span class="intermediate">Intermediate</span>
50. [What is `/etc/fstab`?](#q50) <span class="advanced">Advanced</span>
51. [Check file type?](#q51) <span class="beginner">Beginner</span>
52. [Find where a command is located?](#q52) <span class="beginner">Beginner</span>
53. [What is an Alias?](#q53) <span class="beginner">Beginner</span>
54. [History command?](#q54) <span class="beginner">Beginner</span>
55. [Exit code of last command?](#q55) <span class="intermediate">Intermediate</span>
56. [Chain commands (&& vs ;)?](#q56) <span class="intermediate">Intermediate</span>
57. [What is `xargs`?](#q57) <span class="advanced">Advanced</span>
58. [Compress with gzip?](#q58) <span class="beginner">Beginner</span>
59. [What is `umask`?](#q59) <span class="advanced">Advanced</span>
60. [Sticky Bit?](#q60) <span class="advanced">Advanced</span>
61. [SUID vs SGID?](#q61) <span class="advanced">Advanced</span>
62. [What is LVM?](#q62) <span class="advanced">Advanced</span>
63. [Check open files (lsof)?](#q63) <span class="advanced">Advanced</span>
64. [Trace system calls (strace)?](#q64) <span class="advanced">Advanced</span>
65. [What is /dev/null?](#q65) <span class="intermediate">Intermediate</span>
66. [What is /dev/zero?](#q66) <span class="intermediate">Intermediate</span>
67. [Generate random password?](#q67) <span class="intermediate">Intermediate</span>
68. [Download file from URL (curl/wget)?](#q68) <span class="beginner">Beginner</span>
69. [Check connectivity (ping)?](#q69) <span class="beginner">Beginner</span>
70. [Trace route to host?](#q70) <span class="intermediate">Intermediate</span>
71. [DNS Lookup (nslookup/dig)?](#q71) <span class="intermediate">Intermediate</span>
72. [What is `nc` (Netcat)?](#q72) <span class="advanced">Advanced</span>
73. [Transfer files securely (scp)?](#q73) <span class="intermediate">Intermediate</span>
74. [Sync directories (rsync)?](#q74) <span class="intermediate">Intermediate</span>
75. [What is `iptables` / `ufw`?](#q75) <span class="advanced">Advanced</span>
76. [Check user accounts?](#q76) <span class="beginner">Beginner</span>
77. [Add a new user?](#q77) <span class="intermediate">Intermediate</span>
78. [Lock a user account?](#q78) <span class="intermediate">Intermediate</span>
79. [Check groups?](#q79) <span class="beginner">Beginner</span>
80. [What is `chroot`?](#q80) <span class="advanced">Advanced</span>
81. [Symbolic Link to directory?](#q81) <span class="beginner">Beginner</span>
82. [What is a Zombie Process?](#q82) <span class="advanced">Advanced</span>
83. [What is an Orphan Process?](#q83) <span class="advanced">Advanced</span>
84. [Nice vs Renice?](#q84) <span class="advanced">Advanced</span>
85. [What is `dmesg`?](#q85) <span class="advanced">Advanced</span>
86. [Check last reboot logs?](#q86) <span class="intermediate">Intermediate</span>
87. [Schedule one-time job (at)?](#q87) <span class="intermediate">Intermediate</span>
88. [What is `journalctl`?](#q88) <span class="intermediate">Intermediate</span>
89. [Split a large file?](#q89) <span class="intermediate">Intermediate</span>
90. [Watch command?](#q90) <span class="beginner">Beginner</span>
91. [Print numbers (seq)?](#q91) <span class="beginner">Beginner</span>
92. [Calculator in terminal (bc)?](#q92) <span class="beginner">Beginner</span>
93. [Format output (printf)?](#q93) <span class="intermediate">Intermediate</span>
94. [Search and Replace in file?](#q94) <span class="intermediate">Intermediate</span>
95. [Cut columns from file?](#q95) <span class="beginner">Beginner</span>
96. [Paste files together?](#q96) <span class="beginner">Beginner</span>
97. [Join files by field?](#q97) <span class="advanced">Advanced</span>
98. [What is `tee`?](#q98) <span class="intermediate">Intermediate</span>
99. [What is `shebang` (#!)?](#q99) <span class="beginner">Beginner</span>
100. [Shell script arguments ($1, $@)?](#q100) <span class="intermediate">Intermediate</span>

---

<div id="q1" class="question">1. Check disk space? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <ul>
    <li><code>df -h</code>: Free disk space.</li>
    <li><code>du -sh</code>: Disk usage of directory.</li>
  </ul>
</div>

<div id="q2" class="question">2. File permissions (chmod)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>chmod 755 file</code> (rwx for owner, rx for others).</p>
</div>

<div id="q3" class="question">3. Find file by name? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">find /path -name "filename.txt"</code></pre>
</div>

<div id="q4" class="question">4. Grep usage? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">grep "text" file.txt</code></pre>
</div>

<div id="q5" class="question">5. Check/Kill processes? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><code>ps aux</code>, <code>top</code>, <code>kill PID</code>.</p>
</div>

<div id="q6" class="question">6. Soft vs Hard Link? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Soft:</strong> Shortcut (breaks if moved).<br><strong>Hard:</strong> Direct pointer to inode (same file).</p>
</div>

<div id="q7" class="question">7. Check listening ports? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">ss -tulpn</code></pre>
</div>

<div id="q8" class="question">8. Cron vs Crontab? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><strong>Cron:</strong> Daemon.<br><strong>Crontab:</strong> Schedule file.</p>
</div>

<div id="q9" class="question">9. Process vs Thread? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p><strong>Process:</strong> Isolated memory.<br><strong>Thread:</strong> Shared memory.</p>
</div>

<div id="q10" class="question">10. Check memory usage? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">free -h</code></pre>
</div>

<div id="q11" class="question">11. What is SSH? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Secure Shell. Encrypted remote login.</p>
</div>

<div id="q12" class="question">12. Stdin, Stdout, Stderr? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>0: In, 1: Out, 2: Error.</p>
</div>

<div id="q13" class="question">13. Tail log file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">tail -f /var/log/syslog</code></pre>
</div>

<div id="q14" class="question">14. What is a Daemon? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Background service (e.g., httpd).</p>
</div>

<div id="q15" class="question">15. Change owner (chown)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">chown user:group file</code></pre>
</div>

<div id="q16" class="question">16. What is /proc? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Virtual filesystem for kernel/process info.</p>
</div>

<div id="q17" class="question">17. Tar command? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">tar -czvf archive.tar.gz dir/</code></pre>
</div>

<div id="q18" class="question">18. What is systemd? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Init system (PID 1). Manages services.</p>
</div>

<div id="q19" class="question">19. Check IP address? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">ip a</code></pre>
</div>

<div id="q20" class="question">20. Linux Boot Process? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>BIOS -> Bootloader -> Kernel -> Init.</p>
</div>

<div id="q21" class="question">21. What is an Inode? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Data structure storing file metadata (permissions, owner, location) but not name.</p>
</div>

<div id="q22" class="question">22. What is the Root User? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Superuser with full system privileges (UID 0).</p>
</div>

<div id="q23" class="question">23. What is Sudo? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Execute command as another user (usually root).</p>
</div>

<div id="q24" class="question">24. Explain `ls -l` output? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Permissions, Link count, Owner, Group, Size, Date, Name.</p>
</div>

<div id="q25" class="question">25. Create a directory? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">mkdir dir_name</code></pre>
</div>

<div id="q26" class="question">26. Remove a directory? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">rm -r dir_name</code></pre>
</div>

<div id="q27" class="question">27. Move vs Rename file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Both use <code>mv</code> command.</p>
</div>

<div id="q28" class="question">28. Copy file vs directory? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>File: <code>cp src dst</code>. Dir: <code>cp -r src dst</code>.</p>
</div>

<div id="q29" class="question">29. What is the PATH variable? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>List of directories shell searches for executable commands.</p>
</div>

<div id="q30" class="question">30. How to set an Environment Variable? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">export VAR_NAME=value</code></pre>
</div>

<div id="q31" class="question">31. What is .bashrc? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Script executed whenever a new terminal session is started.</p>
</div>

<div id="q32" class="question">32. Difference between `>` and `>>`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><code>></code> Overwrites. <code>>></code> Appends.</p>
</div>

<div id="q33" class="question">33. What is a Pipe `|`? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Passes output of first command as input to second.</p>
</div>

<div id="q34" class="question">34. Head vs Tail? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p><strong>Head:</strong> First 10 lines.<br><strong>Tail:</strong> Last 10 lines.</p>
</div>

<div id="q35" class="question">35. What is `sed`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Stream Editor. Find and replace text.</p>
  <pre><code class="language-bash">sed 's/old/new/g' file</code></pre>
</div>

<div id="q36" class="question">36. What is `awk`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Text processing language. Good for columns.</p>
  <pre><code class="language-bash">awk '{print $1}' file</code></pre>
</div>

<div id="q37" class="question">37. Count lines in a file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">wc -l file</code></pre>
</div>

<div id="q38" class="question">38. Sort contents of a file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">sort file</code></pre>
</div>

<div id="q39" class="question">39. Remove duplicate lines? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">sort file | uniq</code></pre>
</div>

<div id="q40" class="question">40. Compare two files? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">diff file1 file2</code></pre>
</div>

<div id="q41" class="question">41. What is `nohup`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Run command immune to hangups (keeps running after logout).</p>
</div>

<div id="q42" class="question">42. Run process in background? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Append <code>&</code> to command.</p>
</div>

<div id="q43" class="question">43. Bring background to foreground? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">fg %1</code></pre>
</div>

<div id="q44" class="question">44. What are Signals (SIGINT, SIGKILL)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Messages to processes. SIGINT(Ctrl+C), SIGKILL(Force Kill).</p>
</div>

<div id="q45" class="question">45. What is Load Average? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Average number of processes waiting for CPU (1, 5, 15 min).</p>
</div>

<div id="q46" class="question">46. Check CPU info? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">lscpu</code></pre>
</div>

<div id="q47" class="question">47. Check Kernel version? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">uname -r</code></pre>
</div>

<div id="q48" class="question">48. What is Swap Space? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Disk space used as RAM when RAM is full.</p>
</div>

<div id="q49" class="question">49. Mount vs Unmount? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Attach/Detach filesystem to directory tree.</p>
</div>

<div id="q50" class="question">50. What is `/etc/fstab`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Config file for filesystems to mount at boot.</p>
</div>

<div id="q51" class="question">51. Check file type? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">file filename</code></pre>
</div>

<div id="q52" class="question">52. Find where a command is located? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">which cmd</code></pre>
</div>

<div id="q53" class="question">53. What is an Alias? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Shortcut for a command.</p>
</div>

<div id="q54" class="question">54. History command? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Shows list of previously executed commands.</p>
</div>

<div id="q55" class="question">55. Exit code of last command? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">echo $?</code></pre>
</div>

<div id="q56" class="question">56. Chain commands (&& vs ;)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><code>&&</code>: Run 2nd if 1st succeeds.<br><code>;</code>: Run 2nd regardless.</p>
</div>

<div id="q57" class="question">57. What is `xargs`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Builds argument list from standard input.</p>
</div>

<div id="q58" class="question">58. Compress with gzip? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">gzip file</code></pre>
</div>

<div id="q59" class="question">59. What is `umask`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Default permissions for new files.</p>
</div>

<div id="q60" class="question">60. Sticky Bit? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Permission bit. On directories, prevents users from deleting others' files.</p>
</div>

<div id="q61" class="question">61. SUID vs SGID? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Run executable with permissions of owner/group, not user.</p>
</div>

<div id="q62" class="question">62. What is LVM? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Logical Volume Manager. Flexible disk management.</p>
</div>

<div id="q63" class="question">63. Check open files (lsof)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <pre><code class="language-bash">lsof -i :80</code></pre>
</div>

<div id="q64" class="question">64. Trace system calls (strace)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Debugs program execution by printing syscalls.</p>
</div>

<div id="q65" class="question">65. What is /dev/null? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Black hole. Discards all data written to it.</p>
</div>

<div id="q66" class="question">66. What is /dev/zero? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Source of infinite null bytes.</p>
</div>

<div id="q67" class="question">67. Generate random password? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">openssl rand -base64 12</code></pre>
</div>

<div id="q68" class="question">68. Download file from URL (curl/wget)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">curl -O url</code></pre>
</div>

<div id="q69" class="question">69. Check connectivity (ping)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">ping google.com</code></pre>
</div>

<div id="q70" class="question">70. Trace route to host? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">traceroute google.com</code></pre>
</div>

<div id="q71" class="question">71. DNS Lookup (nslookup/dig)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">dig google.com</code></pre>
</div>

<div id="q72" class="question">72. What is `nc` (Netcat)? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Swiss army knife for TCP/UDP. Debug ports, transfer files.</p>
</div>

<div id="q73" class="question">73. Transfer files securely (scp)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">scp file user@host:/path</code></pre>
</div>

<div id="q74" class="question">74. Sync directories (rsync)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">rsync -av src/ dst/</code></pre>
</div>

<div id="q75" class="question">75. What is `iptables` / `ufw`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Firewall configuration.</p>
</div>

<div id="q76" class="question">76. Check user accounts? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">cat /etc/passwd</code></pre>
</div>

<div id="q77" class="question">77. Add a new user? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">useradd username</code></pre>
</div>

<div id="q78" class="question">78. Lock a user account? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">passwd -l username</code></pre>
</div>

<div id="q79" class="question">79. Check groups? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">groups username</code></pre>
</div>

<div id="q80" class="question">80. What is `chroot`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Change root directory for a process (Jail).</p>
</div>

<div id="q81" class="question">81. Symbolic Link to directory? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">ln -s /path/to/dir linkname</code></pre>
</div>

<div id="q82" class="question">82. What is a Zombie Process? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Finished process waiting for parent to read exit code.</p>
</div>

<div id="q83" class="question">83. What is an Orphan Process? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Process whose parent died. Adopted by init (PID 1).</p>
</div>

<div id="q84" class="question">84. Nice vs Renice? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Set priority of process. -20 (High) to 19 (Low).</p>
</div>

<div id="q85" class="question">85. What is `dmesg`? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Kernel ring buffer messages. Hardware/Driver errors.</p>
</div>

<div id="q86" class="question">86. Check last reboot logs? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">last reboot</code></pre>
</div>

<div id="q87" class="question">87. Schedule one-time job (at)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">echo "cmd" | at 5pm</code></pre>
</div>

<div id="q88" class="question">88. What is `journalctl`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>View logs from systemd-journald.</p>
</div>

<div id="q89" class="question">89. Split a large file? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">split -b 100M largefile</code></pre>
</div>

<div id="q90" class="question">90. Watch command? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">watch -n 1 "ls -l"</code></pre>
</div>

<div id="q91" class="question">91. Print numbers (seq)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">seq 1 10</code></pre>
</div>

<div id="q92" class="question">92. Calculator in terminal (bc)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">echo "5+5" | bc</code></pre>
</div>

<div id="q93" class="question">93. Format output (printf)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Formatted printing like C.</p>
</div>

<div id="q94" class="question">94. Search and Replace in file? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <pre><code class="language-bash">sed -i 's/old/new/g' file</code></pre>
</div>

<div id="q95" class="question">95. Cut columns from file? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <pre><code class="language-bash">cut -d"," -f1 file.csv</code></pre>
</div>

<div id="q96" class="question">96. Paste files together? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>Merges lines of files side-by-side.</p>
</div>

<div id="q97" class="question">97. Join files by field? <span class="difficulty advanced">Advanced</span></div>
<div class="answer">
  <p>Like SQL JOIN for text files.</p>
</div>

<div id="q98" class="question">98. What is `tee`? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p>Read from stdin and write to stdout AND file.</p>
</div>

<div id="q99" class="question">99. What is `shebang` (#!)? <span class="difficulty beginner">Beginner</span></div>
<div class="answer">
  <p>First line of script telling kernel which interpreter to use.</p>
</div>

<div id="q100" class="question">100. Shell script arguments ($1, $@)? <span class="difficulty intermediate">Intermediate</span></div>
<div class="answer">
  <p><code>$1</code>: First arg. <code>$@</code>: All args.</p>
</div>
