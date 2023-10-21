def compose(f, g):
  def ret(*args):
    return f(g(*args), g(*args[::-1]))
  return ret
