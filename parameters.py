import math
from typing import List, NewType

Distance = NewType('Pixels', float)
Angle = NewType('Radians', float)
ScreenPosition = NewType('tuple(Pixels, Pixels)', tuple[int, int])

RED: tuple = (255, 0, 0)
GREEN: tuple = (0, 255, 0)
BLUE: tuple = (0, 128, 255)
WHITE: tuple = (255, 255, 255)

DEG2RAD: float = math.pi / 180
RAD2DEG: float = 180 / math.pi

# Simulator frame dimensions : (480, 640, 3)
# Real Tello frame dimensions : (720, 960, 3)
IMG_SIZE: tuple[int, int] = (640, 480)
SCREEN_SIZE: tuple[int, int] = (800, 480)
DRONE_POS: ScreenPosition = ScreenPosition((IMG_SIZE[0] // 2, IMG_SIZE[1] // 2))

LAPS: bool = True
MARKERS_INTERVAL: tuple[int, int] = (0, 10)  # (lowest marker id, highest marker id)

SIGHT_V_ANGLE: Angle = Angle(41.6 * DEG2RAD)
SIGHT_V_ANGLE_OFFSET: Angle = Angle(11.5 * DEG2RAD)
SIGHT_H_ANGLE: Angle = Angle(53.6 * DEG2RAD)


class ENV:
    REAL: int = 0
    SIMULATION: int = 1
    status: int = SIMULATION


MARKER_OFFSET: tuple[float, float] = (0, 0)
if ENV.status == ENV.REAL:
    MARKER_OFFSET = (3.5, 0)
elif ENV.status == ENV.SIMULATION:
    MARKER_OFFSET = (-4, 0)


class RUN:
    STOP: bool = False
    START: bool = True
    status: bool = STOP


class MODE:
    EMERGENCY: int = 0
    TAKEOFF: int = 1
    LAND: int = 2
    MANUAL_FLIGHT: int = 3
    AUTO_FLIGHT: int = 4
    AUTO_RESEARCH: int = 5
    status = LAND

    @classmethod
    def __get_dict__(cls) -> dict:
        ms: dict = {'Mode': cls.status}
        return ms


def merge_dicts(dict_list: List[dict]) -> dict:
    merged_dict: dict = {}
    for dictionary in dict_list:
        merged_dict.update(dictionary)
    return merged_dict
