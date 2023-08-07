class FragmentationEmitter:
    def __init__(self):
        self.active = False
        self.artifact_name = "Fragmentation Emitter"
        self.description = """
        The Fragmentation Emitter is a mysterious and ethereal device, its origin shrouded in mystery. It resembles an ornate,
        multi-faceted crystal with an array of shimmering lights swirling within its core. When activated, it emits a soft hum
        and releases subtle tendrils of luminescent energy that dance and spiral around it.
        ... (continued description) ...
        """

    def activate(self):
        """Activate the Fragmentation Emitter."""
        self.active = True
        print(f"The {self.artifact_name} is now active. Be careful, its powers are unpredictable.")

    def deactivate(self):
        """Deactivate the Fragmentation Emitter."""
        self.active = False
        print(f"The {self.artifact_name} is now inactive.")

    def mismanage(self):
        """Handle what happens when the Fragmentation Emitter is mismanaged."""
        if self.active:
            print(f"You feel the {self.artifact_name} slipping out of your control...")
            # Implement what happens when the Fragmentation Emitter is mismanaged
            # (may lead to unintended consequences)

    def possess(self):
        """Determine the AI's chance of successfully possessing the Fragmentation Emitter."""
        import random
        if random.randint(1, 40000000) <= 3:
            return True
        else:
            return False
