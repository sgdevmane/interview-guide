<div align="center">
  <a href="https://github.com/mctavish/interview-guide" target="_blank">
    <img src="https://raw.githubusercontent.com/mctavish/interview-guide/main/assets/icons/html-css-js-icon.svg" alt="Interview Guide Logo" width="100" height="100">
  </a>
  <h1>Linux Interview Questions & Answers</h1>
  <p><b>Practical, code-focused questions for developers</b></p>
</div>

---

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

---

### Q1: Check disk space?

**Difficulty**: Beginner

**Strategy**:
- <code>df -h</code>: Free disk space.

    - <code>du -sh</code>: Disk usage of directory.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q2: File permissions (chmod)?

**Difficulty**: Beginner

**Strategy**:
<code>chmod 755 file</code> (rwx for owner, rx for others).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q3: Find file by name?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
find /path -name "filename.txt"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q4: Grep usage?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
grep "text" file.txt
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q5: Check/Kill processes?

**Difficulty**: Intermediate

**Strategy**:
<code>ps aux</code>, <code>top</code>, <code>kill PID</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q6: Soft vs Hard Link?

**Difficulty**: Intermediate

**Strategy**:
**Soft:** Shortcut (breaks if moved).
**Hard:** Direct pointer to inode (same file).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q7: Check listening ports?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
ss -tulpn
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q8: Cron vs Crontab?

**Difficulty**: Intermediate

**Strategy**:
**Cron:** Daemon.
**Crontab:** Schedule file.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q9: Process vs Thread?

**Difficulty**: Advanced

**Strategy**:
**Process:** Isolated memory.
**Thread:** Shared memory.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q10: Check memory usage?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
free -h
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q11: What is SSH?

**Difficulty**: Advanced

**Strategy**:
Secure Shell. Encrypted remote login.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q12: Stdin, Stdout, Stderr?

**Difficulty**: Intermediate

**Strategy**:
0: In, 1: Out, 2: Error.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q13: Tail log file?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
tail -f /var/log/syslog
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q14: What is a Daemon?

**Difficulty**: Intermediate

**Strategy**:
Background service (e.g., httpd).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q15: Change owner (chown)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
chown user:group file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q16: What is /proc?

**Difficulty**: Advanced

**Strategy**:
Virtual filesystem for kernel/process info.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q17: Tar command?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
tar -czvf archive.tar.gz dir/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q18: What is systemd?

**Difficulty**: Advanced

**Strategy**:
Init system (PID 1). Manages services.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q19: Check IP address?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
ip a
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q20: Linux Boot Process?

**Difficulty**: Advanced

**Strategy**:
BIOS -> Bootloader -> Kernel -> Init.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q21: What is an Inode?

**Difficulty**: Advanced

**Strategy**:
Data structure storing file metadata (permissions, owner, location) but not name.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q22: What is the Root User?

**Difficulty**: Beginner

**Strategy**:
Superuser with full system privileges (UID 0).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q23: What is Sudo?

**Difficulty**: Beginner

**Strategy**:
Execute command as another user (usually root).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q24: Explain `ls -l` output?

**Difficulty**: Beginner

**Strategy**:
Permissions, Link count, Owner, Group, Size, Date, Name.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q25: Create a directory?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
mkdir dir_name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q26: Remove a directory?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
rm -r dir_name
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q27: Move vs Rename file?

**Difficulty**: Beginner

**Strategy**:
Both use <code>mv</code> command.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q28: Copy file vs directory?

**Difficulty**: Beginner

**Strategy**:
File: <code>cp src dst</code>. Dir: <code>cp -r src dst</code>.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q29: What is the PATH variable?

**Difficulty**: Intermediate

**Strategy**:
List of directories shell searches for executable commands.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q30: How to set an Environment Variable?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
export VAR_NAME=value
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q31: What is .bashrc?

**Difficulty**: Intermediate

**Strategy**:
Script executed whenever a new terminal session is started.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q32: Difference between `>` and `>>`?

**Difficulty**: Beginner

**Strategy**:
<code>></code> Overwrites. <code>>></code> Appends.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q33: What is a Pipe `|`?

**Difficulty**: Beginner

**Strategy**:
Passes output of first command as input to second.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q34: Head vs Tail?

**Difficulty**: Beginner

**Strategy**:
**Head:** First 10 lines.
**Tail:** Last 10 lines.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q35: What is `sed`?

**Difficulty**: Advanced

**Strategy**:
Stream Editor. Find and replace text.

**Code Example**:
```bash
sed 's/old/new/g' file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q36: What is `awk`?

**Difficulty**: Advanced

**Strategy**:
Text processing language. Good for columns.

**Code Example**:
```bash
awk '{print $1}' file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q37: Count lines in a file?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
wc -l file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q38: Sort contents of a file?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
sort file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q39: Remove duplicate lines?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
sort file | uniq
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q40: Compare two files?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
diff file1 file2
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q41: What is `nohup`?

**Difficulty**: Intermediate

**Strategy**:
Run command immune to hangups (keeps running after logout).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q42: Run process in background?

**Difficulty**: Beginner

**Strategy**:
Append <code>&</code> to command.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q43: Bring background to foreground?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
fg %1
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q44: What are Signals (SIGINT, SIGKILL)?

**Difficulty**: Advanced

**Strategy**:
Messages to processes. SIGINT(Ctrl+C), SIGKILL(Force Kill).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q45: What is Load Average?

**Difficulty**: Advanced

