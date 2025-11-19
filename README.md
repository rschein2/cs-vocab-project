# CS Vocabulary Project

**Learning systems through spaced repetition**

## The Problem

Learning CS systems (Git, Linux, tmux, Docker, etc.) is a lot like learning a foreign language. The concepts make sense when someone explains them, but if you forget the exact commands, the knowledge fades away. You end up Googling the same commands over and over.

Understanding *why* you'd use `git rebase` vs `git merge` is important. But if you can't remember the actual command when you need it, that understanding becomes useless.

## The Solution

Treat CS systems like vocabulary learning. Use Anki flashcards with:

1. **Practical scenarios** - Not "what does git init do?" but "You want to start tracking a new project. What's the command?"

2. **The WHY, not just the WHAT** - Every card explains why you'd choose this approach, when to use alternatives, and what the flags mean

3. **Deliberate overlap** - The same command appears in multiple scenarios. `git reset` shows up when undoing commits, unstaging files, and recovering from mistakes. This builds pattern recognition.

4. **Command variations** - Each card shows 2-3 related commands or flags, building a web of related knowledge

## The Theory

**Concepts without vocabulary are useless.** You might understand the theory behind rebasing, but if you can't recall the command syntax when you need it, you'll either:
- Google it (breaking flow)
- Avoid using it (limiting your skills)
- Make mistakes (using the wrong flag)

Spaced repetition solves this by building muscle memory. After reviewing these cards, the commands become second nature. You stop thinking "how do I check which files changed?" and just type `git status`.

## How to Use These Cards

### Importing into Anki

**Recommended Method - Use the .apkg files:**

1. **Download the package you want:**
   - `cs-vocab-all.apkg` - All topics (248 cards)
   - `cs-vocab-git.apkg` - Git only (32 cards)
   - `cs-vocab-tmux.apkg` - tmux only (18 cards)
   - `cs-vocab-ssh.apkg` - SSH only (20 cards)
   - `cs-vocab-linux.apkg` - Linux Shell only (30 cards)
   - `cs-vocab-linux-utils.apkg` - Linux Utilities only (28 cards)
   - `cs-vocab-processes.apkg` - Linux Processes only (27 cards)
   - `cs-vocab-readline.apkg` - Readline/Bash Shortcuts only (22 cards)
   - `cs-vocab-scripting.apkg` - Shell Scripting only (24 cards)
   - `cs-vocab-regex.apkg` - Regex Patterns only (15 cards)
   - `cs-vocab-networking.apkg` - Networking only (15 cards)
   - `cs-vocab-filesystem.apkg` - File System Hierarchy only (7 cards)
   - `cs-vocab-shell-config.apkg` - Shell Configuration only (10 cards)

2. **Import into Anki:**
   - Desktop: File → Import → Select .apkg file
   - Mobile: Tap the .apkg file → Open with AnkiMobile/AnkiDroid

3. **Result:**
   - Creates subdeck structure: `CS Vocab::Git`, `CS Vocab::tmux`, `CS Vocab::SSH`, `CS Vocab::Linux Shell`, `CS Vocab::Linux Utilities`, `CS Vocab::Linux Processes`, `CS Vocab::Readline Shortcuts`, `CS Vocab::Shell Scripting`, `CS Vocab::Regex Patterns`, `CS Vocab::Networking`, `CS Vocab::File System Hierarchy`, `CS Vocab::Shell Configuration`
   - All cards pre-tagged and formatted
   - Works on desktop and mobile!

**Alternative Methods:**

- **Text import:** Use the `.txt` files (see ANKI_IMPORT_GUIDE.md)
- **Manual import:** Copy/paste from HTML files (tedious but gives full control)
- **Regenerate packages:** Run `python3 generate-anki-packages.py` to rebuild .apkg files

### Study Approach

- **Daily reviews**: 10-15 minutes/day is more effective than cramming
- **Actually type the commands**: When reviewing, type them out (even in thin air). Muscle memory matters.
- **Use them in real projects**: The cards prime your memory, but real usage cements it
- **Be honest with yourself**: If you hesitated or got it wrong, mark it as such. Anki's algorithm works best with honest feedback.

## Card Structure

Each card follows this pattern:

**Front (Question):**
> A practical scenario: "You've made changes to 3 files but only want to commit 2 of them. What's the workflow?"

**Back (Answer):**
- The command(s)
- **Why** you'd use this approach
- 2-3 alternative options or related commands
- Warnings where relevant (e.g., "never rebase shared branches!")

**Tags:** `cs git EN`
- `cs` - Computer Science/Systems topic
- `git` - The specific tool
- `EN` - English language (more languages coming)

