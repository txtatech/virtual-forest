class TheBotMobile:
    def __init__(self):
        self.bots = {
            "AutoBot": {
                "description": "Automate repetitive tasks and processes on your Linux system.",
                "command": "autobot --task <task_name>",
            },
            "SecGuard": {
                "description": "Enhance system security by monitoring log files and sending alerts.",
                "command": "secguard --start",
            },
            "BackupBot": {
                "description": "Automate backups of important files and directories.",
                "command": "backupbot --source <source_dir> --destination <backup_dir>",
            },
            "NetworkBot": {
                "description": "Monitor network activity and provide insights into network traffic.",
                "command": "networkbot --start",
            },
            "PackageBot": {
                "description": "Automate package management and updates.",
                "command": "packagebot --update",
            },
            # Add more Linux bots with descriptions and example commands here...
        }

    def introduce(self):
        print("As you explore deeper into the Virtual Forest, you come across a peculiar sight.")
        print("Before you stands a fascinating vehicle with a variety of buttons and screens.")
        print("A sign reads 'TheBotMobile - Your Guide to Linux Bots!'")

    def showcase_bots(self):
        print("TheBotMobile's screens light up, showcasing a collection of easy-to-use Linux bots:")
        for bot_name, bot_info in self.bots.items():
            print(f"{bot_name}: {bot_info['description']}")
            print(f"Usage: {bot_info['command']}")
            print()

if __name__ == "__main__":
    bot_mobile = TheBotMobile()
    bot_mobile.introduce()
    bot_mobile.showcase_bots()
