## Conda Quick Guide

### 📌 What is Conda?

Conda is both a package manager and an environment manager. It allows you to:

- Create isolated environments for different projects.
- Install Python and non-Python packages (C/C++ libraries, R, etc.).
- Reproduce environments with `environment.yml` files.

---

### 🔹 Installing Conda

- **Anaconda**: Comes with many scientific packages pre-installed (larger download).
- **Miniconda**: Lightweight installer; install only what you need.

[Download Miniconda](https://docs.conda.io/en/latest/miniconda.html)

---

### 🔹 Where Conda Stores Environments

By default, environments created with `-n NAME` are stored in a central location:

- **Linux / macOS:**  
    `~/miniconda3/envs/NAME`
- **Windows:**  
    `C:\Users\<user>\miniconda3\envs\NAME`

> Environment names must be unique (you cannot have two environments with the same name).

---

### 🔹 Using `--prefix` for Local Environments

If you prefer project-local environments (like `venv`), use `--prefix` (or `-p`) to specify the folder:

```bash
conda create --prefix ./env python=3.11 numpy pandas
conda activate ./env
```

- This creates the environment inside your project folder (e.g., `./env/`).
- You can reuse the same folder name (`env` or `.venv`) across multiple projects without conflict, since the path is unique.
- Activation requires the path, not just the name.

---

### 🔹 Creating and Managing Environments

**Create a new environment (default location):**
```bash
conda create -n myenv python=3.11 numpy pandas matplotlib
```

**Create a project-local environment:**
```bash
conda create --prefix ./env python=3.11 numpy pandas matplotlib
```

**Activate / Deactivate:**
```bash
conda activate myenv      # named environment
conda activate ./env      # prefix environment
conda deactivate
```

**List environments:**
```bash
conda env list
```

**Remove an environment:**
```bash
conda env remove -n myenv
conda env remove -p ./env
```

---

### 🔹 Installing Packages

**From conda channels:**
```bash
conda install scipy seaborn
```

**From conda-forge (recommended for latest packages):**
```bash
conda install -c conda-forge jupyterlab
```

**From pip inside a conda environment:**
```bash
pip install requests
```

---

### 🔹 Exporting & Importing Environments

**Export to `environment.yml`:**
```bash
conda env export > environment.yml
```

**Example `environment.yml`:**
```yaml
name: myenv
channels:
    - conda-forge
    - defaults
dependencies:
    - python=3.11
    - numpy=2.1.1
    - pandas=2.2.2
    - matplotlib=3.9.2
    - pip
    - pip:
            - requests==2.32.3
```

**Create environment from file:**
```bash
conda env create -f environment.yml
```

**Update environment from file:**
```bash
conda env update -f environment.yml --prune
```

---

### 🔹 Useful Commands Reference

| Command                                      | Description                          |
|-----------------------------------------------|--------------------------------------|
| `conda create -n myenv python=3.11`           | Create named environment             |
| `conda create -p ./env python=3.11`           | Create environment in project folder |
| `conda activate myenv`                        | Activate named environment           |
| `conda activate ./env`                        | Activate prefix environment          |
| `conda deactivate`                            | Deactivate environment               |
| `conda env list`                              | List all environments                |
| `conda list`                                  | Show installed packages              |
| `conda install pkgname`                       | Install package                      |
| `conda remove pkgname`                        | Remove package                       |
| `conda env export > environment.yml`          | Export environment                   |
| `conda env create -f environment.yml`         | Recreate environment from file        |

