from dataclasses import dataclass


@dataclass
class ProfileConstants:
    ADMINISTRATOR = "administrator"
    COORDINATOR = "coordinator"
    STUDENT = "student"
    SUPPORT = "support"
    TEACHER = "teacher"
    USER = "user"


@dataclass
class StateConstants:
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"


@dataclass
class CountryConstants:
    COL = "colombia"
    ECU = "ecuador"
    ESP = "spain"
    MEX = "mexico"
    PER = "peru"
