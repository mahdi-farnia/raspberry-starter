# Blink

Hello world project for embedded systems!

## Setup

You can use *astral-uv* or pip itself to configure this project.

### Set Up With pip

This approuch does not needs third party installations.

```sh
python -m venv .venv
python -m pip install -r requirements.txt
python -m blink
```

### Set Up With UV

First you need to install [astral-uv](https://docs.astral.sh/uv/getting-started/installation/).

Then in the project directory:
```sh
uv venv .venv
source .venv/bin/activate # powershell: & .\venv\Scripts\Activate
uv sync
```

To run the app:
```sh
uv run -m blink
```

## Setup With Docker (Recommended)

```sh
docker compose up --build
```

Your are good to go!

## Usage

> Assume your raspberry hostname is `pi.local`

- GET `pi.local:8000/on/GPIO_PIN`
  - Makes The GPIO\_PIN active (on)
- GET `pi.local:8000/off/GPIO_PIN`
  - Makes The GPIO\_PIN inactive (off)

### Example

On your browser navigate to `pi.local:8000/on/17`.
This makes gpio 17 (pin 11) high.

On your browser navigate to `pi.local:8000/off/17`.
This makes gpio 17 (pin 11) low.

## Notices

App uses [gpiod](https://pypi.org/project/gpiod/) PyPi package instead of system-wide python3-gpiod.

App runs on port 8000 & listens on all interfaces (0.0.0.0).

This project built for Raspberry PI 4B with kernel version **6.12** OS **Debian Trixie**.

