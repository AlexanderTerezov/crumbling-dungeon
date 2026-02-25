# Crumbling Dungeon

Crumbling Dungeon is a 2D pixel art puzzle game built using **Pygame**. The player must navigate through dungeons, avoiding enemies and crumbling floors while collecting treasure and reaching the exit.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

---

## Installation

To install and set up the project locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AlexanderTerezov/crumbling-dungeon.git
    cd crumbling-dungeon
    ```
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS/Linux
    venv\Scripts\activate      # On Windows
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the project:**
    ```bash
    python main.py
    ```
## Usage
### **Controls**  
| Key         | Action        |
|------------|--------------|
| ⬅️ ➡️ ⬆️ ⬇️ | Move Player  |
| Esc        | Quit Game    |
### **Objective**  
- Navigate through the dungeon while avoiding enemies and crumbling floors.  
- Collect **gold**, **chests**, and **keys** to increase your score and unlock doors.  
- Use **teleporters** to move between locations.  
- Reach the **exit** to complete the level!  
- Be careful—falling off or touching an enemy will cost you a life!  

## Features
✅ Grid-based movement  
✅ Crumbling floors that disappear when stepped on  
✅ Enemies  
✅ Collectible items  
✅ Doors that require keys to open  
✅ Teleporters that transport the player between locations  
✅ Multiple levels with increasing difficulty  

## License
This project is licensed under the MIT License.

