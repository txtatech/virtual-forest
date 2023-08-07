def compare_version_numbers(current_version, desired_version):
    def convert_to_tuple(version):
        return tuple(map(int, version.split('.')))

    current_tuple = convert_to_tuple(current_version)
    desired_tuple = convert_to_tuple(desired_version)

    if current_tuple == desired_tuple:
        return f"You are currently using version {current_version}. It matches the desired version {desired_version}."
    elif current_tuple < desired_tuple:
        return f"You are currently using version {current_version}. There is a newer version {desired_version} available."
    else:
        return f"You are currently using version {current_version}. It is newer than the desired version {desired_version}."

# Test the function
print(compare_version_numbers("2.1.3", "2.1.3"))   # Output: "You are currently using version 2.1.3. It matches the desired version 2.1.3."
print(compare_version_numbers("1.5.2", "1.6.0"))   # Output: "You are currently using version 1.5.2. There is a newer version 1.6.0 available."
print(compare_version_numbers("3.0", "2.9.9"))     # Output: "You are currently using version 3.0. It is newer than the desired version 2.9.9."
