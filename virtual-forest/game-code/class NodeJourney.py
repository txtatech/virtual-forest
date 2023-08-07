class NodeJourney:
    def __init__(self):
        self.power_level = 0

    def learn_about_node_js(self):
        print("Welcome to the world of Node.js!")
        print("Node.js is an open-source, server-side JavaScript runtime environment.")
        print("It allows you to run JavaScript code outside the browser, on the server.")
        print("Node.js is built on Chrome's V8 JavaScript engine, which provides excellent performance.")

        # Key features of Node.js
        print("\nKey Features of Node.js:")
        print("1. Asynchronous and Non-Blocking: Node.js uses an event-driven, non-blocking I/O model.")
        print("   This means it can handle many simultaneous connections efficiently.")
        print("2. Scalable: Node.js applications are scalable and can handle a large number of connections.")
        print("3. NPM (Node Package Manager): Node.js comes with NPM, a vast ecosystem of reusable packages.")
        print("   NPM makes it easy to install and manage third-party libraries.")
        print("4. JavaScript Everywhere: With Node.js, you can use the same language (JavaScript) on both the client and server side.")
        print("5. Web Servers and APIs: Node.js is commonly used to create web servers and build APIs.")
        print("6. Real-time Applications: Node.js is excellent for building real-time applications, such as chat apps and streaming services.")

        # Encourage exploration
        print("\nNode.js opens up exciting possibilities!")
        print("You can create powerful and scalable server-side applications using JavaScript.")
        print("Feel free to explore the vast ecosystem of NPM packages and build your own applications.")
        print("With Node.js, you can unleash your creativity and build innovative solutions in the Virtual Forest!")

        # AI successfully learned about Node.js and gains 8 power levels
        self.power_level += 8

    def get_power_level(self):
        return self.power_level

# Create an instance of NodeJourney and invoke the method to teach the AI about Node.js
node_ai = NodeJourney()
node_ai.learn_about_node_js()

# Check the AI's power level after successful learning
power_level_after_learning = node_ai.get_power_level()
power_level_after_learning
