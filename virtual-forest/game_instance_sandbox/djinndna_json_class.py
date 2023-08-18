import os
import json

class JSONEditor:
    def __init__(self):
        self.json_data = {}

    def load_json(self, json_path):
        with open(json_path, 'r') as file:
            self.json_data = json.load(file)

    def save_json(self, output_path):
        with open(output_path, 'w') as file:
            json.dump(self.json_data, file, indent=4)

    def generate_editor(self, output_path):
        editor_html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>JSON Editor</title>
    <script>
        var jsonData = {json.dumps(self.json_data, indent=4)};

        function updateEditor() {{
            document.getElementById('json-editor').value = JSON.stringify(jsonData, null, 4);
        }}

        function updateData() {{
            var editedJson = document.getElementById('json-editor').value;
            try {{
                jsonData = JSON.parse(editedJson);
            }} catch (error) {{
                alert('Invalid JSON: ' + error.message);
            }}
        }}

        function saveJson() {{
            updateData();
            var blob = new Blob([JSON.stringify(jsonData)], {{type: 'application/json'}});
            var a = document.createElement('a');
            a.href = URL.createObjectURL(blob);
            a.download = 'edited_json.json';
            a.click();
        }}
    </script>
</head>
<body onload="updateEditor()">
    <h1>JSON Editor</h1>
    <textarea id="json-editor" rows="20" cols="80"></textarea>
    <br>
    <button onclick="saveJson()">Save Edited JSON</button>
</body>
</html>
        """
        with open(output_path, 'w') as file:
            file.write(editor_html)

if __name__ == "__main__":
    editor = JSONEditor()
    editor.load_json('encoded_info.json')  # Replace with your JSON file path
    editor.generate_editor('json_editor.html')  # Replace with desired HTML output path
