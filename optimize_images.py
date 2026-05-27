import os
import subprocess

# Define configuration for image types
SLIDER_DIR = "./assets/images/slider"
GALLERY_DIR = "./assets/images/gallery"

def process_slider_images():
    if not os.path.exists(SLIDER_DIR):
        return
    
    for file in os.listdir(SLIDER_DIR):
        if file.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(SLIDER_DIR, file)
            base_name = os.path.splitext(file)[0]
            
            # Desktop WebP (1920px width)
            out_desktop = os.path.join(SLIDER_DIR, f"{base_name}-desktop.webp")
            subprocess.run(["magick", input_path, "-resize", "1920x", "-quality", "85", out_desktop])
            
            # Mobile WebP (768px width)
            out_mobile = os.path.join(SLIDER_DIR, f"{base_name}-mobile.webp")
            subprocess.run(["magick", input_path, "-resize", "768x", "-quality", "80", out_mobile])
            print(f"Processed slider: {file}")

def process_gallery_images():
    # Walk through gallery directory and its nested subfolders (concerts, entreprises, etc.)
    for root, _, files in os.walk(GALLERY_DIR):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)
                base_name = os.path.splitext(file)[0]
                
                # Gallery Grid WebP (600px width max)
                out_webp = os.path.join(root, f"{base_name}.webp")
                subprocess.run(["magick", input_path, "-resize", "600x", "-quality", "80", out_webp])
                print(f"Processed gallery asset: {file}")

if __name__ == "__main__":
    print("Starting automated image optimization compression...")
    process_slider_images()
    process_gallery_images()
    print("Done! All assets mirrored to next-gen WebP format.")