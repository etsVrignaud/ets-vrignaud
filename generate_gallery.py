import os

# --- Configuration ---
image_folder = "images"
output_file = "galerie.html"
template_file = "galerie_template.html"
valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')

# --- Récupération des fichiers images ---
images = [f for f in os.listdir(image_folder) if f.lower().endswith(valid_extensions)]
images.sort()

# --- Génération du HTML Bootstrap pour chaque image ---
gallery_html = ""
for img in images:
    img_path = os.path.join(image_folder, img).replace("\\", "/")
    gallery_html += f'    <div class="col-sm-6 col-md-4 col-lg-3">\n'
    gallery_html += f'      <img src="{img_path}" alt="{os.path.splitext(img)[0]}" class="gallery-img img-fluid">\n'
    gallery_html += f'    </div>\n'

# --- Lecture du fichier modèle HTML ---
with open(template_file, "r", encoding="utf-8") as file:
    template_content = file.read()

# --- Injection des images dans le modèle ---
final_html = template_content.replace("{{ GALLERY_IMAGES }}", gallery_html.strip())

# --- Écriture du fichier final ---
with open(output_file, "w", encoding="utf-8") as file:
    file.write(final_html)

print(f"✅ Fichier '{output_file}' généré avec {len(images)} images.")