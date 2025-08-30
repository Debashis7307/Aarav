#!/usr/bin/env python3
"""
Image Generation Module for Aarav AI
Uses Google Gemini API to generate images from text descriptions
"""

import os
import sys
import time
from datetime import datetime
from PIL import Image
from io import BytesIO
import tkinter as tk
from tkinter import messagebox
import threading
from dotenv import load_dotenv

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('brain')

# Load environment variables from .env file
load_dotenv()

try:
    from google import genai
    from google.genai import types
    GEMINI_AVAILABLE = True
except ImportError:
    print("Warning: Google Gemini API not available. Install with: pip install google-genai")
    GEMINI_AVAILABLE = False

class ImageGenerator:
    def __init__(self):
        """Initialize the image generator."""
        self.generate_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "img", "generate")
        self.is_initialized = False
        self.client = None

        # Create generate directory if it doesn't exist
        if not os.path.exists(self.generate_dir):
            os.makedirs(self.generate_dir)

        # Initialize Gemini client if available
        if GEMINI_AVAILABLE:
            try:
                # Get API key from environment
                api_key = os.getenv('GEMINI_API_KEY')
                if not api_key:
                    print("[ERROR] GEMINI_API_KEY not found in environment variables")
                    print("[INFO] Please check your .env file and ensure GEMINI_API_KEY is set")
                    return

                if api_key == 'your_gemini_api_key_here':
                    print("[ERROR] GEMINI_API_KEY is still set to default placeholder value")
                    print("[INFO] Please replace 'your_gemini_api_key_here' with your actual API key")
                    return

                # Initialize the client with API key
                self.client = genai.Client(api_key=api_key)
                self.is_initialized = True
                print("[OK] Image Generator initialized with Gemini API")

            except Exception as e:
                print(f"[ERROR] Failed to initialize Gemini client: {e}")
                print("[INFO] Make sure GEMINI_API_KEY is set correctly in your .env file")
        else:
            print("[ERROR] Google Gemini API library not installed")
            print("[INFO] Install with: pip install google-genai")

    def generate_image(self, prompt, save_image=True, show_popup=True):
        """
        Generate an image from text prompt using Gemini API.

        Args:
            prompt (str): Text description of the image to generate
            save_image (bool): Whether to save the image to disk
            show_popup (bool): Whether to show popup with the generated image

        Returns:
            tuple: (success, message, image_path)
        """
        if not self.is_initialized:
            return False, "Image generation is not properly initialized. Check API setup.", None

        try:
            print(f"Generating image for prompt: '{prompt}'")

            # Create the generation request using the correct Gemini client
            response = self.client.models.generate_content(
                model="gemini-2.5-flash-image-preview",
                contents=[prompt],
            )

            # Process the response
            generated_images = []
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    print(f"Gemini response: {part.text}")
                elif part.inline_data is not None:
                    # Convert bytes to PIL Image
                    image = Image.open(BytesIO(part.inline_data.data))
                    generated_images.append(image)

            if not generated_images:
                return False, "No images were generated from the prompt.", None

            # Use the first generated image
            generated_image = generated_images[0]

            # Save the image if requested
            image_path = None
            if save_image:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"generated_{timestamp}.png"
                image_path = os.path.join(self.generate_dir, filename)
                generated_image.save(image_path)
                print(f"Image saved to: {image_path}")

            # Show popup if requested
            if show_popup:
                self._show_image_popup(generated_image, prompt, image_path)

            success_message = f"Image generated successfully!"
            if image_path:
                success_message += f" Saved as '{os.path.basename(image_path)}'"

            return True, success_message, image_path

        except Exception as e:
            error_msg = f"Failed to generate image: {str(e)}"
            print(f"[ERROR] {error_msg}")
            return False, error_msg, None

    def _show_image_popup(self, image, prompt, image_path=None):
        """
        Show a popup window with the generated image.

        Args:
            image (PIL.Image): The generated image
            prompt (str): The original prompt
            image_path (str): Path where image was saved (optional)
        """
        def show_popup_thread():
            try:
                # Create popup window
                popup = tk.Tk()
                popup.title("Generated Image - Aarav AI")
                popup.geometry("800x600")
                popup.configure(bg='#2E3440')

                # Create frame for content
                frame = tk.Frame(popup, bg='#2E3440')
                frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

                # Title label
                title_label = tk.Label(
                    frame,
                    text="Image Generated Successfully!",
                    font=("Arial", 16, "bold"),
                    bg='#2E3440',
                    fg='#88C0D0'
                )
                title_label.pack(pady=(0, 10))

                # Prompt label
                prompt_label = tk.Label(
                    frame,
                    text=f"Prompt: {prompt}",
                    font=("Arial", 10),
                    bg='#2E3440',
                    fg='#D8DEE9',
                    wraplength=700,
                    justify=tk.LEFT
                )
                prompt_label.pack(pady=(0, 10))

                # Resize image to fit popup while maintaining aspect ratio
                max_width, max_height = 700, 400
                img_width, img_height = image.size

                # Calculate scaling factor
                width_ratio = max_width / img_width
                height_ratio = max_height / img_height
                scale_factor = min(width_ratio, height_ratio, 1.0)

                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)

                # Resize image
                resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Convert to PhotoImage for tkinter
                from PIL import ImageTk
                photo = ImageTk.PhotoImage(resized_image)

                # Image label
                image_label = tk.Label(frame, image=photo, bg='#2E3440')
                image_label.image = photo  # Keep reference
                image_label.pack(pady=(0, 10))

                # Info label
                if image_path:
                    info_text = f"Saved to: {os.path.basename(image_path)}"
                else:
                    info_text = "Image not saved"

                info_label = tk.Label(
                    frame,
                    text=info_text,
                    font=("Arial", 9),
                    bg='#2E3440',
                    fg='#A3BE8C'
                )
                info_label.pack(pady=(0, 10))

                # Close button
                close_button = tk.Button(
                    frame,
                    text="Close",
                    command=popup.destroy,
                    font=("Arial", 12),
                    bg='#5E81AC',
                    fg='white',
                    relief=tk.RAISED,
                    padx=20,
                    pady=5
                )
                close_button.pack()

                # Center the window
                popup.update_idletasks()
                width = popup.winfo_width()
                height = popup.winfo_height()
                x = (popup.winfo_screenwidth() // 2) - (width // 2)
                y = (popup.winfo_screenheight() // 2) - (height // 2)
                popup.geometry(f'{width}x{height}+{x}+{y}')

                # Make window stay on top
                popup.attributes('-topmost', True)
                popup.after(100, lambda: popup.attributes('-topmost', False))

                # Start the GUI event loop
                popup.mainloop()

            except Exception as e:
                print(f"[ERROR] Error showing image popup: {e}")

        # Run popup in separate thread to avoid blocking
        popup_thread = threading.Thread(target=show_popup_thread, daemon=True)
        popup_thread.start()

    def extract_prompt_from_command(self, command):
        """
        Extract the image description prompt from a voice command.

        Args:
            command (str): Voice command containing image generation request

        Returns:
            str: Extracted prompt or None if not found
        """
        command_lower = command.lower().strip()

        # Common phrases to remove
        remove_phrases = [
            "generate", "create", "make", "draw", "paint", "design", "produce",
            "an", "a", "image", "picture", "photo", "artwork", "illustration",
            "of", "for", "me", "please", "can you", "would you", "i want",
            "show me", "display", "imagine", "imaginary", "img"
        ]

        # Split command into words
        words = command_lower.split()

        # Remove common phrases
        filtered_words = []
        for word in words:
            if word not in remove_phrases:
                filtered_words.append(word)

        # Join remaining words to form prompt
        if filtered_words:
            prompt = " ".join(filtered_words)
            # Clean up extra spaces
            prompt = " ".join(prompt.split())
            return prompt

        return None

# Test function
def test_image_generation():
    """Test the image generation functionality."""
    generator = ImageGenerator()

    if not generator.is_initialized:
        print("[ERROR] Image generator not initialized. Cannot test.")
        return

    test_prompts = [
        "a beautiful sunset over mountains",
        "a cute cat wearing sunglasses",
        "a futuristic city skyline at night"
    ]

    print("\nTesting Image Generation...")
    for prompt in test_prompts:
        print(f"\nTesting prompt: '{prompt}'")
        success, message, image_path = generator.generate_image(prompt, save_image=True, show_popup=False)
        print(f"Result: {message}")

        if success:
            print("[OK] Test passed!")
        else:
            print("[ERROR] Test failed!")

        # Small delay between tests
        time.sleep(2)

if __name__ == "__main__":
    test_image_generation()