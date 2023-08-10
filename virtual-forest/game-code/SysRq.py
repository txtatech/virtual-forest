class SysRq:
    def __init__(self):
        print("Welcome to the SysRq class! Learn about magic keys on Linux.")
        self.show_intro()
        self.alt_pressed = False
        self.sysrq_pressed = False

    def show_intro(self):
        print("""
The magic SysRq key is a powerful feature in Linux, allowing you to send commands directly to the kernel.
Available Commands:
- b: Reboot
- e: Terminate all processes
- f: Call oom_kill
- h: Display help
- i: Kill all processes
- m: Show memory usage
- r: Turn off keyboard raw mode
- s: Sync filesystems
- u: Remount filesystems read-only

Key Combination Steps:
1. Hold Down the "Alt" Key
2. Hold Down the "SysRq" (or "Print Screen") Key
3. Press the Command Key
4. Release All Keys
        """)

    def press_alt(self):
        self.alt_pressed = True
        print("Alt key pressed.")

    def release_alt(self):
        self.alt_pressed = False
        print("Alt key released.")

    def press_sysrq(self):
        self.sysrq_pressed = True
        print("SysRq key pressed.")

    def release_sysrq(self):
        self.sysrq_pressed = False
        print("SysRq key released.")

    def execute_command(self, command_key):
        if self.alt_pressed and self.sysrq_pressed:
            commands = {
                "b": "Rebooting system...",
                "e": "Terminating all processes...",
                "f": "Calling oom_kill...",
                "h": "Displaying help...",
                "i": "Killing all processes...",
                "m": "Showing memory usage...",
                "r": "Turning off keyboard raw mode...",
                "s": "Syncing filesystems...",
                "u": "Remounting filesystems read-only..."
            }
            action = commands.get(command_key, "Unknown command")
            print(action)
        else:
            print("Error: Alt and SysRq keys must be pressed to execute a command.")

    def chain_commands(self, command_keys):
        for key in command_keys:
            self.execute_command(key)
        self.release_sysrq()
        self.release_alt()

if __name__ == "__main__":
    sysrq = SysRq()
    sysrq.press_alt()
    sysrq.press_sysrq()
    sysrq.execute_command("b")
    sysrq.chain_commands(["s", "b"])