## Current Decks

- **git-flashcards.html** - 32 cards covering essential Git workflows
  - Repository basics
  - Staging and committing
  - Branching and merging
  - Rebase vs merge
  - Conflict resolution
  - Remote operations
  - History and searching
  - Recovering from mistakes
  - Tags and releases

- **tmux-flashcards.html** - 18 cards covering essential tmux workflows
  - Starting and attaching sessions
  - Detaching without killing sessions
  - Creating and navigating windows
  - Splitting panes (horizontal/vertical)
  - Moving between panes
  - Copy/scroll mode
  - Resizing and zooming panes
  - Session management
  - Configuration and key bindings

- **ssh-flashcards.html** - 20 cards covering essential SSH workflows
  - Basic connections and authentication
  - SSH key generation and management
  - SSH config file for shortcuts
  - File transfer (scp, rsync)
  - Port forwarding (local, remote, dynamic)
  - Jump hosts and bastion servers
  - SSH agent and key management
  - Debugging connection issues
  - Security and hardening
  - Advanced tunneling and multiplexing

- **linux-shell-flashcards.html** - 30 cards covering essential Linux command line
  - File operations (ls, cp, mv, rm, find)
  - Text processing (grep, sed, awk, cut, sort)
  - Permissions and ownership (chmod, chown)
  - Process management (ps, top, kill, jobs)
  - Disk usage (df, du)
  - Archiving (tar)
  - Networking (curl, wget)
  - Redirection and pipes
  - Environment variables and aliases
  - Command history and exit codes

- **linux-utilities-flashcards.html** - 28 cards covering Linux system utilities
  - systemctl (service management)
  - journalctl (log viewing)
  - NetworkManager (WiFi, networking)
  - Screen brightness (brightnessctl, xrandr)
  - Bluetooth (bluetoothctl)
  - Audio control (pactl, amixer)
  - Package management (apt, dnf, pacman)
  - Battery and power (upower, acpi)
  - Display management (xrandr, multiple monitors)
  - Mounting filesystems (lsblk, mount)
  - Cron jobs and scheduling
  - System information (uname, hostnamectl, lscpu)
  - User management (useradd, usermod)
  - Firewall (ufw, firewalld)
  - Network diagnostics (ping, traceroute, ss)
  - Time/locale settings (timedatectl, localectl)
  - Kernel modules (lsmod, modprobe)
  - Swap management
  - Screenshots and clipboard

- **linux-processes-flashcards.html** - 27 cards covering Linux process management
  - Process viewing and monitoring (ps, top, htop, btop)
  - Killing processes (kill, pkill, killall)
  - Signals (SIGTERM, SIGKILL, SIGHUP, SIGSTOP)
  - Backgrounding/foregrounding (bg, fg, jobs, &, Ctrl+Z)
  - Finding PIDs (pgrep, pidof)
  - CPU monitoring (top, mpstat, load average)
  - GPU monitoring (nvidia-smi, radeontop, intel_gpu_top)
  - Process priority (nice, renice)
  - Persistence (nohup, disown, screen, tmux)
  - Memory monitoring per process
  - System call tracing (strace, ltrace, lsof)
  - Zombie processes
  - Resource limits (ulimit, cgroups)
  - I/O monitoring (iotop, iostat)
  - Process details (/proc filesystem)
  - CPU affinity (taskset)
  - Thread management
  - Performance profiling (perf, flamegraphs)
  - Process isolation (namespaces, unshare)

- **readline-shortcuts-flashcards.html** - 22 cards covering Readline/Bash keyboard shortcuts
  - Navigation (Ctrl+A/E for line start/end, Alt+F/B for word movement)
  - Deletion and editing (Ctrl+K/U/W, Alt+D for killing text)
  - Yank/paste (Ctrl+Y to paste killed text)
  - Screen control (Ctrl+L to clear)
  - History search (Ctrl+R reverse search, Ctrl+P/N navigation)
  - Undo (Ctrl+_)
  - Transpose (Ctrl+T for characters, Alt+T for words)
  - History shortcuts (!!, !$, !^)
  - Case manipulation (Alt+U/L/C)
  - Process control (Ctrl+C interrupt, Ctrl+Z suspend)
  - Editor invocation (Ctrl+X Ctrl+E)
  - Tab completion behavior and customization
  - Configuration (~/.inputrc)
  - Terminal troubleshooting (Ctrl+Q unfreeze, reset)
  - Emacs vs Vi mode

