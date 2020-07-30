### imports
from datetime import datetime
import pandas as pd
import os
from utils import am_or_pm, yes_or_no
from steps import steps

### establish circumstances 

# time
AM = datetime.now().hour <= 12
PM = datetime.now().hour > 12

# prompts
OILY = yes_or_no('Is your skin feeling > oily < right now? (y/-)')

if not OILY: 
  DRY = yes_or_no('Is your skin feeling > dry < right now? (y/-)')

skin_feel = 'oily' if OILY else ('dry' if DRY else 'normal')

# whether a product has been applied that disrupts peptides
LOWPH = False

print(f'Recommendation for > {skin_feel} < skin at > {am_or_pm()} <:')

recommendation = []

if PM:
  recommendation.append('mar')

if PM or OILY:
  recommendation.append('faw')

if OILY:
  recommendation.append('ton')
  LOWPH = True
elif not DRY:
  recommendation.append('fab')

if PM:
  recommendation.append('ret')

if AM and not DRY:
  recommendation.append('vic')
  LOWPH = True

if not LOWPH:
  recommendation.append('pep')

if PM:
  recommendation.append('moi')

if AM:
  recommendation.append('spf')

for i, agree in enumerate(recommendation):
  product = steps[abrev]
  print(i+1, product['name'])
