
<!-- PROJECT LOGO -->
<br />
<div align="center">

  ![hero](https://github.com/user-attachments/assets/cf995745-1778-48e1-89d0-eaf66de62f5a)
  
  
  <h3 align="center">Apophis</h3>
  


  <p align="center">
    Exploit faster with simplicity and ease
    <br />
    <a href="https://github.com/kernelstub/Apophis"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kernelstub/Apophis/">View Demo</a>
    ·
    <a href="https://github.com/kernelstub/Apophis/issues">Report Bug</a>
    ·
    <a href="https://github.com/kernelstub/Apophis/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about">About The Project</a>
    </li>
    <li>
      <a href="#installation">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#customexploits">Custom Exploits</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<br />
<center> <h1 align="left" id="about">About</h1> </center>

Apophis is a straightforward yet effective Python based framework tailored to simplify the process of working with digital exploits. This lightweight program is designed to offer users a user friendly and accessible approach to managing and deploying exploits, catering to both novice and experienced users.

<br />
<center> <h1 align="left" id="installation">Installation</h1> </center>

1. Clone the repo

   ```sh
   git clone https://github.com/kernelstub/Apophis.git
    ```

   Install dependencies:

   ```sh
    python3 -m pip install -r requirements.txt
   ```
  
    Optional install as a CLI:
  
     ```sh
      python3 -m pip install .
     ```
  
    Configuration:
  
     ```sh
      APOPHIS_SCRIPTS_DIR      # set to an alternate scripts directory (default: ./scripts)
     ```

<br />
<center> <h1 align="left" id="usage">Usage</h1> </center>

1. Run Apophis

   ```sh
    python3 main.py          # interactive REPL
    apophis list             # list available exploits (after install)
    apophis search <term>    # search exploits
    apophis run <name>       # run a specific exploit by name
    apophis repl             # start interactive mode via CLI
   ```

   Inside the REPL:

   ```text
    scripts                  # list available script categories under ./scripts
    help <folder>            # show table with path, author, date, description
    scripts/<folder>/<file>  # run by path, e.g. scripts/cves/CVE-2021-42013
    search <term>            # search exploits by name
   ```

   
See the [open issues](https://github.com/kernelstub/Apophis) for a full list of proposed features (and known issues).

<br />
<center> <h1 align="left" id="features">Features</h1> </center>

### Key Features of Apophis Exploit Framework:

- **Automated Exploit Loading:** Apophis streamlines the process of loading exploits, saving you time and effort.
  
- **Customizability:** Tailor Apophis to your preferences and project needs. Make it an integral part of your workflow.

- **Speed and Efficiency:** Apophis's automated capabilities ensure quick and efficient exploit deployment.
  
- **Custom Command Naming:** Personalize exploit commands to align with your project's conventions.
  
- **Modular Exploit Storage:** Store, organize, and manage your preferred exploits with ease.
  
- **Detailed Descriptions:** Each exploit comes with customizable descriptions for clarity and context.
  
- **Fine-Tuned Matching:** Specify criteria for exploit selection, ensuring precise vulnerability targeting.
  
- **Version Management:** Stay up-to-date with the latest exploit versions, enhancing project security.
  
- **Customizable Appearance:** Tailor Apophis's visuals to seamlessly blend with your project's branding and aesthetics.
  
- **Comprehensive Documentation:** Apophis generates detailed reports and logs for thorough project documentation.

PS: Some are not added yet!

<br />
<center> <h1 align="left" id="customexploits">Custom Exploits</h1> </center>

You can also load custom exploits of your choice. Create `scripts/<category>/your_exploit.py` with a class inheriting from `Module` and a unique `name`:

```py
from dataclasses import dataclass
from core.modular import Module

@dataclass
class ExploitMeta:
    name: str
    description: str
    author: str
    creation_date: str


class Exploit(Module):
    def __init__(self) -> None:
        meta = ExploitMeta(
            name="test",
            description="Example description of this exploit.",
            author="username",
            creation_date="10-10-2025",
        )
        self.meta: ExploitMeta = meta
        self.name: str = meta.name
        self.description: str = meta.description
        self.author: str = meta.author
        self.creation_date: str = meta.creation_date

    def execute(self) -> None:
        print("Hello world!")
        ChildClass.execute()

# You can also add child classes to your exploit for other stuff you need.
class ChildClass:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def execute() -> None:
        print("Hello child class!")
```