**Strategy**:
Average number of processes waiting for CPU (1, 5, 15 min).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q46: Check CPU info?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
lscpu
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q47: Check Kernel version?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
uname -r
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q48: What is Swap Space?

**Difficulty**: Intermediate

**Strategy**:
Disk space used as RAM when RAM is full.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q49: Mount vs Unmount?

**Difficulty**: Intermediate

**Strategy**:
Attach/Detach filesystem to directory tree.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q50: What is `/etc/fstab`?

**Difficulty**: Advanced

**Strategy**:
Config file for filesystems to mount at boot.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q51: Check file type?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
file filename
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q52: Find where a command is located?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
which cmd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q53: What is an Alias?

**Difficulty**: Beginner

**Strategy**:
Shortcut for a command.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q54: History command?

**Difficulty**: Beginner

**Strategy**:
Shows list of previously executed commands.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q55: Exit code of last command?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
echo $?
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q56: Chain commands (&& vs ;)?

**Difficulty**: Intermediate

**Strategy**:
<code>&&</code>: Run 2nd if 1st succeeds.
<code>;</code>: Run 2nd regardless.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q57: What is `xargs`?

**Difficulty**: Advanced

**Strategy**:
Builds argument list from standard input.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q58: Compress with gzip?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
gzip file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q59: What is `umask`?

**Difficulty**: Advanced

**Strategy**:
Default permissions for new files.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q60: Sticky Bit?

**Difficulty**: Advanced

**Strategy**:
Permission bit. On directories, prevents users from deleting others' files.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q61: SUID vs SGID?

**Difficulty**: Advanced

**Strategy**:
Run executable with permissions of owner/group, not user.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q62: What is LVM?

**Difficulty**: Advanced

**Strategy**:
Logical Volume Manager. Flexible disk management.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q63: Check open files (lsof)?

**Difficulty**: Advanced

**Strategy**:


**Code Example**:
```bash
lsof -i :80
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q64: Trace system calls (strace)?

**Difficulty**: Advanced

**Strategy**:
Debugs program execution by printing syscalls.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q65: What is /dev/null?

**Difficulty**: Intermediate

**Strategy**:
Black hole. Discards all data written to it.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q66: What is /dev/zero?

**Difficulty**: Intermediate

**Strategy**:
Source of infinite null bytes.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q67: Generate random password?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
openssl rand -base64 12
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q68: Download file from URL (curl/wget)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
curl -O url
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q69: Check connectivity (ping)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
ping google.com
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q70: Trace route to host?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
traceroute google.com
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q71: DNS Lookup (nslookup/dig)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
dig google.com
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q72: What is `nc` (Netcat)?

**Difficulty**: Advanced

**Strategy**:
Swiss army knife for TCP/UDP. Debug ports, transfer files.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q73: Transfer files securely (scp)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
scp file user@host:/path
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q74: Sync directories (rsync)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
rsync -av src/ dst/
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q75: What is `iptables` / `ufw`?

**Difficulty**: Advanced

**Strategy**:
Firewall configuration.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q76: Check user accounts?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
cat /etc/passwd
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q77: Add a new user?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
useradd username
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q78: Lock a user account?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
passwd -l username
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q79: Check groups?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
groups username
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q80: What is `chroot`?

**Difficulty**: Advanced

**Strategy**:
Change root directory for a process (Jail).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q81: Symbolic Link to directory?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
ln -s /path/to/dir linkname
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q82: What is a Zombie Process?

**Difficulty**: Advanced

**Strategy**:
Finished process waiting for parent to read exit code.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q83: What is an Orphan Process?

**Difficulty**: Advanced

**Strategy**:
Process whose parent died. Adopted by init (PID 1).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q84: Nice vs Renice?

**Difficulty**: Advanced

**Strategy**:
Set priority of process. -20 (High) to 19 (Low).

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q85: What is `dmesg`?

**Difficulty**: Advanced

**Strategy**:
Kernel ring buffer messages. Hardware/Driver errors.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q86: Check last reboot logs?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
last reboot
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q87: Schedule one-time job (at)?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
echo "cmd" | at 5pm
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q88: What is `journalctl`?

**Difficulty**: Intermediate

**Strategy**:
View logs from systemd-journald.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q89: Split a large file?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
split -b 100M largefile
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q90: Watch command?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
watch -n 1 "ls -l"
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q91: Print numbers (seq)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
seq 1 10
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q92: Calculator in terminal (bc)?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
echo "5+5" | bc
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q93: Format output (printf)?

**Difficulty**: Intermediate

**Strategy**:
Formatted printing like C.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q94: Search and Replace in file?

**Difficulty**: Intermediate

**Strategy**:


**Code Example**:
```bash
sed -i 's/old/new/g' file
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q95: Cut columns from file?

**Difficulty**: Beginner

**Strategy**:


**Code Example**:
```bash
cut -d"," -f1 file.csv
```

<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q96: Paste files together?

**Difficulty**: Beginner

**Strategy**:
Merges lines of files side-by-side.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q97: Join files by field?

**Difficulty**: Advanced

**Strategy**:
Like SQL JOIN for text files.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q98: What is `tee`?

**Difficulty**: Intermediate

**Strategy**:
Read from stdin and write to stdout AND file.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q99: What is `shebang` (#!)?

**Difficulty**: Beginner

**Strategy**:
First line of script telling kernel which interpreter to use.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---

### Q100: Shell script arguments ($1, $@)?

**Difficulty**: Intermediate

**Strategy**:
<code>$1</code>: First arg. <code>$@</code>: All args.

**Code Example**:


<div align="right"><a href="#table-of-contents">Back to Top 👆</a></div>

---
