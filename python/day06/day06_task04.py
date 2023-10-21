import re
def evalform(formula, *args):
  return eval(formula, dict(zip(sorted(set(re.findall(r'[a-z]+', formula))), args)))