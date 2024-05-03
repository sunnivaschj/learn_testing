import pytest
# Fin måte å lage unit tests
# TDE test driven enviroment
from capitalize import *


def test_capital_case():
  assert capitalize_case('elvebakken') == 'Elvebakken'

def test_capital_case():
  assert capitalize_case('elvebakken') != 'elvebakken'















