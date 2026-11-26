# Solar System Simulator

### An Interactive Solar System Simulation Using Python Turtle Graphics

A Computer Graphics Lab project that simulates the Solar System using Python's Turtle Graphics. The project demonstrates the movement of planets around the Sun through graphical animation, illustrating fundamental concepts of computer graphics, coordinate systems, and motion simulation.

---

## Project Overview

The **Solar System Simulator** is a Python-based graphical application designed to represent the Solar System in an animated 2D environment.

Using Python's built-in Turtle Graphics library, the simulator creates a visual representation of the Sun and eight planets, demonstrating their orbital movements around the Sun.

This project was developed collaboratively by three students as part of our Computer Graphics Lab to explore graphical programming, animation techniques, object movement, and collaborative software development using Git and GitHub.

## Features

- **Sun Representation:** A central representation of the Sun.
- **Planetary Visualization:** Graphical representations of the eight planets.
- **Orbital Animation:** Animated planetary movement around the Sun.
- **Orbital Paths:** Visual representations of planetary orbits.
- **Space Background:** A graphical environment representing outer space.
- **Animation Controls:** Pause, resume, and reset the simulation.
- **Speed Adjustment:** Increase or decrease the animation speed.
- **Turtle Graphics:** Built using Python's Turtle Graphics library.
- **Real-Time Animation:** Continuous animation of the simulated planetary system.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Turtle Graphics | 2D graphics and animation |
| PyCharm | Integrated Development Environment |
| Git | Version control |
| GitHub | Project hosting and collaboration |

## Requirements

Before running the project, make sure you have:

- Python 3.8 or later
- PyCharm or another Python IDE
- Git (optional, for cloning the repository)

## Installation and Setup

Follow these steps to run the project on your computer.

### 1. Clone the Repository

```bash
git clone https://github.com/Computer-Graphics-Lab/Solar-System-Simulator.git
```

### 2. Navigate to the Project Directory

```bash
cd Solar-System-Simulator
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python main.py
```

The Solar System Simulator window should now open.

## Project Structure

The project is organized into separate Python modules to improve code readability, maintainability, and collaboration.

```text
Solar-System-Simulator/
│
├── main.py
├── config.py
├── background.py
├── planets.py
├── orbits.py
├── controls.py
│
├── .gitignore
└── README.md
```

### Module Description

| File | Description |
|---|---|
| `main.py` | Main application entry point and simulation coordination |
| `config.py` | Configuration settings for the simulation |
| `background.py` | Background rendering and visual environment |
| `planets.py` | Planet creation and visualization |
| `orbits.py` | Orbital paths and related functionality |
| `controls.py` | Simulation controls and user interactions |
| `.gitignore` | Files and directories excluded from Git |

## Learning Objectives

This project demonstrates practical applications of fundamental computer graphics concepts, including:

- 2D graphical object creation.
- Coordinate systems and positioning.
- Circular motion and orbital paths.
- Animation and object movement.
- Graphical rendering using Python Turtle.
- Modular programming and code organization.
- Collaborative software development.
- Version control using Git and GitHub.

## Future Improvements

Potential enhancements for future versions include:

- [ ] Display planetary names and additional information.
- [ ] Add planetary information panels.
- [ ] Improve the realism of planetary proportions and orbital distances.
- [ ] Include additional celestial objects, such as moons and asteroids.
- [ ] Introduce more advanced visual effects and graphical enhancements.

## Contributors

This project was developed collaboratively by a team of three students as part of our Computer Graphics Lab.

| Contributor | Role |
|---|---|
| Mohib | Project Leadership, Core Development and Integration |
| Nayem | Planet and Orbit Development |
| Fahad | Background Development and Interactive Controls |

## Collaborative Development

The project was developed using Git and GitHub to facilitate teamwork and version control.

Each team member worked on assigned components using separate feature branches.

The collaboration workflow included:

1. Cloning the shared repository.
2. Creating individual feature branches.
3. Developing assigned features independently.
4. Committing and pushing changes.
5. Creating Pull Requests.
6. Reviewing and merging contributions into the main branch.

This workflow helped the team practice collaborative software development and GitHub-based project management.

## Contributing

Contributions, suggestions, and improvements are welcome.

If you are a member of the development team:

1. Clone the repository.
2. Create a separate branch for your work.
3. Make your changes.
4. Commit your changes with meaningful commit messages.
5. Push your branch to GitHub.
6. Open a Pull Request for review.

Please avoid pushing unfinished changes directly to the `main` branch.

---

<div align="center">

### Exploring the Universe Through Code

**Solar System Simulator**

Built with Python and Turtle Graphics.

Developed as part of the Computer Graphics Lab.

</div>