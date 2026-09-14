import tkinter as tk
import math
import random

# =========================================================
# ⭐ CONFIGURATION: APNA AUR APNI GF KA NAAM YAHAN LIKHO ⭐
GF_NAME = "MY QUEEN"  # <--- "MY QUEEN" hata kar uska naam likho
BOY_NAME = "YOUR NAME" # <--- "YOUR NAME" hata kar apna naam likho
# =========================================================

class JhakaasHeart:
    def __init__(self, root):
        self.root = root
        self.root.title(f"Special Matrix For {GF_NAME} ❤️")
        self.root.geometry("900x650")
        self.root.configure(bg="#020205")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(root, bg="#020205", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Core variables
        self.scale = 14
        self.pulse_angle = 0
        self.rot_angle = 0
        self.mouse_particles = []
        
        # Color Palettes
        self.colors = ["#ff0055", "#ff5080", "#ff007f", "#ff3366", "#ff99bb", "#cc0052"]
        
        # Setup elements
        self.create_background_stars()
        self.create_heart_matrix()
        
        # Typing Animation Variables
        self.full_text = f"YOU ARE MY WHOLE UNIVERSE, {GF_NAME.upper()}! 💖"
        self.typed_text = ""
        self.text_index = 0
        
        # Bind Mouse Motion for Interactive Trail
        self.canvas.bind("<Motion>", self.save_mouse_position)
        
        # Start Engine
        self.animate_all()

    def create_background_stars(self):
        self.stars = []
        for _ in range(60):
            x = random.randint(10, 890)
            y = random.randint(10, 640)
            size = random.uniform(0.5, 2.0)
            self.stars.append({'x': x, 'y': y, 'size': size, 'alpha': random.random()})

    def heart_formula(self, t):
        x = 16 * (math.sin(t) ** 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        return x, y

    def create_heart_matrix(self):
        self.heart_particles = []
        # 1200 high-density neon nodes
        for _ in range(1200):
            t = random.uniform(0, 2 * math.pi)
            hx, hy = self.heart_formula(t)
            
            # 3D Depth layering
            spread = random.uniform(0.6, 1.25)
            bx = hx * spread + random.uniform(-0.5, 0.5)
            by = hy * spread + random.uniform(-0.5, 0.5)
            
            base_color = random.choice(self.colors)
            size = random.uniform(1.5, 4.5)
            # Distance from center for rotational physics
            dist = math.sqrt(bx*bx + by*by)
            angle = math.atan2(by, bx)
            
            self.heart_particles.append({
                'dist': dist, 'angle': angle, 
                'color': base_color, 'size': size,
                'shimmer_prop': random.random()
            })

    def save_mouse_position(self, event):
        # Create trail particles on hover
        if random.random() > 0.4:  # Control density
            self.mouse_particles.append({
                'x': event.x, 'y': event.y,
                'vx': random.uniform(-1.5, 1.5), 'vy': random.uniform(-2, -0.5),
                'life': 1.0, 'color': random.choice(["#00ffff", "#ff007f", "#ffff00", "#ff99ff"])
            })

    def animate_all(self):
        self.canvas.delete("all")
        
        # 1. Background Twinkling Stars
        for s in self.stars:
            s['alpha'] += random.choice([-0.05, 0.05])
            if s['alpha'] < 0.2: s['alpha'] = 0.2
            if s['alpha'] > 1.0: s['alpha'] = 1.0
            fill_val = int(s['alpha'] * 255)
            color = f"#{fill_val:02x}{fill_val:02x}{fill_val:02x}"
            self.canvas.create_oval(s['x'], s['y'], s['x']+s['size'], s['y']+s['size'], fill=color, outline="")

        # 2. Mathematical Heart Animation (Pulse + Subtle Rotation)
        self.pulse_angle += 0.06
        self.rot_angle += 0.005  # Slow elegant 3D drift
        pulse = 1.0 + 0.09 * math.sin(self.pulse_angle)
        
        for p in self.heart_particles:
            # Rotate points dynamically
            current_angle = p['angle'] + math.sin(self.rot_angle) * 0.15
            bx = p['dist'] * math.cos(current_angle)
            by = p['dist'] * math.sin(current_angle)
            
            # Map coordinates to screen center
            x = 450 + bx * self.scale * pulse
            y = 260 + by * self.scale * pulse
            
            # Dynamic Shimmer / Glittering effect
            sz = p['size']
            if random.random() > 0.85:
                sz *= 0.4
                
            self.canvas.create_oval(x-sz, y-sz, x+sz, y+sz, fill=p['color'], outline="")

        # 3. Interactive Mouse Magic Trail
        for mp in self.mouse_particles[:]:
            mp['x'] += mp['vx']
            mp['y'] += mp['vy']
            mp['life'] -= 0.04  # Fade out
            
            if mp['life'] <= 0:
                self.mouse_particles.remove(mp)
            else:
                sz = 4 * mp['life']
                self.canvas.create_oval(mp['x']-sz, mp['y']-sz, mp['x']+sz, mp['y']+sz, fill=mp['color'], outline="")

        # 4. Hacker-Style Text Typing Machine
        if self.text_index < len(self.full_text) and random.random() > 0.7:
            self.typed_text += self.full_text[self.text_index]
            self.text_index += 1
            
        # Draw Interface Text elements
        self.canvas.create_text(450, 490, text=self.typed_text, fill="#ffffff", font=("Arial", 22, "bold"))
        self.canvas.create_text(450, 535, text="[ status: connected_forever.exe ]", fill="#00ffcc", font=("Courier", 11, "bold"))
        self.canvas.create_text(450, 570, text=f"coded with 💖 by {BOY_NAME}", fill="#555566", font=("Arial", 11, "italic"))
        
        # Smooth Frame Update (Approx 60 FPS)
        self.root.after(16, self.animate_all)

if __name__ == "__main__":
    root = tk.Tk()
    app = JhakaasHeart(root)
    root.mainloop()
