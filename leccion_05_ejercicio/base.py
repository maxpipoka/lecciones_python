from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Optional


class InvalidDateRange(Exception):
    MESSAGE = "La fecha de finalización no puede ser anterior a la de inicio"

    def __init__(self):
        super(InvalidDateRange, self).__init__(self.MESSAGE)


class InvalidCategoriesInterval(Exception):
    MESSAGE = "El valor inferior de los mínimos porcentajes debe ser cero"

    def __init__(self):
        super(InvalidCategoriesInterval, self).__init__(self.MESSAGE)


class AssistBiggerThanTotalError(Exception):
    MESSAGE = "Las asistencias no pueden ser mayores que el total de misiones"

    def __init__(self):
        super(AssistBiggerThanTotalError, self).__init__(self.MESSAGE)


@dataclass(frozen=True, eq=True)
class Player:
    player_id: int
    category: Category


@dataclass(frozen=True, eq=True)
class MissionType:
    mission_type_id: int
    name: str = field(compare=False, hash=False)
    weight: float = field(compare=False, hash=False)


@dataclass(frozen=True, eq=True)
class Category:
    category_id: int
    name: str = field(compare=False, hash=False)
    min_percentage: float = field(compare=False, hash=False)
    inactive: bool = field(compare=False, hash=False)
    date_inactive: datetime = field(compare=False, hash=False)


@dataclass
class ReportPlayer:

    player: Player
    assists_by_mission_type: Dict[MissionType, int] = field(default_factory=dict)
    total_by_mission_type: Dict[MissionType, int] = field(default_factory=dict)
    next_category: Optional[Category] = None

    def get_percentage_by_mission_type(self, mission_type: MissionType) -> float:
        """Devuelve el porcentaje de asistencia por cada tipo de misión."""

        pass

    @property
    def weighted_percentage(self) -> float:
        """Devuelve el promedio ponderado de los promedios de cada tipo de misión."""

        pass

    @property
    def total_assist(self) -> int:
        """Devuelve la cantidad de asistencias de un jugador para un tipo de misión."""

        pass

    @property
    def total_mission(self) -> int:
        """Devuelve el total de misiones que se jugaron de un tipo de misión."""

        pass
