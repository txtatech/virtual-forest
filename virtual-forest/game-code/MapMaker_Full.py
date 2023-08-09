import os
import qrcode
from collections import deque

class MapMaker:
    def generate_text_tree(self, qr_info, output_file="file_system_tree.txt"):
        with open(os.path.join('outputs', output_file), 'w') as file:
            for directory, info in qr_info.items():
                # Calculate the indentation level based on the directory depth
                indentation_level = directory.count(os.sep)
                indentation = '  ' * indentation_level

                # Write the directory name, coordinates, and neighbors to the file
                file.write(f"{indentation}Directory: {directory}, Coordinates: {info['coordinates']}, Neighbors: {', '.join(info['neighbors'])}\n")

    def generate_qr_with_info(self, directory, coordinates, neighbors):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )

        # Add directory, coordinates, and neighbors to QR code
        qr.add_data(f"Directory: {directory}")
        qr.add_data(f"Coordinates: {coordinates}")
        qr.add_data(f"Neighbors: {', '.join(neighbors)}")

        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        # Prepare a valid filename
        safe_directory_name = directory.replace('/', '_').strip('_')

        # Save QR code as ASCII text
        ascii_qr = qr.get_matrix()
        text_filename = f"qr_{safe_directory_name}_{coordinates.replace(', ', '_')}.txt"
        text_filepath = os.path.join('outputs', text_filename)
        with open(text_filepath, "w") as file:
            for row in ascii_qr:
                file.write("".join(["##" if module else "  " for module in row]) + "\n")

        # Save QR code as PNG
        image_filename = f"qr_{safe_directory_name}_{coordinates.replace(', ', '_')}.png"
        image_filepath = os.path.join('outputs', image_filename)
        qr_img.save(image_filepath)

        return text_filepath, image_filepath

    def get_neighbors(self, coordinates, coordinate_dict):
        x, y = coordinates
        neighbors = []

        # Check north, south, west, and east neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_coordinates = (x + dx, y + dy)
            if neighbor_coordinates in coordinate_dict:
                neighbors.append(coordinate_dict[neighbor_coordinates])

        return neighbors

    def generate_file_system_map(self):
        start_dir = '/'
        start_coordinates = (0, 0)
        coordinate_dict = {start_coordinates: start_dir}
        queue = deque([(start_dir, start_coordinates)])
        os.makedirs('outputs', exist_ok=True)
        qr_info = {}

        while queue:
            current_dir, current_coordinates = queue.popleft()
            x, y = current_coordinates

            # Skip directories inside /proc
            if '/proc' in current_dir:
                continue

            # Generate QR code with directory, coordinates, and neighbors
            neighbors = self.get_neighbors(current_coordinates, coordinate_dict)
            text_filepath, image_filepath = self.generate_qr_with_info(current_dir, f"{x:09}_{y:09}", neighbors)

            # Store QR code info
            qr_info[current_dir] = {
                'coordinates': f"{x:09}_{y:09}",
                'neighbors': neighbors,
                'text_filename': text_filepath,
                'image_filename': image_filepath
            }

            # Visit subdirectories
            try:
                for sub_dir in os.listdir(current_dir):
                    path = os.path.join(current_dir, sub_dir)
                    if os.path.isdir(path):
                        coordinates = (x + 1, y) if sub_dir.startswith('.') else (x, y + 1)
                        coordinate_dict[coordinates] = path
                        queue.append((path, coordinates))
            except (PermissionError, ProcessLookupError, FileNotFoundError):
                continue

        return qr_info

    def generate_x3dom_page(self, qr_info, output_file="index.html"):
        with open(os.path.join('outputs', output_file), 'w') as file:
            file.write("""
<!DOCTYPE html>
<html>
<head>
    <title>3D Grid</title>
    <script src="https://www.x3dom.org/download/x3dom.js"></script>
    <link rel="stylesheet" href="https://www.x3dom.org/download/x3dom.css">
    <style>
        html, body {
            height: 100%;
            margin: 0;
            overflow: hidden;
        }
        #x3d-container {
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>
    <div id="x3d-container">
        <x3d width='100%' height='100%'>
            <scene>
                <viewpoint position='0 5 10'></viewpoint>
        """)

            for info in qr_info.values():
                coordinates = info['coordinates']
                x, y = [int(coord) for coord in coordinates.split('_')]

                file.write(f"""
            <transform translation='{x} 0 {y}'>
                <shape>
                    <appearance>
                        <material diffuseColor='1 1 1'></material>
                        <ImageTexture url='{info['image_filename']}'/>
                    </appearance>
                    <box></box>
                </shape>
            </transform>
            """)

            file.write("""
        </scene>
    </x3d>
</body>
</html>
        """)

    def encounter_with_gnome(self):
        print("You encounter a wise gnome. He holds a magical map of the Virtual Forest.")
        print("Gnome: Where do you wish to create your magical map of the Virtual Forest?")
        self.start_dir = input("Enter the starting directory (default is '/'): ") or '/'
        print(f"Gnome: Very well. I will create a magical map starting from {self.start_dir}.")
        qr_info = self.generate_file_system_map()
        self.generate_x3dom_page(qr_info)
        self.generate_text_tree(qr_info)


if __name__ == "__main__":
    map_maker = MapMaker()
    map_maker.encounter_with_gnome()