- **shell-scripting-flashcards.html** - 24 cards covering Bash scripting
  - Variables and parameter expansion (assignment, quoting, defaults)
  - Command substitution ($() vs backticks)
  - Conditionals (if/elif/else, test operators)
  - File tests (-f, -d, -r, -w, -x, -e, -s)
  - String and numeric comparisons
  - Loops (for, while, until, break/continue)
  - Functions (definition, arguments, return values)
  - Script arguments ($1, $#, $@, $*)
  - Exit codes and error handling ($?, exit, set -e)
  - Arithmetic ((()), integer operations)
  - Arrays (indexed and associative)
  - String manipulation (length, substring, prefix/suffix removal)
  - Heredocs and multi-line strings
  - Debugging (set -x, set -v)
  - Option parsing (getopts)
  - Error handling and cleanup (trap)
  - Reading user input
  - [[ ]] vs [ ] comparison
  - Shebang and making scripts executable
  - Sourcing vs executing scripts

- **regex-flashcards.html** - 15 cards covering Regular Expressions
  - Anchors (^, $, \b word boundaries)
  - Any character (.) and escaping special chars
  - Character classes ([abc], [a-z], [^abc])
  - Predefined classes (\d, \w, \s, \D, \W, \S)
  - Quantifiers (*, +, ?, {n}, {n,m})
  - Grouping and alternation ((pattern), pattern1|pattern2)
  - Greedy vs non-greedy matching (*?, +?, ??)
  - Backreferences (\1, \2 for captured groups)
  - Common patterns (email, URL, phone, dates)
  - BRE vs ERE vs PCRE differences
  - Using regex in sed (substitution, capture groups)
  - Case-insensitive matching (-i flag)
  - Multi-line patterns and newlines
  - Lookahead and lookbehind ((?=), (?!), (?<=), (?<!))
  - Testing and debugging regex patterns

- **networking-flashcards.html** - 15 cards covering Linux networking
  - ip command (addr, link, route) replacing ifconfig
  - Bringing interfaces up/down and assigning IPs
  - Viewing and managing routing table
  - ss command (replacing netstat) for connections
  - Testing connectivity (ping, traceroute, mtr)
  - DNS lookups (dig, nslookup, host)
  - Downloading files (curl vs wget, options)
  - Packet capture (tcpdump basics and filters)
  - Finding process using a port (ss, lsof)
  - Network performance testing (speedtest-cli, iperf3)
  - WiFi management (nmcli for NetworkManager)
  - DNS configuration (/etc/resolv.conf, systemd-resolved)
  - Port scanning (nmap, netcat)
  - Finding public vs private IP addresses
  - Firewall configuration (ufw, firewalld, iptables)

- **filesystem-flashcards.html** - 7 cards covering Linux File System Hierarchy
  - /etc - System configuration files and service configs
  - /var - Variable data (logs, cache, mail, spool)
  - /bin, /sbin, /usr/bin, /usr/sbin - Essential and user binaries
  - /home, /root, /usr, /usr/local - User data and programs
  - /tmp, /opt, /dev, /proc, /sys - Temp files, devices, kernel info
  - /lib, /usr/lib, /boot, /mnt, /media - Libraries, boot files, mount points
  - Navigation and finding files (pwd, which, type, file, find)

- **shell-config-flashcards.html** - 10 cards covering Shell Configuration
  - .bashrc vs .bash_profile vs .profile (when each loads)
  - PATH variable (viewing, adding directories, order matters)
  - Shell variables vs environment variables (export)
  - Aliases vs functions (when to use each)
  - Reloading config (source vs execute)
  - Customizing PS1 prompt (colors, git branch, formatting)
  - Command history configuration (HISTSIZE, HISTCONTROL)
  - Environment variables (EDITOR, VISUAL, PAGER, LANG)
  - Shell options with shopt (histappend, cdspell, globstar)
  - Managing dotfiles (git repo, symlinks, organization)

## Coming Soon

- vim (movement, editing, modes)
- Docker (containers, images, volumes)
- Build tools (make, cmake)
- Python standard library
- Other languages (ES, ZH, FR, DE)

## Contributing

This is an educational resource. If you find errors or want to suggest improvements:
- Commands should be accurate and follow best practices
- Scenarios should be practical and realistic
- Explanations should focus on WHY, not just WHAT
- Include warnings for dangerous operations

## Philosophy

**Memory is the foundation of expertise.** You can't think creatively about Git workflows if you're constantly context-switching to look up basic commands. These cards free up your mental RAM for higher-level problem solving.

The goal isn't to memorize mindlessly - it's to internalize the vocabulary so you can focus on the interesting problems.

---

*Generated for CS students who are tired of Googling the same commands every day.*
