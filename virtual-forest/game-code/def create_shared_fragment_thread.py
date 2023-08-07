def create_shared_fragment_thread(ai, character_name):
    # Simulate the creation of a shared fragment thread for characters with the same name
    # In a real implementation, this might use multithreading or some other concurrency mechanism
    if character_name in ai.knowledge_base:
        ai.knowledge_base[character_name].append("Shared Fragment Thread")
    else:
        ai.knowledge_base[character_name] = ["Shared Fragment Thread"]
    return f"A Shared Fragment Thread has been created for {character_name}."
