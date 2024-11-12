# example of hybrid inheritance
class one:
    pass

class two(one):
    pass

class three(one):
    pass

class jist(two,three):
    pass

# hierarchical ineritance 
class Base:
  pass

class D1(Base):
  pass

class D2(Base):
  pass

class D3(D1):
  pass