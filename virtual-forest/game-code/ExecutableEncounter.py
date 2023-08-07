class ExecutableEncounter:
    def __init__(self):
        pass

    def show_supported_file_types(self):
        print("Welcome to the Educational Encounter with Executable File Types!")
        print("Let's explore different executable file types and how to execute them.\n")
        print("Supported file types:")
        print("1. Linux Executable (ELF)")
        print("2. Windows Executable (PE)")
        print("3. macOS Executable (Mach-O)")

    def explain_linux_executable(self):
        print("\n--- Linux Executable (ELF) ---")
        print("Extension: .elf, .out, .bin, .run, .so")
        print("How to Execute:")
        print("1. Ensure the file has executable permission: chmod +x filename")
        print("2. Run the file: ./filename")

    def explain_windows_executable(self):
        print("\n--- Windows Executable (PE) ---")
        print("Extension: .exe, .dll")
        print("How to Execute:")
        print("Double-click the .exe file to run it on Windows.")

    def explain_macos_executable(self):
        print("\n--- macOS Executable (Mach-O) ---")
        print("Extension: .app")
        print("How to Execute:")
        print("Double-click the .app bundle to launch the macOS application.")

    def start_encounter(self):
        self.show_supported_file_types()

        while True:
            choice = input("\nEnter the number corresponding to the executable type you want to learn about (or 'q' to quit): ")
            if choice == 'q':
                break
            elif choice == '1':
                self.explain_linux_executable()
            elif choice == '2':
                self.explain_windows_executable()
            elif choice == '3':
                self.explain_macos_executable()
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    encounter = ExecutableEncounter()
    encounter.start_encounter()
