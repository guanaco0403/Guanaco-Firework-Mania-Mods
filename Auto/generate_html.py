import pandas as pd

# Load the Excel file
df = pd.read_excel('mods.xlsx')

# Start the HTML file
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mods Grid</title>
<style>
  .grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
  }
  .grid-item {
    text-align: center;
    padding: 10px;
    border: 1px solid #ccc;
  }
  .grid-item img {
    width: 100%;
    height: auto;
  }
</style>
</head>
<body>
<div class="grid-container">
'''

# Add each mod to the HTML file
for index, row in df.iterrows():
    html_content += f'''
    <div class="grid-item">
        <a href="{row['mod_url']}" target="_blank">
            <img src="{row['mod_image']}" alt="{row['mod_name']}">
            <div>{row['mod_name']}</div>
        </a>
    </div>
    '''

# End the HTML file
html_content += '''
</div>
</body>
</html>
'''

# Write the HTML file
with open('mods_grid.html', 'w') as f:
    f.write(html_content)

print('HTML file generated successfully.')
