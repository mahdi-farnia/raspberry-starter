import gpiod
from gpiod.line import Direction, Value
from contextlib import contextmanager

GPIO_CHIP = "/dev/gpiochip0"

ACTIVE=Value.ACTIVE
INACTIVE=Value.INACTIVE

@contextmanager
def get_gpio(line: int):
  with gpiod.request_lines(
    GPIO_CHIP,
    consumer="blink",
    config={
        line: gpiod.LineSettings(
          direction=Direction.OUTPUT, output_value=Value.ACTIVE
      )
    },
  ) as request:
    yield request
