# GroupProjectT23 – Text Adventure Game with GUI

A collaborative **text-based adventure game** featuring a **graphical interface built using Pygame and Pygame GUI**.  
This project was created as part of our CM1101 group coursework at Cardiff University.

---

## 📁 Project Structure

```
├── game.py             # Main game logic and execution
├── gameParser.py       # Handles command parsing and player input
├── gui.py              # Manages GUI and interface elements
├── requirements.txt    # Lists Python dependencies
└── Assets/             # Contains fonts, images, and other resources
```

---

## 🧩 Description

The game allows players to explore rooms, collect items, and complete objectives through both text commands and GUI interaction.  
It blends classic text-adventure mechanics with modern UI design to enhance usability and engagement.

**Key Features**
- Room exploration and navigation  
- Item management and interaction system  
- GUI elements for input/output using `pygame_gui`  
- Scalable structure for adding new rooms, items, and features  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://git.cardiff.ac.uk/c25032830/groupprojectt23.git
cd groupprojectt23
```

### 2. Set Up a Virtual Environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `pygame`
- `pygame_gui`

---

## 🎮 Running the Game

```bash
python3 game.py
```

The GUI window will appear automatically.  
You can enter commands directly or use the interactive interface.

---

## 🧠 Developer Information.

### Code Overview (Update when new files added)
- **`game.py`** – Core game loop and logic controller.  
- **`gameParser.py`** – Parses and validates player commands.  
- **`gui.py`** – Builds and updates the game’s visual layout.  
- **`dungeon_map.py`** - Provides a dictionary of different rooms in dungeon
- **`items.py`** - Provides a dictionary for all the items the player can find
- **`player.py`** - Provides a dictionary for all the different classes the player can be
- **`players.py`** - Provides essential subroutines and classes for the player
- **`enemies.py`** – Defines the `Enemy` dataclass and a registry of enemy types with unique stats, behaviour, and descriptions.  
  Includes helper functions for fetching and listing enemies.
- **`Assets/`** – Stores any graphical or font resources used by the GUI.

### Collaboration Guidelines
1. Create a new branch for any feature or fix:
   ```bash
   git checkout -b feature/your-feature
   ```
2. Commit regularly with descriptive messages.  
3. Test your changes before merging.  
4. Keep file and variable naming consistent.

---

## 🧾 Credits

Developed by **Group 23**  
**Cardiff University – CM1101 Programming Coursework**

Contributors:
- James Harvey  
- Harri Latewood
- Rida Shah
- Ruby Lewis
- Thomas Cox
- William Sydenham

---

## 📜 Licence

This project is for educational use only and not for commercial distribution.
