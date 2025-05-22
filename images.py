import os
import re
import shutil

# Paths
posts_dir = "/Users/zeeshanpatel/Documents/ObsidianVault/docs"
attachments_dir = "/Users/zeeshanpatel/Documents/ObsidianVault/attachments/"
static_images_dir = "/Users/zeeshanpatel/Documents/s4g/static/images/"

# Step 1: Recursively process each markdown file in the posts directory
for root, dirs, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            with open(filepath, "r") as file:
                content = file.read()
            
            # Step 2: Find all image links like [[filename.png]]
            images = re.findall(r'\[\[([^]]*\.png)\]\]', content)
            
            # Step 3: Replace and copy images
            for image in images:
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)

                # Step 4: Copy image from ObsidianVault to Hugo static folder
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)
                else:
                    print(f"❌ Image not found: {image_source}")

            # Step 5: Save updated markdown
            with open(filepath, "w") as file:
                file.write(content)

print("✅ Markdown files processed and images copied (if found).")