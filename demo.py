###############################
# File Generated from DeepSeek
###############################

import torch
from torchvision import transforms
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import timm
import os

# Configuration - CORRECTED CLASS NAMES
MODEL_PATH = "model.pth"
CLASS_NAMES = {0: "AI-Generated", 1: "Real"}  # Changed the labels here

# Set device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"\nUsing device: {device}")

# Image transforms
test_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def load_model():
    """Load the trained EfficientNet-B0 model"""
    model = torch.load(MODEL_PATH, weights_only=False)
    model.to(device)
    model.eval()
    return model

def predict_image(image_path, model):
    """Make prediction on a single image"""
    try:
        img = Image.open(image_path).convert('RGB')
        img_tensor = test_transform(img).unsqueeze(0).to(device)
        
        with torch.no_grad():
            outputs = model(img_tensor)
            probs = torch.softmax(outputs, dim=1)[0]
            pred_class = torch.argmax(probs).item()
        
        return {
            'filename': os.path.basename(image_path),
            'image': img,
            'prediction': CLASS_NAMES[pred_class],  # Now uses corrected labels
            'confidence': probs[pred_class].item(),
            'probabilities': {
                CLASS_NAMES[0]: probs[0].item(),
                CLASS_NAMES[1]: probs[1].item()
            }
        }
    except Exception as e:
        return {'error': str(e)}

class ImageClassifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Image Classifier")
        self.root.geometry("800x600")
        self.root.minsize(700, 500)
        
        # Configure style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0')
        self.style.configure('TButton', font=('Arial', 10))
        
        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Load model
        try:
            self.model = load_model()
            print(f"Model loaded successfully from {MODEL_PATH}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load model: {e}")
            self.root.destroy()
            return
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Left panel - Image display
        self.image_frame = ttk.Frame(self.main_frame, width=400, relief=tk.RIDGE, borderwidth=2)
        self.image_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.image_label = ttk.Label(self.image_frame, text="No image selected", anchor='center')
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Right panel - Controls and results
        self.control_frame = ttk.Frame(self.main_frame, width=300)
        self.control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        
        # File selection
        ttk.Label(self.control_frame, text="AI Image Classifier", font=('Arial', 14, 'bold')).pack(pady=10)
        
        self.select_btn = ttk.Button(self.control_frame, text="Select Image", command=self.select_image)
        self.select_btn.pack(pady=10, fill=tk.X)
        
        # File info
        self.file_frame = ttk.LabelFrame(self.control_frame, text="File Info")
        self.file_frame.pack(fill=tk.X, pady=5)
        
        self.filename_label = ttk.Label(self.file_frame, text="File: None")
        self.filename_label.pack(anchor='w', padx=5, pady=2)
        
        # Results
        self.result_frame = ttk.LabelFrame(self.control_frame, text="Results")
        self.result_frame.pack(fill=tk.X, pady=5)
        
        self.prediction_label = ttk.Label(self.result_frame, text="Prediction: -", font=('Arial', 12))
        self.prediction_label.pack(anchor='w', padx=5, pady=2)
        
        self.confidence_label = ttk.Label(self.result_frame, text="Confidence: -")
        self.confidence_label.pack(anchor='w', padx=5, pady=2)
        
        self.prob_frame = ttk.Frame(self.result_frame)
        self.prob_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(self.prob_frame, text="Probabilities:", font=('Arial', 10)).pack(anchor='w')
        self.ai_prob = ttk.Label(self.prob_frame, text="AI-Generated: -")  # Changed order
        self.ai_prob.pack(anchor='w', padx=20, pady=2)
        self.real_prob = ttk.Label(self.prob_frame, text="Real: -")  # Changed order
        self.real_prob.pack(anchor='w', padx=20, pady=2)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        ttk.Label(self.control_frame, textvariable=self.status_var, relief=tk.SUNKEN, 
                 anchor=tk.W, font=('Arial', 9)).pack(fill=tk.X, pady=(10,0))
    
    def select_image(self):
        filetypes = (
            ('Image files', '*.jpg *.jpeg *.png *.bmp *.gif'),
            ('All files', '*.*')
        )
        
        image_path = filedialog.askopenfilename(
            title="Select an image",
            initialdir=os.path.expanduser('~'),
            filetypes=filetypes
        )
        
        if image_path:
            self.status_var.set("Processing image...")
            self.root.update()
            
            result = predict_image(image_path, self.model)
            
            if 'error' in result:
                messagebox.showerror("Error", result['error'])
                self.status_var.set("Error processing image")
            else:
                # Display image
                self.display_image(result['image'])
                
                # Update file info
                self.filename_label.config(text=f"File: {result['filename']}")
                
                # Update results with corrected labels
                self.prediction_label.config(
                    text=f"Prediction: {result['prediction']}",
                    foreground="red" if result['prediction'] == "AI-Generated" else "green"  # Swapped colors
                )
                self.confidence_label.config(
                    text=f"Confidence: {result['confidence']:.2%}"
                )
                self.ai_prob.config(
                    text=f"AI-Generated: {result['probabilities']['AI-Generated']:.2%}"  # Corrected key
                )
                self.real_prob.config(
                    text=f"Real: {result['probabilities']['Real']:.2%}"  # Corrected key
                )
                
                self.status_var.set("Ready")
    
    def display_image(self, pil_image):
        """Display the selected image in the GUI"""
        max_width = self.image_frame.winfo_width() - 20
        max_height = self.image_frame.winfo_height() - 20
        
        img_width, img_height = pil_image.size
        ratio = min(max_width/img_width, max_height/img_height)
        new_size = (int(img_width * ratio), int(img_height * ratio))
        
        resized_img = pil_image.resize(new_size, Image.LANCZOS)
        tk_img = ImageTk.PhotoImage(resized_img)
        
        self.image_label.config(image=tk_img)
        self.image_label.image = tk_img  # Keep reference

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageClassifierApp(root)
    root.mainloop()
