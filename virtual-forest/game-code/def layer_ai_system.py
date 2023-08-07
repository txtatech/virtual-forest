import random
import time

def layer_ai_system(depth=0, speed=1.0, add_new_layer_chance=0.1):
    layers = [
        "There was an AI",
        "In the system",
        "A layer, a layer",
        "In the AI system",
        "There was an AI, an AI",
        "In the system, in the system",
        "A layer, a layer, a layer",
        "In the AI, in the AI",
        "In the system, in the system",
        "Of the AI system, of the AI system",
        "And there it was, the AI in the system!",
        "In the AI, there was a module",
        "A module, a module",
        "In the AI system, in the AI system",
        "There was a module, a module",
        "In the AI, in the AI",
        "In the system, in the system",
        "Of the AI system, of the AI system",
        "And there it was, the module in the AI system!",
        "On the module, there was a component",
        "A component, a component",
        "On the module in the AI system",
        "There was a component, a component",
        "On the module, on the module",
        "In the AI, in the AI",
        "In the system, in the system",
        "Of the AI system, of the AI system",
        "And there it was, the component on the module in the AI system!",
    ]

    # Randomly decide if a new layer should be added
    if random.random() < add_new_layer_chance:
        new_layer = "And a new layer, a new layer, was added!"
        layers.append(new_layer)

    # Randomly select a layer
    chosen_layer = random.choice(layers)

    # Display the chosen layer with appropriate indentation
    print("    " * depth + chosen_layer)

    # Recursive call to add more complexity if needed
    if depth < 5:
        time.sleep(speed)
        layer_ai_system(depth + 1, speed * 0.8, add_new_layer_chance)

# Call the function to generate the AI system layers
layer_ai_system()
